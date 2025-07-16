<script>
  import { onMount } from 'svelte'
  
  // Dynamic content using JavaScript
  let heading = ''
  
  // Function to load content with animation
  function loadContent() {
    setTimeout(() => {
      heading = 'About Our Company'
    }, 300)
  }
  
  onMount(() => {
    loadContent()
  })
</script>

<div class="page about-page">
  <div class="content-section">
    <h1 class="page-heading">{heading || 'Loading...'}</h1>
    <p class="insert-content">Both medical students and doctors have notoriously bad handwriting which could make people recieve the incorrect medicine or dosage for that medicine. For example, in a study done by Yimeng Zhang et al., 150 experienced medical students and 50 professional doctors prescribed 5 medications on a standard hospital prescription chart.</p>
    <p class="insert-content">The results are as followed: “Handwriting quality was of print quality in 25% of both student and doctor participants, legible in 50%, but poorly legible in 25%. Prescription errors were committed by 92% of all participants, with a mean/median of 2 errors per participant.”</p>
    <p class="insert-content">“111 errors were found in the transcription of the patient's name, identification, age, height, weight and allergies. 422 errors were identified in the prescriptions of the 5 given medications, including the omission of drug details in 53%, incorrect dosage in 49% and incorrect instructions for administration in 47% of prescriptions. ”</p>
    <p class="insert-content">“Although 78% of participants admitted to being concerned with poor handwriting and would take appropriate action, 22% reported that they would choose to ignore illegible writing, an attitude that could potentially increase the risk of medication errors.”</p>
    <p class="page-info">Page ID: about</p>
  </div>
</div>

<style>
  .about-page {
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
  
  .insert-content {
    font-size: 1.2rem;
    color: #7f8c8d;
    margin-bottom: 1rem;
  }
  
  .page-info {
    font-size: 1rem;
    color: #95a5a6;
    font-style: italic;
  }
</style> 
