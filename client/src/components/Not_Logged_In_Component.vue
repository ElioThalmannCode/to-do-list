<template>
        <v-col cols="12">
          <v-row
            align="center"
            justify="center"
            style="height: 200px;"
            class="text-center"
          >
            <v-card
              class="ma-3 pa-6"
              rounded
            >
            <h1>
                TodoCreator+
            </h1>
            <p>
                TodoCreator+ is a tool created to make Todos. <br> Its easy to use, accessible, open source and of course free. <br> Check out our <a href="https://github.com/ElioThalmannCode/to-do-liste">Github</a>.
            </p>
            <p>
                You need to be logged in to use TodoCreator+.
            </p>
            <v-btn-toggle>
            <v-btn to="/login" active>Login</v-btn>
            <v-btn to="/register">Register</v-btn>
            </v-btn-toggle>
            <br>
            <v-btn class="ma-2" color="#252525" dark><v-icon>$vuetify.icons.custom</v-icon>github</v-btn>
            </v-card>
          </v-row>
          <v-row>
            </v-row>
          </v-col>
</template>
<script>
export default {
name: "Not_Logged_In_Component",
  components: {
  },  
}
</script>

<v-icon>$vuetify.icons.custom</v-icon>