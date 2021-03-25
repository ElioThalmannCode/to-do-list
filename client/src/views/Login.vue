<template>
  <div>
    <h1>Login</h1>
    <Login_Component/>
  </div>
</template>
<script>

import Login_Component from "@/components/Login_Component.vue"

export default {
  name: 'Login',
  components: {
    Login_Component
  }
}
</script>