<template>
  <nav class="navbar navbar-expand-lg">
    <router-link to='/' class="navbar-brand" >Tangoo</router-link>
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
      </ul>
      <!-- <form class="form-inline my-2 my-lg-0">
        <input class="form-control mr-sm-2 search-form" type="text" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-secondary my-2 my-sm-0" type="submit">Search</button>
      </form> -->
    </div>
  </nav>
</template>

<style lang="scss" scoped>
// .search-form{
//   outline: none;;
//   background-color:$main_background_color;
//   color:$main_moji_color;
//   outline:none !important;
//   border-color:$main_background_color;
//   &:focus{
//     background-color: $main_background_color;
//     color:$main_moji_color;
//     outline:none !important;
//     box-shadow: none;
//     border-color: $main_background_color;
//   }
// }
// .btn-outline-secondary{
//   color:white;
//   border:none;
//   &:hover{
//     background-color: $main_background_color;
//   }
//   &:focus{
//     border:none;
//     box-shadow: none !important;
//   }
// }
// btn-outline-secondary:not(:disabled):not(.disabled).active, 
// .btn-outline-secondary:not(:disabled):not(.disabled):active, 
// .show>.btn-outline-secondary.dropdown-toggle {
//   color: #fff;
//   background-color:$main_background_color;
//   border-color:$main_background_color ;
// }
</style>