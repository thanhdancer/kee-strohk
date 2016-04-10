<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-3 item" v-for="assignment in assignments">
        <h4><a href="#" v-link="{ path: '/assignment/'+assignment.id }">{{ assignment.name }}</a></h4>
        <p>{{ assignment.description | truncate 60 }}</p>
      </div>
    </div>
    </div>
  </div>
</template>
<style lang="sass">
  .item {
    min-height: 130px;
  }
</style>
<script>
export default {
  data: function () {
    return {
      assignments: []
    }
  },
  ready: function () {
    var self = this;
    this.$http.get(self.$parent.route('assignment.index')).then(function (response) {
      if (!response.data) {
        return;
      }
      this.assignments = response.data
    })
  }
}
</script>