<template>
  <div>
    <DisplayContents v-bind:contents="contents"></DisplayContents>
  </div>
</template>

<script>
import axios from 'axios'
import DisplayContents from './components/DisplayContents.vue'

export default {

  data: function(){
    return{
      contents: null,
    }
  },
  components:{
    DisplayContents
  },

  //axiosによるデータ取得処理
  created: function(){
    console.log("axios")
    axios.get('http://localhost:8000/api/')
    .then(function(response){
        this.contents = response.data
        console.log(this.contents)
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
