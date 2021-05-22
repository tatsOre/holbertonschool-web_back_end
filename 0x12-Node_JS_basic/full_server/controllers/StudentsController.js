const readDatabase = require('../utils');

const database = process.argv[2];

class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(database)
      .then((studentsPerFields) => {
        const firstline = 'This is the list of our students';
        const message = [];
        for (const [key, value] of Object.entries(studentsPerFields)) {
          message.push(`Number of students in ${key}: ${value.length}. List: ${value.join(', ')}`);
        }
        response.status(200).send(`${firstline}\n${message.join('\n')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    readDatabase(database)
      .then((studentsPerFields) => {
        const MAJOR = request.params.major;
        if (!Object.keys(studentsPerFields).includes(MAJOR)) {
          response.status(500).send('Major parameter must be CS or SWE');
        }
        const message = `List: ${studentsPerFields[MAJOR].join(', ')}`;
        response.status(200).send(message);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}

module.exports = StudentsController;
