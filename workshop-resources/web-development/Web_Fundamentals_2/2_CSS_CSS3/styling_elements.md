# Styling Elements

Below are some of the common styling properties that will affect all elements. This is not a definitive list and you should search for other properties that can help you add style to your documents.

## Width and height
The values are commonly expressed in pixels (`px`) and percentage (`%`). When working with static content, using `px` is suitable as you will be defining your page to not change. If you are working with responsive design, you may want to use `%`.

Be careful when setting your height property, as this will determine how much content the element can hold. If you leave it unset, your element will expand to fit the content it holds. If you define it and you have more content than can be displayed, then you will need to either manually adjust the height each time you change the content or utilize the [overflow](##overflow) property:

When you want your element to resize, you can size just one property--width or height--and the other will adjust appropriately to keep the relative dimensions of the image.

``` css
  a {
    width: 25px;
  }
  div {
    width: 100%;
    height: 200px;
  }
  img {
    width: 250px;
  }
```

## Overflow
`overflow` determines what should happen when the content is larger than the container that holds it. You can set the container to `hide` the additional information that does not fit, `show` the information regardless, or add a `scroll` bar so the content is contained but still viewable:

``` css
  div {
    overflow: scroll;
  }
```

## Background
`background` can modify the background of an element in one line. This is a shorter solution than splitting each property into its own line of code. The color can be defined using hex, rgb, or semantic code:

``` css
  p {
    background: #ffffff url("cherries.png") no-repeat fixed center;
  }
 ```

### Background sub-properties

You'll notice we specified multiple properties for `background`. Some properties, like `background`, have sub-properties which can be set. In the case of `background`, you could specify an image (`background-image`) or position (`background-position`). For `background`, the values are in this order:

```background-color | background-image | background-position | background-size | background-repeat```

These background properties adjust the background by property type. Like background, background-color can be defined using hex, rgb or semantic code:

``` css
  p {
    background-color: blue;
  }
  div {
    background-image: url("cherries.png");
    background-position: center;
    background-size: auto;
    background-repeat: no-repeat;
  }
```

## Border
`border` allows you to set the border of a box. The first value is the border thickness. The second value is the border type. The third value is the border color. The color can be hex, rgb, or semantic code.

The border property can also be broken down into separate lines using border-width, border-style, and border color. Additionally, you can be specific about which border you want to style by using ```border-top, border-bottom, border-right, border-left```.

``` css
  button {
    border: 2px dotted green;
  }
  div {
    border: 1px solid #000000;
  }
  p {
    border-right: 1px groove rgb(100,100,100);
    border-left: 1px groove rgb(200,200,200);
  }
```

## Border-radius
This property allows the corners of your border to have a rounded appearance. The values can be set using `px` or `%`:

``` css
  button {
    border-radius: 5px;
  }
```

NEXT: [Styling Text](./styling_text.md)
