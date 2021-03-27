<template>
  <v-app>
    <v-app-bar
      absolute
      elevate-on-scroll
      scroll-target="#scrolling-techniques-7"
    >
      <v-app-bar-nav-icon
        class="d-flex d-sm-none"
        @click.stop="drawer = !drawer"
      ></v-app-bar-nav-icon>
      <v-btn-toggle
        class="d-none d-sm-flex"
        tile
        color="deep-purple accent-3"
        @click="drawer = !drawer"
      >
        <v-btn to="/"> Home </v-btn>
        <v-btn to="/add_todo"> Add Todo </v-btn>
        <v-btn to="/Login" value="Login"> Login </v-btn>
        <v-btn to="/Register"> Register </v-btn>
      </v-btn-toggle>
      <v-spacer />
      <v-switch
        class="d-none d-sm-flex"
        v-model="darkmode"
        @click="toggle_dark_mode"
        label="Darkmode"
        color="#651fff"
        
      ></v-switch>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list nav dense>
        <v-list-item-group active-class="deep-purple--text text--accent-4">
          <v-list-item to="/" @click="drawer = !drawer">
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>

          <v-list-item to="/add_todo" @click="drawer = !drawer">
            <v-list-item-title>Add Todo</v-list-item-title>
          </v-list-item>

          <v-list-item to="/Login" @click="drawer = !drawer">
            <v-list-item-title>Login</v-list-item-title>
          </v-list-item>

          <v-list-item to="/Register" @click="drawer = !drawer">
            <v-list-item-title>Register</v-list-item-title>
          </v-list-item>

        </v-list-item-group>
        <v-spacer />
        <v-switch
        class="mamamam"
        mt-5
        v-model="darkmode"
        @click="toggle_dark_mode"
        label="Darkmode"
        color="#651fff">
        </v-switch>
      </v-list>
    </v-navigation-drawer>

    <v-content style="margin-top: 70px">
      <v-container>
        <router-view />
      </v-container>
    </v-content>

    <v-footer padless>
      <v-col class="text-center" cols="12">
        {{ new Date().getFullYear() }} — <strong>Elio Thalmann</strong>
      </v-col>
    </v-footer>
  </v-app>
</template>
<script>
export default {
name: "App",
  data() {
    return {
      drawer: false,
      darkmode: true
    };
  },
  methods: {
  toggle_dark_mode: function() { 
    this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
    this.darkmode = this.$vuetify.theme.dark
    }}
};
</script>
