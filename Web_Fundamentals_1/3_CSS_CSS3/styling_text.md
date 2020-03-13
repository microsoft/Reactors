# Styling Text

As with the size and border of an element, we have a lot of control over the text. Let's walk through a few popular properties.

## color

`color` is used to set the color. The value of the color property can be expressed using hex, RGB or semantic code.

``` css
p {
  color: #ffffff;
}
a {
  color: rgb(255, 255, 255);
}
span {
  color: white;
}
```

## text-align

`text-align` is used to set the horizontal alignment of any text. Text can be `centered`, or aligned to the `left` or `right`, or `justified`. This property will only work if the property is also `display: block`.

``` css
h1 {
  text-align: center;
}
```

## text-decoration

`text-decoration` is used to add and remove `underline`s, `overline`s, and `line-through`s.

``` css
a {
  text-decoration: none; /* removes the underline */
}
```

> **NOTE**: Use caution when either adding or removing underlines. Adding underline to text which isn't a link can be confusing to users viewing your page. Removing underlines from a link can make your page less accessible as it becomes tougher to see where the links are.

## font-style

`font-size` controls the slanted emphasis of the text. Some text may have an italic property built into the font and so selecting italic would be fine. For fonts that do not have an italic style, the value oblique can be used to mimic italicized text.

``` css
span {
  font-style: italic;
}
```

> **NOTE**: Italics may not display overly clean on many browsers; use it with caution.

## font-weight

`font-weight` defines the thickness of a character line. `normal` is often the default value. The values can be set numerically or semantically.

``` css
p {
  font-weight: bold;
}
```

## Font

Setting fonts is a relatively involved topic as you need to ensure the font you wish to use is actually available. As a result, you'll notice you typically either give the browser some guidance of what type (or family) of font to use, or provide fallback options if the specific font you wish to use isn't available.

### font-family

`font-family` property specifies the font style to use for an element. There are two types of font families - named, where you're providing a specific class of font such as `courier` or `arial`, or generic where you're providing more high-level guidance of the type of font to use, such as `serif` or `sans-serif`.

``` css
p{
  font-family: serif; /* feet on the font */
}
div{
  font-family: courier; /* courier or similar */
}
```

### Web-safe fonts

There are fonts that are installed on pretty much all systems and so are termed web safe fonts because you can with some certainty know it will look the same regardless of the system the user has. Some of these are `Verdana`, `Arial`, `Trebuchet MS`, `Times New Roman`, `Georgia`, `Andale Mono`, `Courier New`, `Comic Sans`, and `Impact`.

``` css
p {
  font-family: "helvetica neue", arial, verdana, sans-serif;
}
```

Font-family allows for multiple options to be entered where the browser goes through them from left to right until it finds a font that is installed on the system which can be used. This means that you always want to make sure you have a generic-family option as your last value so that if none of the others can be found, the browser will use the system default for the family specified.

The browser searches for Helvetica Neue on the user's system and uses this if it finds it. If Helvetica Neue isn't found, the browser searches for Arial on the user's system and uses it if it finds it. If Arial isn't found, we'll use Verdana.

As a last resort, if none of the fonts in the font stack are found we fall back to sans-serif, which basically instructs the browser to use whatever the system's default sans-serif font is. You don't know exactly what will be used in this eventuality, but at least this is better than ending up with the browser default, Times New Roman, which is [a serif font](https://www.fonts.com/content/learning/fontology/level-1/type-anatomy/serif-vs-sans-for-text-in-print)!

> **NOTE**: that fonts with more than one word in their name need surrounding in quotes.

## font-size

`font-size` values can be expressed in different units including `pt`, `px`, and `em`. `pt` and `px` (point and pixel) are considered static sizing and will not adjust properly when resizing your page. `em` (responsive measure) however will resize based on the font size of the parent. If the parent is using `font-size` of `10px`, and the child is set to `.8em`, you are requesting it to be 80% of the size of the parent or `8px`.

``` css
h3 {
  font-size: 10pt;
}
p {
  font-size: 14px;
}
a {
  font-size: 1.2em;
}
```

## The `span` tag

If you wanted to highlight specific text within a paragraph or division, `<span>` can be used.  Unlike `<div>` which puts the next `<div>` on a separate line by default, `<span>` leaves the element on the same line.  

For example, `<h1>Hello <div>World</div> </h1>` would by default would put **World** on a new line.  

However if you wanted **World** to show up in the same line, you could instead use `<h1>Hello <span>World</span> </h1>`. Then in the css, you could have done something like this to just highlight the word **World**:

``` css
h1 span {
   font-weight: bold;
   color: blue;
}
```

## What you learned

This lesson taught us how to use fonts within our HTML and to change colors and create links. Many times I would rather style my elements rather than using the built-in styling that comes along with using elements like `<h1>`. The next section will show us how to inspect specific HTML elements and see CSS properties.

NEXT: [Using the Inspect Tool](./inspect_element.md)
