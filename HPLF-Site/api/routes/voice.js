const routes = require('express').Router();
const AuthorizationV1 = require('ibm-watson/authorization/v1');

const credentials = {
  iam_apikey: process.env.SPEECH_TO_TEXT_IAM_APIKEY,
  url: process.env.SPEECH_TO_TEXT_IAM_URL,
}

routes.get('/', (req, res) => {
  const authService = new AuthorizationV1(credentials);
  authService.getToken((err, res2) => {
    if (err) {
      console.log('Error retrieving token: ', err);
      res.status(500).send('Error retrieving token');
      return;
    }

    const token = res2.token || res2;

    if (process.env.SPEECH_TO_TEXT_IAM_APIKEY) {
      res.json({ access_token: token, url: credentials.url });
      return;
    } 

    res.json({ token: token, url: credentials.url });
  })
});

module.exports = routes;