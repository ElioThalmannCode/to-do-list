<template>
  <h1>Todos</h1>
</template>

<script>

import axios from "axios";

export default {
  name: "Todo_Component",
  data() {
    return {};
  },
  created() {
    axios
      .get(`http://localhost:8000/todo`, { headers: { "content-type": "application/json", token: ("token " + localStorage.getItem('token')) } })
      .then((response) => {
        console.log(response.data)
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>