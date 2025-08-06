<script>
  import { onMount } from 'svelte'
  import Button from "../components/button.svelte";
  import Converter from './Converter.svelte'
  import { createEventDispatcher } from 'svelte'
  import ex1 from '../assets/example1.png';
  import ex2 from '../assets/example2.png';
  import ex3 from '../assets/example3.png';

  const dispatch = createEventDispatcher()
  let clicked = false;
  let heading = ''
  
  function loadContent() {
    setTimeout(() => {
      heading = 'Introducing an AI-powered Doctors Handwriting Recognition Model'
    }, 300)
  }
  
  function handleClick() {
    dispatch('changePage', 'converter')
  }

  onMount(() => {
    loadContent()
  })

  let currentPage = 'home'

  function changePage(event) {
    currentPage = event.detail
  }

  const examples = [
    {
      image: ex1,
      alt: "ex1",
      text: "Odmon",
    },
    {
      image: ex2,
      alt: "ex2",
      text: "Azithrocin",
    },
    {
      image: ex3,
      alt: "ex3",
      text: "Aceta",
    },
  ]

  function getCurrentPage() {
    switch (currentPage) {
      case 'converter':
        return Converter;
      default:
        return null;
    }
  }

  onMount(() => {
    loadContent();
  });
  
  // const dispatch = createEventDispatcher();

</script>

<svelte:head>
  <title>Home</title>
</svelte:head>

{#if currentPage === 'home'}
<div class="page home-page">
  <div class="content-section">
    <h1 class="page-heading">{heading || 'Loading...'}</h1>
    <p class="insert-content">MediScribe is an AI tool that converts messy handwriting - especially from doctors - into digital easy-to-read text. MediScribe helps reduce errors and miscommunication in healthcare by making notes and prescriptions easier to read, improving organization and safety in healthcare.</p>
    
    <div class="stats-container">
      <div class="stat-block">
        <div class="stat-content">
          <span class="stat-highlight">1.5 million injuries</span>
          <p>Each year, doctors' messy and illegible handwriting leads to 1.5 million injuries and contributes to over 7,000 deaths in the U.S.</p>
        </div>
      </div>
      
      <div class="stat-block">
        <div class="stat-content">
          <span class="stat-highlight">30,000 deaths annually</span>
          <p>Illegible doctor's handwriting contributes to medical errors, which are estimated to cause up to 30,000 deaths each year in Britain.</p>
        </div>
      </div>
    </div>

    <!-- <Navigation {currentPage} on:changePage={changePage} /> -->
  
    <!-- <div class="content">
      <svelte:component this={getCurrentPage()} />
    </div> -->
    <div class="button-container">
      <Button to="converter" on:changePage={changePage}>
        Try it out for free!
      </Button>
    </div>

    <div class="examples">
      <div class="examples-container">
        {#each examples as example}
        <div class="example-block">
          <div class="example-content">
            <div class="image-box">
              <img src="{example.image}" alt="{example.alt}" />
            </div>
            <div class = "text-overlay">
              <p>{example.text}</p>
            </div>
          </div>
        </div>
        {/each}
      </div>
      </div>
      </div>
  </div>
  {:else}
      <svelte:component this={getCurrentPage()} />
{/if}

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
    color: #1f377fff;
    margin-bottom: 2rem;
    font-weight: 700;
  }

  .nav-button-clicked {
    animation: clickPop 0.3s ease;
  }

  @keyframes clickPop {
    0% { transform: scale(1); }
    50% { transform: scale(0.92); }
    100% { transform: scale(1); }
  }

  .insert-content {
    font-size: 1.2rem;
    color: #7f8c8d;
    margin-bottom: 3rem;
  }

  .stats-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 3rem;
  }

  .stat-block {
    background: linear-gradient(135deg, #27449b, #1f377fff);
    border-radius: 12px;
    padding: 2rem;
    color: white;
    box-shadow: 0 8px 25px rgb(28, 50, 117);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .stat-block:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 35px rgb(39, 72, 172);
  }

  .stat-content {
    text-align: left;
  }

  .stat-highlight {
    display: block;
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: #fff;
  }

  .stat-block p {
    font-size: 1rem;
    line-height: 1.5;
    margin: 0;
    color: rgba(255, 255, 255, 0.95);
  }

  .examples-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
    margin-top: 3rem;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
  }

  .example-block {
    background: linear-gradient(135deg, #d9d8ff, #abaed2);
    border-radius: 12px;
    padding: 2rem;
    color: white;
    box-shadow: 0 8px 25px rgb(28, 50, 117);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .example-block:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 35px rgb(86, 106, 164);
  }

  .example-content {
    text-align: left;
  }

  .example-highlight {
    display: block;
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: #1f377fff;
  }

  .example-block p {
    font-size: 1rem;
    line-height: 1.5;
    margin: 0;
    color: #fffffff2;
  }

  .my-div {
    font-size: 1.5rem;
    border: 4px solid black;
    border-radius: 12px;
    background-color: white;
    color: white;
    padding: 10px 20px;
    cursor: pointer;
    margin-bottom: 75px;
    margin-top: 75px;
  }

  .page-info {
    font-size: 1rem;
    color: #95a5a6;
    font-style: italic;
  }

  .button-container {
    display: flex;
    justify-content: center;
    margin-top: 5rem;
    margin-bottom: 5rem;
    font-size: 3rem;
  }

  .image-box {
    width: 200px;
    height: auto;
  }

  .image-box img {
    width: 100%;
    height: 100%;
    object-fit: fill;
  }

  .example-block {
    position: relative;
  }

  .text-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
  padding: 1rem;
  background: rgba(31, 55, 127, 0.95);
  border-radius: 8px;
}

.text-overlay p {
  font-size: 1rem;
  line-height: 1.4;
  margin: 0;
  color: white;
  text-align: center;
}

.example-block:hover .image-box {
  opacity: 0;
}

.example-block:hover .text-overlay {
  opacity: 1;
}

</style>