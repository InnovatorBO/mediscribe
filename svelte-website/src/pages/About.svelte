<script>
  import { onMount } from 'svelte'
  
  // Dynamic content using JavaScript
  let heading = ''
  
  // Function to load content with animation
  function loadContent() {
    setTimeout(() => {
      heading = 'About Us'
    }, 300)
  }
  
  onMount(() => {
    loadContent()
  })
</script>

<div class="page about-page">
  <div class="content-section">
    <h1 class="page-heading">{heading || 'Loading...'}</h1>
    <div class = "heading">What is Mediscribe?</div>
    <p class="insert-content">Introducing MediScribe, an AI powered model that analyzes messy or hard-to-read handwriting and converts it into clear, readable text. Trained specifically for doctor's handwriting, This helps reduce errors and miscommunication in hospitals and doctor’s offices by making notes and prescriptions easier to read. MediScribe improves organization and safety in healthcare by turning handwritten records into accurate digital copies.</p>
    
    <div class = "heading">Our Mission</div>
    <p class="insert-content">Our mission with MediScribe is to ensure safety in healthcare by solving the critical problem of illegible medical handwriting. Misreading a doctor’s notes can lead to dangerous mistakes, such as delayed treatments and miscommunication between patients and doctors. A 2005 study in a British hospital revealed that only 24% of handwritten operative notes were rated as “excellent” or “good,” while a shocking 37% were considered “poor.” These concerning statistics highlight the urgent need for change. MediScribe was created to ensure that every prescription, diagnosis, and instruction is clearly understood, because in healthcare, clarity can save lives.</p>
    
  <div class = "heading">About BranchOut! (Our Team)</div>
    <p class="insert-content">BranchOut! is a student led non-profit organization promoting STEM learning through fostering cultural understanding and civic engagement. Our goal is to inspire a passion for learning through connections between communities, creating and maintaining safe spaces for innovation, collaboration, and support.</p>
    <p class = "insert-content">Regarding the BranchOut! Innovator program specifically, participants use their programming, design, and marketing skills in order to create an online application with a specific task to accomplish. This project-based program also is designed for participants to use their creativity skills to create this effective and unique project.</p>
    <p class="page-info"></p>
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
    text-align: left;
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

  .heading {
    font-size: 24px;
    font-weight: bold;
    color: rgb(16, 27, 63);
    text-align: left;
    margin-top: 50px;

  }

</style>