<template>
  <div id="app">
    <aside id="sidebar">
      <textarea class="textarea">{{ source | truncate message }}</textarea>
    </aside>
    <main id="main">
      <textarea v-model="message" v-on:keydown="keydown" v-on:keyup="keyup" rows="10" cols="30"></textarea>
      <div id="download">
        <a href="#" v-on:click.prevent="toggleResult">{{ resultShown ? 'Hide' : 'Show' }} result</a>
        <a href="#" v-on:click.prevent="exportResult">Download as export.txt</a>
        <a href="#" v-on:click.prevent="clearResult">Clear result</a>
      </div>
      <pre id="result" v-show="resultShown"><span v-for="key in keys">{{ key.code }}, {{ key.down }}, {{ key.up }}<br/></span></pre>
    </main>
  </div>
</template>
<script>
var AVIM = require('./assets/avim.js')
var looper = require('lodash/forEachRight')
export default {
  data: function () {
    return {
      message: null,
      source: null,
      keys: this.$root.Storage.fetch(),
      resultShown: true
    }
  },
  watch: {
    keys: {
      handler: function (keys) {
        this.$root.Storage.save(keys)
      },
      deep: true
    }
  },
  methods: {
    keydown: function (e) {
      var key = {
        code: e.which || e.keyCode || 0,
        down: Date.now(),
        up: null
      }
      this.keys.push(key)
    },
    keyup: function (e) {
      var self = this
      var keyCode = e.which || e.keyCode || 0
      var now = Date.now()
      looper(self.keys, function (key, i) {
        if (key.code !== keyCode) {
          return true
        }
        if (key.up) {
          return true
        }
        key.up = now
        self.keys.$set(i, key)
        return false
      })
    },
    toggleResult: function () {
      this.resultShown = !this.resultShown
    },
    exportResult: function () {
      var element = document.getElementById('result')
      if (!element || element.innerText) {
        return window.alert('Shit! ABORT MISSION. ABANDON SHIP')
      }
      return this.download(element.innerText)
    },
    clearResult: function () {
      this.keys = []
    },
    download: function (content) {
      var pom = document.createElement('a')
      pom.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(content))
      pom.setAttribute('download', 'export.txt')
      if (document.createEvent) {
        var event = document.createEvent('MouseEvents')
        event.initEvent('click', true, true)
        return pom.dispatchEvent(event)
      }
      return pom.click()
    },
    avim: function () {
      var AVIMObj = new AVIM.Avim()
      function AVIMAJAXFix () {
        var a = 50
        while (a < 5000) {
          setTimeout(AVIM.Init(AVIMObj), a)
          a += 50
        }
      }
      // AVIMAJAXFix();
      AVIMObj.attachEvt(document, 'mousedown', AVIMAJAXFix, false)
      AVIMObj.attachEvt(document, 'keydown', AVIMObj.keyDownHandler, true)
      AVIMObj.attachEvt(document, 'keypress', function (e) {
        var a = AVIMObj.keyPressHandler(e)
        if (a === false) {
          if (AVIMObj.is_ie) window.event.returnValue = false
          else e.preventDefault()
        }
      }, true)
    }
  },
  filters: {
    truncate: function (value, message) {
      return value
    }
  },
  ready: function () {
    this.avim()
  }
}
</script>

<style lang="scss">
.clearfix:before,
.clearfix:after {
  content: " "; /* 1 */
  display: table; /* 2 */
}
.clearfix:after {
  clear: both;
}
.clearfix {
  *zoom: 1;
}
html {
  box-sizing: border-box;
}
*, *:before, *:after {
  box-sizing: inherit;
}
html {
  height: 100%;
}
body {
  padding: 0;
  height: 100%;
  font-family: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;
   font-weight: 300;
}
#app {
  color: #2c3e50;
  height: 100%;
  width: 100%;
  font-family: Source Sans Pro, Helvetica, sans-serif;
  text-align: center;
  a {
    color: #42b983;
    text-decoration: none;
  }
  #sidebar, #main {
    padding: 1em;
    float: left;
    width: 50%;
    height: 100%;
  }
  #sidebar > .textarea {
    display: block;
    width: 100%;
    height: 100%;
    overflow-y: scroll;
    text-align: justify;
    line-height: 1.5;
    background-color: #f5f5f5;
    padding: 1em;
    border: 0;
  }
  #main > textarea {
    width: 100%;
  }
  #result {
    max-height: 300px;
    overflow-y:scroll;
    text-align: left;
  }
  #download {
    a {
      display: inline-block;
      background-color: #42b983;
      color: #fff!important;
      padding: .5em 1em;
      border-radius: 4px;
    }
  }
}
</style>
