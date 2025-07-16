<script>
  import { createEventDispatcher } from 'svelte'
  
  const dispatch = createEventDispatcher()
  
  export let currentPage = 'home'
  
  // Menu items
  const menuItems = [
    { id: 'home', label: 'Home' },
    { id: 'about', label: 'About' },
    { id: 'contact', label: 'Contact' },
    { id: 'converter', label: 'Converter'}
  ]
  
  // Function to handle page change
  function handlePageChange(pageId) {
    dispatch('changePage', pageId)
  }
</script>

<nav class="nav-container">
  <div class="nav-header">
    <div class="logo-section">
      <img src="/src/assets/logo.png" alt="Logo" class="site-logo" />
    </div>
    
    <div class="nav-menu">
      {#each menuItems as item}
        <button 
          class="nav-item {currentPage === item.id ? 'active' : ''}"
          on:click={() => handlePageChange(item.id)}
        >
          {item.label}
        </button>
      {/each}
    </div>
  </div>
</nav>

<style>
  .nav-container {
    background: #1f377fff;
    padding: 0.75rem 2rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  }
  
  .nav-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .logo-section {
    display: flex;
    align-items: center;
  }
  
  .logo {
    color: white;
    margin: 0;
    font-size: 1.5rem;
    font-weight: bold;
  }

  .site-logo {
    height: 50px;
    width: auto;
    vertical-align: middle;
  }
  
  .nav-menu {
    display: flex;
    gap: 1rem;
    align-items: center;
  }
  
  .nav-item {
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    color: white;
    padding: 0.6rem 1.2rem;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.95rem;
    transition: all 0.3s ease;
    white-space: nowrap;
  }
  
  .nav-item:hover {
    background: rgba(255,255,255,0.2);
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }
  
  .nav-item.active {
    background: rgba(255,255,255,0.3);
    border-color: rgba(255,255,255,0.4);
    font-weight: 600;
  }
  
  /* Responsive design for smaller screens */
  @media (max-width: 768px) {
    .nav-header {
      flex-direction: column;
      gap: 1rem;
    }
    
    .nav-menu {
      gap: 0.5rem;
    }
    
    .nav-item {
      padding: 0.5rem 1rem;
      font-size: 0.9rem;
    }
  }
  
  @media (max-width: 480px) {
    .nav-container {
      padding: 0.5rem 1rem;
    }
    
    .nav-menu {
      flex-wrap: wrap;
      justify-content: center;
    }
    
    .nav-item {
      padding: 0.4rem 0.8rem;
      font-size: 0.85rem;
    }
  }
</style>
