# CSS Selectors

A selector is used to identify what items to modify. You can use selectors to identify an individual element, all elements of a particular type, elements with certain attributes or groupings, or even items based on their page location.

## Common selectors

* All elements with a specific HTML tag (such as p, h1).
* Elements specified by the following attributes:
  * ID: These are preceded by *#* in CSS. They must be unique and can only be used once on a page.
  * Class: These are preceded by *.* in CSS. They can be used multiple times to share repeating CSS code.

## Declaration block

A declaration block is a list of declarations contained within braces. Each declaration consists of a property, a colon (":"), and a value. If a block has multiple declarations, they must be separated by a semi-colon (";").

### Declaration block examples

For all "p" HTML tags, make the font color blue:

``` css
p{
  color: blue;
}
```

For an element with the ID "important", make the font size 36px:

``` css
#important{
  font-size: 36px;
}
```

For all elements with the class "info", make the background green and add a 1px wide black border:

``` css
.info{
  background-color: green;
  border: 1px solid black;
}
```

In the above examples, ```p```, ```#important```, and ```.info``` are selectors. Color, font-size, background-color, and border are properties.

## Prioritizing selectors

Now that we know a little more about how to use selectors, let’s make a general list of the internal priorities for CSS and how they are weighted. CSS breaks conflicts by using this weighted scoring system:

* Element (1 point)
* .class (10 points)
* #id (100 points)

This is the default priority order. In addition to this, specificity will also count. For example, *ul li* will override *li*. [W3C has good information about specificity](https://www.w3schools.com/css/css_specificity.asp), including how to calculate internal weight.

li            {...}  /* a=0 b=0 c=1 -> specificity =   1 */
ul li         {...}  /* a=0 b=0 c=2 -> specificity =   2 */
ul ol li      {...}  /* a=0 b=0 c=3 -> specificity =   3 */
li.red        {...}  /* a=0 b=1 c=1 -> specificity =  11 */
ul ol li.red  {...}  /* a=0 b=1 c=3 -> specificity =  13 */
 list         {...}  /* a=1 b=0 c=0 -> specificity = 100 */

* **a** represents the number of #id attributes in the selector.
* **b** represents the number of class attributes.
* **c** represents the number of tag names.

Combining these into a number will provide their actual weight. This means that *li #list* will have the same weight as *ul #list*. This may appear to be very confusing, but it’s actually simpler than you might think: **it’s all about counting**.

Check out these useful CSS selector resources:

* [10 CSS Selectors You Shouldn't Code Without](http://www.webdesignerdepot.com/2013/08/10-css-selectors-you-shouldnt-code-without/)
*[CSS Selector Reference Guide](http://www.w3schools.com/cssref/css_selectors.asp)


Next: [Activity: Dojo Diner](./dojo-diner.md)
