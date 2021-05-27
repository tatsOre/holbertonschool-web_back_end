const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function() {
  it('getPaymentTokenFromAPI response', function(done) {
    getPaymentTokenFromAPI('sucess')
      .then((response) => {
        expect(response).to.deep.equal({ data: 'Successful response from the API' });
        done();
      })
      .catch((err) => done(err))
  });
});
