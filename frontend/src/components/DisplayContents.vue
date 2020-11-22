<template>
    <div class="display-contents">
    <table class="table">
      <tbody>
        <tr v-for="content in contents" v-bind:key=content.id>
          <td>{{ content.id }} ({{ (content.c_counter / content.s_counter)*100 }}%)</td>
          <td>{{ content.phrase_en }}</td>
          <td>{{ content.phrase_ja }}</td>
          <td>{{ content.word_en }}</td>
        </tr>
      </tbody>
    </table>
    </div>
  
</template>

<script>
export default {
    props:{
        contents:{
            type:Array,
        }
    },
}
</script>

<style scoped lang="scss">
</style>