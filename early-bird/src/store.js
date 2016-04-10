var exports = module.exports = {}
var STORAGE_KEY = 'early-bird-keystroke'

exports.storage = {
  fetch: function () {
    return JSON.parse(window.localStorage.getItem(STORAGE_KEY) || '[]')
  },
  save: function (todos) {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(todos))
  }
}

