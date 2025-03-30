<template>
  <router-view></router-view>

</template>

<script>

export default {
name: 'App',
methods: {
  goBack() {
    this.$router.go(-1); // Navigates to the previous page
  },
},

};
</script>

<style>
</style>
