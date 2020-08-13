# Styling Text

The following are some of the most common text style properties utilized. This is not a complete list and you are encouraged to search the internet for other useful text styling properties.

```color:```
The text color is specified using the color property. The value of the color property can be expressed using hex, RGB or semantic code.

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

```text-align:```
This property is used to set the horizontal alignment of any text. Text can be centered, or aligned to the left or right, or justified. This property will only work if the property is also display block.

``` css
  h1 {
    text-align: center;
  }
```

```text-decoration:```
The text-decoration property is used to add and remove underlines, overlines, and line-throughs.

``` css
  a {
    text-decoration: none;
  }
```

## Font

```font-family:```
The font-family property specifies the font style to use for an element. There are two types of font family names:

``` css
named-family - Examples "times", "courier", "arial"
generic-family - Examples "serif", "sans-serif", "cursive", "fantasy", "monospace"
```

## Web-safe fonts

There are fonts that are installed on pretty much all systems and so are termed web safe fonts because you can with some certainty know it will look the same regardless of the system the user has. Some of these are; ```Verdana, Arial, Trebuchet MS, Times New Roman, Georgia, Andale Mono, Courier New, Comic Sans, and Impact```.

``` css
  p {
    font-family: "helvetica neue", arial, verdana, sans-serif;
  }
```

Font-family allows for multiple options to be entered where the browser goes through them from left to right until it finds a font that is installed on the system which can be used. This means that you always want to make sure you have a generic-family option as your last value so that if none of the others can be found, the browser will use the system default for the family specified.

The browser searches for Helvetica Neue on the user's system and uses this if it finds it. If Helvetica Neue isn't found, the browser searches for Arial on the user's system and uses it if it finds it. If Arial isn't found, we'll use Verdana.

As a last resort, if none of the fonts in the font stack are found we fall back to sans-serif, which basically instructs the browser to use whatever the system's default sans-serif font is. You don't know exactly what will be used in this eventuality, but at least this is better than ending up with the browser default, Times New Roman, which is a serif font!

[Read more about the difference between sans and sans serif fonts.](https://www.fonts.com/content/learning/fontology/level-1/type-anatomy/serif-vs-sans-for-text-in-print)

Note that fonts with more than one word in their name need surrounding in quotes.

```font-size:```
The font-size property values can be expressed in four different units pt, px, em, %. pt and px (point and pixel) are considered static sizing and will not adjust properly when resizing your page. em and % (responsive measure and percent) however will resize and are what most developers recommend using. Below is a drop-down chart showing the approximate equivalents between the four units.

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
  span {
    font-size: 80%;
  }
```

```font-style```
This property controls the slanted emphasis of the text. Some text may have an italic property built into the font and so selecting italic would be fine. For fonts that do not have an italic style, the value oblique can be used to mimic italicized text.

``` css
  span {
    font-style: italic;
  }
```

```font-weight```
This property defines the thickness of a character line. normal is often the default value. The values can be set numerically or semantically.

``` css
  p {
    font-weight: bold;
  }
  span {
    font-weight: 600;
  }
```

## The ```span``` tag

If you wanted to highlight specific text within a paragraph or division, ```<span>``` can be used.  Unlike ```<div>``` which puts the next ```<div>``` on a separate line, ```<span>``` by default puts the element on the same line.  

For example, consider:
```<h1>Hello <div>World</div> </h1>```
Above by default would put 'World' on a new line.  

However if you wanted World to show up in the same line, you could instead do:
```<h1>Hello <span>World</span> </h1>```
Then in the css, you could have done something like this to just highlight the word 'World':

``` css
h1 span {
   font-weight: bold;
   color: blue;
}
```

To learn more about the difference between ```<div>``` and ```<span>```, you can also read: <https://www.codecademy.com/en/forum_questions/502ad0ea558dfe0002026d69>

NEXT: [Using the Inspect Tool](./inspect_element.md)
