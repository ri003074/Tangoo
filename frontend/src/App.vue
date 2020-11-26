<template>
  <div>
    <DisplayHeader></DisplayHeader> 
    <router-view :loc = 'loc' 
                 :contents = 'contents' 
                 :contents_quiz = 'contents_quiz' 
                 :randomNum = 'randomNum' 
                 v-on:update-counter-value="updatedCounterValue" 
                 v-on:update-quiz-blank="updateQuizBlank"
                 v-on:next-quiz="nextQuiz">
                 </router-view>  
  </div>
</template>

<script>
import 'normalize.css'
import axios from 'axios'
import DisplayHeader from './components/DisplayHeader.vue'

export default {

  data: function(){
    return {
      loc:1,
      contents: null,
      contents_quiz: [],
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

        //Quiz用のデータを作成する。
        for(var i=0;i<this.contents.length;i++){
          const content = this.contents[i]
          const word_en_begin  = content.word_en.slice(0,1);

          const data = {
            word_blank_begin:word_en_begin,
            phrase_quiz : content.phrase_en.replace(content.word_en, '_'.repeat(content.word_en.length)),
            word_blank : word_en_begin + '_'.repeat(content.word_en.length-1),
            phrase_ja   : content.phrase_ja,
            word_en     : content.word_en,
          }

          this.contents_quiz.push(data)
        }
        this.setRandomNum()
      }.bind(this))
      .catch(function(error){
        console.log(error)
      })
  },
  methods:{
    setRandomNum(){
      this.randomNum = Math.floor(Math.random() * this.contents.length)
    },
    updateQuizBlank(){
      const content = this.contents_quiz[this.randomNum]
      this.loc++;
      this.contents_quiz[this.randomNum].word_blank = content.word_en.substring(0, this.loc) + '_'.repeat(content.word_en.length - this.loc);
    },
    updataDatabase(){
      var data = this.contents[this.arrNum] // data for updte
      axios
        .put("http://localhost:8000/api/" + data.id + "/", data)
        .then(function(response){
          console.log(response.data)
        })
    },
    nextQuiz(){
      console.log("finish! go to next")
      this.contents_quiz[this.randomNum].word_blank = this.contents_quiz[this.randomNum].word_blank_begin + '_'.repeat(this.contents_quiz[this.randomNum].word_en.length-1)
      this.setRandomNum()
      this.loc = 1;
    },
    updatedCounterValue(...args){ //update s,c counter value from child component
      const [sCounter, cCounter, id] = args
      this.arrNum = this.contents.findIndex( x => x.id===id) //get array number from id
      this.contents[this.arrNum].s_counter = sCounter
      this.contents[this.arrNum].c_counter = cCounter
    },
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
    &:hover {
    color:$sub_moji_color;
  }
}
</style>
