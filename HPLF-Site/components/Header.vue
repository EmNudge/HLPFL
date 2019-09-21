<template>
  <header>
    <div class="logo">
      <h1>HLPFL</h1>
      <span>helper</span>
    </div>
    <nav>
      <div><a href="#">Current Disasters</a></div>
      <div><a href="#">Organizations</a></div>
      <div><a href="#">Contact</a></div>
    </nav>
  </header>
</template>

<script>
export default {

}
</script>

<style lang="scss">
  header {
    display: flex;
    justify-content: space-between;

    nav {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
    }
  }
</style>