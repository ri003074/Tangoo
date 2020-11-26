<template>
<div v-if="contents">
    <div style="text-align:center;">
        <div class="quiz">{{ contents_quiz[random_number].phrase_ja }} ({{ ((contents[random_number].c_counter / contents[random_number].s_counter)*100).toFixed(1) }}%)</div>
        <div class="quiz">{{ contents_quiz[random_number].phrase_quiz }}</div>
        <div class="quiz quiz_answer">{{ contents_quiz[random_number].word_blank }}</div>
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
        contents_quiz:{
            type:Array,
        },
        contents:{
            type:Array,
        },
        random_number:{
            type:Number,
        },
        letter_location:{
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
            const content = this.contents[this.random_number]
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
            console.log(this.letter_location)
            const content = this.contents_quiz[this.random_number]
            if(this.pageStatus=='playing'){

                if(content.word_en[this.letter_location] == event.key){
                    this.$emit("update-quiz-blank")

                    if(this.letter_location == content.word_en.length-1){
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
        random_number:{
            handler:function(){
                console.log("watch random_number!!")
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