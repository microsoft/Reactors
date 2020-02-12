# Arrow Functions

Understanding and utilizing anonymous functions is important to becoming a skilled JavaScript developer. ES6 introduces a new shortened syntax for writing anonymous functions that is the focus of this section.

## Function Keyword

Consider a simple sayHello function assigned to a variable.

```javascript
var sayHello = function(name) {
  console.log('Hello ' + name);
};
```

Utilizing ES6 arrow functions, colloquially fat arrow functions, we can rewrite as such:

```javascript
const sayHello = (name) => {
  console.log(`Hello ${name}`);
};
```

Notice we've ommitted the function keyword and now have an arrow(=>) pointing to the function body. Interesting, but what benefits does this provide other than less typing?

For simple methods we can refine this example further. Single parameters don't need parenthesis and with the function body being a single statement we can remove the curly braces.

```javascript
const sayHello = name => console.log(`Hello ${name}`);
```

Concise. More complex functions will need a more complete body ({}), and multiple parameters will require parenthesis. Another benefit of utilizing arrow functions for simple expressions is implicit returns. Let's create a new example.

```javascript
var square = function(n) {
  return n * n;
};
```

will become

```javascript
const square = n => n * n;
```

Traditional functions require explicit returns, such as in the first square. With arrow function the result of our expressions, n * n, is implicitly returned to the caller. As you might expect this can be chained.

```javascript
const multiplyThrice = x => y => z => x * y * z;
multiplyThrice(2)(4)(6);
// => 48
```

The multiplyThrice variable contains a function that accepts a single parameter and returns another arrow function, which does the same, until the final function multiplies the three passed in numbers. Comparing this to an ES5- implementation

```javascript
var multiplyThrice = function(x) {
  return function(y) {
    return function(z) {
      return x * y * z;
    };
  };
};
```

it is significantly more concise, but potentially much less readable. Also of note, if you're returning an object literal you may not implicitly return that content. The Javascript interpreter will view that as a function body. Reusing our nest function from the Enhanced Object Literals section you might expect to do this:

```javascript
function nest(array, insert) {
  return array
    .reduceRight((accumulator, key) =>
      {
        [key]: accumulator
      }
    , insert);
}
```

Resulting in this error: SyntaxError: Unexpected token :. What used to be the body of the returned object is now the body of our function, so [key]: accumulator is standalone and invalid. Proper usage is with an explicit return.

```javascript
function nest(array, insert) {
  return array
    .reduceRight((accumulator, key) => {
      return {
        [key]: accumulator
      }
    }, insert);
}
```

Or you may wrap your object in parentheses.

```javascript
function nest(array, insert) {
  return array.reduceRight((accumulator, key) => ({ [key]: accumulator }), insert);
}
```

## Context

Fancy syntax isn't the only change with arrow functions. They also inherit context from the parent scope. To demonstrate this let's bring back our Deck class.

```javascript
class Deck {
  initialize() {
    const suits = ['Diamond', 'Heart', 'Spade', 'Club'];
    ="keyword from-rainbow">const faces = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'];
    const deck = [];
    for (const suit of suits) {
      for (const face of faces) {
        deck.push(this.createCard(suit, face));
      }
    }
    this.deck = deck;
  }
}
```

We'll start refactoring for a more functional approach using forEach, but continue using traditional anonymous functions.

```javascript
initialize() {
    const suits = ['Diamond', 'Heart', 'Spade', 'Club'];
    const faces = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'];
    const deck = [];
    suits.forEach(function(suit) {
      faces.forEach(function(face) {
        deck.push(this.createCard(suit, face));
      });
    });
    this.deck = deck;
  }
```

Creating a new Deck will now result in a TypeError: TypeError: Cannot read property 'createCard' of undefined, because this in our anonymous functions don't have the same context as our loops. Pre-ES6 the solution was to save context to a variable.

```javascript
initialize() {
  ...
  var self = this;
  suits.forEach(function(suit) {
    faces.forEach(function(face) {
      deck.push(self.createCard(suit, face));
    });
  });
}
```

Capturing this, our context, into a variable called self, _this or that is pretty common in older codebases. With arrow functions this workaround is no longer necessary.

```javascript
initialize() {
  ...
  suits.forEach(suit => {
    faces.forEach(face => {
      deck.push(this.createCard(suit, face));
    });
  });
}
```

Arrow functions don't create their own context, it looks to the enclosing scope for that information. Therefore this should now refer to the Deck instance, which has a createCard method. Extraneous variables removed, let's turn this fully functional before wrapping up.

```javascript
initialize() {
  const suits = ['Diamond', 'Heart', 'Spade', 'Club'];
  const faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'];
  this.deck = suits.map(
    suit => faces.map(
      face => this.createCard(suit, face)))
    .reduce((deck, cards) => [...deck, ...cards], []);
}
```

## Conclusion

Arrow functions provide a simpler syntax with implicit returns for succinct expressions. Additionally they inherit context from parent scopes. While this is great much of the time there are instances when you want context to change, so be aware of how an arrow function might affect your code.

NEXT: [Using the Fetch API](./fetch.md)
