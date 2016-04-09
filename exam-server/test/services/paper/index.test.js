'use strict';

const assert = require('assert');
const app = require('../../../src/app');

describe('paper service', () => {
  it('registered the papers service', () => {
    assert.ok(app.service('papers'));
  });
});
