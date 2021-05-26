const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function() {
  it('validate the usage of the Utils calculateNumber', function() {
    const calSpy = sinon.spy(Utils, 'calculateNumber');
    const apiReq = sendPaymentRequestToApi(100, 2);

    expect(calSpy.calledOnce).to.be.true;
    expect(Utils.calculateNumber('SUM', 100, 2)).to.equal(apiReq);

    calSpy.restore();
  });
});
