# Styling Elements

Below are some of the most common styling properties that will affect all elements. This is not a definitive list and you should try doing a search for other properties that can help you to add style to your documents.
```width | height:```
The width and height properties are used to determine the size of your elements. The values can be expressed in pixels (```px```) and percentage (```%```). When working with static content using px is suitable as you will be defining your page to not change. If you are working with responsive design, you will want to use ```%```.

Be careful when setting your height property as this will determine how much content the element can hold. If you leave it unset, your element will expand to fit the content it holds. If you set it and you have more content than can be displayed then you will need to either manually adjust the height each time you change the content or utilize the overflow property.

When you want your element to resize ie: images, you can size just one property (width or height) and the other will adjust appropriately to keep the relative dimensions of the image.

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

```overflow:```
This property determines what should happen when the content inside of a container is too much for the container size. You can set the container to hide the additional information that does not fit, show the information no matter what, or have a scroll bar added to the element so the content is contained but still viewable.

``` css
  div {
    overflow: scroll;
  }
```

```background:```
The background property can modify the background of an element all in one line. This is a shorter version than splitting each property on its own line of code. The color can be defined using hex, rgb or semantic code.

``` css
  p {
    background: #ffffff url("cherries.png") no-repeat fixed center;
  }
 ```

```background-color | background-image | background-position | background-size | background-repeat```:
These background properties adjust the background by property type. Like background, background-color can be defined using hex, rgb or semantic code.

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

```border:```
This property adjusts all border elements in one line. The first value is the border thickness. The second value is the border type. The third value is the border color. The color can be hex, rgb or semantic code.

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

```border-radius```
This property allows the corners of your border to be given a rounded appearance. The values can be set using ```px``` or ```%```.

``` css
  button {
    border-radius: 5px;
  }
```

NEXT: [Styling Text](./styling_text.md)
