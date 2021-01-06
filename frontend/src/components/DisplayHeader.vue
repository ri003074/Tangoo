<template>
  <nav class="navbar navbar-expand-lg">
    <router-link to="/" class="navbar-brand" style="padding: 0px 8px"
      >Tangoo
      <!-- <span class="h6">
           ({{contentsCount}})
        </span> -->
    </router-link>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link to="/" class="nav-link"
            >Home <span class="sr-only">(current)</span></router-link
          >
        </li>
        <li class="nav-item">
          <router-link to="/add" class="nav-link">Add</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/quiz" class="nav-link">Quiz</router-link>
        </li>
        <li class="nav-item" v-if="this.$route.path == '/quiz'">
          <div v-if="isRandom" class="nav-link" v-on:click="switchRandom">
            random
          </div>
          <div v-if="!isRandom" class="nav-link" v-on:click="switchRandom">
            sequential
          </div>
        </li>
      </ul>
      <form class="form-inline" v-if="token === ''">
        <input
          type="text"
          class="form-control mr-sm-2"
          v-model.trim="username"
          placeholder="username"
        />
        <input
          type="password"
          class="form-control mr-sm-2"
          v-model.trim="password"
          placeholder="password"
        />
        <div class="mr-5" v-on:click="logIn">logIn</div>
      </form>

      <div v-if="token !== ''" class="mr-5" v-on:click="logOut">logOut</div>
    </div>
  </nav>
</template>
<script>
import axios from "axios";
export default {
  data: function () {
    return {
      username: "",
      password: "",
    };
  },
  props: {
    isRandom: { type: Boolean },
    contentsCount: { type: Number },
    token: { type: String },
  },
  methods: {
    switchRandom() {
      this.$emit("select-random");
    },
    logIn() {
      console.log("login!");
      axios
        .post(
          `http://localhost:8000/api/v1/auth/token/login`,
          { username: this.username, password: this.password },
          {}
        )
        .then(function (response) {
          console.log(response.data.auth_token);
          localStorage.setItem("token", "Token " + response.data.auth_token);
          window.location.reload();
        });
    },
    logOut() {
      localStorage.setItem("token", "");
      window.location.reload();
    },
  },
};
</script>

<style lang="scss" scoped>
.v-application a {
  color: $main_moji_color;
}
</style>
