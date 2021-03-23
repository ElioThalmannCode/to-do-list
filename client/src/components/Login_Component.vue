<template>
  <div>
      {{ Antwort }}
  </div>
</template>

<style>

</style>>
<script>
import axios from "axios";

export default {
  name: 'Login',
  data() {
    return {
      Antwort: null
    };
  },

created() {
  // Simple POST request with a JSON body using axios
  const article = { username: "levin2", password: "fortwenty4202", email: "fortwenty4202@gmail.com" };
  axios.post("http://localhost:8000/auth/register", article)
    .then(response => console.log(response));
} };


</script>



