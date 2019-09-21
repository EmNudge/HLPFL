
const { Router } = require('express')
const router = Router()

// DOES NOT WORK!!!

// const serviceUrl = 'https://stream.watsonplatform.net/speech-to-text/api';

// const SpeechToTextV1 = require('ibm-watson/speech-to-text/v1');

// const speechToText = new SpeechToTextV1({
//   iam_apikey: process.env.SPEECH_TO_TEXT_IAM_APIKEY,
//   url: 'https://iam.bluemix.net/identity/token',
// });

// router.get('/v1/credentials', function (req, res, next) {
// //   tokenManager.getToken((err, token) => {
// //     if (err) console.log(err);
// //     res.json({ token, serviceUrl });
// //   })
//   res.json({ hello: '' })
// })

// ---------------------------
// assistant code
// ---------------------------


const AssistantV2 = require('ibm-watson/assistant/v2');
router.get('/bot/', async function (req, res, next) {
  console.log(process.env)
  const service = new AssistantV2({
    iam_apikey: process.env.ASSISTANT_IAM_API_KEY, 
    version: '2019-02-28',
  });

  console.log('YOU GOT PASSED HERE')
  const assistantId = process.env.ASSISTANT_ID; 
  console.log('YOU GOT PASSED HERE AS WELL')

  // Create session.
  const { session_id: sessionId } = await service.createSession({ assistant_id: assistantId })
  sendMessage({
    message_type: 'text',
    text: '' 
  });

  async function sendMessage(messageInput) {
    const res = await service.message({
      assistant_id: assistantId,
      session_id: sessionId,
      input: messageInput
    })

    processResponse(res);
  }

  async function processResponse(response) {
    if (response.output.generic 
    && response.output.generic.length > 0
    && response.output.generic[0].response_type === 'text') {
      console.log(response.output.generic[0].text);
    }

    service.deleteSession({
      assistant_id: assistantId,
      session_id: sessionId,
    })
  }
})

module.exports = router;