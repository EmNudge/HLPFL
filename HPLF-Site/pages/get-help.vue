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
    <div class="input-container">
      <VoiceInput 
        :isActive="isActive" 
        @click="() => isActive = !isActive" 
      />
    </div>
  </div>
</template>

<script>
import VoiceInput from '~/components/VoiceInput.vue'

export default {
  data() {
    return { 
      isActive: false,
    }
  },
  methods:{
   
  handleMicClick() {
    if (this.state.audioSource === 'mic') {
      this.stopTranscription();
      return;
    }
    this.reset();
    this.setState({ audioSource: 'mic' });

    // The recognizeMicrophone() method is a helper method provided by the watson-speech package
    // It sets up the microphone, converts and downsamples the audio, and then transcribes it
    // over a WebSocket connection
    // It also provides a number of optional features, some of which are enabled by default:
    //  * enables object mode by default (options.objectMode)
    //  * formats results (Capitals, periods, etc.) (options.format)
    //  * outputs the text to a DOM element - not used in this demo because it doesn't play nice
    // with react (options.outputElement)
    //  * a few other things for backwards compatibility and sane defaults
    // In addition to this, it passes other service-level options along to the RecognizeStream that
    // manages the actual WebSocket connection.
    this.handleStream(recognizeMicrophone(this.getRecognizeOptions()));
  },

  handleStream(stream) {
    console.log(stream);
    // cleanup old stream if appropriate
    if (this.stream) {
      this.stream.stop();
      this.stream.removeAllListeners();
      this.stream.recognizeStream.removeAllListeners();
    }
    this.stream = stream;
    this.captureSettings();

    // grab the formatted messages and also handle errors and such
    stream.on('data', this.handleFormattedMessage).on('end', this.handleTranscriptEnd).on('error', this.handleError);

    // when errors occur, the end event may not propagate through the helper streams.
    // However, the recognizeStream should always fire a end and close events
    stream.recognizeStream.on('end', () => {
      if (this.state.error) {
        this.handleTranscriptEnd();
      }
    });

    // grab raw messages from the debugging events for display on the JSON tab
    stream.recognizeStream
      .on('message', (frame, json) => this.handleRawMessage({ sent: false, frame, json }))
      .on('send-json', json => this.handleRawMessage({ sent: true, json }))
      .once('send-data', () => this.handleRawMessage({
        sent: true, binary: true, data: true, // discard the binary data to avoid waisting memory
      }))
      .on('close', (code, message) => this.handleRawMessage({ close: true, code, message }));

    // ['open','close','finish','end','error', 'pipe'].forEach(e => {
    //     stream.recognizeStream.on(e, console.log.bind(console, 'rs event: ', e));
    //     stream.on(e, console.log.bind(console, 'stream event: ', e));
    // });
  },
  async asyncData({req}) {
    const url = `${req.protocol}://${req.get('host')}`;
    const jsonData = await fetch(url + '/api/voice');
    const { serviceUrl, token } = await jsonData.json();
    return { token }
  },
   handleFormattedMessage(msg) {
    const { formattedMessages } = this.state;
    this.setState({ formattedMessages: formattedMessages.concat(msg) });
  },
  handleTranscriptEnd() {
    // note: this function will be called twice on a clean end,
    // but may only be called once in the event of an error
    this.setState({ audioSource: null });
  },
  componentDidMount() {
    this.fetchToken();
    // tokens expire after 60 minutes, so automatcally fetch a new one ever 50 minutes
    // Not sure if this will work properly if a computer goes to sleep for > 50 minutes
    // and then wakes back up
    // react automatically binds the call to this
    // eslint-disable-next-line
    this.setState({ tokenInterval: setInterval(this.fetchToken, 50 * 60 * 1000) });
  },

  },
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
.input-container {
  display: flex;
  justify-content: center;
}
</style>
