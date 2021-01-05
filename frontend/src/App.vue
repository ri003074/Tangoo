<template>
        <div>
            <DisplayHeader  :isRandom          = 'isRandom'
                            :contentsCount     = 'contentsCount'
                            :token             = 'token'
                            v-on:select-random = "selectRandom">
                            </DisplayHeader> 
    
            <router-view :letterLocation = 'letterLocation' 
                         :contents       = 'contents' 
                         :quizNumber     = 'quizNumber' 
                         :token          = 'token'
                         v-on:update-counter-value        = "updatedCounterValue" 
                         v-on:update-contents-count-value = "updateContentsCountValue"
                         v-on:update-quiz-blank           = "updateQuizBlank"
                         v-on:next-quiz                   = "nextQuiz">
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
            contents             : [],
            contentsCount        : 0,
            letterLocation       : 1,
            arrayNumberForUpdate : 0,
            quizNumber           : 0,
            isRandom             : false,
            token                :'',
        }
    },
    components: { 
        DisplayHeader
    },

    //axiosによるデータ取得処理
    created(){
        console.log("axios")
        this.token = localStorage.getItem('token')
        axios
            .get('http://localhost:8000/api/',{
                headers: {
                    'Authorization': this.token
                }
            })
            .then(function(response){

            let tmpData =[]
            this.contentsCount = response.data.length;
            //Quiz用のデータを作成する。
            for(let i=0; i<this.contentsCount; i++){
                const content             = response.data[i]
                const word_en_begin       = content.word_en.slice(0,1);
                
                content.word_en_begin       = word_en_begin
                content.word_blank          = word_en_begin + '_'.repeat(content.word_en.length-1), //
                content.phrase_quiz         = content.phrase_en.replace(content.word_en, '_'.repeat(content.word_en.length)), //英語のフレーズのなかで問題となる部分をを'_'で置き換える
                content.correct_answer_rate = (content.c_counter / content.s_counter)*100
                tmpData.push(content)
            }
            tmpData.sort(function(a,b){ //正答率が低い順番に並び替える
                return a.correct_answer_rate - b.correct_answer_rate
            })
            this.contents = tmpData

            // this.setRandomNum()
            }.bind(this))
            .catch(function(error){
                console.log(error)
            })
    },
    methods:{
        setRandomNum(){ //最初は乱数にしていたが、正答率が低い順に並べることにしたので、やめた。
            if(this.isRandom){
                this.quizNumber = Math.floor(Math.random() * this.contents.length)
            }else{
                this.quizNumber += 1;
            }
        },
        selectRandom(){
            if(this.isRandom == true){
                this.isRandom = false;
            }else{
                this.isRandom = true;
            }
        },
        updateContentsCountValue(action){
            if(action == "increment"){
                this.contentsCount+=1;
            }else if(action == "decrement"){
                this.contentsCount-=1;
            }
        },
        updateQuizBlank(){
            const content = this.contents[this.quizNumber]
            this.letterLocation++;
            this.contents[this.quizNumber].word_blank = content.word_en.substring(0, this.letterLocation) + '_'.repeat(content.word_en.length - this.letterLocation);
        },
        updataDatabase(){
            let data = this.contents[this.arrayNumberForUpdate] // data for updte
            axios
                .put("http://localhost:8000/api/" + data.id + "/", data)
                .then(function(response){
                    console.log(response.data)
                })
        },
        nextQuiz(){
            console.log("finish! go to next")
            this.contents[this.quizNumber].word_blank = this.contents[this.quizNumber].word_en_begin + '_'.repeat(this.contents[this.quizNumber].word_en.length-1)
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
    &:focus{
      outline: none;
    }
}
//TODO 何故必要かわからない
.btn{
    padding:8px !important;
    border:none !important;
    color:$main_moji_color;
    &:hover {
        color:$sub_moji_color;
    }
}
.nav-link{
    color:$main_moji_color;
    &:hover {
        color:$sub_moji_color;
        cursor: pointer;
        user-select: none;
    }
}
</style>
