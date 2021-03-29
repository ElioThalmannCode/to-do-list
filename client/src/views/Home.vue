<template>
  <div>
  <Alltodos_Component></Alltodos_Component>
  </div>
</template>
<script>

import Alltodos_Component from '@/components/Alltodos_Component.vue';



export default {
  name: "Home",
  components: {
    Alltodos_Component
  },
  data() {
    return {
    };
  },
};
</script>