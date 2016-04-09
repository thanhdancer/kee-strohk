<template>
  <div class="container">
  	<form class="form-signin" v-on:submit.prevent="onSubmit">
      <h2 class="form-signin-heading">Please sign in</h2>
      <label for="email" class="sr-only">Email address</label>
      <input type="email" v-model="email" id="email" class="form-control" placeholder="Email address" required="" autofocus="">
      <label for="password" class="sr-only">Password</label>
      <input type="password" v-model="password" id="password" class="form-control" placeholder="Password" required="">
      <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
    </form>
  </div>
</template>
<style lang="sass">
  body {
    background-color: #eee;
  }
  .form-signin {
    max-width: 330px;
    padding: 15px;
    margin: 0 auto;
  }
  .form-signin .form-signin-heading,
  .form-signin .checkbox {
    margin-bottom: 10px;
  }
  .form-signin .checkbox {
    font-weight: normal;
  }
  .form-signin .form-control {
    position: relative;
    height: auto;
    -webkit-box-sizing: border-box;
       -moz-box-sizing: border-box;
            box-sizing: border-box;
    padding: 10px;
    font-size: 16px;
  }
  .form-signin .form-control:focus {
    z-index: 2;
  }
  .form-signin input[type="email"] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
  }
  .form-signin input[type="password"] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }
</style>
<script>
export default {
  data () {
    return {
      email: null,
      password: null
    }
  },
  created: function () {
    if (this.$parent.authenticated) {
      this.$route.router.go(this.$parent.route('home'));
    }
  },
  methods: {
    submitCallback: function (response) {
      if (!response.data) {
        return;
      }
      var data = response.data;
      if (data.error_code != 0) {
        return alert(data.message ? data.message : 'Something\' wrong');
      }
      this.$parent.authenticate(data.user);
    },
    onSubmit: function () {
      var self = this;
      self.$http.post(self.$parent.route('login'), {
        email: self.email,
        password: self.password
      }).then(self.submitCallback, self.submitCallback);
    }
  }
}
</script>