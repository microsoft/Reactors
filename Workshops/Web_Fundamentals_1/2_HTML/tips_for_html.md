# Important Tips To Avoid Headaches

HTML is a language that allows poor code to execute and render to varying levels of accuracy. Successful rendering, however, does not mean that our code is correct or guarantee that it will validate as standards compliant. Poor code is unpredictable, and you can't be certain what you're going to get when it renders. We have to pay close attention when writing HTML and be sure to nest/indent and close all elements correctly and to always validate our code.

## Use Proper Document Structure

Pages will render without the use of the ```<!DOCTYPE html>``` doctype or ```<html>, <head>, and <body>``` elements. However, without the doctype and these structural elements, pages will not render properly in every browser.

Bad Code

``` html
<html>
    <h1> Hello World! </h1>
    <p> This is my first website </p>
</html>
```

Good Code

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

### Constantly Validate Your Code

While writing HTML, make a habit to validate frequently; this will save you from issues that are harder to pinpoint (or redo) once your work is completed and lengthier.

HTML validation services such as the free  W3C Markup Validation Service are useful debuggers that help you identify rendering errors.

### Organize HTML Syntax

As your HTML gets bigger, managing it can become quite a task. Below are quick rules that can help you keep your syntax clean and organized:

Use lowercase letters within element names, attributes, and values.

### Indent nested elements

Use double quotes, not single or completely omitted quotes to store in values for HTML attributes. Good example:

``` html
<h1 id="page_title">My First Website!</h1>
<p class="sub_title">This is <span class="emphasize">Cool!</span></p>
```

### Avoid Using Too Many divs

When writing HTML, it is easy to get carried away adding ```<div>``` elements here and there to build out necessary styles. While this works, it can add quite a bit of bloat to a page, and before too long we're not sure what each ```<div>``` element does.

Bad Code

``` html
<div class="container">
    <div class="article">
        <div class="headline"> HTML Rocks! </div>
    </div>
</div>
```

Good Code

``` html
<div class="container">
    <article>
        <h1>HTML Rocks!</h1>
    </article>
</div>
```

### Make Use of Semantic Elements

Deciding which elements to use to describe different content may be difficult, but these elements are the backbone of semantics.

> Note: Semantic HTML is the use of HTML markup to reinforce the semantics, or meaning, of the information in webpages rather than merely to define its presentation or look.
via:  en.wikipedia.org/wiki/Semantic_HTML

Here the HTML doesn't use the proper heading and paragraph elements; instead, it uses meaningless elements to group content.

Bad Code

``` html
<span class="heading"><strong>Welcome Back</span></strong>
```

It has been a while. What have you been up to lately?

Good Code

``` html
<h1>Welcome Back</h1>
<p> It has been a while. What have you been up to lately?</p>
```

### Keep Your Tag Names Lowercase

Technically, you can get away with capitalizing your tag names.

``` html
<DIV>
    <P> I'm out of random stuff! </P>
</DIV>
```

Having said that, the best practice is to keep all tags lowercase.

### Use alt Attribute With Images

Using meaningful alt attributes with `<img>` elements is a must for writing valid and semantic code. The alt information is helpful for when a user cannot view your image - whether due to a connection issue, a missing image, or because the user is utilizing a screen reader.

Bad Code

``` html
<img id="logo" src="images/logo.png" alt="logo.png">
```

Good Code

``` html
<img id="logo" src="images/logo.png" alt="My First Website's logo">
```

NEXT: [Part 3. CSS: Selectors, Styling, and Display](../Part%203.%20CSS%20%26%20CSS3)
