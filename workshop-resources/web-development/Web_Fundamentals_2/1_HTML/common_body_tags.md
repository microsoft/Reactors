# Common HTML Body Tags

It's time to learn about the most common tags that you'll be using inside the body tag. You might recall from the overview that we talked about the common elements that you might place on a web page, including:

* Headings and paragraphs of text
* Images
* Links
* Lists
* Tables
* Forms

## Headings

A heading is a section title, which means that often (but not always!) each section on a page (```<div>```) will have a heading. There are 6 levels of headings that you can use (named ```<h1>``` through ```<h6>```), each indicating the importance of its section.

Let's look at this page for examples. At the top of the page, you see "Common Body Tags" in large and bold letters. This is an ```<h1>``` tag, written as:

```<h1>Common Body Tags</h1>```

H1 is the main heading for the page.

## Paragraphs

Any chunk of text is a paragraph and, therefore, needs to be encapsulated in paragraph ```<p>``` tags.

Here's an example of how to use ```<p>``` tags:

``` html
<p>
 velit lectus, ut congue ligula molestie nec. Fusce a facilisis risus. Nullam
 id magna semper, semper eros quis, varius velit. Duis sagittis porta enim ac
 mattis. Cum sociis natoque penatibus et magnis dis parturient montes, nascet
 ur ridiculus mus. Donec sodales lorem id orci blandit, ac tincidunt lorem po
 rta. Sed euismod a arcu sed mollis.
 </p>

<p>
 Maecenas imperdiet risus at nisl aliquet, eu ullamcorper enim imperdiet. Sed
 id metus consectetur, sollicitudin eros at, dapibus ipsum. Morbi cursus nibh
 sit amet porta fringilla. Nam egestas nisi dui, a varius lectus egestas non.
 Nulla facilisi. Donec sed mauris vitae sem volutpat auctor nec eu nisi. Maec
 enas quis diam consequat, semper felis ullamcorper, mollis nisi. Morbi turpi
 s nulla, pellentesque sit amet erat eu, pretium sagittis mi. Fusce rhoncus i
 mperdiet eros, ac porta ligula ullamcorper in. Suspendisse nulla urna, facil
 isis non nunc ut, faucibus condimentum leo.
 </p>
```

## Images

There are two ways to use images on a web page: as page elements (such as album art on your favorite music sharing site, or the photos in your LinkedIn feed) or as background images (this is covered in the [CSS](../2_CSS_CSS3) module).

To embed images as page elements, you use the ```<img>``` tag. This tag is unique because it does not require a closing tag like other tags. It's considered a "self-closing tag": ```<img src="[location of the image goes here]" alt="[This is a description of the image]">```.

The ```<img>``` tag has two required attributes: ```src``` and ```alt```.  The ```src``` attribute stands for "source". This is the link where the image resides. The alt attribute stands for "alternate". This will include text that describes the image. This text appears in place of the image if the image fails to load.

### About the `alt` attribute

There are a couple reasons to use the `alt` attribute in images on your web pages:
- It makes your website 508-compliant, a requirement by the US government to provide accessibility to disabled people. 
- Using `alt` attributes is considered a best practice for search engine optimization (SEO) so that search engines can know something about the images within the content.

`alt` attributes are read by screen readers (images are not), allowing the meaning and function of the image to be conveyed to those with visual or certain cognitive disabilities. They can also be read by search engines to identify the content of the image and display it in search results.

## Links
Links are clickable items that redirect us to another page. Usually, links are in text format, but you can also turn an image into a link.

The tag used for links is the `<a>` tag, which stands for "anchor". Similar to images, links must have an attribute that tells the browser where the link is pointing. For links, this is called the `href` attribute.

Possible values for the `href` attribute are:

* Absolute URL: Points to another website (```href="http://www.example.com/default.html"```)
* Relative URL: Points to a file within a website (`href="default.html"`)
* Anchor URL:  Points to an anchor inside a page (`href="#top"`)

Example:

``` html
<a href="https://www.microsoft.com">Link Text to Visit Microsoft.com</a>
<a href="https://www.microsoft.com">
    <img src="">
</a>
```

## Lists

How we think of lists in HTML is different from how we think of them in our day-to-day life.

What kinds of topics do we normally consider as lists?

* Shopping items
* Chapter/topic names
* Rosters

So what's a list for our HTML scripting purposes?

It is any collection of elements that are of the same type. The most common use for lists in HTML is for navigation links.

There are two types of HTML lists: ordered lists (lists that are numbered) and unordered lists. Ordered lists use the `<ol>` tag, and unordered lists use the `<ul>` tag. Both lists use the `<li>` tag to describe each list item.

``` html
<ul>
    <li>
        <a href="home.html">Home</a>
    </li>
    <li>
        <a href="about.html">About</a>
    </li>
    <li>
        <a href="contact_us.html">Contact Us</a>
    </li>
</ul>
```

## Tables

We often find ourselves using tables to display data. Don't be intimidated by the word "data"; it just means information.

Tables have many tags associated with them because they consist of many parts. They have:

A table head (```<thead>```), which contains rows (```<tr>```) and column names (```<th>```).
A table body (```<tbody>```), which contains rows (```<tr>```) filled with table data (```<td>```).

So the tags we need are:

```<table>, <thead>, <th>, <tbody>, <tr> and <td>```

Example:

``` html
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Phone number</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Sample Name</td>
            <td>an_email@gmail.com</td>
            <td>555-5555</td>
        </tr>
        <tr>
            <td>Another Name</td>
            <td>another_email@gmail.com</td>
            <td>444-4444</td>
        </tr>
    </tbody>
</table>
```

Copy and paste this into your code editor and see what happens!

NEXT: [Forms](./forms.md)
