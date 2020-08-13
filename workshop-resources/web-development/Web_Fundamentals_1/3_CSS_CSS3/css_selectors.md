# CSS Selectors

A selector is used to identify what items to modify. You can use selectors to identify an individual element, all elements of a particular type, elements with certain attributes or groupings, or even identify items based on their location in a page.

## Declaration block

A declaration block is a list of declarations contained within braces. Each individual declaration consists of a property, a colon (":"), and a value. If a block has multiple declarations, they must be separated by a semi-colon(";").

## Selecting elements

To select all elements of a particular type, such as `a`, `strong` or `div`, you simply use the name of the element. If you wanted to make all `p` elements blue, you could use the following:

``` css
p{
  color: blue;
}
```

## Selecting an individual element by id

HTML allows you to add IDs to elements. While we mostly focused on this behavior for [links](../2_HTML/common_body_tags.md#anchors) and [forms](../2_HTML/forms.md), you can add an ID to any element to identify it for use with CSS (or with JavaScript). We could identify an item with an ID of **heading** by using its name with a `#` in front.

``` css
#heading{
  font-size: 36px;
}
```

## Classes

You may wish to group items of a certain type together to ensure they're all displayed the same way. For example, you might want to bold links in a navigation pane, or ensure certain `h3` elements are blue. By using a `class` attribute you can group these items together, regardless of where they appear on a page. If you wish to add multiple classes to an item, you simply add spaces between the class names. So if we wanted a `div` to use both the `navigation` and `banner` class, we could use the following:

``` html
<div class="navigation banner">Hello, world!</div>
```

We can then create CSS to apply to classes by prepending the name of the class with a `.`.

``` css
.navigation {
  text-weight:bold;
}
.banner {
  color: blue;
}
```

> **NOTE**: If an element has multiple classes which match items in your stylesheet, all settings will be applied.

## Scoring

It doesn't take long to realize you could wind up in a situation where you could have a conflict in CSS settings. Consider the following:

``` html
<div class="header">Hello, world</div>
```

``` css
div{
  color: red;
}
.header{
  color: blue;
}
```

What color will **Hello, world** be? You could use a tool like [CodePen](https://codepen.io) to find out.

CSS breaks these types of conflicts by using a scoring system. At its root level, the following values are applied:

- element (1 point)
- .class (10 points)
- #id (100 points)

In a nutshell, the scoring is used to identify how specific of a reference to the item was made.

So in our example, the class entry of `div` would have a score of **1**, and the class of `header` **10**. Thus, the color would be red.

## Getting more specific

The three selectors listed above are the most common. However, there are [many more selectors](https://www.w3schools.com/cssref/css_selectors.asp) offering you quite a bit of power for identifying specific items in a page.

However, even with those three we can still get more specific. Here's just a few possibilities

``` css
div{
  /* all div elements */
  color: red;
}
div.header{
  /* only div elements with a class of header */
  color: blue;
}
div a{
  /* only a elements inside a div */
  color: green;
}
div a.navigation{
  /* only a elements with a class of navigation inside a div */
  color: purple;
}
```

### Exercise

What color will the items in this HTML page be displayed?

``` html
<div>div</div>
<div class="header">div with header</div>
<div class="navigation">div with navigation</div>
<a>anchor</a>
<a class="navigation">anchor with navigation</a>
<div>
  <a class="navigation">anchor in div with navigation</a>
  <br />
  <a>anchor in div</a>
</div>
```

## What you learned

In this lesson, We learned how to style HTML elements by selecting them with their tag or by using a class or ID. Remember that IDs are used only once, And classes are designed to be used over and over again to style elements. Let’s look at how to style HTML elements.

Next: [Styling Elements](./styling_elements.md)
