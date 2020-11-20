<template>
    <div>
        <div v-for = "content in contents" v-bind:key = content.id>
            {{ content.phrase_en }}
            {{ content.phrase_ja }}
            {{ content.word_en }}
        </div>    
    </div>
</template>

<script>
export default {
    props:{
        contents:{
            type:Object,
        }
    }    
}
</script>

