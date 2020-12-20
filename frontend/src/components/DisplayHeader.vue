<template>
    <nav class="navbar navbar-expand-lg">
        <router-link to='/' class="navbar-brand" >Tangoo
        <span class="h6">
           ({{contentsCount}})
        </span>
        </router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
  
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                    <router-link to  = '/' class="nav-link" >Home <span class="sr-only">(current)</span></router-link>
                </li>
                <li class="nav-item">
                    <router-link to='/add' class="nav-link">Add</router-link>
                </li>
                <li class="nav-item">
                    <router-link to='/quiz' class="nav-link">Quiz</router-link>
                </li>
               <li class="nav-item" v-if="this.$route.path == '/quiz'">
                   <div v-if="isRandom" class="nav-link"  v-on:click="switchRandom">random </div>
                   <div v-if="!isRandom" class="nav-link" v-on:click="switchRandom">sequential </div>
               </li>
            </ul>
        </div>
    </nav>
</template>
<script>
export default {
    props:{
        isRandom      : { type : Boolean },
        contentsCount : { type : Number  }
    },
    methods:{
        switchRandom(){
            this.$emit("select-random");
        },
    }
}
</script>

<style lang="scss" scoped>
    .v-application a{
      color:$main_moji_color;
    }
</style>