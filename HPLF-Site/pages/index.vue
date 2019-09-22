<template>
  <div class="help-page">
    <header>
      <h1>Protect.</h1>
      <h1>Prevent.</h1>
      <h1>Persevere.</h1>
    </header>
    
  </div>
</template>

<script>
import Header from '~/components/Header.vue'
import Button from '~/components/Button.vue'

export default {
  components: {
    Button,
    Header,
  }
}
</script>

<style lang="scss">
  .help-page {
    --theme-color: #923434;
  }

  header {
    background: var(--theme-color);
    display: flex;
    flex-direction: column;
  }
</style>
