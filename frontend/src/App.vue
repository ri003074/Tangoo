<template>
  <div>
    <DisplayHeader></DisplayHeader> 
    <router-view :letterLocation = 'letterLocation' 
                 :contents       = 'contents' 
                 :contentsQuiz   = 'contentsQuiz' 
                 :randomNumber   = 'randomNumber' 
                 v-on:update-counter-value = "updatedCounterValue" 
                 v-on:update-quiz-blank    = "updateQuizBlank"
                 v-on:next-quiz            = "nextQuiz">
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
            letterLocation       : 1,
            contents             : null,
            contentsQuiz         : [],
            arrayNumberForUpdate : 0,
            randomNumber         : 0,
        }
    },
    components: { 
        DisplayHeader
    },

    //axiosによるデータ取得処理
    created(){
        console.log("axios")
        axios
            .get('http://localhost:8000/api/')
            .then(function(response){
            this.contents = response.data

            //Quiz用のデータを作成する。
            for(var i=0; i<this.contents.length; i++){
                const content       = this.contents[i]
                const word_en_begin = content.word_en.slice(0,1);
                const correct_answer_rate = ((content.c_counter / content.s_counter)*100).toFixed(1)

                const data = {
                    word_blank_begin    : word_en_begin,
                    phrase_quiz         : content.phrase_en.replace(content.word_en, '_'.repeat(content.word_en.length)), //英語のフレーズのなかで問題となる部分をを'_'で置き換える
                    word_blank          : word_en_begin + '_'.repeat(content.word_en.length-1), //
                    phrase_ja           : content.phrase_ja,
                    word_en             : content.word_en,
                    correct_answer_rate : correct_answer_rate
                }
  
            this.contentsQuiz.push(data)
            }
            this.setRandomNum()
            }.bind(this))
            .catch(function(error){
                console.log(error)
            })
    },
    methods:{
        setRandomNum(){
        this.randomNumber = Math.floor(Math.random() * this.contents.length)
        },
        updateQuizBlank(){
            const content = this.contentsQuiz[this.randomNumber]
            this.letterLocation++;
            this.contentsQuiz[this.randomNumber].word_blank = content.word_en.substring(0, this.letterLocation) + '_'.repeat(content.word_en.length - this.letterLocation);
        },
        updataDatabase(){
            var data = this.contents[this.arrayNumberForUpdate] // data for updte
            axios
                .put("http://localhost:8000/api/" + data.id + "/", data)
                .then(function(response){
                    console.log(response.data)
                })
        },
        nextQuiz(){
            console.log("finish! go to next")
            this.contentsQuiz[this.randomNumber].word_blank = this.contentsQuiz[this.randomNumber].word_blank_begin + '_'.repeat(this.contentsQuiz[this.randomNumber].word_en.length-1)
            this.setRandomNum()
            this.letterLocation = 1;
        },
        updatedCounterValue(...args){ //update s,c counter value from child component
            const [sCounter, cCounter, id] = args
            this.arrayNumberForUpdate = this.contents.findIndex( x => x.id===id) //get array number from id
            this.contents[this.arrayNumberForUpdate].s_counter = sCounter
            this.contents[this.arrayNumberForUpdate].c_counter = cCounter
        },
    },
    watch:{
        contents:{
            handler(){
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
