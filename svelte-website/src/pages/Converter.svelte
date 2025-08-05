<script>
  import { onMount } from 'svelte'
  import { createEventDispatcher } from 'svelte'
  import Select from 'svelte-select'
  import { medicines } from '../data/medicines.js'
  const dispatch = createEventDispatcher()
  
  let heading = ''
  let selectedFile = null
  let isDragOver = false
  let conversionStatus = ''
  let convertedData = null
  let selectedMedicine = null
  let isLoading = false
    
  function loadContent() {
    setTimeout(() => {
      heading = 'Prescription Reader'
    }, 300)
  }
  
  function handleFileSelect(event) {
    const file = event.target.files[0]
    if (file) {
      // Validate file type
      const validTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'image/bmp', 'image/tiff']
      if (!validTypes.includes(file.type)) {
        conversionStatus = 'Error: Please select a valid image file (JPG, PNG, GIF, BMP, TIFF)'
        return
      }
      
      // Validate file size (max 10MB)
      if (file.size > 10 * 1024 * 1024) {
        conversionStatus = 'Error: File size must be less than 10MB'
        return
      }
      
      selectedFile = file
      conversionStatus = `Selected: ${file.name}`
      convertedData = null // Reset previous results
    }
  }
  
  function handleDragOver(event) {
    event.preventDefault()
    isDragOver = true
  }
  
  function handleDragLeave(event) {
    event.preventDefault()
    isDragOver = false
  }
  
  function handleDrop(event) {
    event.preventDefault()
    isDragOver = false
    
    const files = event.dataTransfer.files
    if (files.length > 0) {
      const file = files[0]
      
      // Validate file type
      const validTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'image/bmp', 'image/tiff']
      if (!validTypes.includes(file.type)) {
        conversionStatus = 'Error: Please drop a valid image file (JPG, PNG, GIF, BMP, TIFF)'
        return
      }
      
      selectedFile = file
      conversionStatus = `Selected: ${selectedFile.name}`
      convertedData = null // Reset previous results
    }
  }
  
  async function convertFile() {
    if (!selectedFile) {
      conversionStatus = 'Please select a file first'
      return
    }

    isLoading = true
    conversionStatus = 'Processing image...'

    const formData = new FormData()
    formData.append('file', selectedFile)

    try {
      const response = await fetch('https://mediscribe.onrender.com/predict', {
        method: 'POST',
        body: formData
      })

      const result = await response.json()

      if (!response.ok) {
        throw new Error(result.error || 'Server error')
      }

      convertedData = {
        originalName: selectedFile.name,
        prediction: result.prediction,
        confidence: result.confidence
      }
      
      conversionStatus = `Analysis completed! Confidence: ${(result.confidence * 100).toFixed(1)}%`
      
    } catch (error) {
      console.error('Conversion error:', error)
      conversionStatus = `Error: ${error.message}`
      convertedData = null
    } finally {
      isLoading = false
    }
  }
  
  function resetConverter() {
    selectedFile = null
    convertedData = null
    conversionStatus = ''
    isLoading = false
    const fileInput = document.getElementById('fileInput')
    if (fileInput) fileInput.value = ''
  }

  function goBack() {
    dispatch('changePage', 'home')
  }
  
  function reloadHome() {
    window.location.href = '/'
  }
  
  onMount(() => {
    loadContent()
  })
</script>

<svelte:head>
  <title>Home</title>
</svelte:head>

<div class="page converter">
  <div class="content-section">
    <h1 class="page-heading">{heading || 'Loading...'}</h1>
    <button on:click={reloadHome} class="back-button">← Back to Home</button>
    
    <div
      class="upload-area {isDragOver ? 'drag-over' : ''}"
      on:dragover={handleDragOver}
      on:dragleave={handleDragLeave}
      on:drop={handleDrop}
    >
      <div class="upload-content">
        <svg class="upload-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
          <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M17 8l-5-5-5 5M12 3v12"/>
        </svg>
        <p class="upload-text">Drag and drop your prescription image here, or click to browse</p>
        <p class="upload-subtext">Supported formats: JPG, PNG, GIF, BMP, TIFF (Max 10MB)</p>
        <input 
          type="file" 
          id="fileInput"
          class="file-input"
          on:change={handleFileSelect}
          accept=".jpg,.jpeg,.png,.gif,.bmp,.tiff,image/*"
        />
      </div>
    </div>
    
    {#if selectedFile}
      <div class="file-info">
        <h3>Selected File:</h3>
        <div class="file-preview">
          {#if selectedFile.type.startsWith('image/')}
            <img 
              src={URL.createObjectURL(selectedFile)} 
              alt="Preview" 
              class="image-preview"
            />
          {/if}
          <div class="file-details">
            <p><strong>Name:</strong> {selectedFile.name}</p>
            <p><strong>Size:</strong> {(selectedFile.size / 1024).toFixed(2)} KB</p>
            <p><strong>Type:</strong> {selectedFile.type || 'Unknown'}</p>
          </div>
        </div>
      </div>
    {/if}
    
    <div class="controls">
      <button 
        class="btn btn-primary" 
        on:click={convertFile}
        disabled={!selectedFile || isLoading}
      >
        {#if isLoading}
          <span class="spinner"></span>
          Processing...
        {:else}
          Analyze Prescription
        {/if}
      </button>
      
      <button 
        class="btn btn-secondary" 
        on:click={resetConverter}
        disabled={isLoading}
      >
        Reset
      </button>
    </div>
    
    {#if conversionStatus}
      <div class="status-message {conversionStatus.includes('completed') || conversionStatus.includes('Confidence') ? 'success' : conversionStatus.includes('Error') ? 'error' : ''}">
        {conversionStatus}
      </div>
    {/if}
    
    {#if convertedData}
      <div class="converted-info">
        <h3>OCR Analysis Results:</h3>
        <div class="result-grid">
          <div class="result-item">
            <strong>Original File:</strong>
            <span>{convertedData.originalName}</span>
          </div>
          <div class="result-item">
            <strong>Detected Medicine:</strong>
            <span class="medicine-name">{convertedData.prediction}</span>
          </div>
          <div class="result-item">
            <strong>Confidence Level:</strong>
            <span class="confidence">{(convertedData.confidence * 100).toFixed(1)}%</span>
          </div>
        </div>
      </div>
    {/if}

    <div class="section-break">
      <label for="medicine-select">Browse Common Medicines:</label>
      <Select
        id="medicine-select"
        items={medicines}
        bind:value={selectedMedicine}
        placeholder="Select a medicine to view details"
      />

      {#if selectedMedicine}
        <div class="medicine-info">
          {#if selectedMedicine.image}
            <img
              src={selectedMedicine.image}
              alt={selectedMedicine.label}
              class="medicine-image"
            />
          {/if}

          <div class="medicine-details">
            <h2>{selectedMedicine.label}</h2>
            <p><strong>Generic Name:</strong> {selectedMedicine.genericName}</p>
            <p><strong>Description:</strong> {selectedMedicine.description}</p>
            <p><strong>Uses:</strong> {selectedMedicine.uses}</p>
            <p><strong>Dosage Information:</strong></p>
            <ul>
              {#each selectedMedicine.dosageRange as dosage}
                <li>{dosage}</li>
              {/each}
            </ul>
            <p><strong>Side Effects:</strong> {selectedMedicine.sideEffects}</p>
          </div>
        </div>
      {/if}
    </div>
  </div>
</div>

<style>
  .converter {
    animation: fadeIn 0.5s ease-in;
  }
  
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }
  
  .content-section {
    text-align: center;
    padding: 4rem 2rem;
    max-width: 800px;
    margin: 0 auto;
  }
  
  .page-heading {
    font-size: 2.5rem;
    color: #2c3e50;
    margin-bottom: 1rem;
    font-weight: 700;
  }
  
  .back-button {
    background: none;
    border: none;
    color: #3498db;
    cursor: pointer;
    font-size: 1rem;
    margin-bottom: 2rem;
    padding: 0.5rem;
  }
  
  .back-button:hover {
    text-decoration: underline;
  }
  
  .upload-area {
    border: 2px dashed #bdc3c7;
    border-radius: 12px;
    padding: 3rem 2rem;
    margin: 2rem 0;
    background: #f8f9fa;
    transition: all 0.3s ease;
    cursor: pointer;
    position: relative;
  }
  
  .upload-area:hover,
  .upload-area.drag-over {
    border-color: #3498db;
    background: #e3f2fd;
    transform: translateY(-2px);
  }
  
  .upload-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }
  
  .upload-icon {
    width: 48px;
    height: 48px;
    color: #7f8c8d;
  }
  
  .upload-text {
    font-size: 1.1rem;
    color: #7f8c8d;
    margin: 0;
  }
  
  .upload-subtext {
    font-size: 0.9rem;
    color: #95a5a6;
    margin: 0;
  }
  
  .file-input {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0;
    cursor: pointer;
  }
  
  .file-info {
    background: #ecf0f1;
    border-radius: 8px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    text-align: left;
  }
  
  .file-info h3 {
    margin: 0 0 1rem 0;
    color: #2c3e50;
  }
  
  .file-preview {
    display: flex;
    gap: 1rem;
    align-items: flex-start;
  }
  
  .image-preview {
    width: 150px;
    height: 150px;
    object-fit: cover;
    border-radius: 8px;
    border: 1px solid #ddd;
  }
  
  .file-details p {
    margin: 0.5rem 0;
    color: #34495e;
  }
  
  .controls {
    display: flex;
    gap: 1rem;
    justify-content: center;
    margin: 2rem 0;
    flex-wrap: wrap;
  }
  
  .btn {
    padding: 0.8rem 1.5rem;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1rem;
    font-weight: 600;
    transition: all 0.3s ease;
    min-width: 120px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
  }
  
  .btn:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }
  
  .btn-primary {
    background: #3498db;
    color: white;
  }
  
  .btn-primary:hover:not(:disabled) {
    background: #2980b9;
    transform: translateY(-2px);
  }
  
  .btn-secondary {
    background: #95a5a6;
    color: white;
  }
  
  .btn-secondary:hover:not(:disabled) {
    background: #7f8c8d;
    transform: translateY(-2px);
  }
  
  .spinner {
    width: 16px;
    height: 16px;
    border: 2px solid #ffffff;
    border-top: 2px solid transparent;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }
  
  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
  
  .status-message {
    padding: 1rem;
    border-radius: 6px;
    margin: 1rem 0;
    background: #e8f4f8;
    color: #2c3e50;
    border-left: 4px solid #3498db;
  }
  
  .status-message.success {
    background: #d5f4e6;
    border-left-color: #27ae60;
    color: #27ae60;
  }
  
  .status-message.error {
    background: #f8e6e6;
    border-left-color: #e74c3c;
    color: #e74c3c;
  }
  
  .converted-info {
    background: #d5f4e6;
    border-radius: 8px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    text-align: left;
  }
  
  .converted-info h3 {
    margin: 0 0 1rem 0;
    color: #27ae60;
  }
  
  .result-grid {
    display: grid;
    gap: 1rem;
  }
  
  .result-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 0;
    border-bottom: 1px solid #c8e6c9;
  }
  
  .result-item:last-child {
    border-bottom: none;
  }
  
  .medicine-name {
    font-weight: bold;
    color: #2c3e50;
    font-size: 1.1rem;
  }
  
  .confidence {
    font-weight: bold;
    color: #27ae60;
  }
  
  .section-break {
    margin-top: 4rem;
    border-top: 2px solid #ddd;
    padding-top: 2rem; 
  }

  .medicine-info {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-top: 1.5rem;
    padding: 1rem;
    background: #f9f9f9;
    border-radius: 6px;
    max-width: 800px;
    text-align: left;
  }

  .medicine-image {
    display: block;
    margin: 0 auto;
    border: 1px solid #ccc;
    border-radius: 8px;
    width: 300px;
    height: auto;
    object-fit: contain;
    background: white;
  }

  .medicine-details {
    border-left: 4px solid #0077cc;
    padding-left: 1rem;
    flex: 1;
    text-align: left;
  }

  .medicine-details strong {
    display: block;
    margin-bottom: 0.25rem;
    color: #0077cc;
    font-weight: 700;
  }

  ul {
    margin: 0.25rem 0 0 1.25rem;
  }

  .medicine-details p,
  .medicine-details ul {
    margin-bottom: 1rem;
  }
  
  @media (max-width: 600px) {
    .content-section {
      padding: 2rem 1rem;
    }
    
    .upload-area {
      padding: 2rem 1rem;
    }
    
    .controls {
      flex-direction: column;
      align-items: center;
    }
    
    .btn {
      width: 100%;
      max-width: 200px;
    }
    
    .file-preview {
      flex-direction: column;
    }
    
    .result-item {
      flex-direction: column;
      align-items: flex-start;
      gap: 0.25rem;
    }
  }
</style>