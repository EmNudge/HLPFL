<template>
  <a :href="href" class="base-button">
    {{text}}
  </a>
</template>

<script>
export default {
  props: {
    href: {
      type: String,
      default: '#'
    },
    text: {
      type: String,
      default: 'Click Here!'
    }
  }
}
</script>

<style>
  .base-button {
    padding: 10px 20px;
    background: black;
    color: white;
    text-decoration: none;
    font-size: 2em;
    text-align: center;
  }
</style>