<script>
import Navbar from './components/Navbar.vue'
import storage from './store.js'
export default {
  components: {
    Navbar
  },
  data: function () {
    return {
      router: {},
      uri: {
        base: 'http://keystroke.dev'
      },
      routes: {
        'home': '/home',
        'login': '/api/v1/login',
        'assignment.index': '/api/v1/assignments',
        'assignment.show': '/api/v1/assignment/{id}'
      },
      user: storage.storage.fetch('exam-keystroke:user')
    }
  },
  watch: {
    user: {
      handler: function (user) {
        storage.storage.save('exam-keystroke:user', user)
        this.$route.router.go(this.route('home'));
      },
      deep: true
    }
  },
  computed: {
    authenticated: function () {
      return this.user ? this.user.api_token : false;
    }
  },
  methods: {
    route: function (name) {
      return this.uri.base + this.routes[name];
    },
    authenticate: function (user) {
      this.user = user;
    },
    logout: function () {
      this.user = {}
    },
    getAuthorizationHeader: function () {
      return 'Bearer ' + this.authenticated
    }
  }
}
</script>
<style lang="sass">
@import "node_modules/bootstrap-sass/assets/stylesheets/bootstrap";
body {
font-family: Helvetica, sans-serif;
}
#app {
height: 100%;
}
body {
min-height: 2000px;
padding-top: 70px;
}
</style>
