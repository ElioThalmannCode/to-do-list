<template>
  <div>
    <v-text-field color="primary" v-model="username_input" label="Username"></v-text-field>
    <v-text-field color="primary" type="password" @keyup.enter="Login_User" v-model="password_input" label="Password"></v-text-field>

    <v-btn color="primary" class="white--text" @click="Login_User">submit</v-btn>
  </div>
</template>

<style>
</style>

<script>


export default {
  name: "Login_Component",
  data() {
    return {
    username_input: null,
    password_input: null,
    answer: null,
    };
  },
  methods: {
    Login_User: function () {
      const article = {
        username: this.username_input,
        password: this.password_input,
      };
    this.$store.dispatch('login', article)
    .then(() => {
          this.$router.push('/')
        })
    },
  },
};
</script>



