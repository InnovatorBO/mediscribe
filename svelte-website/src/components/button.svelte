<script>
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();

  export let type = "button";
  export let to = null;
  export let variant = "primary"; // You can add different variants
</script>

<button
  type={type}
  on:click={() => to && dispatch('changePage', to)}
  class="button {variant}"
>
  <slot />
</button>

<style>
  .button {
    padding: 1.25rem 2.5rem;
    font-size: 1.25rem;
    font-weight: bold;
    border-radius: 12px;
    border: none;
    cursor: pointer;
    font-family: 'Oswald', sans-serif;
    box-shadow: 0 0 15px rgba(40, 142, 224, 0.5);
    background-size: 200% auto;
    transition: all 0.5s ease, transform 0.3s ease;
  }
  
  .button.primary {
    color: #fff;
    background: linear-gradient(90deg, #288ee0 0%, #5bb0f5 50%, #288ee0 85%);
    background-size: 200% auto;
  }
  
  .button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(40, 142, 224, 0.8);
    background-position: right center;
  }

</style>