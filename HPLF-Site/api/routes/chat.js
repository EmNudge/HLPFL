const routes = require('express').Router();

const AssistantV2 = require('ibm-watson/assistant/v2');

routes.get('/', async (req, res) => {
  const service = new AssistantV2({
    iam_apikey: process.env.ASSISTANT_IAM_API_KEY, 
    version: '2019-02-28',
  });

  const assistantId = process.env.ASSISTANT_ID;

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
      res.send(response.output.generic[0].text);
    }

    service.deleteSession({
      assistant_id: assistantId,
      session_id: sessionId,
    })
  }
});

module.exports = routes;