<template>
  <div class="container">
      <!-- Main component for a primary marketing message or call to action -->
      <div class="jumbotron" v-if="!$parent.authenticated">
        <h1>Hello, stranger</h1>
        <p>We'll do it real quick. Please sign in first !</p>
      </div>
      <div class="jumbotron" v-if="!$parent.authenticated">
        <h1>Waddup, {{ $parent.user.name }}</h1>
        <p>Check out assignments</p>
      </div>

    </div> <!-- /container -->
</template>

<script>
export default {
  data () {
    return {
    }
  }
}
</script>