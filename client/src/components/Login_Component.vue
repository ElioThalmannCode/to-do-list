<template>
  <div>
    <v-text-field v-model="username_input" label="Name"></v-text-field>
    <v-text-field type="password" @keyup.enter="Login_User" v-model="password_input" label="Password"></v-text-field>

    <v-btn @click="Login_User">submit</v-btn>
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
            localStorage.setItem("isAuthenticated", JSON.stringify("yes"));
            this.$router.push('/');
        })
        .catch(error =>{
            console.log(error);
            alert("Wrong Login Data")
        })
    },
  },
};
</script>



