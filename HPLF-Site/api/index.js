const app = require('express')();

const chat = require('./routes/chat.js');
const voice = require('./routes/voice.js');

app.use('/chat', chat);
app.use('/voice', voice);

module.exports = app;