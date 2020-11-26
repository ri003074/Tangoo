<template>
<div v-if="contents">
    <div style="text-align:center;">
        <div class="quiz">{{ contentsQuiz[randomNumber].phrase_ja }} ({{ ((contents[randomNumber].c_counter / contents[randomNumber].s_counter)*100).toFixed(1) }}%)</div>
        <div class="quiz">{{ contentsQuiz[randomNumber].phrase_quiz }}</div>
        <div class="quiz quiz_answer">{{ contentsQuiz[randomNumber].word_blank }}</div>
    </div>
</div>
</template>

<script>
export default {
    data: function(){
        return {
            missCount:0,
            pageStatus:'playing',
        }
    },
    props:{
        contentsQuiz:{
            type:Array,
        },
        contents:{
            type:Array,
        },
        randomNumber:{
            type:Number,
        },
        letterLocation:{
            type:Number,
        }
    },
    created: function(){
        console.log("quiz created")
    },
    mounted: function () {
        //キーが入力されたときにkeydown関数を実行する。
        window.addEventListener('keydown', this.keydown);
    },
    beforeDestroy:function(){
        console.log("before destroy")
        window.removeEventListener('keydown', this.keydown);
    },
    computed:{
    },
    methods:{
        updateCounterValue(miss){
            const content = this.contents[this.randomNumber]
            var cCounter = content.c_counter
            if(miss<1){
                cCounter = cCounter+1
            }
            this.$emit("update-counter-value", content.s_counter+1, cCounter, content.id)//s_counter, c_counter, id
        },
        keydown(event){
            console.log("keydown!")
            console.log(event.key)
            console.log(event.keyCode)
            console.log(this.letterLocation)
            const content = this.contentsQuiz[this.randomNumber]
            if(this.pageStatus=='playing'){

                if(content.word_en[this.letterLocation] == event.key){
                    this.$emit("update-quiz-blank")

                    if(this.letterLocation == content.word_en.length-1){
                        this.updateCounterValue(this.missCount)
                        this.missCount=0
                        this.pageStatus='stop'
                        console.log("set page status to stop")
                        // this.$emit("next-quiz")
                    }

                }else{
                    console.log("miss")
                    this.missCount++;
                }
            }else{
                console.log("else")
                if(event.keyCode==32){
                    this.$emit("next-quiz")
                        this.pageStatus='playing'

                }
            }
        }
    },
    watch:{
        randomNumber:{
            handler:function(){
                console.log("watch randomNumber!!")
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