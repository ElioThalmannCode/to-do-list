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
          <th class="text-left">Todo</th>
          <v-spacer />
          <th small class="text-left"><v-layout justify-end>Aktionen</v-layout></th>
        </tr>
      </thead>
      <tbody>
        <tr @click="overlay = !overlay,id_item = item" v-for="item in todos" :key="item.id">
          <td>{{ item.title }}</td>
          <v-spacer />
          <td><v-layout justify-end><v-btn large @click="delete_post(item.id)" icon>
        <v-icon>{{ icons.mdiDelete }}</v-icon>
      </v-btn></v-layout></td>

        </tr>
      </tbody>
    </template>
  </v-simple-table>
  <v-overlay :value="overlay">
    <v-card
      class="mx-auto"
      max-width="600"
      outlined
    >
<v-simple-table>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">Name</th>
          <th class="text-left">Beschreibung</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{ id_item.title }}</td>
          <td>{{ id_item.description }}</td>

        </tr>
      </tbody>
    </template>
  </v-simple-table>
  <v-card-actions>
        <v-btn @click="delete_post(id_item.id), overlay = false">
        <v-icon>{{ icons.mdiDelete }}</v-icon>
      Delete</v-btn>
      <v-spacer />
      <v-btn
          @click="overlay = false"
        >Close
          <v-icon right>mdi-close</v-icon>
        </v-btn>
      </v-card-actions>

    </v-card>
      </v-overlay>
  </div>
</template>

<script>
import { mdiDelete } from '@mdi/js'; 
import axios from "axios";
export default {
  name: "Home",
  components: {},
  data() {
    return {
      todos: null,
      overlay: false,
      id_item: "x",
      icons: {
      mdiDelete,
    },
    };
  },
    methods: {
    delete_post: function (id) {
    axios.defaults.headers.common['Authorization'] = this.$store.getters.gettoken
    axios
      .delete("http://localhost:8000/todo/" + id + "/")
      .then((response) => {
        console.log(response.data);
        this.load_data()
      })
      .catch((error) => {
        console.log(error);
        if (error.response.status == 401) {
          this.$store.dispatch('logout')
        }
      });
    },
    load_data: function() {
    axios.defaults.headers.common['Authorization'] = this.$store.getters.gettoken
    axios
      .get("http://localhost:8000/todo/")
      .then((response) => {
        this.todos = response.data;
      })
      .catch((error) => {
        console.log(error);
        if (error.response.status == 401) {
          this.$store.dispatch('logout')
        }
      });
    }
  },
  mounted() {
    this.load_data()
  },
};
</script>