<template>
  <div>
    <form>
      <div class="form-group">
        <!-- v-model.trim, lazy, number -->
        <input type="text" class="form-control col-4" v-model.trim="content.phrase_en" placeholder="English Phrase">
      </div>
      <div class="form-group">
        <input type="text" class="form-control col-4" v-model.trim="content.phrase_ja" placeholder="Japanese Phrase">
      </div>
      <div class="form-group">
        <input type="text" class="form-control col-4" v-model.trim="content.word_en" placeholder="English Word">
      </div>
      <div>
        <button class="btn my-2 my-sm-0" v-on:click="addData()">add</button>
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
        s_counter  : "1", //initial value
        c_counter  : "1", //initial value
        supplement : "",  //initial value
      }
    }
  },
  methods:{
    addData: function(){
      axios
      // .put("http://localhost:8000/api/" + data.id + "/",data)
        .post("http://localhost:8000/api/",this.content)
        .then(function(response){
          console.log(response.data)
      })
    }
  }
}
</script>