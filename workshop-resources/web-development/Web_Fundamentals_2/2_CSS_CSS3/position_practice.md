# The Position Property

In addition to the display property and the box model, the **position property** can also be used to move elements on a page. Use the position property **only when you need to**. Otherwise, use the display property and the box model to position your elements. The CSS specification offers six position values, but you will learn the main four: **static, relative, absolute, and fixed**. Each property serves a specific purpose; understanding that purpose is the key to mastering CSS-based layouts.

## Positioning example

``` html
<div id="container">
  <div id="box-1">
  </div>
  <div id="box-2">
  </div>
  <div id="box-3">
  </div>
</div>
```

``` css
#container{
  background-color: yellow;
  display: inline-block;
}
#box-1, #box-2, #box-3{
  height: 100px;
  width: 100px;
  margin: 10px;
  display: inline-block;
}
#box-1{
  background-color: green;
}
#box-2{
  background-color: pink;
}
#box-3{
  background-color: blue;
}
```

This results in:

![Positioning Example](../images/positioning-03.gif)

## Static positioning

Static positioning is the default. For any element that has position, static is in the normal document flow. The location rules and its effect on other boxes are defined by the [**box model**](../box_model.md).

A statically-positioned element will ignore any values for the properties (top, right, bottom, left) as well as any z-index declarations. To use those properties, your element must have absolute, relative, or fixed positioning applied.

## Absolute positioning

Absolutely-positioned elements are completely removed from the normal document flow. As far as the elements around them are concerned, the absolutely-positioned element doesn't exist. **It's as though the display property of the element was set to "none".** If you want to maintain the space so other elements can't fill it, you must account for it in other ways.

To maintain the space, you can set the location using the top, right, bottom, and left properties. You'll usually define only two of these--either top or bottom or left or right. By default, each will have a value of auto set.

The key to understanding absolute positioning is understanding where the origin is. If the top is set to 20px, the question you should be asking is: 20px from where?

**An absolutely-positioned element is positioned relative to the first parent element that has a position other than static position applied to it. If no parent element meets that condition, the absolutely-positioned element is positioned relative to the document window.**

So, here's how you can use absolute positioning on box-1:

``` css
#container{
  background-color: yellow;
  display: inline-block;
}
#box-1, #box-2, #box-3{
  height: 100px;
  width: 100px;
  margin: 10px;
  display: inline-block;
}
#box-1{
  background-color: green;
  position: absolute;
  top: 40px;
}
#box-2{
  background-color: pink;
}
#box-3{
  background-color: blue;
}
```

This results in:

![Absolute Position](../images/absolute-03.gif)

## Relative positioning

Relatively-positioned elements are positioned based on the same top, right, bottom, and left properties, but are simply shifted from where they would normally sit. In a sense, adding relative positioning is similar to adding a margin with **one very important difference: the elements around a relatively-positioned element act as though that shift didn't exist**. They ignore it.

This is the code to use relative positioning on box-2:

``` css
#container{
  background-color: yellow;
  display: inline-block;
}
#box-1, #box-2, #box-3{
  height: 100px;
  width: 100px;
  margin: 10px;
  display: inline-block;
}
#box-1{
  background-color: green;
}
#box-2{
  background-color: pink;
  position: relative;
  top: 20px;
  left: 20px;
}
#box-3{
  background-color: blue;
}
```

This results in:

![Relative Position](../images/relative-03.gif)

## Fixed positioning

Fixed positioning acts similarly to absolute positioning with a couple of differences. First, the fixed position element is always positioned relative to the browser window and takes the now familiar top, right, bottom, and left properties. The second difference is inherent in the name: fixed position elements are fixed. They don't move as the page is scrolled.

## Tips and resources

An easy way to center an element inside a container:

``` html
<div id="container">
  <div id="center-me">
  </div>
</div>
```

``` css
#container{
  width:200px;
  height:200px;
  background: blue;
  position:relative;
}
#center-me{
  background: red;
  height: 100px;
  width: 100px;
  margin: auto;
  position: absolute;
  left: 0;
  bottom: 0;
  top: 0;
  right: 0;
}
```

Another way to horizontally-center an element:

``` html
<div id="container">
  <div id="center-me">
  </div>
</div>
```

``` css
#container{
  width:200px;
  height:200px;
  background: blue;
  position:relative;
}
#center-me{
  background: red;
  height: 100px;
  width: 100px;
  margin: 0 auto;
}
```
Design Shack has a good article on [How to Center Anything With CSS](http://designshack.net/articles/css/how-to-center-anything-with-css/).

NEXT: [Activity: Re-Create a Portfolio Page](./portfolio_activity.md)
