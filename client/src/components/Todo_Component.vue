<template>
  <div>
    <h1>Todos</h1>
    
  </div>
</template>

<script>

import axios from "axios";

export default {
  name: "Todo_Component",
  data() {
    return {
      todos: null,
    };
  },
  mounted() {
          axios
        .get("http://localhost:8000/todo/")
        .then((response) => {
          console.log(response)
          this.todos = (response.data);
        })
        .catch((error) => {
          console.log(error);
        });
  },
};
</script>