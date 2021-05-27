const { expect } = require('chai');
const request = require('request');

describe('/GET index page', () => {
  it('check index page response', (done) => {
    request('http://localhost:7865', (err, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(response.statusMessage).to.equal('OK');
      expect(body).to.equal('Welcome to the payment system');
    });
    done();
  });
});

describe('GET /cart/:id', () => {
  it('request to /cart/:id on success', (done) => {
    request('http://localhost:7865/cart/12', (err, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(response.statusMessage).to.equal('OK');
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('request to /cart/:id on failure', (done) => {
    request('http://localhost:7865/cart/hello', (err, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});
