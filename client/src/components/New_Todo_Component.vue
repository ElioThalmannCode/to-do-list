<template>
  <div>
    <h1>Add Todo</h1>
    <v-text-field v-model="title" label="Name"></v-text-field>
    <v-text-field v-model="description" label="Description"></v-text-field>
    <v-text-field v-model="importance" label="Importance"></v-text-field>
    <v-text-field v-model="status" label="Status"></v-text-field>

    <v-btn @click="add_todo">Add Todo</v-btn>
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
          this.$router.push('/');
        })
        .catch((error) => {
          console.log(error);
          this.$router.push('/login');
        });
    },
  },
};
</script>