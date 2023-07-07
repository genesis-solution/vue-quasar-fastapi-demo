<template>
    <div v-if="show">
      <p>{{ message }}</p>
      <!-- <button @click="show = false">Close</button> -->
    </div>
  </template>
  
  <script>
  export default {
    props: {
      message: {
        type: String,
        required: true
      }
    },
    data() {
      return {
        show: true
      }
    }
  }
  </script>