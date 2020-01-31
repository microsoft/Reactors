# Javascript Objects

An object is something that we can describe with attributes. In the real world a car is an object. It is an object because we can give it properties like color and max_speed, and we can also give it methods like brake, signal, stop, and drive.

## Car Object Properties and Methods

**Car Properties:**

* car.color = red
* car.model = XF-RS
* car.make = Jaguar
* car.max_speed = 200

**Car Methods:**

* car.start()
* car.stop()
* car.signal()
* car.brake()

All cars have the same properties and methods. The specific values for the car's properties will be different for each car and the car's methods will be executed separately and at different times from other cars.

## Using JavaScript

We know that JS variables are storage containers for information, and in this case car values. We can assign a value, in this case the car's make to a variable we create called `car`:
`var car = "Jaguar";`

Don't forget that we can treat objects just like variables, since they are variables that can contain multiple values. Look at this code:
`var car = {color:"red", model:"XFRS", color:"red", max_speed:250};`

Here we are defining the car with an "object literal" that we can also express like this:

```javascript
var car = {
        color:"red",
        model:"XFRS",
        color:"red",
        max_speed:250
};
```

The values are written as **name:value pairs** (name and value separated by a colon). We can access the values inside of our objects more than one way. To access the color value of the car we can use: `car.color` or, we can also access color like this: `car["color"]`

We can work with the car's methods in the same way. [To learn more about JS Objects read up on them here.](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)

NEXT: [The DOM](./the_dom.md)
