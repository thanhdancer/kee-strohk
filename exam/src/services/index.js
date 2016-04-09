'use strict';
const paper = require('./paper');
const paper = require('./paper');
const authentication = require('./authentication');
const user = require('./user');

module.exports = function() {
  const app = this;


  app.configure(authentication);
  app.configure(user);
  app.configure(paper);
  app.configure(paper);
};
