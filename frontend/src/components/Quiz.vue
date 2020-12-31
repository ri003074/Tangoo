<template>
    <div v-if="contents[quizNumber]">
        <div style="text-align:center;">
            <div class="quiz">{{ quizNumber }}/{{ contents.length }}</div>
            <div class="quiz">{{ contents[quizNumber].phrase_ja }} ({{ ((contents[quizNumber].c_counter / contents[quizNumber].s_counter)*100).toFixed(1) }}%)</div>
            <div class="quiz">{{ contents[quizNumber].phrase_quiz }}</div>
            <div class="quiz quiz_answer">{{ contents[quizNumber].word_blank }}</div>

            <div v-if="isCorrect" class="mt-4">
                <font-awesome-icon icon="thumbs-up" />
            </div>
            <div v-else class="mt-4">
                <font-awesome-icon icon="thumbs-down" />
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data: function(){
        return {
            missCount  : 0,
            isCorrect  : true,
            music      : undefined,
            musicSound : "se_maoudamashii_battle_gun01.mp3",
        }
    },
    props:{
        contents       : { type : Array  },
        quizNumber     : { type : Number },
        letterLocation : { type : Number },
    },
    created(){
        console.log("quiz created")
    },
    mounted() {
        //キーが入力されたときにkeydown関数を実行する。
        window.addEventListener('keydown', this.keydown);
        this.music = new Audio(this.musicSound);
        this.music.volume = 0.1;
    },
    beforeDestroy(){
        console.log("before destroy")
        window.removeEventListener('keydown', this.keydown);
    },
    computed:{
    },
    methods:{
        speak(){
            var speak = new SpeechSynthesisUtterance();
            speak.text = this.contents[this.quizNumber].phrase_en
            speak.rate = 1.0
            speak.pitch = 0
            speak.lang = 'en-US'
            speechSynthesis.speak(speak)
        },
        updateCounterValue(miss){
            const content = this.contents[this.quizNumber]
            let cCounter  = content.c_counter
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
            this.speak()
            await this.sleep(this.contents[this.quizNumber].phrase_en.length*80) //フレーズの文字数で待ち時間を変える
            this.$emit("next-quiz")
            window.addEventListener('keydown', this.keydown);
        },
        keydown(event){
            console.log("keydown!")
            console.log(event.key)
            const content = this.contents[this.quizNumber]

            if(content.word_en[this.letterLocation] == event.key || this.missCount > 5){
                this.music.currentTime=0;
                this.music.play();
                this.isCorrect=true
                this.$emit("update-quiz-blank")

                if(this.letterLocation == content.word_en.length-1){
                    this.proceedToNextQuiz()
                }
            }else{
                console.log("miss")
                this.isCorrect=false
                this.missCount++;
            }
        }
    },
    watch:{
        quizNumber:{
            handler(){
                console.log("watch quizNumber!!")
            }
        },
        contents:{
            handler(){
                console.log("watch contents at Quiz.vue")
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