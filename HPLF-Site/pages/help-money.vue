<template>
  <div class="help-page">
    <Header bgColor="var(--theme-color)" />
    <div class="svg-banner">
      <h1>Donate</h1>
      <TransferMoney />
    </div>
    <div class="donations">
      <section>
        <h2>Donate Housing</h2>
        <p>When it comes to disaster relief, a place to live and take shelter even temporarily can be invaluable.</p>
        <Button text="Donate" bgColor="var(--theme-color)" />
      </section>
      <section>
        <h2>Donate Money</h2>
        <p>Money can be donated for food, essentials, hygeine, and resources. Truly necessary items and expendatures can always be dontated quickly by providing the money with which to buy them.</p>
        <Button text="Donate" bgColor="var(--theme-color)" />
      </section>
      <section>
        <h2>Donate Time</h2>
        <p>If you’re unable to donate money or housing, perhaps you can reache someone else who can. Share this page on social media or in chats to help spread the cause.</p>
        <Button text="Share" bgColor="var(--theme-color)" />
      </section>
    </div>
  </div>
</template>

<script>
import Header from '~/components/Header.vue'
import Button from '~/components/Button.vue'
import TransferMoney from '~/components/SVGs/TransferMoney.vue';

export default {
  components: {
    Button,
    Header,
    TransferMoney,
  }
}
</script>

<style lang="scss">
  .help-page {
    --theme-color: #257BFC;
  }
  .svg-banner {
    text-align: center;
    margin-top: -400px;
    h1 {
      position: relative;
      left: -300px;
      color: white;
      font-size: 4.5em;
      margin-bottom: -20px;
    }
  }
  .donations {
    max-width: 600px;
    margin: 0 auto;
    margin-top: 100px;
    section {
      margin: 60px 20px;
      h2 {
        font-size: 3em;
        margin-bottom: 15px;
        color: var(--theme-color);
      }
      p {
        margin-bottom: 20px;
      }
    }
  }
</style>
