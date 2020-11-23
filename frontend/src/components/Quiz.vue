<template>
<div v-if="contents">
    <div style="text-align:center;">
        <div class="quiz">{{ contents_quiz[randomNum].phrase_ja }}</div>
        <div class="quiz">{{ contents_quiz[randomNum].phrase_quiz }}</div>
        <div class="quiz quiz_answer">{{ contents_quiz[randomNum].word_blank }}</div>


    </div>
</div>
</template>

<script>
export default {
    data: function(){
        return {
        }
    },
    props:{
        contents_quiz:{
            type:Array,
        },
        contents:{
            type:Array,
        },
        randomNum:{
            type:Number,
        },
        loc:{
            type:Number,
        }
    },
    created: function(){
        console.log("quiz created")
        // this.arrNum = Math.floor(Math.random()*2)
    },
        mounted: function () {
        //キーが入力されたときにkeydown関数を実行する。
        window.addEventListener('keydown', this.keydown);
    },
    computed:{
    },
    methods:{
        updateDatabase(){
            const content = this.contents[this.randomNum]

            this.$emit("update-database", content.s_counter+1, 2, content.id)//s_counter, c_counter, id
        },
        keydown(event){
            console.log("keydown!")
            console.log(event.key)
            console.log(this.loc)
            const content = this.contents_quiz[this.randomNum]
            if(content.word_en[this.loc] == event.key){
                this.$emit("update-quiz-blank")

                if( this.loc == content.word_en.length-1 ){
                    this.updateDatabase()
                    this.$emit("next-quiz")
                }

            }else{
                console.log("miss")
            }
        }
    },
    watch:{
        randomNum:{
            handler:function(){
                console.log("watch randomNum!!")
            }
        },
        contents:{
            handler:function(){
                console.log("watch contents at Quiz.vue")
                console.log(this.contents.length)
            },
            deep:true
        }
    }
}
</script>

<style lang="scss">
    .quiz{
        margin-top:8px;
        margin-bottom:8px;
    }

    .quiz_answer{
        letter-spacing: 0.1em;
        font-size:32px;
    }
</style>