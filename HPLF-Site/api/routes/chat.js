const routes = require('express').Router();

const prompt = require('prompt-sync')();
const AssistantV2 = require('ibm-watson/assistant/v2');


routes.get("/:sentence", async (req, res) => {
  console.log(req.params.sentence);
  const service = new AssistantV2({
    iam_apikey: process.env.ASSISTANT_IAM_API_KEY, 
    version: '2019-02-28',
    url: "https://gateway.watsonplatform.net/assistant/api"
  });

  const assistantId = process.env.ASSISTANT_ID;
  let sessionId

  //   // Create session.
  // service
  // .createSession({
  //   assistant_id: assistantId,
  // })
  // .then(res => {
  //   sessionId = res.session_id;
  //   sendMessage({
  //     message_type: 'text',
  //     text: req.params.sentence
  //   })
  // }).catch(err => {
  //   console.log(err); // something went wrong
  // });


  //  function sendMessage(messageInput) {
  //   service
  //     .message({
  //       assistant_id: assistantId,
  //       session_id: sessionId,
  //       input: messageInput
  //     })
  //     .then(res => {
  //       processResponse(res);
  //     })
  //     .catch(err => {
  //       console.log(err); // something went wrong
  //     });
  // }

  // function processResponse(response) {
  //   // If an intent was detected, log it out to the console.
  //   if (response.output.intents.length > 0) {
  //     console.log('Detected intent: #' + response.output.intents[0].intent);
  //   }

  //   // Display the output from assistant, if any. Supports only a single
  //   // text response.
  //   if (response.output.generic) {
  //     if (response.output.generic.length > 0) {
  //       if (response.output.generic[0].response_type === 'text') {
  //         console.log(response.output.generic[0].text);
  //       }
  //     }
  //   }
  //   // Prompt for the next round of input.
  //   const newMessageFromUser = prompt('>> ');
  //   if (newMessageFromUser === 'quit') {
  //     service
  //       .deleteSession({
  //         assistant_id: assistantId,
  //         session_id: sessionId,
  //       })
  //       .catch(err => {
  //         console.log(err); // something went wrong
  //       });
  //     return;
  //   }
  //   const newMessageInput = {
  //     message_type: 'text',
  //     text: newMessageFromUser
  //   }
  //   sendMessage(newMessageInput);
  // }





  // Create session.
service
.createSession({
  assistant_id: assistantId,
})
.then(res => {
  sessionId = res.session_id;
  sendMessage({
    message_type: 'text',
    text: req.params.sentence // start conversation with empty message
  });
})
.catch(err => {
  console.log(err); // something went wrong
});

// Send message to assistant.
function sendMessage(messageInput) {
service
  .message({
    assistant_id: assistantId,
    session_id: sessionId,
    input: messageInput
  })
  .then(res => {
    processResponse(res);
  })
  .catch(err => {
    console.log(err); // something went wrong
  });
}


// Process the response.
function processResponse(response) {
  // Display the output from assistant, if any. Supports only a single
  // text response.
  if (response.output.generic) {
    if (response.output.generic.length > 0) {
      if (response.output.generic[0].response_type === 'text') {
        console.log(response.output.generic[0].text);
      }
    }
  }


// We're done, so we close the session.
service
  .deleteSession({
    assistant_id: assistantId,
    session_id: sessionId,
  })
  .catch(err => {
    console.log(err); // something went wrong








});
}
});




 
  

module.exports = routes;
