<template>
<div v-if="contents">
    <div style="text-align:center;">
        <div class="quiz">{{ contents_quiz[randomNum].phrase_ja }} ({{ ((contents[randomNum].c_counter / contents[randomNum].s_counter)*100).toFixed(1) }}%)</div>
        <div class="quiz">{{ contents_quiz[randomNum].phrase_quiz }}</div>
        <div class="quiz quiz_answer">{{ contents_quiz[randomNum].word_blank }}</div>
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
    beforeDestroy:function(){
        console.log("before destroy")
        window.removeEventListener('keydown', this.keydown);
    },
    computed:{
    },
    methods:{
        updateCounterValue(miss){
            const content = this.contents[this.randomNum]
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
            console.log(this.loc)
            const content = this.contents_quiz[this.randomNum]
            if(this.pageStatus=='playing'){

                if(content.word_en[this.loc] == event.key){
                    this.$emit("update-quiz-blank")

                    if(this.loc == content.word_en.length-1){
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