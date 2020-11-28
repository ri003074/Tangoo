<template>
<div v-if="contents">
    <div style="text-align:center;">
        <div class="quiz">{{ contents[randomNumber].phrase_ja }} ({{ ((contents[randomNumber].c_counter / contents[randomNumber].s_counter)*100).toFixed(1) }}%)</div>
        <div class="quiz">{{ contents[randomNumber].phrase_quiz }}</div>
        <div class="quiz quiz_answer">{{ contents[randomNumber].word_blank }}</div>
    </div>
</div>
</template>

<script>
export default {
    data: function(){
        return {
            missCount:0,
        }
    },
    props:{
        contents:  { type:Array  },
        randomNumber:  { type:Number },
        letterLocation:{ type:Number },
    },
    created(){
        console.log("quiz created")
    },
    mounted() {
        //キーが入力されたときにkeydown関数を実行する。
        window.addEventListener('keydown', this.keydown);
    },
    beforeDestroy(){
        console.log("before destroy")
        window.removeEventListener('keydown', this.keydown);
    },
    computed:{
    },
    methods:{
        updateCounterValue(miss){
            const content = this.contents[this.randomNumber]
            var cCounter  = content.c_counter
            if(miss<1){
                cCounter = cCounter+1
            }
            this.$emit("update-counter-value", content.s_counter+1, cCounter, content.id)//s_counter, c_counter, id
        },
        sleep(msec) {
            return new Promise(function(resolve) {
            setTimeout(function() {resolve()}, msec);
 
            })
        },
        async proceedToNextQuiz(){
            window.removeEventListener('keydown', this.keydown);
            this.updateCounterValue(this.missCount)
            this.missCount=0
            await this.sleep(1000)
            this.$emit("next-quiz")
            window.addEventListener('keydown', this.keydown);
        },
        keydown(event){
            console.log("keydown!")
            console.log(event.key)
            console.log(event.keyCode)
            console.log(this.letterLocation)
            const content = this.contents[this.randomNumber]

            if(content.word_en[this.letterLocation] == event.key || this.missCount > 5){
                this.$emit("update-quiz-blank")
            } else {
                console.log("miss")
                this.missCount++;
            }

            if(this.letterLocation == content.word_en.length-1){
                this.proceedToNextQuiz()
            }
        }
    },
    watch:{
        randomNumber:{
            handler(){
                console.log("watch randomNumber!!")
            }
        },
        contents:{
            handler(){
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