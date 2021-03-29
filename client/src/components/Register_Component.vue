<template>
  <div>
    <v-text-field color="deep-purple accent-3" v-model="username_input" label="Username"></v-text-field>
    <v-text-field color="deep-purple accent-3" v-model="email_input" label="E-mail"></v-text-field>
    <v-text-field
      type="password"
      @keyup.enter="Register_User"
      v-model="password_input"
      label="Password"
      color="deep-purple accent-3"
    ></v-text-field>

    <v-btn class="white--text" color="deep-purple accent-3" @click="Register_User">submit</v-btn>
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
        .then((response) => {
          this.answer = response.data;
          localStorage.setItem("token", response.data.token);
          this.$router.push("/");
        })
        .catch((error) => {
          console.log(error);
          alert("Please enter valid data!");
        });
    },
  },
};
</script>
