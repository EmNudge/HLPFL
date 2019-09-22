<template>
  <div class="help-page">
    <header>
      <h1>HLPFL</h1>
      <div class="motto">
        <h2>Protect.</h2>
        <h2>Prevent.</h2>
        <h2>Persevere.</h2>
      </div>
    </header>
    <div class="buttons">
      <Button text="Help" bgColor="#861717" href="/help-money" />
      <Button text="Get Help" bgColor="#861717" href="/get-help" />
    </div>
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
    padding-bottom: 100px;

    h1 {
      text-align: center;
      font-size: 4em;
    }
    display: flex;
    flex-direction: column;
    align-items: center;
    .motto {
      margin-top: 100px;
      h2 {
        font-size: 2em;
        position: relative;
        &:nth-child(1) { left: -100px; }
        &:nth-child(3) { left: 100px; }
      }
    }
  }

  .buttons {
    max-width: 300px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding-top: 40px;
    > * {
      margin: 20px;
    }
  }
</style>
