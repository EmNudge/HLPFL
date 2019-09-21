
const { Router } = require('express')
const router = Router()

const SpeechToTextV1 = require('ibm-watson/speech-to-text/v1');
const AuthorizationV1 = require('ibm-watson/authorization/v1');

const serviceUrl = 'https://stream.watsonplatform.net/speech-to-text/api';
const speechToText = new SpeechToTextV1({
  iam_apikey: process.env.API_TOKEN,
  url: serviceUrl
})
const tokenManager = new AuthorizationV1(speechToText.getServiceCredentials());

router.get('/v1/credentials', function (req, res, next) {
  tokenManager.getToken((err, token) => {
    if (err) console.log(err);
    res.json({ token, serviceUrl });
  })
})

module.exports = router;