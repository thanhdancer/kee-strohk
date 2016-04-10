<template>
  <div class="container">
    <div :class="[new ? 'col-md-12' : 'col-md-7']">
      <div class="blog-header">
        <h1 class="blog-title">{{ assignment.name }}</h1>
        <p class="lead blog-description">{{ assignment.description | truncate 100 }}</p>
      </div>
      <div class="blog-post">
        <p>{{ assignment.content }}</p>
      </div>
    </div>
    <div :class="[new ? 'col-md-12' : 'col-md-5']">
      <div class="text-center" v-if="new">
        <a class="btn btn-lg btn-success" href="#" role="button">Tham gia bài học</a>
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
      if (!this.assignment) {
        return true;
      }
      return this.assignment.submissions.length == 0;
    }
  },
  ready: function () {
    var self = this;
    this.$http.get(self.$parent.route('assignment.show'), {id: self.$route.params.id, api_token: self.$parent.authenticated}, {
      headers: {
        'Authorization': self.$parent.getAuthorizationHeader()
      }
    }).then(function (response) {
      if (!response.data) {
        return;
      }
      this.assignment = response.data
    })
  }
}
</script>