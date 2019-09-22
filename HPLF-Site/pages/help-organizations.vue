<template>
  <div class="help-page">
    <Header bgColor="var(--theme-color)" />
    <div class="svg-banner">
      <h1>Organizations</h1>
      <Organizations />
    </div>
    <div class="donations">
      <section>
        <h2>Red Cross</h2>
        <p>A humanitarian organization that provides emergency assistance, disaster relief, and disaster preparedness education throughout the United States.</p>
        <Button text="Visit" bgColor="var(--theme-color)" />
      </section>
      <section>
        <h2>Miami Relief Org</h2>
        <p>Local disaster relief organization providing shelter, food, and supplies for peoples and families affected by drastic conditions.</p>
        <Button text="Visit" bgColor="var(--theme-color)" />
      </section>
      <section>
        <h2>Gocinco of Oregon</h2>
        <p>State wide humanitarian organizatiion with the interum disturbed inside furthering the movement of populous in order of a desctructive magnitude.</p>
        <Button text="Visit" bgColor="var(--theme-color)" />
      </section>
    </div>
  </div>
</template>

<script>
import Header from '~/components/Header.vue'
import Button from '~/components/Button.vue'
import Organizations from '~/components/SVGs/Organizations.vue';

export default {
  components: {
    Button,
    Header,
    Organizations,
  }
}
</script>

<style lang="scss">
  .help-page {
    --theme-color: #FCB325;
  }
  .svg-banner {
    text-align: center;
    margin-top: -400px;
    h1 {
      position: relative;
      left: -150px;
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
