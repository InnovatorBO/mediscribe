<script>
  import { onMount } from 'svelte'
let heading = ''
let whatIsMediscribeHeading = ''
let whatIsMediscribeContent = ''
let ourGoalsMissionHeading = ''
let ourGoalsMissionContent = ''
let aboutBranchOutHeading = ''
let aboutBranchOutContent1 = ''
let aboutBranchOutContent2 = ''
    function loadContent() {
    setTimeout(() => {
      heading = 'About Our Company'
      whatIsMediscribeHeading = 'What Is MediScribe:'
      whatIsMediscribeContent = 'Introducing MediScribe, an AI powered model that analyzes messy or hard-to-read handwriting and converts it into clear, readable text. Trained specifically for doctor\'s handwriting, This helps reduce errors and miscommunication in hospitals and doctor’s offices by making notes and prescriptions easier to read. MediScribe improves organization and safety in healthcare by turning handwritten records into accurate digital copies.'
      ourGoalsMissionHeading = 'Our Goals/Mission:'
      ourGoalsMissionContent = 'Our mission with MediScribe is to ensure safety in healthcare by solving the critical problem of illegible medical handwriting. Misreading a doctor’s notes can lead to dangerous mistakes, such as delayed treatments and miscommunication between patients and doctors. A 2005 study in a British hospital revealed that only 24% of handwritten operative notes were rated as “excellent” or “good,” while a shocking 37% were considered “poor.” These concerning statistics highlight the urgent need for change. MediScribe was created to ensure that every prescription, diagnosis, and instruction is clearly understood, because in healthcare, clarity can save lives.'
      aboutBranchOutHeading = 'About BranchOut (Our Team):'
      aboutBranchOutContent1 = 'BranchOut is a student led non-profit organization promoting STEM learning through fostering cultural understanding and civic engagement. Our goal is to inspire a passion for learning through connections between communities, creating and maintaining safe spaces for innovation, collaboration, and support.'
      aboutBranchOutContent2 = 'Regarding the BranchOut Innovator program specifically, participants use their programming, design, and marketing skills in order to create an online application with a specific task to accomplish. This project-based program also is designed for participants to use their creativity skills to create this effective and unique project.'
    }, 300)
  }
  
  onMount(() => {
    loadContent()
  })
</script>

<div class="page about-page">
  <div class="content-section">
    <h1 class="page-heading">{heading || 'Loading...'}</h1>
    <p class="insert-content">This is the about page content. You can add information about your company here.</p>
    <p class="page-info">Page ID: about</p>
    <h2 class="subheading">{whatIsMediscribeHeading || ''}</h2>
    <p class="paragraph">{whatIsMediscribeContent || ''}</p>
    <h2 class="subheading">{ourGoalsMissionHeading || ''}</h2>
    <p class="paragraph">{ourGoalsMissionContent || ''}</p>
    <h2 class="subheading">{aboutBranchOutHeading || ''}</h2>
    <p class="paragraph">{aboutBranchOutContent1 || ''}</p>
    <p class="paragraph">{aboutBranchOutContent2 || ''}</p>
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
    margin-bottom: 4rem;
  }
  
  .subheading {
    font-size: 2rem;
    color: #2c3e50;
    margin-bottom: 1rem;
    font-weight: 600;
  }
  
.paragraph {
    font-size: 1.2rem;
    color: #7f8c8d;
    margin-bottom: 2rem;
    text-align: justify;
  }
</style>