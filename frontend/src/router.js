import Vue from 'vue'
import Router from 'vue-router'
import DisplayContents from './components/DisplayContents.vue'
// import HeaderDisplay from './components/HeaderDisplay.vue'
import Quiz from './components/Quiz.vue'
import AddContent from './components/AddContent.vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { fas } from '@fortawesome/free-solid-svg-icons'
// import { fab } from '@fortawesome/free-brands-svg-icons'
// import { far } from '@fortawesome/free-regular-svg-icons'

// library.add(fas, fab, far)
library.add(fas, )

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.use(Router)

export default new Router({
    mode: "history",
    routes: [
        { path: "/", component: DisplayContents, props:true },
        { path: "/quiz", component: Quiz },
        { path: "/add", component: AddContent },
        { path: "*", redirect: "/" } 
    ]
})