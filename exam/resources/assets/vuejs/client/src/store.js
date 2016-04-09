var exports = module.exports = {}
exports.storage = {
  fetch: function (STORAGE_KEY) {
    return JSON.parse(window.localStorage.getItem(STORAGE_KEY) || '[]')
  },
  save: function (STORAGE_KEY, todos) {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(todos))
  }
}