<template>
<div v-if="contents">
    <div style="text-align:center;">
        <div class="quiz">{{ contents[randomNum].phrase_ja }}</div>
        <div class="quiz">{{ contents[randomNum].phrase_quiz }}</div>
        <div class="quiz quiz_answer">{{ contents[randomNum].word_blank }}</div>

        <!-- <div>{{ contents[0].phrase_en }}</div>
        <div>{{ contents[0].word_en }}</div>
        <div>{{ contents[0].c_counter }}</div>
        <div>{{ contents[0].s_counter }}</div> -->
        <!-- <button @click="updateDatabase">btn</button> -->

    </div>
</div>
</template>

<script>
export default {
    data: function(){
        return {
            // arrNum:0,
        }
    },
    props:{
        contents:{
            type:Array,
        },
        randomNum:{
            type:Number,
        }
    },
    created: function(){
        console.log("quiz created")
        // this.arrNum = Math.floor(Math.random()*2)
    },
    computed:{
    },
    methods:{
        updateDatabase(){
            this.$emit("update-database", 7, 7, 5)//s_counter, c_counter, id
        }
    },
    watch:{
        contents:{
            handler:function(){
                console.log("watch contents at Quiz.vue")
                console.log(this.contents.length)
            }
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