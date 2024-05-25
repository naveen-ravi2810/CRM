<template >
  <nav class="navbar">
    <div class="navbar-logo">
      <img src="https://s3-alpha.figma.com/hub/file/1913095808/a7bdc469-cd70-4ea1-bb57-b59204ad8182-cover.png"/>
    </div>
    <div>
      <ul class="nav-ulist">
        <router-link class="nav-options" v-for="option in options" :to="option.link">{{ option.name }}</router-link>
      </ul>
    </div>
  </nav>
</template>
<script>
export default {
  name: 'Navbar',
  data() {
    return {
      options: [
        {
          name: 'home',
          link: '/home'
        },
        {
          name: 'about',
          link: '/about'
        },
        {
          name: 'Profile',
          link: '/profile'
        },
      ]
    };
  }
}
</script>
<style scoped>
  .navbar-logo img{
    height: 80ox;
    width: 80px;
  }
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .nav-ulist{
    gap: 10px;
    display: flex;
  }
  .nav-options{
    text-decoration: none;
    font-size: 20px;
    color: black;
    text-transform: capitalize;
  }
  .nav-options:hover{
    text-decoration: underline;
  }
</style>