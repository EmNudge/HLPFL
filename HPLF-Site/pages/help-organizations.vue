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
        <Button text="Visit" bgColor="var(--theme-color)"   href="https://www.redcross.org"/>
      </section>
      <section>
        <h2>Direct relief</h2>
        <p>California’s largest international humanitarian nonprofit organization. The organization provides medical assistance to improve the health and lives of people affected by poverty and disaster, both in the United States and throughout the world.</p>
        <Button text="Visit" bgColor="var(--theme-color)" href="https://www.directrelief.org"/>
      </section>
      <section>
        <h2>Coalition for The Homeless</h2>
        <p>Nation's oldest advocacy and direct service organization helping homeless men, women & children; believes that affordable housing, sufficient food, and the chance to work for a living wage are fundamental rights in a civilized society.</p>
        <Button text="Visit" bgColor="var(--theme-color)" href="https://www.coalitionforthehomeless.org"/>
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
  }, 
 
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
