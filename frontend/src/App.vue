<template>
  <div>
    <!-- <img alt="Vue logo" src="./assets/logo.png" /> -->
    <!-- <HelloWorld msg="test" /> -->
    <RegisterImage />
  </div>
</template>

<script>
// import HelloWorld from "./components/HelloWorld.vue";
import RegisterImage from './components/RegisterImage.vue'

export default {
  name: "app",
  components: {
    // HelloWorld,
    RegisterImage
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
