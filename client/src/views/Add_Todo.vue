<template>
<div>
    <New_Todo_Component/>
</div>
    
</template>

<script>
import New_Todo_Component from '@/components/New_Todo_Component.vue';
export default {
  name: 'Add_Todo',
  components: {
    New_Todo_Component
  }
}
</script>