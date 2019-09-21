<template>
  <div>
    <header>
      <h1><a href="/">HLPFL</a></h1>
    </header>
    <div class="msg-container">
      <div class="message">Speak Or Type To Get Help</div>
    </div>
    <div class="messages">
      <Messages 
        :userMsgs="userMsgs"
        :botMsgs="botMsgs"
      />
    </div>
    {{msg}}
    <div class="input-container">
      <VoiceInput 
        v-model="userInput"
        :isActive="isActive" 
        @click="handleMicClick" 
        @submit="handleSubmit"
      />
    </div>
  </div>
</template>

<script>
import VoiceInput from '~/components/VoiceInput.vue'
import Messages from '~/components/Messages.vue'
import recognizeMicrophone from 'watson-speech/speech-to-text/recognize-microphone';

export default {
  data() {
    return { 
      userInput: '',
      isActive: false,
      userMsgs: ['hello', 'goodbye'],
      // watson state
      model: 'en-US_BroadbandModel',
      msg: '',
      formattedMessages: [],
      stream: null,
    }
  },
  methods: {
    handleSubmit() {
      this.userMsgs.push(this.userInput)
      this.userInput = "";
    },
    handleMicClick() {
      if (this.isActive) {
        this.isActive = false;
        if (this.stream) this.strean.stop();
        return;
      }

      this.isActive = true;

      const stream = recognizeMicrophone({
        token: this.token,
      });
      return;
      if (this.stream) {
        this.stream.stop();
        this.stream.removeAllListeners();
        this.stream.recognizeStream.removeAllListeners();
      }
      this.stream = stream;

      stream
        .on('data', msg => this.msg += msg)
        .on('end', () => {
          if (this.stream) this.stream.stop();
          this.isActive = false
        })
        .on('error', err => console.log(err));
    }
  },
  async asyncData({req}) {
    // const url = `${req.protocol}://${req.get('host')}`;
    // const jsonData = await fetch(url + '/api/v1/credentials');
    // const { serviceUrl, token } = await jsonData.json();
    // return { token }
  },
  computed: {
    botMsgs() {
      const msgs = this.userMsgs.map(msg => {
        const arr = msg.split('');
        arr.reverse();
        return arr.join('');
      });
      return ['HI!', ...msgs];
    }
  },
  components: {
    VoiceInput,
    Messages
  }
}
</script>

<style lang="scss" scoped>
header {
  h1 {
    font-size: 2.5em;
    a {
      color: white;
      text-decoration: none;
    }
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
.input-container {
  display: flex;
  justify-content: center;
}
.messages {
  margin: 40px auto;
  max-width: 400px;
}
</style>
