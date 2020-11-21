<template>
  <div>
    <HeaderDisplay> </HeaderDisplay> 
    <router-view :contents = 'contents'></router-view>  
  </div>
</template>

<script>
import 'normalize.css'
import axios from 'axios'
import HeaderDisplay from './components/HeaderDisplay.vue'

export default {

  data: function(){
    return {
      contents: null,
    }
  },
  components:{ HeaderDisplay
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

<style lang="scss">
/* $main_moji_color : #FFF;
$sub_moji_color:#8899A6;
$main_background_color:#15202B;
$sub_background_color:#192734; */

  
</style>
