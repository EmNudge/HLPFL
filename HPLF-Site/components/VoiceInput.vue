<template>
  <div class="voice-input">
    <input type="text" placeholder="Type here...">
    <button>
      <svg width="56" height="76" viewBox="0 0 56 76" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path fill-rule="evenodd" clip-rule="evenodd" d="M28 47.7917C34.5017 47.7917 39.7109 42.5434 39.7109 36.0417L39.75 12.5417C39.75 6.04008 34.5017 0.791748 28 0.791748C21.4984 0.791748 16.25 6.04008 16.25 12.5417V36.0417C16.25 42.5434 21.4984 47.7917 28 47.7917ZM23.3002 12.1499C23.3002 9.56494 25.4152 7.44994 28.0002 7.44994C30.5852 7.44994 32.7002 9.56494 32.7002 12.1499L32.661 36.4333C32.661 39.0183 30.5852 41.1333 28.0002 41.1333C25.4152 41.1333 23.3002 39.0183 23.3002 36.4333V12.1499ZM28 56.0167C38.81 56.0167 48.7584 47.7917 48.7584 36.0417H55.4167C55.4167 49.4367 44.7634 60.4817 31.9167 62.3617V75.2084H24.0834V62.3617C11.2367 60.4426 0.583374 49.3976 0.583374 36.0417H7.24171C7.24171 47.7917 17.19 56.0167 28 56.0167Z" fill="black" fill-opacity="0.54"/>
      </svg>
    </button>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>
  .voice-input {
    input {
      padding: 20px 10px;
      box-shadow: 4px 0px 6px grey;
      font-size: 1.5em;
    }
  }
</style>