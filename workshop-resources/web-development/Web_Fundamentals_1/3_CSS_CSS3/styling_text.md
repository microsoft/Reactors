# Styling Text

As with the size and border elements, we have control over the text. Let's walk through a few popular properties.

## Color

`color` is used to set the color. The value of the color property can be expressed using hex, RGB, or semantic code:

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

## Text-align

`text-align` is used to set the horizontal alignment of any text. Text can be `centered`, aligned to the `left` or `right`, or `justified`. This property will only work if the property is also `display: block`:

``` css
h1 {
  text-align: center;
}
```

## Text-decoration

`text-decoration` is used to add and remove `underline`s, `overline`s, and `line-through`s:

``` css
a {
  text-decoration: none; /* removes the underline */
}
```

> **NOTE**: Use caution when adding or removing underlines. Adding underlines to text that isn't a link can be confusing to users viewing your page. Removing underlines from a link can make your page less accessible, as it becomes tougher to see where the links are.

## Font-style

`font-size` controls the slanted emphasis of the text. Text that has an italic property built into the font is fine for selecting italic. For fonts that do not have an italic style, the value oblique can be used to mimic italicized text.

``` css
span {
  font-style: italic;
}
```

> **NOTE**: Italic may not display cleanly on many browsers; use it with caution.

## Font-weight

`font-weight` defines the thickness of a character line. `normal` is often the default value. The values can be set numerically or semantically:

``` css
p {
  font-weight: bold;
}
```

## Font

Setting fonts is a relatively involved topic, as you must ensure the font you use is available. As a result, you'll either give the browser some guidance of what type (or family) of font to use or provide fallback options if the font you wish to use isn't available.

### Font-family

The `font-family` property specifies the font style for an element. There are two types of font families: named, where you're providing a specific class of font such as `courier` or `arial`, or generic, where you're providing high-level guidance on the type of font to use, such as `serif` or `sans-serif`:

``` css
p{
  font-family: serif; /* feet on the font */
}
div{
  font-family: courier; /* courier or similar */
}
```

### Web safe fonts

There are fonts that are installed on almost all systems and are termed "web safe" fonts. Using these fonts lets you know they will look the same regardless of the user's system. Some of these fonts are `Verdana`, `Arial`, `Trebuchet MS`, `Times New Roman`, `Georgia`, `Andale Mono`, `Courier New`, `Comic Sans`, and `Impact`:

``` css
p {
  font-family: "helvetica neue", arial, verdana, sans-serif;
}
```

Font-family allows for multiple options to be entered The browser detects them from left to right until it finds a font that it can use. This means that you should have a generic font-family option as your last value so if none of the others can be found, the browser will use the system default for the family specified.

The browser searches for Helvetica Neue on the user's system and uses this if available. If Helvetica Neue isn't found, the browser searches for Arial and uses it. If Arial isn't found, it will use Verdana.

If none of the fonts in the font stack are found, it will default to sans-serif, which basically instructs the browser to use the system's default sans-serif font. You don't know exactly what font will be used in this eventuality, but it is better than displaying the browser's default, Times New Roman, which is [a serif font](https://www.fonts.com/content/learning/fontology/level-1/type-anatomy/serif-vs-sans-for-text-in-print)!

> **NOTE**: Fonts with more than one word in their name need surrounding quotes.

## Font-size

`font-size` values can be expressed in the following units: `pt`, `px`, and `em`. `pt` and `px` (point and pixel) are considered static sizing and will not adjust when resizing your page. `em` (responsive measure) will resize based on the font size of the parent. If the parent is using `font-size` of `10px`, and the child is set to `.8em`, you are requesting it to be 80% of the size of the parent, or `8px`:

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

If you wanted to highlight specific text within a paragraph or division, `<span>` can be used.  Unlike `<div>`, which puts the next `<div>` on a separate line by default, `<span>` leaves the element on the same line.  

For example, `<h1>Hello <div>World</div> </h1>` would, by default, put **World** on a new line.  

However, if you wanted **World** to appear in the same line, you could use `<h1>Hello <span>World</span> </h1>`. Then, in the CSS, you could use this code to highlight the word **World**:

``` css
h1 span {
   font-weight: bold;
   color: blue;
}
```

## What you learned

This lesson taught you how to use fonts within HTML and how to change colors and create links. Many times, it is preferable to style elements rather than use the built-in styling that is included with elements like `<h1>`. The next section will teach you how to inspect specific HTML elements and see CSS properties.

NEXT: [Using the Inspect Tool](./inspect_element.md)
