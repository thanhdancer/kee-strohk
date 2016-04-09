<template>
  <nav class="navbar navbar-default navbar-fixed-top">
    <div class="container">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" v-link="{ path: '/home' }">KeyStroke</a>
      </div>
      <div id="navbar" class="navbar-collapse collapse">
        <ul class="nav navbar-nav">
          <li v-link="{ path: '/home', activeClass: 'active' }"><a href="#" v-link="{ path: '/home' }">Home</a></li>
          <li v-link="{ path: '/assignments', activeClass: 'active' }"><a href="#" v-link="{ path: '/assignments' }">Assignments</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <li v-link="{ path: '/login', activeClass: 'active' }"><a href="#login" v-link="{ path: '/login' }" v-if="!$parent.authenticated">Sign In</a></li>
          <li ><a href="#logout" v-if="$parent.authenticated" v-on:click.prevent="$parent.logout">Logout</a></li>
        </ul>
      </div><!--/.nav-collapse -->
    </div>
  </nav>
</template>

<script>
export default {
  data () {
    return {
    }
  }
}
</script>