const app = require('express')();
const bodyParser = require('body-parser');

const chat = require('./routes/chat.js');
const voice = require('./routes/voice.js');

app.use(bodyParser.json())
app.use('/chat', chat);
app.use('/voice', voice);

module.exports = app;