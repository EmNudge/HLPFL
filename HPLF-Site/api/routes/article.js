const routes = require('express').Router();

routes.post('/', (req, res) => {
  // this is where the call was going to be put to avoid the CORS policy
  // problem, but it was fixed on the Flask server before this code was finished.

});

module.exports = routes;