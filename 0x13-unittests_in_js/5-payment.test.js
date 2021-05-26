const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function() {
  const sandbox = sinon.createSandbox();

  beforeEach(() => {
    sandbox.spy(console, 'log');
  });

  afterEach(() => {
    sandbox.restore();
  });

  it('output of sendPaymentRequestToApi with 100 and 20 as args', function() {
    sendPaymentRequestToApi(100, 20);
    expect(console.log.calledOnceWith('The total is: 120')).to.be.true;
  });

  it('output of sendPaymentRequestToApi with 10 and 10 as args', function() {
    sendPaymentRequestToApi(10, 10);
    expect(console.log.calledOnceWith('The total is: 20')).to.be.true;
  });
});
