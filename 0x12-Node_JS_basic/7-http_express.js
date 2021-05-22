const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;
const database = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const { totalMsg, csMsg, sweMsg } = await countStudents(database);
  const response = `${totalMsg}\n${csMsg}\n${sweMsg}`;
  res.send(response);
});

app.listen(port);

module.exports = app;
