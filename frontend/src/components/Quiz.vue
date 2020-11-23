<template>
<div v-if="contents">
    <div style="text-align:center;">
        <div>Quiz</div>
        <div>{{ contents[0].phrase_en }}</div>
        <div>{{ contents[0].phrase_ja }}</div>
        <div>{{ contents[0].word_en }}</div>
        <div>{{ contents[0].c_counter }}</div>
        <div>{{ contents[0].s_counter }}</div>
        <button @click="updateDatabase">btn</button>

    </div>
</div>
</template>

<script>
export default {
    computed:{
    },
    props:{
        contents:{
            type:Array,
        }
    },
    methods:{
        updateDatabase(){
            this.$emit("update-database", 7, 7, 4)//s_counter, c_counter, id
        }
    },
    created: function(){
        console.log("quiz created")
    }
}
</script>