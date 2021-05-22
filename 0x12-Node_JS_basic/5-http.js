const http = require('http');
const countStudents = require('./3-read_file_async');

const HOSTNAME = '127.0.0.1';
const PORT = 1245;
const DATABASE = process.argv[2];

const app = http.createServer(async (req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    try {
      const { totalMsg, csMsg, sweMsg } = await countStudents(DATABASE);
      const response = `${totalMsg}\n${csMsg}\n${sweMsg}`;
      res.write('This is the list of our students\n');
      res.end(response);
    } catch (error) {
      res.end(error.toString());
    }
  } else {
    res.writeHead(404);
    res.end('Invalid request');
  }
}).listen(PORT, HOSTNAME);

module.exports = app;
