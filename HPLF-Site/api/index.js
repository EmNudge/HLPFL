const app = require('express')();
const bodyParser = require('body-parser');

const chat = require('./routes/chat.js');
const voice = require('./routes/voice.js');
const article = require('./routes/article.js');

app.use(bodyParser.json())
app.use('/chat', chat);
app.use('/voice', voice);
app.use('/article', article);

module.exports = app;