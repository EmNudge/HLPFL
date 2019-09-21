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
      for (const [index, msg] of this.botMsgs.entries()) {
        if (msg) newMsgs.push({msg, type: 'bot'});
        const userMsg = this.userMsgs[index];
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

  > * {
    padding: 10px 0;
  }
  
  .bot-message {
    color: green;
    text-align: left;
  }
  .user-message {
    text-align: right;
  }
}
</style>