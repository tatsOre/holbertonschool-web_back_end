const express = require('express');
const router = require('./routes/index');

const app = express();
const port = 1245;
app.listen(port);

app.use('/', router);
app.use('/students', router);
app.use('/students/:major', router);

module.exports = app;
