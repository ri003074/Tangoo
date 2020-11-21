import Vue from 'vue'
import Router from 'vue-router'
import DisplayContents from './components/DisplayContents.vue'
// import HeaderDisplay from './components/HeaderDisplay.vue'
import Quiz from './components/Quiz.vue'

Vue.use(Router)

export default new Router({
    mode: "history",
    routes: [
        { path: "/", component: DisplayContents, props:true},
        { path: "/quiz", component: Quiz},
    ]
})