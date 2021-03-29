<template>
<div>
    <h1>
    Todos:
    </h1>
    <br>
  <v-simple-table>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">Name</th>
          <th class="text-left">Beschreibung</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in todos" :key="item.name">
          <td>{{ item.title }}</td>
          <td>{{ item.description }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Home",
  components: {},
  data() {
    return {
      todos: null,
    };
  },
  mounted() {
    axios
      .get("http://localhost:8000/todo/", {
        headers: { Authorization: "Token " + localStorage.getItem("token") },
      })
      .then((response) => {
        this.todos = response.data;
      })
      .catch((error) => {
        console.log(error);
        this.$router.push("/login");
      });
  },
};
</script>