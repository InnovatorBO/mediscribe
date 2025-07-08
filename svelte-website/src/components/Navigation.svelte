<script>
  import { createEventDispatcher } from 'svelte'
  
  const dispatch = createEventDispatcher()
  
  export let currentPage = 'home'
  
  // Dropdown state
  let isDropdownOpen = false
  
  // Menu items
  const menuItems = [
    { id: 'home', label: 'Home' },
    { id: 'about', label: 'About' },
    { id: 'contact', label: 'Contact' }
  ]
  
  // Function to handle page change
  function handlePageChange(pageId) {
    dispatch('changePage', pageId)
    isDropdownOpen = false
  }
  
  // Function to toggle dropdown
  function toggleDropdown() {
    isDropdownOpen = !isDropdownOpen
  }
  
  // Function to close dropdown when clicking outside
  function handleClickOutside(event) {
    if (!event.target.closest('.nav-container')) {
      isDropdownOpen = false
    }
  }
</script>

<svelte:window on:click={handleClickOutside} />

<nav class="nav-container">
  <div class="nav-header">
    <h1 class="logo">My Website</h1>
    
    <div class="dropdown">
      <button 
        class="dropdown-toggle" 
        on:click={toggleDropdown}
        aria-expanded={isDropdownOpen}
      >
        {menuItems.find(item => item.id === currentPage)?.label || 'Menu'}
        <span class="arrow">▼</span>
      </button>
      
      {#if isDropdownOpen}
        <ul class="dropdown-menu">
          {#each menuItems as item}
            <li>
              <button 
                class="dropdown-item {currentPage === item.id ? 'active' : ''}"
                on:click={() => handlePageChange(item.id)}
              >
                {item.label}
              </button>
            </li>
          {/each}
        </ul>
      {/if}
    </div>
  </div>
</nav>

<style>
  .nav-container {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 1rem 2rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  }
  
  .nav-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .logo {
    color: white;
    margin: 0;
    font-size: 1.5rem;
    font-weight: bold;
  }
  
  .dropdown {
    position: relative;
  }
  
  .dropdown-toggle {
    background: rgba(255,255,255,0.2);
    border: 1px solid rgba(255,255,255,0.3);
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    transition: all 0.3s ease;
  }
  
  .dropdown-toggle:hover {
    background: rgba(255,255,255,0.3);
    transform: translateY(-2px);
  }
  
  .arrow {
    font-size: 0.8rem;
    transition: transform 0.3s ease;
  }
  
  .dropdown-toggle[aria-expanded="true"] .arrow {
    transform: rotate(180deg);
  }
  
  .dropdown-menu {
    position: absolute;
    top: 100%;
    right: 0;
    background: white;
    border-radius: 8px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    padding: 0.5rem 0;
    margin-top: 0.5rem;
    min-width: 150px;
    list-style: none;
    z-index: 1000;
    animation: slideDown 0.3s ease;
  }
  
  @keyframes slideDown {
    from {
      opacity: 0;
      transform: translateY(-10px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  .dropdown-item {
    width: 100%;
    padding: 0.75rem 1rem;
    border: none;
    background: none;
    text-align: left;
    cursor: pointer;
    font-size: 1rem;
    color: #333;
    transition: background-color 0.2s ease;
  }
  
  .dropdown-item:hover {
    background-color: #f5f5f5;
  }
  
  .dropdown-item.active {
    background-color: #667eea;
    color: white;
  }
</style> 