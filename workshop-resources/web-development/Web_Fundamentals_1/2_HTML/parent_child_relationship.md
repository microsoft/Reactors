# Indentation and Parent, Child, Sibling Relationships

In this subsection, we will be covering two very important concepts: indentation and the parent, child, sibling relationships.

Consider the following example:

> **Bacon Ipsum, Dolor Amet?**
Bacon ipsum dolor amet tail salami ball tip leberkas venison. Pig pork loin shoulder pork fatback corned beef chuck shank drumstick cow doner cupim capicola. Swine beef ground round, kielbasa meatball doner jowl rump chuck pastrami venison spare ribs turducken sirloin sausage. Sausage venison doner brisket, andouille pork pastrami strip steak drumstick tri-tip cupim.

In the code example below, notice how the header is centered in the middle of the page. Also notice that the first word at the beginning of the paragraph is indented.

As programmers, we want our fellow programmers to distinguish where one `code block` ends and the next begins. Applying this concept to HTML, our "Bacon Ipsum" paragraph should be coded like this:

``` html
<!DOCTYPE html>
<html>
    <head>
        <title> Hello World! </title>
    </head>
    <body>
        <h1> Here is a heading tag </h1>
        <p> Now a paragraph tag </p>
    </body>
</html>
```

Wait. Isn't it supposed to be indented like below?

``` html
<!DOCTYPE html>
<html lang="en">
   <head>
        <meta charset="UTF-8">
        <title>Document</title>
   </head>
   <body>
                                   <h3>Bacon Ipsum, Dolor Amet?</h3>
                <p> Bacon ipsum dolor amet tail salami ball tip leberkas venison. Pig pork
        loin shoulder pork fatback corned beef chuck shank drumstick cow doner cupim capicola. Swine
        beef ground round, kielbasa meatball doner jowl rump chuck pastrami venison spare ribs turdu
        ken sirloin sausage. Sausage venison doner brisket, andouille pork pastrami strip steak drums
        tick tri-tip cupim.</p>
   </body>
</html>
```

Simple answer: **NO.**

![Pic of Frustrated Man](../images/what.jpeg)

Remember, we don't indent our code by our website's **content**, we indent it using the HTML tag's **parent, child, sibling relationships**. So how did we get the title centered? Good question! That will require some CSS that we will cover in part three of the workshop. For now, just understand that indentation is determined by the parent, child, sibling relationships, **not** by how we want the HTML to be visually-rendered in the browser.

## HTML and parent, child, sibling relationships

The parent, child, sibling relationships reference is a term to describe the relationship between tags and elements inside an HTML document.

To know the relationship between tags, we must first determine the parents, children, and siblings within our HTML document.

For example:

``` html
<!DOCTYPE html>
<html>
    <head>
        <title> Hello World! </title>
    </head>
    <body>
        <h1> Here is a heading tag </h1>
        <p> Now a paragraph tag </p>
    </body>
</html>
```

From the HTML above you can read:

``` html
* <html> is the root element
* <html> has no parents
* <html> is the parent of <head> and <body>
* <head> is the first child of <html>
* <body> is the last child of <html>
```

and:

``` html
* <head> has one child: <title>
* <title> has one content (text): "Hello World!"
* <body> has two children: <h1> and <p>
* <h1> has one content (text): "Here is a heading tag"
* <p> has one content (text): "Now a paragraph tag"
* <h1> and <p> are siblings
* <head> and <body> are siblings
```

### Is it required to indent HTML code?

It's not required, but it is highly recommended because:

- Beautiful-looking code can make you happy, and one way to make them look beautiful is to properly indent them.
- Properly indented code leads to less time spent troubleshooting. Imagine struggling to solve a coding problem, perhaps even cursing the inventor of HTML--only to find out that you missed a closing tag. You were not able to see it quickly because you did not properly indent!
- It's easy to browse your own code. With a glance, you know right away which part is the header and which is the footer.
- It's a good coding habit. Popular programming languages such as PHP, Java, or Ruby recommend proper code indentation. Python even enforces it.

### **How to indent**

Tap the Tab key. One tab is equal to four spaces. Some people use two spaces and you can change this option within your text editor's settings. We recommend that you are consistent and do your best to make your code readable and clear.

## What you learned

In the section, you learned about indentation and how different HTML elements are nested within each other. You learned that because of this, nesting has a parent-child relationship. Similarly, children of parent elements in HTML are called siblings. HTML is recursive, and siblings can also have children.  

NEXT: We will [practice how to indent our HTML code](./indentation_practice.md).
