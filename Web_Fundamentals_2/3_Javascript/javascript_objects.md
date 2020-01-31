# Javascript Objects

In this section, we will focus on another way of storing a collection of information. When we are presented with a number of pieces of information and we wish to keep them in a collection since they are related to each other, normally we would store this collection of information as an array. We will cover the creation of Objects, updating values in an object, and deleting keys of information out of an object. Objects are one of the best ways to store information in an organized way.

Objects are a way to store information where a Key accesses a set Value. Let us keep on reading through the material to find out how this occurs and why we need to learn this.

## Why Objects

Let's say we had information regarding Daenerys Targaryen from Game of Thrones we wanted to store in a variable.

```javascript
var Dany = ['Daenerys', 'Targaryen', 22, 'House Targaryen', 'Valyrian', 'Queen of the Andals the Rhoynar and the First Men', 'Lady Regnant of the Seven Kingdoms', 'Protector of the Realm', 'Khaleesi of the Great Grass Sea', 'Breaker of Chains', 'Mother of Dragons', 'Queen of Meereen']
```

Now that we have a variable of all the information regarding Daenerys, how do we access what culture Daenerys hails from?

```console.log(Dany[4]); // Valyrian```

Notice how we had to remember the exact index of where that information is located. Not only that but how do we know which String in our array is related to her last name? This can be a little confusing since we might not be the creators of the collection we get back. If we wanted to make this easier for ourselves we would be able to state something like this:

```console.log(Dany.last_name); // Targaryen```

But with arrays, we cannot find a named index. To accomplish that, we need to use a structure called an object. An object allows us to find information inside of a collection by naming a key to that value. Let's take a look at that in action.

```javascript
var Dany = {
  first_name: 'Daenerys',
  last_name: 'Targaryen',
  age: 22,
  allegiance: 'House Targaryen',
  ancestry: 'Valyrian',
  titles: ['Queen of the Andals, the Rhoynar and the First Men', 'Lady Regent of the Seven Kingdoms', 'Protector of the Realm', 'Khaleesi of the Great Grass Sea', 'Breaker of Chains', 'Mother of Dragons', 'Queen of Meereen']
}
```

As we can see there are a few changes that were made. First, we are using curly braces. This defines this collection of information as an Object. Next, we can see that we have 'first_name:' which is how we name a key to a value. This portion on the left-hand side is referred to as a key. Using this key unlocks access to the value on the right-hand side. One last thing to note, those values we hold on the right-hand side can be of any type; we can store Strings, Numbers, Arrays or other Objects.

Here is how we access a key-value pair for the Dany variable.

```console.log(Dany.allegiance); // House Targaryen```

NEXT: [The DOM](./the_dom.md)
