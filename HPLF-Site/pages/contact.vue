<template>
  <div class="help-page">
    <Header bgColor="var(--theme-color)" />
    <div class="svg-banner">
      <h1>Contact</h1>
    </div>
    <div class="donations">
      <p>To make larger donations or offers (for housing or otherwise), feel free to contact us at <br>contatc@hlpfl.health</p>
    </div>
  </div>
</template>

<script>
import Header from '~/components/Header.vue'
import Button from '~/components/Button.vue'
import Wheatherman from '~/components/SVGs/Wheatherman.vue';

export default {
  components: {
    Button,
    Header,
    Wheatherman,
  }
}
</script>

<style lang="scss">
  .help-page {
    --theme-color: #FC5825;
  }
  .svg-banner {
    text-align: center;
    margin-bottom: -100px;

    h1 {
      color: white;
      font-size: 4.5em;
      position: relative;
      top: -300px;
    }
  }
  .donations {
    max-width: 600px;
    margin: 0 auto;
    margin-top: 100px;
    p {
      text-align: center;
      font-size: 1.5em;
    }
  }
</style>
