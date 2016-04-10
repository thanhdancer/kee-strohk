<template>
  <div class="container">
    <div :class="col-md-12">
      <div class="blog-header">
        <h1 class="blog-title">{{ assignment.name }}</h1>
        <p class="lead blog-description">{{ assignment.description | truncate 100 }}</p>
      </div>
      <div class="blog-post">
        <p>{{ assignment.content }}</p>
      </div>
    </div>
    <div :class="col-md-12">
      <div class="text-center" v-if="new">
        <a class="btn btn-lg btn-success" href="#" role="button" v-on:click.prevent="doAssignment">Bắt đầu làm bài</a>
      </div>
      <div class="text-center" v-if="unfinished">
        <a class="btn btn-lg btn-success" href="#" role="button" v-on:click.prevent="doAssignment">Quay lại làm bài</a>
      </div>   
    </div>
  </div>
</template>
<style lang="sass">
  .blog-post {
    text-align: justify;
  }
</style>
<script>
export default {
  data: function () {
    return {
      assignment: {}
    }
  },
  computed: {
    new: function () {
      if (!this.assignment || !this.assignment.submissions) {
        return true;
      }
      return this.assignment.submissions.length == 0;
    },
    unfinished: function () {
      if (!this.assignment || !this.assignment.submissions) {
        return false;
      }
      return this.assignment.submissions.filter(function (submission) {
        return !submission.finished;
      }).length > 0;
    }
  },
  methods: {
    doAssignment: function () {
      var self = this;
      var uri = self.$parent.route('api.assignment.do', {id: self.assignment.id});
      this.$http.put(uri, {assignment_id:self.assignment.id, api_token: self.$parent.authenticated}).then(function (response) {
          if (!response.data) {
            return;
          }
          var submission = response.data;
          var url = this.$parent.route('submission.edit', {id: submission.id}, true);
          console.log(url);
          this.$route.router.go(url);
        })
    }
  },
  ready: function () {
    var self = this;
    this.$http.get(self.$parent.route('api.assignment.show'), {id: self.$route.params.id, api_token: self.$parent.authenticated}).then(function (response) {
      if (!response.data) {
        return;
      }
      this.assignment = response.data
    })
  }
}
</script>