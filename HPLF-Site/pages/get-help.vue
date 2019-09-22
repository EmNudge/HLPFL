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
      userMsgs: [''],
      botMsgs: ['Hello. How may I be of service?'],
      // watson state
      model: 'en-US_BroadbandModel',
      formattedMessages: [],
      stream: null,
    }
  },
  methods: {
    handleSubmit() {
      this.userMsgs.push(this.userInput);
      const sentence = this.userInput;
      this.userInput = "";

      fetch(this.url + '/api/chat', {
        method: 'POST', 
        mode: 'cors',
        cache: 'no-cache', 
        credentials: 'same-origin', 
        headers: {
          'Content-Type': 'application/json',
        },
        redirect: 'follow',
        referrer: 'no-referrer',
        body: JSON.stringify({sentence}),
      }).then(async res => {
        const message = await res.json();
        this.botMsgs.push(message.response);
      })
    },
    handleMicClick() {
      if (this.isActive) {
        setTimeout(this.handleSubmit, 500);
        this.isActive = false;
        if (this.stream) this.stream.stop();
        return;
      }

      this.isActive = true;
      const { access_token } = this;
      const stream = recognizeMicrophone({ access_token });

      if (this.stream) {
        this.stream.stop();
        this.stream.removeAllListeners();
        this.stream.recognizeStream.removeAllListeners();
      }
      
      this.stream = stream;

      stream
        .on('data', msg => {
          console.log('GETTING DATA')
          this.userInput += msg
        })
        .on('end', () => {
          if (this.stream) this.stream.stop();
          this.isActive = false
        })
        .on('error', err => console.log(err));
    }
  },
  async asyncData({req}) {
    const url = `${req.protocol}://${req.get('host')}`;
    const jsonData = await fetch(url + '/api/voice');
    const { serviceUrl, access_token } = await jsonData.json();
    return { access_token, url }
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