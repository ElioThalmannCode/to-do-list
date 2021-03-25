<template>
  <div id="app">
    <v-app>

        <v-app-bar absolute  elevate-on-scroll scroll-target="#scrolling-techniques-7">
          <v-btn-toggle tile color="deep-purple accent-3"  group>
            <v-btn to="/" value="Home">
              Home
            </v-btn>
          <v-btn to="/add_todo">
              Add Todo
            </v-btn>
  
            <v-btn to="/Login" value="Login">
              Login
            </v-btn>
  
            <v-btn to="/Register">
              Register
            </v-btn>

          </v-btn-toggle>
  
        </v-app-bar>
        <v-content style= "margin-top: 70px" >
          <v-container>
            <router-view />
            <h1>{{ this.isAuth }}</h1>
          </v-container>
          </v-content>
 
      <v-footer  padless>
      <v-col
        class="text-center"
        cols="12"
      >
        {{ new Date().getFullYear() }} — <strong >Elio Thalmann</strong>
      </v-col>
    </v-footer>
    </v-app>
  </div>
</template>

<script>
export default {
  name: "App",

  components: {},
    data() {
    return {
    };
  },
  methods: {
    }}