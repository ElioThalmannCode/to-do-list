<template>
  <div>
    <input v-model="username_input" placeholder="Username" />
    <input v-model="password_input" placeholder="Password" />
    <button type="button" @click="Login_User">Login</button>
    <br>
    {{ answer }}
  </div>
</template>

<style>
</style>

<script>

import axios from "axios";

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
      axios
        .post("http://localhost:8000/auth/login", article)
        .then(response => {
            this.answer = response.data;
            console.log(response.data.token)
            localStorage.setItem('token', response.data.token);
        })
        .catch(error =>{
            console.log(error);
        })
    },
  },
};
</script>



