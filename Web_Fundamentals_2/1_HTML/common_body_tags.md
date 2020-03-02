# Common HTML tags used in the body of webpages

It's time to learn about the most common tags that you'll be using inside the body tag. Recall that when we were doing the overview, we talked about the common elements that you might want to place on a webpage, which are:

* Headings and paragraphs of text
* Images
* Links
* Lists
* Tables
* Forms

## Headings

A heading is a section title, which means that often (but not always!) each section (```<div>```) will have a heading. There are 6 levels of headings that you can use (named ```<h1>``` through ```<h6>```) each indicating the importance of its section.

Let's look at this page for examples. At the top of the page, you see "Common Body Tags" in large and bold letters. This is an ```<h1>``` tag, written as...

```<h1>Common Body Tags</h1>```

...and is the main heading for the whole page.

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


## Images

There are two ways that we use images on a web page: as page elements (such as album art on your favorite music sharing site, or the photos in your LinkedIn feed), or as background images (this is covered in CSS section).

For embedding images as page elements you use the ```<img>``` tag. This tag is special and does not require a closing tag like other tags. It's considered a "self-closing tag". ```<img src="[location of the image goes here]" alt="[This is a description of the image]">```

It has two required attributes: ```src``` and ```alt```.  The ```src``` attribute stands for source. This is the link to where the image is residing. The alt attribute stands for alternate. This is a few words of text to describe the image, in case it fails to load. This text will show up where the image should be in case the image fails to load.

## Special Note About the `alt` tag

There are several reasons for using the `alt` tag (attribute) when using images in your webpages. Using the tag with your images is required to make your website 508 compliant, the US government's laws about providing accessibility to disabled people. It's also important to mention that using `alt` tags is considered best practices for SEO so that search engines can know something about the images in our content.

`alt` tags are read by screen readers in place of images allowing the content and function of the image to be accessible to those with visual or certain cognitive disabilities.

The text stored in the tag is displayed in place of the image in browsers if the image file is not loaded or when the user has chosen not to view images.

`alt' tags provide a semantic meaning and description to images which can be read by search engines or be used to later determine the content of the image from page context alone.

## Links
Links are things that we click on that redirect us to another page. Usually, links are in text format, but you can also use an image as a link.

The tag used for links is the `<a>` tag, which stands for the anchor tag. Similar to images, links also need to have an attribute that tells the browser where the link is pointing. For links, this is called the href attribute.

Possible values for the href attribute are:

An absolute URL - points to another website (like ```href="http://www.example.com/default.html"```)

* A relative URL - points to a file within a website (like `href="default.html"`)
* An anchor URL - points to an anchor inside a page (like `href="#top"`)

Example:

``` html
<a href="https://www.microsoft.com">Link Text to Visit Microsoft.com</a>
<a href="https://www.microsoft.com">
    <img src="">
</a>
```

## Lists

How we think of lists in HTML is a little different from how we think of them in our day to day life.

What kind of stuff do we normally consider as lists?

* Shopping lists
* Chapter/topic names
* etc..

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

We will often find ourselves using tables to display data. Don't be intimidated by the word "data", it just means information.

Tables have many tags associated with them because they are made up of many different parts. They have:

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
