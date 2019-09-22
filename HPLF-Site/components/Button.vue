<template>
  <a :href="href" class="base-button" :style="{background: bgColor}">
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
    },
    bgColor: {
      type: String,
      default: 'black'
    }
  }
}
</script>

<style>
  .base-button {
    display: inline-block;
    padding: 10px 20px;
    color: white;
    text-decoration: none;
    font-size: 2em;
    text-align: center;
  }
</style>