<template>
  <div>
    <DisplayHeader></DisplayHeader> 
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
  components: { 
    DisplayHeader
  },

  //axiosによるデータ取得処理
  created: function(){
    console.log("axios")
    axios
      .get('http://localhost:8000/api/')
      .then(function(response){
        this.contents = response.data
        console.log(this.contents)
      }
      .bind(this))
      .catch(function(error){
        console.log(error)
      })
  },
  methods:{
  }
}  
</script>

<style lang="scss">
* {
    color:$main_moji_color;
    font-family: 'Courier New', Courier, monospace;
    background-color: $main_background_color;;
}
a {
//TODO 何故必要かわからない
  color:$main_moji_color;
  &:hover {
    color:$sub_moji_color;
  }
}
//TODO 何故必要かわからない
.btn{
  color:$main_moji_color;
}

  
</style>
