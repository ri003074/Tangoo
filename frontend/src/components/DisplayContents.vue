<template>
    <div class="display-contents">
        <table class="table">
            <tbody>
                <tr v-for="(content,index) in contents" v-bind:key=content.id>
                    <td style="width:10%;text-align:center;">{{ ('000' + index).slice(-3) }}</td>
                    <td style="width:30%;">{{ content.phrase_en }}</td>
                    <td style="width:25%;">{{ content.phrase_ja }}</td>
                    <td style="width:15%;">{{ content.word_en }}</td>
                    <td style="width:10%;text-align:center;">{{ ((content.c_counter / content.s_counter)*100).toFixed(1) }}%</td>
                    <td style="width:10%;text-align:center;" class="delete_button" v-on:click="deleteContent(index)">[x]</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    props:{
        contents:{
            type:Array,
        }
    },
    methods:{
        deleteContent(contentNumber){
            let data = this.contents[contentNumber] // data for updte
            this.contents.splice(contentNumber,1) //delete from contents

            axios //delete from database
                .delete("http://localhost:8000/api/" + data.id + "/", data)
                .then(function(response){
                    console.log(response.data)
                })
        }
    }
}
</script>

<style scoped lang="scss">
.delete_button{
    cursor: pointer;
}
</style>