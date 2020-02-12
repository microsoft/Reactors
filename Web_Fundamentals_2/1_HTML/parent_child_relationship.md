# Parent, Child, Sibling Relationship

In this chapter, we will be covering 2 very important concepts: Indentation and the Parent, Child, Sibling Relationship.

Consider the following example:

> **Bacon Ipsum, Dolor Amet?**
Bacon ipsum dolor amet tail salami ball tip leberkas venison. Pig pork loin shoulder pork fatback corned beef chuck shank drumstick cow doner cupim capicola. Swine beef ground round, kielbasa meatball doner jowl rump chuck pastrami venison spare ribs turducken sirloin sausage. Sausage venison doner brisket, andouille pork pastrami strip steak drumstick tri-tip cupim.

Notice how the header is centered in the middle of the page. Also notice that the first word at the beginning of the paragraph is indented a few spaces over. As programmers, we also want our co-programmers to distinguish where our
 ```code block``` ends and the next begins.

 Applying this concept to coding, our "Bacon Ipsum" paragraph should be translated like this in HTML:

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

Remember, we don't indent our code by our website's
  _content,_ we indent them via the HTML tag's **parent, child, sibling relationship**. So how did we get the title centered? Good question! That'll require some CSS that we will be going over in part three of the workshop. For now, just understand that indentation is determined by the PCS relationship, _not_by how we want the HTML to be visually rendered on the browser.

## HTML PCS Relationship

The PCS relationship is just a term to describe the relationship between tags/elements inside an HTML document.

To know the relationship between tags, we must first determine the parents, children, and siblings within our HTML document.

Example:

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

```html
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

## Is it really required to indent HTML code

It's not required, but it is _highly recommended_, and here are the reasons why:

* Beautiful-looking code can make you happy, and one way to make them look beautiful is to properly indent them.
* Properly indented code leads to less time spent on troubleshooting. Imagine being stuck with a problem, and you curse the inventor of HTML (damn you, Tim Berners-Lee!) -- only to find out that you just missed a closing tag. You were not able to quickly see it because you did not properly indent!
* It's easy to browse through your own code. With a glance, you know right away which part is the header part, and which part is the footer.
* It's a good coding habit. Popular programming languages such as PHP, Java, or Ruby recommend proper code indentation. Python even enforces it.

### **How to Indent**

* Just tap the tab key. One tab is equal to four spaces. Some people like two spaces and you can change this option within the settings in your favorite text editor. We recommend you to be consistent and do your best to make your code readable and clear.

At this point, you may not appreciate the significance of HTML PCSrelationship -- and that's okay. Just know that as early as the HTML course, you will be dealing with them (through properly indenting your code), but will not be directly working on them (target, and manipulate related elements via CSS and or jQuery).

NEXT: [Activity: Indentation Practice](./indentation_practice.md)
