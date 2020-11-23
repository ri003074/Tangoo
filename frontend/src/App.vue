<template>
  <div>
    <DisplayHeader></DisplayHeader> 
    <router-view :contents = 'contents' :randomNum = 'randomNum' v-on:update-database="setUpdatedCounterValue"></router-view>  
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
      arrNum:0,
      randomNum:0,
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

        //Quiz用のデータを追加する。
        for(var i=0;i<this.contents.length;i++){
          const content = this.contents[i]
          this.contents[i].phrase_quiz = content.phrase_en.replace(content.word_en, '_'.repeat(content.word_en.length))
          this.contents[i].word_blank  = content.word_en.replace(/./g, '_')
        }
        this.randomNum = Math.floor(Math.random() * this.contents.length)
      }
      .bind(this))
      .catch(function(error){
        console.log(error)
      })
  },
  methods:{
    setUpdatedCounterValue(...args){ //update s,c counter value from child component
        const [sCounter, cCounter, id] = args
        this.arrNum = this.contents.findIndex( x => x.id===id) //get array number from id
        this.contents[this.arrNum].s_counter = sCounter
        this.contents[this.arrNum].c_counter = cCounter
    },
    updataDatabase(){
        var data = this.contents[this.arrNum] // data for updte
        axios
          .put("http://localhost:8000/api/" + data.id + "/", data)
          .then(function(response){
            console.log(response.data)
        })
    }
  },
  watch:{
    contents:{
      handler: function(){
        console.log("watch contents!")
        this.updataDatabase();
      },
    deep:true
    },
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
