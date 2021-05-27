const { expect } = require('chai');
const request = require('request');

describe('Basic Integration testing', () => {
  describe('/GET index page', () => {
    it('check index page response', (done) => {
      request('http://localhost:7865', (err, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(response.statusMessage).to.equal('OK');
        expect(body).to.equal('Welcome to the payment system');
      }, done());
    });
  });
});
