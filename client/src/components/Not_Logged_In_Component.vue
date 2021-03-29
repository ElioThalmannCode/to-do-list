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
            >
            <h1>
                TodoCreator+
            </h1>
            <p>
                You need to be logged in to use TodoCreator+.
            </p>
            <v-btn-toggle>
            <v-btn to="/login" active>Login</v-btn>
            <v-btn to="/register">Register</v-btn>
            </v-btn-toggle>
            </v-card>
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

