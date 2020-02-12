# Basic Functions I

## Objective: Understand how a computer executes each line of code

* Get comfortable with how a function works and how its return statement works
* Identify some common mistakes students make and learn how to avoid them
* Predict the output of the following code snippets.  Please do NOT run any of this code directly, but first predict the output on paper. Once you've predicted the output for all of the codes, then run the code one by one and compare the two.

## Note

Open a text file and write down the predictions you have for each code snippet. To test them open your console in your browser and run the code there.

```javascript
function a(){
    return 35;
}
console.log(a())
```

```javascript
function a(){
    return 4;
}
console.log(a()+a());
```

```javascript
function a(b){
    return b;
}
console.log(a(2)+a(4));
```

```javascript
function a(b){
    console.log(b);
    return b*3;
}
console.log(a(3));
```

```javascript
function a(b){
   return b*4;
   console.log(b);
}
console.log(a(10));
```

```javascript
function a(b){
    if(b<10) {
        return 2;
    }
    else     {
        return 4;
    }
    console.log(b);
}
console.log(a(15));
```

```javascript
function a(b,c){
    return b*c;
}
console.log(10,3);
console.log( a(3,10) );
```

```javascript
function a(b){
    for(var i=0; i<10; i++){
        console.log(i);
    }
    return i;
}
console.log(3);
console.log(4);
```

```javascript
function a(){
    for(var i=0; i<10; i++){
        i = i +2;
        console.log(i);
    }
}
a();
```

```javascript
function a(b,c){
    for(var i=b; i<c; i++) {
       console.log(i);
   }
   return b*c;
}
a(0,10);
console.log(a(0,10));
```

```javascript
function a(){
    for(var i=0; i<10; i++){
       for(var j=0; j<10; j++){
           console.log(j);
       }
       console.log(i);
    }
}
```

```javascript
function a(){
    for(var i=0; i<10; i++){
        for(var j=0; j<10; j++){
            console.log(i,j);
        }
        console.log(j,i);
    }
}
```

```javascript
var z = 10;
function a(){
    var z = 15;
    console.log(z);
}
console.log(z);
```

```javascript
var z = 10;
function a(){
    var z = 15;
    console.log(z);
}
a();
console.log(z);
```

```javascript
var z = 10;
function a(){
    var z = 15;
    console.log(z);
    return z;
}
z = a();
console.log(z);
```

NEXT: [Javascript Foundations](./javascript_foundations_1.md)
