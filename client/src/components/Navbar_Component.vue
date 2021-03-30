<template>
  <div>
    <v-app-bar height="50px" absolute elevate-on-scroll>
      <v-app-bar-nav-icon
        class="d-flex d-sm-none"
        @click.stop="drawer = !drawer"
      ></v-app-bar-nav-icon>
      <v-tabs
        borderless
        tile
        class="d-none d-sm-flex"
        color="primary"
        @click="drawer = !drawer"
      >
        <v-tab to="/"> Home </v-tab>
        <v-tab v-if="!isLoggedIn" to="/add_todo"> Add Todo </v-tab>
        <v-tab v-if="isLoggedIn" to="/Login" value="Login"> Login </v-tab>
        <v-tab v-if="isLoggedIn" to="/Register"> Register </v-tab>
        <v-tab v-if="!isLoggedIn" @click="logout"> logout </v-tab>
      </v-tabs>
      <v-spacer />
      <v-btn icon href="https://github.com/ElioThalmannCode/to-do-liste" color="#252525" dark><v-icon>$vuetify.icons.custom</v-icon></v-btn>
      <v-menu  bottom left>
        
        <template class="d-none d-sm-flex" v-slot:activator="{ on, attrs }">
          <v-btn class="d-none d-sm-flex" icon v-bind="attrs" v-on="on">
            <v-icon>{{ icons.mdiCogOutline }}</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item>
            <v-switch
              class="d-none d-sm-flex slider"
              v-model="darkmode"
              @click="toggle_dark_mode"
              label="Darkmode"
            ></v-switch>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list nav dense>
        <v-list-item-group active-class="primary--text text--accent-4">
          <v-list-item to="/" @click="drawer = !drawer">
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>

          <v-list-item
            v-if="!isLoggedIn"
            to="/add_todo"
            @click="drawer = !drawer"
          >
            <v-list-item-title>Add Todo</v-list-item-title>
          </v-list-item>

          <v-list-item v-if="isLoggedIn" to="/Login" @click="drawer = !drawer">
            <v-list-item-title>Login</v-list-item-title>
          </v-list-item>

          <v-list-item
            v-if="isLoggedIn"
            to="/Register"
            @click="drawer = !drawer"
          >
            <v-list-item-title>Register</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="!isLoggedIn" @click="logout">
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
        <v-spacer />
        <v-switch
          mt-5
          v-model="darkmode"
          @click="toggle_dark_mode"
          label="Darkmode"
          color="primary"
        >
        </v-switch>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>
<script>

import { mdiCogOutline } from '@mdi/js'; 
export default {
  name: "App",
  data() {
    return {
      drawer: false,
      darkmode: true,
          icons: {
      mdiCogOutline,
    },
    };
  },
  computed: {
    isLoggedIn: function () {
      return !this.$store.getters.isLoggedIn;
    },
  },
  methods: {
    logout: function () {
      this.$store.dispatch("logout").then(() => {
        this.$router.push("/");
      });
    },
    toggle_dark_mode: function () {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
      this.darkmode = this.$vuetify.theme.dark;
    },
  },
};
</script>
<style scoped>
.slider {
  margin-top: 20px !important;
}
</style>