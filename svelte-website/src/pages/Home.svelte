<script>
  import { onMount } from 'svelte'
  
  // Dynamic content using JavaScript
  let heading = ''
  
  // Function to load content with animation
  function loadContent() {
    setTimeout(() => {
      heading = 'Introducing an AI-powered doctor handwriting recognition model'
    }, 300)
  }
  
  function handleClick() {
    clicked=true
    setTimeout(() => clicked=false, 300);
    window.location.href = '/converter'
  }

  onMount(() => {
    loadContent()
  })
</script>

<div class="page home-page">
  <div class="content-section">
    <h1 class="page-heading">{heading || 'Loading...'}</h1>
    <p class="insert-content">This is the home page content. You can add your main content here.</p>
    <p class="page-info">Page ID: home</p>
    <button class="nav-button" on:click={() => window.location.href = '/converter'}> 
      Try it out for free!
    </button>
  </div>
</div>

<style>
  .home-page {
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
  .nav-button {
    background-color: #1f377fff;
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 2rem;
    font-family: Oswald, sans-serif;
    transition: background-color 0.3s ease;
    margin-top: 2rem;
  }
  .nav-button:hover {
    background-color: #1f377fff;
  }
  .page-heading {
    font-size: 2.5rem;
    color: #1f377fff;;
    margin-bottom: 2rem;
    font-weight: 700;
  }
 
.nav-button-clicked { 
  animation:clickPop 0.3s ease;
  }
 
  @keyframes clickPop {
    0% { transform: scale(1); }
    50% { transform: scale(0.92); }
    100% { transform: scale(1); }
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