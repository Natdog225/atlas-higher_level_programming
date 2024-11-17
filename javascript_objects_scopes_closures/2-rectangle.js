#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) { // Check if w and h are positive integers
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
