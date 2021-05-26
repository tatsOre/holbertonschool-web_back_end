const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function() {
  it('validate the usage of the Utils calculateNumber', function() {
    const logSpy = sinon.spy(console, 'log');
    const calStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    sendPaymentRequestToApi(100, 20);

    expect(calStub.calledWith('SUM', 100, 20)).to.be.true;
    expect(logSpy.calledOnceWith('The total is: 10'));

    logSpy.restore();
    calStub.restore();
  });
});
