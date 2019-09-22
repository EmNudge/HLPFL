const routes = require('express').Router()
const AssistantV2 = require('ibm-watson/assistant/v2')

routes.post('/', async (req, res) => {
  const service = new AssistantV2({
    iam_apikey: process.env.ASSISTANT_IAM_API_KEY,
    version: '2019-02-28',
    url: 'https://gateway.watsonplatform.net/assistant/api'
  })

  const assistantId = process.env.ASSISTANT_ID;

  const {session_id: sessionId} = await service.createSession({ assistant_id: assistantId })
  sendMessage({
    message_type: 'text',
    text: req.body.sentence // start conversation with empty message
  });

  // Send message to assistant.
  async function sendMessage(messageInput) {
    service.message({
      assistant_id: assistantId,
      session_id: sessionId,
      input: messageInput
    }).then(res => {
      processResponse(res);
    })
  }

  function processResponse(response) {
    
    if (response.output.generic
    && response.output.generic.length > 0
    && response.output.generic[0].response_type === 'text') {
      res.json({ response: response.output.generic[0].text });
    }
      
    service.deleteSession({
      assistant_id: assistantId,
      session_id: sessionId
    })
  }
})

module.exports = routes
