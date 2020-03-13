# Overview

HyperText Markup Language (HTML) is the main markup language for all web pages. HTML elements are the basic building-blocks of the internet.

## Objectives

- Understand the theoretical components of the web and how they interact
- Understand the client-server model
- Understand the most important parts of what is displayed on the browser
- Understand the roles of HTML vs. CSS vs. Javascript
- Understand how to incrementally break down building a web page into its fundamental components

### What is HTML

HTML is the language of the Web. Its purpose is to let us communicate with the browser the meaning of the content that we wish to place on a web page. To achieve this, HTML defines a number of **tags** or **elements** that we can wrap the contents with.

- Headings and paragraphs of text
- Images
- Links
- Lists
- Tables
- Forms

HTML tags describe the content they contain. For example, there are paragraph tags for paragraphs, anchor tags for links, etc. The browser does not display the HTML tags but uses the tags to interpret the content of the page.

> **NOTE:** HTML uses **tags** or **elements** to describe the information for the browser to use for display. By definition, a tag is an inidivual marker (such as `<strong>`, which indicates important information), while an element includes the start and end tag (such as `<strong>Hello, world</strong>`). However, you will notice most web developers use the two terms interchangeably.

### Why HTML and CSS

The HTML and CSS (Cascading Stylesheets) chapters are designed to take you through the theoretical components of the web as well as the first step in creating a web application (building out the client-side). When building a web application we believe it is best to always start with a clickable prototype involving only HTML, CSS, and Javascript so it is only natural to teach these technologies first.

### Create a Simple HTML Document

- Create a new file in the Text Editor of your choice
- Type "Hello World!" into the file
- Save the file as **hello_world.html**
- Drag the file into your browser to open it

That's it! You should see the text "Hello World!" displayed in your browser.

Now, you may have noticed that we didn't add any tags to our text. To see how the browser handles this situation, right click in your browser and click **Inspect**. A new module should open at the bottom of your browser with various tabs.

We're currently interested in the **Elements** tab. When you click on it, you should see:

``` html
<html>
    <head></head>
    <body>Hello World!</body>
</html>
```

One of each of ```<html>, <head>, and <body>```above are required for each valid HTML document. If we don't provide valid HTML to a browser, it will automatically make a best effort to ensure the document is setup correctly.

## Terminology

### "Opening and closing tags"

Since tags are supposed to wrap things, **most tags come in pairs**: one opening and one closing tag, that denote the beginning and end of content. Tags without a leading forward slash are called opening tags while tags with leading forward slashes are called closing tags.

In the above example, `<body>` is an opening tag - it's equivalent to you telling the browser "Hey, I'm going to start putting in body content now". `</body>`is a closing tag that means "OK, I'm done with body content."

### Nesting

Notice that between the opening and closing HTML tags, we also have head and body tags. **Tags can encapsulate other tags**. This is called nesting. Nested items are **indented with a tab*- to make the document easier to read.

The hierarchy that rises from **nesting** is called **DOM**, which stands for Document Object Model.

**Commenting**
The format for commenting in an HTML file is as follows:

``` html
<p> Some paragraph content. </p>
<!-- This is a comment in HTML -->
```

> **NOTE**: The information in a comment is still readable by the user. Do not put any sensitive information in a comment.

## What you learned

In the section, we learned about how HTML and CSS interact with each other and how to create a simple HTML document we also learned that tags come in pairs and that nesting is a common practice when using HTML. The next section will look at the relationships between different elements within a webpage.

NEXT: [Parent, Child, Sibling Relationships in HTML](./parent_child_relationship.md)
