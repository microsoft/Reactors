# Asynchronous Programming in JavaScript
Performing long-running operations, like calling external endpoints, shouldn't be confusing or cause performance issues. Use asynchronous programming in JavaScript to create more efficient and performant programs by running multiple chunks of code at a time.

## Main principles:
- Statements are executed in parallel.
- Non-blocking: Application can continue to handle user input and perform other tasks while a task is already running.
- Use a worker to run expensive processes off the main thread so that user interaction is not blocked.
- Useful for managing long-running operations which will otherwise stop execution, such as: 
  - Server calls 
  - Database access 
  - Complex algorithms
  
## Callbacks:
- Original mechanism for managing long-running operations.
  - Pass a function to be called when operation is complete. 
- Specify what should happen after statement is executed (Ex: `setTimeout()`).
- [CodePen example of using callbacks](https://codepen.io/GeekTrainer/pen/PoqBZVJ?editors=0011).

## Promises:
- Act as an IOU:
  - Basically saying "Hey, go do this task, and get back to me when you're done".
  - Execute additional code after async function is complete.
  - Contain info about the operation and track status.
  - Can string together multiple, then calls to process a series of async calls.
- Now part of ES6.
- How are promises different than callbacks?
  - Promises are essentially callbacks under the hood but they let us write the syntax that’s easier to work with.
  - Provide more organization and readability than nested callbacks.
- [CodePen example of an HTTP call using fetch with promises](https://codepen.io/GeekTrainer/pen/KKpBMPp?editors=0011).

## Async/await:
- Streamlines asynchronous programming:
  - Makes calls feel synchronous as execution "awaits" long-running operation.
  - Runtime is free to use process for other operations while waiting. 
  - Eliminates need to create callback functions. 
- Added with ES2017: 
  - May not be supported in some environments.
- How is async/await different than promises?  
  - async/await keyworkd more closesly resembles synchronous code patterns.
  - Simpler and more human readable syntax.
- [CodePen example of fetch using async/await](https://codepen.io/GeekTrainer/pen/qBdyNEp?editors=0011).

## Resources:
- [Asynchronous Programming Concepts on Wikipedia](https://en.wikipedia.org/wiki/Asynchrony_(computer_programming))
- [Javascript.info on Callbacks](https://javascript.info/callbacks)
- [MDN Docs on Promises](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Promises)
- [MDN Docs on async/await](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Async_await)
- [Reactors Web Fundamentals 2 Course](https://github.com/microsoft/Reactors/tree/main/Web_Fundamentals_2)
