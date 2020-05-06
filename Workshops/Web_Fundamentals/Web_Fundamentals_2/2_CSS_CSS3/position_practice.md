# The Position Property

In addition to the display property and the box model, the **position property**can also be used to move elements on a page. Use the position property **only when you need to**. Otherwise, use the display property and the box model to position your elements. The CSS specification offers us six position values, but we'll be covering the main four: **static, relative, absolute and fixed**. Each property serves a specific purpose. Understanding that purpose is the key to mastering CSS-based layouts.

## **Consider the following:**

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

## **Static**

Static positioning is the default. Any element that has position: static applied is in the normal document flow. The rules for where it sits and how it affects other boxes are defined by the **box model** (refer to the previous tab for the box model).

A statically positioned element will ignore any values for the properties, top, right, bottom, and left as well as any z-index declarations. In order to use any of those properties, your element must have absolute, relative, or fixed positioning applied.

## **Absolute**

Absolutely positioned elements are completely removed from the normal document flow. As far as the elements around them are concerned the absolutely positioned element doesn't exist. **It's as though the display property of the element was set to none.** If you want to maintain the space so other elements don't move to fill it you need to account for it in other ways.

You set the location of an absolutely positioned element through the top, right, bottom, and left properties. You'll usually define only two of these, either top or bottom, and either left or right. By default, each will have a value of auto set.

The key to understanding absolute positioning is understanding where the origin is. If the top is set to 20px, the question you should be asking is: 20px from where?

**An absolutely positioned element is positioned relative to the first parent element that has a position other than static applied to it. If no parent element up the chain meets that condition the absolutely positioned element is positioned relative to the document window.**

Using absolute positioning on box-1:

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

## **Relative**

Relatively positioned elements are positioned based on the same top, right, bottom, and left properties, but are simply shifted from where they would normally sit. In a sense adding relative positioning is similar to adding a margin with **one very important difference: the elements around a relatively positioned element act as though that shift didn't exist**. They ignore it.

Using relative positioning on box-2:

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

## **Fixed**

Fixed positioning acts similarly to absolute positioning with a couple of differences. First, the fixed positioned element is always positioned relative to the browser window and takes the now familiar top, right, bottom, and left properties. The second difference is inherent in the name: fixed positioned elements are fixed. They don't move as the page is scrolled.

## **Extras**

An awesome resource on how to center elements: [http://designshack.net/articles/css/how-to-center-anything-with-css/](http://designshack.net/articles/css/how-to-center-anything-with-css/)

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

Another way to horizontally center an element:

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

NEXT: [Activity: Portfolio Webpage](./portfolio_activity.md)
