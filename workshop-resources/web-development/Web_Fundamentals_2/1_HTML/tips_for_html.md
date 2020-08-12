# Important Tips To Avoid Headaches

HTML is a language that allows poor code to execute and render to varying levels of accuracy. Successful rendering, however, does not mean that your code is correct or that it guarantees it will validate as compliant with standards. Poor code is unpredictable, and you can't be certain what you're going to get when it renders. You must pay close attention when writing HTML and be sure to nest/indent, close all elements correctly, and validate your code.

## Use proper document structure

Pages will render without the use of the ```<!DOCTYPE html>``` doctype or ```<html>, <head>, and <body>``` elements. However, without the doctype and structural elements, pages will not render properly in every browser.

Example of bad code:

``` html
<html>
    <h1> Hello World! </h1>
    <p> This is my first website </p>
</html>
```

Example of good code:

``` html
<!DOCTYPE html>
<html>
    <head>
        <title> My First Website </title>
    </head>
    <body>
        <h1> Hello World! </h1>
        <p> This is my first website </p>
    </body>
</html>
```

### Constantly validate your code

While writing HTML, make it a habit to validate frequently; this will save you from issues that are harder to pinpoint (or redo) once your work is completed and lengthy.

HTML validation services, such as the free [W3C Markup Validation Service](https://validator.w3.org/) are useful debuggers that help you identify rendering errors.

### Organize HTML syntax

As your HTML gets bigger, managing it can become quite a task. One quick rule that can help you keep your syntax clean and organized is to use lowercase letters within element names, attributes, and values.

### Indent nested elements

Use double quotes, not single or no quotes, to store values for HTML attributes. A good example:

``` html
<h1 id="page_title">My First Website!</h1>
<p class="sub_title">This is <span class="emphasize">Cool!</span></p>
```

### Avoid using too many divs

When writing HTML, it is easy to get carried away adding ```<div>``` elements here and there to develop necessary styles. While this works, it can add bloat to a page, and before too long you're not sure what each ```<div>``` element does.

Example of bad code:

``` html
<div class="container">
    <div class="article">
        <div class="headline"> HTML Rocks! </div>
    </div>
</div>
```

Example of good code:

``` html
<div class="container">
    <article>
        <h1>HTML Rocks!</h1>
    </article>
</div>
```

### Make use of semantic elements

Deciding which elements to use to describe content types may be difficult, but these elements are the backbone of semantics.

> Note: Semantic HTML is the use of HTML markup to reinforce the semantics, or meaning, of the information in web pages rather than merely to define its look.
(Source: ["Semantic HTML" on Wikipedia](en.wikipedia.org/wiki/Semantic_HTML))

In this example, the HTML doesn't use the proper heading and paragraph elements; instead, it uses meaningless elements to group content.

Example of bad code:

``` html
<span class="heading"><strong>Welcome Back</span></strong>
```

It has been a while. What have you been up to lately?

Example of good code:

``` html
<h1>Welcome Back</h1>
<p> It has been a while. What have you been up to lately?</p>
```

### Keep your tag names lowercase

Technically, you can get away with capitalizing your tag names.

``` html
<DIV>
    <P> I'm out of random stuff! </P>
</DIV>
```

Having said that, the best practice is to keep all tags lowercase.

### Use alt attribute with images

Using meaningful alt attributes with `<img>` elements is a must for writing valid and semantic code. The alt information is helpful for a user who cannot view your image--whether due to a connection issue, a missing image, or if the user is using a screen reader.

Example of bad code:

``` html
<img id="logo" src="images/logo.png" alt="logo.png">
```

Example of good code:

``` html
<img id="logo" src="images/logo.png" alt="My First Website's logo">
```

NEXT: [Part 2. CSS: Selectors, Styling, and Display](Part%202.%20CSS%20%26%20CSS3)
