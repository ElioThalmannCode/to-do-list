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
  mounted() {
    axios
      .get(`http://localhost:8000/todo`)
      .then((response) => {
        console.log(response.data)
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>