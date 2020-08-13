# Common HTML tags used in the body of webpages

It's time to learn about the most common tags that you'll be using inside the body tag. Recall that when we were doing the overview, we talked about the common elements that you might want to place on a webpage, which are:

- Headings and paragraphs of text
- Images
- Links
- Lists
- Tables
- Forms

## Headings

A heading is a section title, which means that often (but not always!) each section will have a heading. There are 6 levels of headings that you can use (named `<h1>` through `<h6>`), allowing you to indicate sections and subsections.

Let's look at this page for examples. At the top of the page, you see "Common Body Tags" in large and bold letters. This is an `<h1>` tag, written as `<h1>Common Body Tags</h1>` and is the main heading for the whole page.

## Paragraphs

Any chunk of text is a paragraph and, therefore, needs to be encapsulated in paragraph `<p>` tags. Here's an example of how to use `<p>` tags:

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

There are two ways that we use images on a web page: as page elements (such as album art on your favorite music sharing site, or the photos in your LinkedIn feed), or as background images (this is covered in CSS section).

For embedding images as page elements you use the `<img>` tag. This tag is special and does not require a closing tag like other tags. It's considered a "self-closing tag". `<img src="[location of the image goes here]" alt="[This is a description of the image]">`

It has two required attributes: `src` and `alt`.  The `src` attribute stands for source. This is the link to where the image is residing. The alt attribute stands for alternate. This is a few words of text to describe the image, in case it fails to load. This text will show up where the image should be in case the image fails to load.

### About the `alt` attribute

The `alt` attribute indicates to the browser what to display in the event the image is not available, or while it's loading on a slow connection. More importantly, though, it's the information which will be read by a [screen reader](https://en.wikipedia.org/wiki/Screen_reader), an assistive application used by those who are vision impared.

As a result, in order to ensure your page is accessible, it's imperitive to use `alt` attributes on **all images**. The University of Minnesota has a [fantastic set of resources for making your page accessible to all](https://accessibility.umn.edu/), including an article on [properly describing images](https://accessibility.umn.edu/core-skills/alt-text).

Besides just making your page accessible, `alt` text is used by search engines when indexing your pages. As a result, proper `alt` text is key to [search engine optimization (SEO)](https://en.wikipedia.org/wiki/Search_engine_optimization).

## Hyperlinks
Hyperlinks, or simply links are things that we click on that redirect us to another page. Usually, links are in text format, but you can also use an image as a link.

The tag used for links is the `<a>` tag, which stands for the anchor tag. Similar to images, links also need to have an attribute that tells the browser where the link is pointing. For links, this is called the href attribute.

Possible values for the href attribute are:

- An absolute URL to point to another website (like `href="http://www.example.com/default.html"`)
- A relative URL to point to a file within a website (like `href="default.html"`)

Example:

``` html
<a href="https://www.microsoft.com">Visit Microsoft.com</a>
<a href="https://www.microsoft.com">
    <img src="" alt="Descriptive text">
</a>
```

### Link text

#### Click here

The text between `<a>` and `</a>` which appears "clickable" to the user is known as link text. Proper link text is key to ensuring your page is accessible, and easier to navigate in general. Consider the following:

``` html
<a href="someurl">Click here!</a>
```

**Click here** is one of the most common, yet poor, link texts. The first problem with **Click here** is it doesn't indicate where link will take the user. In addition, the user might not be clicking on the link at all, and instead might be using a screen reader, where different keys would be tapped to navigate, or of course the smartphone user would also be tapping.

#### Find information here

A common "solution" to this problem is to create text like this:

``` html
Find information about alpacas <a href="someurl">here</a>!
```

While the text on the screen might be describing where the link is going, there's still a problem for screen readers. Screen readers allow the user to have all links read. As such, the user would simply hear "here" without context. When we also consider the fact the sentence is a bit unnatural, we can see it's not an effective solution.

#### Proper link text

[Creating good link text](https://accessibility.umn.edu/core-skills/hyperlinks) is one of the core skills every web developer, if not everyone who creates content of any variety - even emails - should have. The link text should clearly describe the document being referenced in a succinct manner.

``` html
<!-- good link text -->
<a href="https://en.wikipedia.org/wiki/Alpaca">Alpacas are a domesticated farm animal</a> commonly used for their fur.
```

Notice the text is rather short, yet clearly describes what the document will elaborate on and flows well in the sentence.

### Anchors

If you have a rather long page, such as an [frequently asked questions (FAQ) page](https://en.wikipedia.org/wiki/FAQ), you may want to allow users to quickly access a part of the page farther down on the screen, such as the answer to the question being posted. You can enable this by creating an **anchor**. (I bet you were wondering where **anchor** came from - now you know!) To create the target, you will use the `id` attribute on any tag you like. You will then create a link to the target by using `#` in front of the ID you've identified.

``` html
Q: <a href="#bite">Do alpacas bite?</a>

<p id="bite">
    <div>Do alpacas bite?</div>
    <div>Alpacas rarely bite humans.</div>
</p>
```

## Lists

How we think of lists in HTML is a little different from how we think of them in our day to day life.

What kind of stuff do we normally consider as lists?

- Shopping lists
- Chapter/topic names
- Rosters

When creating a page, we may display a collection of elements that are of the same type. The most common use for lists in HTML is for navigation links.

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

## What you've learned

We covered a lot of HTML in this section and learned how to create tables, make links, and embed images. These are just a couple of the many HTML tags that you need to know. Let's move on to another important feature of most web pages, the form. With web forms we can create surveys, contact forms, and comment boxes.

NEXT: [Forms](./forms.md)
