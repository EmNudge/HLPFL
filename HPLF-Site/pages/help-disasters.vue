<template>
  <div class="help-page">
    <Header bgColor="var(--theme-color)" />
    <div class="svg-banner">
      <h1>Disasters</h1>
      <Wheatherman />
    </div>
    <div class="donations">
      <section v-for="disaster in disasters" :key="disaster.summary">
        <h2>{{disaster.event}} - {{disaster.location}}</h2>
        <a :href="disaster.url" class="small">{{disaster.url}}</a>
        <p>{{disaster.summary}}</p>
        <Button text="View Article" :href="disaster.url" bgColor="var(--theme-color)" />
      </section>
    </div>
  </div>
</template>

<script>
import Header from '~/components/Header.vue'
import Button from '~/components/Button.vue'
import Wheatherman from '~/components/SVGs/Wheatherman.vue';
import firestoreDB from '~/plugins/firebase';

export default {
  async asyncData({isDev, route, store, env, params, query, req, res, redirect, error}) {
    const disasters = await firestoreDB.collection("disasters").get();
    const distatersData = [];
    disasters.forEach(disaster => distatersData.push(disaster.data()))
    distatersData.sort((a, b) => a.count - b.count);

    return { disasters: distatersData }
  },
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
    margin-top: -400px;
    h1 {
      position: relative;
      left: -250px;
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
        margin-bottom: 5px;
        color: var(--theme-color);
      }
      a.small {
        font-size: .6em;
        margin-top: -6px;
        margin-bottom: 20px;
        display: block;
        text-decoration: none;
        color: black;
      }
      p {
        margin-bottom: 20px;
      }
    }
  }
</style>
