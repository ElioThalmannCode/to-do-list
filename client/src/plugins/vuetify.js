import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);


import Githubsvg_Component from "@/components/Githubsvg_Component.vue"
export default new Vuetify({
    theme: { dark: true },
    icons: {
      values: {
        custom: {
          component: Githubsvg_Component,
        },
      },
    },
  })