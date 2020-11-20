<template>
<div class="app">
  <p v-if="contents<0">Loading...</p>
  <div v-else>
    <div>
      <div v-for="content in contents" :key ="content.id">
        {{ content.phrase_en }}
        {{ content.phrase_ja }}
        {{ content.word_en }}
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
  name:'app',

//API格納用のプロパティ
  data(){
    return{
      contents: null,
    }
  },

//axiosによるデータ取得処理
  created: function(){
    axios.get('http://localhost:8000/api/')
    .then(function(response){
        this.contents = response.data
    }.bind(this))
    .then (function(){
    })
    .catch(function(error){
        console.log(error)
    })
  },
  mounted: function(){
  }
}  
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
