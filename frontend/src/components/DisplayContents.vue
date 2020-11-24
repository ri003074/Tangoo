<template>
  <div class="display-contents">
    <table class="table">
      <tbody>
        <tr v-for="(content,index) in contents" v-bind:key=content.id>
          <td style="width:10%;text-align:center;">{{ ('000' + index).slice(-3) }}</td>
          <td style="width:30%;">{{ content.phrase_en }}</td>
          <td style="width:30%;">{{ content.phrase_ja }}</td>
          <td style="width:20%;">{{ content.word_en }}</td>
          <td style="width:10%;text-align:center;">{{ ((content.c_counter / content.s_counter)*100).toFixed(1) }}%</td>
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