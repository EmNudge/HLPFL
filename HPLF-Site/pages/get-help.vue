<template>
  <div>
    <header>
      <h1>HLPFL</h1>
    </header>
    <div class="msg-container">
      <div class="message">Speak Or Type To Get Help</div>
    </div>
    <div class="messages">

    </div>
    <VoiceInput />
  </div>
</template>

<script>
import VoiceInput from '~/components/VoiceInput.vue'

export default {
  components: {
    VoiceInput
  }
}
</script>

<style lang="scss" scoped>
header {
  h1 {
    font-size: 2.5em;
  }
  background: #38905B;
  color: white;
  text-align: center;
  padding: 40px 0;
  padding-bottom: 80px;
}
.msg-container {
  display: flex;
  justify-content: center;
  margin-top: -40px;
  font-size: 1.5em;
  .message {
    position: relative;
    z-index: 2;
    color: white;
    background: #2A6C44;
    padding: 30px 10px;
    display: inline-block;
    width: 500px;
    margin: 0 auto;
    text-align: center;
    border-radius: 50px;
  }
}
</style>
