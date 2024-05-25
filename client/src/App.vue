<template>
  <Navbar/>
  <router-view />
</template>
<script lang="">
import { Navbar } from './components';
export default {
  components: {
    Navbar
  }
}
</script>
<style >
body {
  padding: 0 20% 0 20%;
}
</style>
