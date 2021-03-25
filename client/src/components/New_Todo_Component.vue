<template>
  <div>
    <input v-model="title" placeholder="title" />
    <input v-model="description" placeholder="description" />
    <input v-model="importance" placeholder="importance" />
    <input v-model="status" placeholder="status" />
    <button type="button" @click="add_todo">new todo</button>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "New_Post_Component",
  data() {
    return {
      title: null,
      description: null,
      importance: null,
      status: null,
    };
},  methods: {
    add_todo: function () {
      const article = {
        title: this.title,
        description: this.description,
        importance: this.importance,
        status: this.status,
        creator: "x"
      };
      axios
        .post("http://localhost:8000/todo/", article, {headers: {Authorization: ("Token " + (localStorage.getItem("token"))),}})
        .then((response) => {
          console.log(response)
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>