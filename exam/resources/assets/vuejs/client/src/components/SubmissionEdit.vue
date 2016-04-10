<template>
  <div class="container">
    <div class="row">
      <div class="col-md-7">
        <div class="blog-header">
          <h1 class="blog-title">{{ submission.assignment.name }}</h1>
          <p class="lead blog-description">{{ submission.assignment.description | truncate 100 }}</p>
        </div>
        <div class="blog-post">
          <p>{{ submission.assignment.content }}</p>
        </div>
      </div>
      <div class="col-md-5">
        <form v-on:submit.prevent="onSubmit">
          <div class="form-group">
            <textarea v-model="submission.content" v-on:keydown="keydown" v-on:keyup="keyup" rows="30" cols="30" class="form-control"></textarea>
          </div>
          <button type="submit" class="btn btn-default">Submit</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
var looper = require('lodash/forEachRight')
export default {
	data: function () {
    return {
      keys: [],
      submission: {
        assignment: {}
      }
    }
  },
  methods: {
    onSubmit: function () {
      var self = this;
      this.submission.keys = this.submission.keys + '\n' + this.getKeys();
      var obj = JSON.parse(JSON.stringify(this.submission))
      obj.assignment = [];
      obj.user = {}
      obj.api_token = self.$parent.authenticated
      obj.finished = 1
      self.$http.post(self.$parent.route('api.submission.finish', {id: obj.id}), obj ).then(function (response) {
        if (response) {
          var assignment = response.data;
          var url = this.$parent.route('assignment.show', {id:assignment.assignment_id}, true)
          this.$route.router.go(url);
        }
      });
    },
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
    getKeys: function () {
      return this.keys.map(function (key) {
        return key.code + ', ' + key.down + ', ' + key.up
      }).join('\n')
    },
  },
  ready: function () {
  	var self = this;
    this.$http.get(self.$parent.route('api.submission.edit'), {id: self.$route.params.id, api_token: self.$parent.authenticated}).then(function (response) {
      if (!response.data) {
        return;
      }
      this.submission = response.data
    })
  }
}
</script>