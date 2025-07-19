<script>
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();

  export let type = "button";
  export let to = null; // destination page name, like 'converter'

  function handleClick() {
    if (to) {
      dispatch('changePage', to);
    }
  }
</script>

<button on:click={handleClick} class="px-4 py-2 rounded bg-blue-600 text-white hover:bg-blue-700 transition">
  <slot />
</button>