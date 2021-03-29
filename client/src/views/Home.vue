<template>
  <div>
  <Alltodos_Component v-if="!isLoggedIn"  />
  <Not_Logged_In_Component v-if="isLoggedIn" />
  </div>
</template>
<script>

import Alltodos_Component from '@/components/Alltodos_Component.vue';
import Not_Logged_In_Component from '@/components/Not_Logged_In_Component.vue';


export default {
  name: "Home",
  components: {
    Alltodos_Component,
    Not_Logged_In_Component
  },
  computed : {
      isLoggedIn : function(){ return !this.$store.getters.isLoggedIn}
    },
  data() {
    return {
    };
  },
};
</script>