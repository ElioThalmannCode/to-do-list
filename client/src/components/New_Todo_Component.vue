<template>
  <div>
    <h1>Add Todo</h1>
    <v-text-field color="deep-purple accent-3" v-model="title" label="Title"></v-text-field>
    <v-text-field color="deep-purple accent-3" v-model="description" label="Description"></v-text-field>

    <v-btn color="white--text deep-purple accent-3" @click="add_todo">Add Todo</v-btn>
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
      importance: 1,
      status: 1,
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
          alert("Wrong data or not logged in")
        });
    },
  },
};
</script>