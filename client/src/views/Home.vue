<template>
  <div>
    <h1>Home</h1>
    <Todo_Component/>
  </div>
</template>
<script>

import Todo_Component from "@/components/Todo_Component.vue"

export default {
  name: 'Home',
  components: {
      Todo_Component
  }
}
</script>