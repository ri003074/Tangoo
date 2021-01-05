<template>
    <div>
        <form>
            <div class="form-group ml-2">
              <!-- v-model.trim, lazy, number -->
                <input type="text" class="form-control col-4" v-model.trim="content.phrase_en" placeholder="English Phrase" autofocus>
            </div>
            <div class="form-group ml-2">
                <input type="text" class="form-control col-4" v-model.trim="content.phrase_ja" placeholder="Japanese Phrase">
            </div>
            <div class="form-group ml-2">
                <input type="text" class="form-control col-4" v-model.trim="content.word_en" placeholder="English Word">
            </div>
            <div>
                <button class="btn my-2 my-sm-0 ml-2" v-on:click="addData()">Add</button>
            </div>
        </form>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  data: function(){
    return {
      content:{
        phrase_en  : '',
        phrase_ja  : '',
        word_en    : '',
      }
    }
  },
  props:{
      token         : { type : String  },
  },
  methods:{
      addData: function(){
          axios
            .post("http://localhost:8000/api/",this.content,{
                headers: {
                    'Content-type': 'application/json',
                    'Authorization': this.token
                }
            })
            .then(function(response){
              console.log(response.data)
          })

      // this.$emit("update-contents-counter-value","increment")
      }
  }
}
</script>

<style lang="scss">
.form-control {
  border:none;;
  &:focus{
    border-color:$main_background_color;
    box-shadow: none;;
  }
}
</style>