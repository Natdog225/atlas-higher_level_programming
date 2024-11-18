#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { // Check if positive
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = class Rectangle {};