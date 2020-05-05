# Styling elements

Now that we know how to select items, let's explore what we can do with them. As you might expect, the list of options are almost limitless. We're going to walk you through a few of the common ones.

## width and height

Probably the most basic property you can configure is the height and width of an item. Each item is a [box](box_model.md), and the `height` and `width` identify how large that box will be.

The values are commonly expressed in pixels (`px`) and percentage (`%`). When working with static content using px is suitable as you will be defining your page to not change. If you are working with responsive design, you may want to use `%`.

Be careful when setting your height property as this will determine how much content the element can hold. If you leave it unset, your element will expand to fit the content it holds. If you set it and you have more content than can be displayed then you will need to either manually adjust the height each time you change the content or utilize the [overflow](#overflow) property.

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

## overflow

`overflow` determines what should happen when the content inside of a container is too much for the container size. You can set the container to `hide` the additional information that does not fit, `show` the information no matter what, or have a `scroll` bar added to the element so the content is contained but still viewable.

``` css
div {
  overflow: scroll;
}
```

## background

`background` can modify the background of an element all in one line. This is a shorter version than splitting each property on its own line of code. The color can be defined using hex, rgb or semantic code.

``` css
p {
  background: #ffffff url("cherries.png") no-repeat fixed center;
}
 ```

### Breaking down background

You'll notice we specified multiple properties for `background` in one go. Some properties, like `background` have sub-properties which can be set. In the case of `background`, we could specify an image (`background-image`) or position (`background-position`). For `background`, the values are in this order:

`background-color | background-image | background-position | background-size | background-repeat`

The above CSS could be broken down into smaller components.

``` css
div {
  background-color: #ffffff;
  background-image: url("cherries.png");
  background-position: center;
  background-size: fixed;
  background-repeat: no-repeat;
}
```

> **Discussion point**: You will notice there are often multiple ways to accomplish the same thing in HTML, CSS and JavaScript. Oftentimes, the choosing one is little more than a personal preference. You may decide for something like `background`, where the order of application isn't overly clear, to break things down. However for [`border`](#border) you might decide to go with the "all-in-one" approach.

## border

`border` allows you to set the border of a box. The first value is the border thickness. The second value is the border type. The third value is the border color. The color can be hex, rgb or semantic code.

The border property can also be broken down into separate lines using border-width, border-style and border color. Additionally, you can select very specifically which border you want to style by using ```border-top, border-bottom, border-right, border-left```.

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

## border-radius

This property allows the corners of your border to be given a rounded appearance. The values can be set using `px` or `%`.

``` css
button {
  border-radius: 5px;
}
```

> **NOTE**: CSS is an ever-changing standard. In fact, even using the word standard here might be a little generous, as browser creators have a long history of adding their own capabilities. `border-radius` is an attribute which is relatively newly supported broadly. You may notice sometimes the setting you wish to use works in Chrome, but not in Edge, or vice versa.

## What you learned

We learned how to add style to elements in HTML. Remember that now we should be using only external CSS style sheets rather than trying to do inline styling. If we do too much inline styling, if we have to make changes later, it will become challenging because we will have to make changes at every place we’ve used inline styling. In the next section, we will focus on styling text.

NEXT: [Styling Text](./styling_text.md)
