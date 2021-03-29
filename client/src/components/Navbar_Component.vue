<template>
  <div>
    <v-app-bar
      absolute
      elevate-on-scroll
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
        class="d-none d-sm-flex slider"
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
        mt-5
        v-model="darkmode"
        @click="toggle_dark_mode"
        label="Darkmode"
        color="#651fff">
        </v-switch>
      </v-list>
    </v-navigation-drawer>
    </div>
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
<style scoped>
.slider {
margin-top: 20px !important;;
}
</style>