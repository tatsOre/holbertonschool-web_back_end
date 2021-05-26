const calculateNumber = require("./2-calcul_chai.js");
const { expect } = require('chai');

describe('calculateNumber - SUM', function() {
  it('output with positive numbers', function() {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
  });
  it('output with negative numbers', function() {
    expect(calculateNumber('SUM', 1, -3.4)).to.equal(-2);
    expect(calculateNumber('SUM', -5, -3.5)).to.equal(-8);
  });
  it('check arguments/TypeError', function() {
    expect(() => calculateNumber('SUM', NaN, 0)).to.throw(TypeError);
  });
});

describe('calculateNumber - SUBTRACT', function() {
  it('output with positive numbers', function() {
    expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(-2);
    expect(calculateNumber('SUBTRACT', 1, 3.7)).to.equal(-3);
  });
  it('output with negative numbers', function() {
    expect(calculateNumber('SUBTRACT', 1, -3.4)).to.equal(4);
    expect(calculateNumber('SUBTRACT', -5, -3.5)).to.equal(-2);
  });
  it('check arguments/TypeError', function() {
    expect(() => calculateNumber('SUBTRACT', NaN, 0)).to.throw(TypeError);
  });
});

describe('calculateNumber - DIVIDE', function() {
  it('output with positive numbers', function() {
    expect(calculateNumber('DIVIDE', 15, 3)).to.equal(5);
    expect(calculateNumber('DIVIDE', 25.4, 3.7)).to.equal(6.25);
  });
  it('output with negative numbers', function() {
    expect(calculateNumber('DIVIDE', 60, -3.4)).to.equal(-20);
    expect(calculateNumber('DIVIDE', -54, -3.5)).to.equal(18);
  });
  it('arguments/TypeError', function() {
    expect(() => calculateNumber('DIVIDE', 0, NaN)).to.throw(TypeError);
  });
  it('division by 0', function() {
    expect(calculateNumber('DIVIDE', 45, 0)).to.equal('Error');
  });
});
