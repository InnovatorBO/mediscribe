<script>
  import { onMount } from 'svelte'
  import Select from 'svelte-select'
  import { medicines } from '../data/medicines.js'
  
  let heading = ''
  let selectedFile = null
  let isDragOver = false
  let conversionStatus = ''
  let convertedData = null
  let selectedMedicine = null
    
  function loadContent() {
    setTimeout(() => {
      heading = 'Prescription Reader'
    }, 300)
  }
  
  function handleFileSelect(event) {
    const file = event.target.files[0]
    if (file) {
      selectedFile = file
      conversionStatus = `Selected: ${file.name}`
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
      selectedFile = files[0]
      conversionStatus = `Selected: ${selectedFile.name}`
    }
  }
  
  function convertFile() {
    if (!selectedFile) {
      conversionStatus = 'Please select a file first'
      return
    }
    
    conversionStatus = 'Converting...'
    
    setTimeout(() => {
      convertedData = {
        originalName: selectedFile.name,
        originalSize: selectedFile.size,
        convertedName: selectedFile.name.replace(/\.[^/.]+$/, '_converted.txt'),
        convertedSize: Math.floor(selectedFile.size * 0.8)
      }
      conversionStatus = 'Conversion completed!'
    }, 2000)
  }
  
  function downloadConverted() {
    const blob = new Blob(['This is your converted file content.'], { type: 'text/plain' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = convertedData.convertedName
    a.click()
    URL.revokeObjectURL(url)
  }
  
  function resetConverter() {
    selectedFile = null
    convertedData = null
    conversionStatus = ''
    const fileInput = document.getElementById('fileInput')
    if (fileInput) fileInput.value = ''
  }
  
  onMount(() => {
    loadContent()
  })
</script>

<div class="page converter">
  <div class="content-section">
    <h1 class="page-heading">{heading || 'Loading...'}</h1>
    
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
        <p class="upload-text">Drag and drop your file here, or click to browse</p>
        <input 
          type="file" 
          id="fileInput"
          class="file-input"
          on:change={handleFileSelect}
          accept=".txt,.csv,.json,.xml"
        />
      </div>
    </div>
    
    {#if selectedFile}
      <div class="file-info">
        <h3>Selected File:</h3>
        <p><strong>Name:</strong> {selectedFile.name}</p>
        <p><strong>Size:</strong> {(selectedFile.size / 1024).toFixed(2)} KB</p>
        <p><strong>Type:</strong> {selectedFile.type || 'Unknown'}</p>
      </div>
    {/if}
    
    <div class="controls">
      <button 
        class="btn btn-primary" 
        on:click={convertFile}
        disabled={!selectedFile || conversionStatus === 'Converting...'}
      >
        {conversionStatus === 'Converting...' ? 'Converting...' : 'Convert File'}
      </button>
      
      <button 
        class="btn btn-secondary" 
        on:click={resetConverter}
      >
        Reset
      </button>
    </div>
    
    {#if conversionStatus}
      <div class="status-message {conversionStatus.includes('completed') ? 'success' : ''}">
        {conversionStatus}
      </div>
    {/if}
    
    {#if convertedData}
      <div class="converted-info">
        <h3>Conversion Results:</h3>
        <p><strong>Original:</strong> {convertedData.originalName} ({(convertedData.originalSize / 1024).toFixed(2)} KB)</p>
        <p><strong>Converted:</strong> {convertedData.convertedName} ({(convertedData.convertedSize / 1024).toFixed(2)} KB)</p>
        
        <button 
          class="btn btn-success" 
          on:click={downloadConverted}
        >
          Download Converted File
        </button>
      </div>
    {/if}
    
    <div class="section-break">
      <label>Common Medicines:</label>
      <Select
        items={medicines}
        bind:value={selectedMedicine}
        placeholder="Select a medicine"
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
            <p><strong>Dosage Amount:</strong></p>
            <ul>
              {#each selectedMedicine.dosageRange as effect}
                <li>{effect}</li>
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
    margin-bottom: 2rem;
    font-weight: 700;
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
  
  .file-info p {
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
  
  .btn-secondary:hover {
    background: #7f8c8d;
    transform: translateY(-2px);
  }
  
  .btn-success {
    background: #27ae60;
    color: white;
  }
  
  .btn-success:hover {
    background: #219a52;
    transform: translateY(-2px);
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
  
  .converted-info p {
    margin: 0.5rem 0;
    color: #2c3e50;
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
    margin-bottom: 1rem; /* adds space below each paragraph and list */
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
  }
</style>