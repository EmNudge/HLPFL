<template>
  <div class="messages-container">
    <div 
      v-for="msg in messages" 
      :key="msg.msg"
      :class="msg.type + '-message'"
    >{{msg.msg}}</div>
  </div>
</template>

<script>
export default {
  props: {
    userMsgs: {
      type: Array,
      default: []
    },
    botMsgs: {
      type: Array,
      default: []
    },
  },
  computed: {
    messages() {
      const newMsgs = [];
      for (const [index, msg] of this.userMsgs.entries()) {
        if (msg) newMsgs.push({msg, type: 'bot'});
        const userMsg = this.botMsgs[index];
        if (userMsg) newMsgs.push({msg: userMsg, type: 'user'});
      }
      return newMsgs;
    }
  }
}
</script>

<style lang="scss">
.messages-container {
  font-size: 1.25em;
  height: 300px;
  overflow-y: scroll;
  padding: 0 20px;

  > * {
    padding: 10px 0;
  }
  
  .bot-message {
    color: green;
    text-align: right;
  }
  .user-message {
    text-align: left;
  }
}
</style>