<script>
  import Navigation from './components/Navigation.svelte'
  import Home from './pages/Home.svelte'
  import About from './pages/About.svelte'
  import Contact from './pages/Contact.svelte'
  import Converter from './pages/Converter.svelte'

  // Current page state
  let currentPage = 'home'

  // Function to change pages
  function changePage(event) {
    currentPage = event.detail
  }

  // Function to get current page component
  function getCurrentPage() {
    switch (currentPage) {
      case 'home':
        return Home
      case 'about':
        return About
      case 'contact':
        return Contact
      case 'converter':
        return Converter
      default:
        return Home
    }
  }
</script>

<main>
  <Navigation {currentPage} on:changePage={changePage} />
  
  <div class="content">
    <svelte:component this={getCurrentPage()} />
  </div>
</main>

<style>
  main {
    min-height: 100vh;
    font-family: 'Allerta', Georgia, 'Times New Roman', Times, serif;
  }

  .content {
    padding: 20px;
    max-width: 1200px;
    margin: 0 auto;
  }
</style>