# CSS Selectors

Selectors are used for declaring the HTML elements to which a style will apply.

## The most common selectors are

* all elements with a specific HTML tag (e.g., p, h1)
* elements specified by the following attributes:
  * id (these are preceded by # in CSS) These must be unique and can only be used once on your page.
  * class (these are preceded by .  in CSS) These can be used multiple times to share repeating CSS code.
Declaration Block
A declaration block is a list of declarations contained within braces. Each individual declaration consists of a property, a colon (":"), and a value. If a block has multiple declarations, they must be separated by a semi-colon(";").

## Here are some examples

For all "p" HTML tags, make the font color blue:

``` css
p{
  color: blue;
}
```

For an element with the id "important", make the font size 36px.

```css
#important{
  font-size: 36px;
}
```

For all elements with the class "info", make the background green and add a 1px wide black border.

```css
.info{
  background-color: green;
  border: 1px solid black;
}
```

In the above examples, ```p```, ```#important```, and ```.info``` are selectors. Color, font-size, background-color, and border are properties.

## More on selectors

<http://www.webdesignerdepot.com/2013/08/10-css-selectors-you-shouldnt-code-without/>
<http://www.w3schools.com/cssref/css_selectors.asp>

Now that we know a little more about how to use selectors, let’s make a general list of the internal priorities for CSS:

* element (1 point)
* .class (10 points)
* #id (100 points)

This is the default priority order. In addition to this, specificity will also count, for example,  ul li will override li. W3C has made a decent table over how you should calculate internal weight:

li            {...}  /* a=0 b=0 c=1 -> specificity =   1 */
ul li         {...}  /* a=0 b=0 c=2 -> specificity =   2 */
ul ol li      {...}  /* a=0 b=0 c=3 -> specificity =   3 */
li.red        {...}  /* a=0 b=1 c=1 -> specificity =  11 */
ul ol li.red  {...}  /* a=0 b=1 c=3 -> specificity =  13 */
 list         {...}  /* a=1 b=0 c=0 -> specificity = 100 */

a represents the number of #id attributes in the selector
b represents the number of class attributes
c represents the number of tag names

Combining these into a number will give you the actual weight. This means that  li #list will have the same weight as ul #list. This is probably one of the most confusing things about the cascade scheme, but it’s actually simpler than you might think: **it’s all about counting**.

## What you learned

In this lesson, We learned how to style HTML elements by selecting them with their tag or by using a class or ID. Remember that IDs are used only once, And classes are designed to be used over and over again to style elements. Let’s look at how to style HTML elements.

Next: [Styling Elements](./styling_elements.md)
