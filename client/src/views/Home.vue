<template>
  <div>
  <Single_Todo_Component v-bind:data=todo v-for="todo in todos" :key="todo.id"></Single_Todo_Component>
  </div>
</template>
<script>

import axios from "axios";
import Single_Todo_Component from '@/components/Single_Todo_Component.vue';



export default {
  name: "Home",
  components: {
    Single_Todo_Component
  },
  data() {
    return {
      todos: null,
    };
  },
  mounted() {
          axios
        .get("http://localhost:8000/todo/", {headers: {Authorization: ("Token " + (localStorage.getItem("token"))),}})
        .then((response) => {
          this.todos = (response.data);
        })
        .catch((error) => {
          console.log(error);
          this.$router.push('/login');
        });
  },
};
</script>