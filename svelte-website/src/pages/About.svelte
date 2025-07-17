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
    <p class="insert-content">This is the about page content. You can add information about your company here.</p>
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