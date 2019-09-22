<template>
  <header :style="{background: bgColor}">
    <a class="logo" href="/">
      <h1>HLPFL</h1>
      <span>helper</span>
    </a>
    <nav>
      <a href="/help-money">
        <span>Donations</span>
      </a>
      <a href="/help-disasters">
        <span>Disasters</span>
      </a>
      <a href="/help-organizations">
        <span>Organizations</span>
      </a>
      <a href="/contact">
        <span>Contact</span>
      </a>
    </nav>
  </header>
</template>

<script>
export default {
  props: {
    bgColor: {
      type: String,
    }
  }
}
</script>

<style lang="scss">
  header {
    display: flex;
    justify-content: space-between;
    color: white;
    padding: 40px 60px;
    padding-bottom: 450px;
    > a {
      color: white;
      text-decoration: none;
    }
    
    nav {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      grid-gap: 20px;
      align-items: center;
      justify-content: center;
      a {
        text-decoration: none;
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
      }
      
    }
  }
</style>