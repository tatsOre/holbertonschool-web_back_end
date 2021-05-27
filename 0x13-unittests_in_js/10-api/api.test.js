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

describe('GET /available_payments', () => {
  it('request to /available_payments', (done) => {
    request('http://localhost:7865/available_payments', (err, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(JSON.parse(body)).to.eql({ payment_methods: { credit_cards: true, paypal: false } });
      done();
    });
  });
});

describe('POST /login', () => {
  it('request to /login sucess', (done) => {
    const options = {
      url: 'http://localhost:7865/login',
      json: { userName: 'Betty' }
    };
    request.post(options, (err, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).equals('Welcome Betty');
    }, done());
  });

  it('request to /login undefined', (done) => {
    const options = {
      url: 'http://localhost:7865/login'
    };
    request.post(options, (err, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).equals('Welcome undefined');
    }, done());
  });
});
