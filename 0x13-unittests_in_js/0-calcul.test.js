const calculateNumber = require("./0-calcul.js");
const assert = require('assert');

describe('calculateNumber', function() {
  it('output with positive numbers', function() {
    assert.equal(calculateNumber(1, 3), 4);
    assert.equal(calculateNumber(1, 3.7), 5);
    assert.equal(calculateNumber(1.2, 3.7), 5);
    assert.equal(calculateNumber(1.5, 3.7), 6);
  });

  it('output with negative numbers', function() {
    assert.equal(calculateNumber(1, -3.4), -2);
    assert.equal(calculateNumber(-5, -3.5), -8);
  });

  it('check arguments/TypeError', function() {
    assert.throws(() => calculateNumber(NaN, 0), { name: 'TypeError' });
  });
});
