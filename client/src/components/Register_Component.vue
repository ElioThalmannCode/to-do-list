<template>
<div>
<input type="text" v-model="username_input" placeholder="Username">
<input v-model="email_input" placeholder="Email">
<input v-model="password_input" placeholder="Password">
<button type="button" @click="Register_User">Register</button>
<br>
{{ answer }}
</div>
</template>
<script>

import axios from "axios";

export default {
  name: "Register_Component",
  data() {
    return {
    username_input: null,
    email_input: null,
    password_input: null,
    answer: null,
    };
  },
  methods: {
    Register_User: function () {
      const article = {
        username: this.username_input,
        password: this.password_input,
        email: this.email_input,
      };
      axios
        .post("http://localhost:8000/auth/register", article)
        .then(response => {
            this.answer = response.data;
            localStorage.setItem("token", response.data.token);
        })
        .catch(error =>{
            console.log(error);
        })
    },
  },
};
</script>