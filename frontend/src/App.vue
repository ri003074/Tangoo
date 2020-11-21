<template>
  <div class="app">
    <DisplayHeader> </DisplayHeader> 
    <router-view :contents = 'contents'></router-view>  
  </div>
</template>

<script>
import 'normalize.css'
import axios from 'axios'
import DisplayHeader from './components/DisplayHeader.vue'

export default {

  data: function(){
    return {
      contents: null,
    }
  },
  components:{ DisplayHeader
  },

  //axiosによるデータ取得処理
  created: function(){
    console.log("axios")
    axios.get('http://localhost:8000/api/')
    .then(function(response){
        this.contents = response.data
        console.log(this.contents)
    }
    .bind(this))
    .catch(function(error){
        console.log(error)
    })
  },
}  
</script>

<style lang="scss" scoped>

.app{
    font-family: 'Courier New', Courier, monospace;
}
  
</style>
