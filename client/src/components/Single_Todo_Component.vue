<template>
<div class="box">
    <p>{{ data.title }}|{{ data.description }}|{{ data.importance }}|{{ data.status }}</p>
</div>
</template>



  props: {
  data: Array,
},

<script>
export default {
  name: "Single_Todo_Component",
  props: {
  data: Array,
},
}
</script>

<style scoped>
.box {
    border: 4px solid gray;
}
</style>
