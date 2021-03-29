<template>
  <v-app>
    <Navbar_Component />
    <v-content style="margin-top: 70px">
      <v-container>
        <router-view />
      </v-container>
    </v-content>
    <Footer_Component />
  </v-app>
</template>

<script>
import Navbar_Component from '@/components/Navbar_Component.vue'
import Footer_Component from '@/components/Footer_Component.vue'
export default {
  name: "App",
  components: {
    Navbar_Component,
    Footer_Component,
  },

};

</script>