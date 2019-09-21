<template>
  <div class="container">
    <img src="~static/main_bg.jpg" alt="disaster">
    <h1>HLPFL</h1>
    <div class="tagline">
      <p>Protect.</p>
      <p>Prevent.</p>
      <p>Persevere.</p>
    </div>
    <div class="buttons">
      <Button text="Help" />
      <Button text="Get Help" />
    </div>
  </div>
</template>

<script>
import Button from '~/components/Button.vue'

export default {
  components: {
    Button
  }
}
</script>

<style lang="scss">
  .container {
    position: relative;
    width: 100vw;
    height: 100vh;
    padding-top: 25vw;
    padding-left: 30vw;
    > * { position: relative; }

    img {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
    }
    h1 {
      position: absolute;
      top: 50px;
      left: 50px;
    }
    .tagline {
      position: relative;
      font-size: 4em;
      color: white;
      font-weight: bold;
      margin-bottom: 70px;
    }

    .buttons {
      display: flex;
      flex-direction: column;
      width: 200px;

      > a:nth-child(1) {
        position: relative;
        left: -80px;
      }
      > a:nth-child(2) {
        position: relative;
        right: -80px;
      }
    }
  }
</style>
