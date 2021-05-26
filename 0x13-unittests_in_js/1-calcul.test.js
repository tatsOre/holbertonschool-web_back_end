const calculateNumber = require('./1-calcul');
const assert = require('assert');

describe('calculateNumber - SUM', function() {
  it('output with positive numbers', function() {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
  });
  it('output with negative numbers', function() {
    assert.strictEqual(calculateNumber('SUM', 1, -3.4), -2);
    assert.strictEqual(calculateNumber('SUM', -5, -3.5), -8);
  });
  it('check arguments/TypeError', function() {
    assert.throws(() => calculateNumber('SUM', NaN, 0), { name: 'TypeError' });
  });
});

describe('calculateNumber - SUBTRACT', function() {
  it('output with positive numbers', function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 3), -2);
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 3.7), -3);
  });
  it('output with negative numbers', function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 1, -3.4), 4);
    assert.strictEqual(calculateNumber('SUBTRACT', -5, -3.5), -2);
  });
  it('check arguments/TypeError', function() {
    assert.throws(() => calculateNumber('SUBTRACT', NaN, 0), { name: 'TypeError' });
  });
});

describe('calculateNumber - DIVIDE', function() {
  it('output with positive numbers', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 15, 3), 5);
    assert.strictEqual(calculateNumber('DIVIDE', 25.4, 3.7), 6.25);
  });
  it('output with negative numbers', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 60, -3.4), -20);
    assert.strictEqual(calculateNumber('DIVIDE', -54, -3.5), 18);
  });
  it('arguments/TypeError', function() {
    assert.throws(() => calculateNumber('DIVIDE', 0, NaN), { name: 'TypeError' });
  });
  it('division by 0', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 45, 0), 'Error');
  });
});
