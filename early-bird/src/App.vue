<template>
  <div id="app">
    <aside id="sidebar">
      <textarea class="textarea">{{ source | truncate message }}</textarea>
    </aside>
    <main id="main">
      <textarea v-model="message" v-on:keydown="keydown" v-on:keyup="keyup" rows="10" cols="30"></textarea>
      <div id="download">
        <a href="#" v-on:click.prevent="exportResult">Download as export.txt</a>
      </div>
      <pre id="result"><span v-for="key in keys">{{ key.code }}, {{ key.down }}, {{ key.up }}<br/></span></pre>
    </main>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      message: null,
      keys: [],
      source: null
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
      console.log(keyCode)
      var now = Date.now()
      self.keys.forEach(function (key, i) {
        if (key.code === keyCode) {
          if (!key.up) {
            key.up = now
            self.keys.$set(i, key)
          }
        }
      })
    },
    exportResult: function () {
      var element = document.getElementById('result')
      console.log(element)
      return this.download(element.innerText)
    },
    download: function (content) {
      var pom = document.createElement('a')
      pom.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(content))
      pom.setAttribute('download', 'export.txt')
      pom.click()
    }
  },
  filters: {
    truncate: function (value, message) {
      // if (message) {
      //   return value.substr(message.length)
      // }
      return value
    }
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
}
</style>
