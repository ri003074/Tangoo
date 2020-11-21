<template>
    <div>
    <table class="table table-hover">
      <thead>
        <tr>
          <th>#</th>
          <th>Phrase</th>
          <th>Japanese</th>
          <th>word</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="content in contents" v-bind:key=content.id>
          <th scope="row">{{ content.id }}</th>
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

<style >
   body{
       background-color: black;
   } 
</style>