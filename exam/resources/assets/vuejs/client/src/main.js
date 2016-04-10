import Vue from 'vue'
import Home from './components/Home.vue'
import LogIn from './components/LogIn.vue'
import Assignments from './components/Assignments.vue'
import AssignmentShow from './components/AssignmentShow.vue'
import SubmissionEdit from './components/SubmissionEdit.vue'
import App from './App.vue'
var VueRouter = require('vue-router')
Vue.use(VueRouter)
Vue.use(require('vue-resource'));
Vue.use(require('vue-truncate'));
Vue.http.options.emulateJSON = true;

/* eslint-disable no-new */
var router = new VueRouter()
router.map({
    '/login': {
        component: LogIn
    },
    '/home': {
        component: Home
    },
    '/assignment': {
    	component: Assignments
    },
    '/assignment/:id': {
        component: AssignmentShow
    },
    '/submission/:id/edit': {
        component: SubmissionEdit
    }
})
router.redirect({
  '*': '/home'
})
router.start(App, '#app')
