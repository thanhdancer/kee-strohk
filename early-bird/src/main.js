import Vue from 'vue'
import App from './App'
import storage from './store.js'
/* eslint-disable no-new */
new Vue({
  el: 'body',
  components: { App },
  data: {
    Storage: storage.storage
  }
})
