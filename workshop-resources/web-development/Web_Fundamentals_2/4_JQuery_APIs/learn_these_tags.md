# Recommended Function Tags

There are more than one hundred jQuery functions in the library. That is a lot of jQuery! You can build anything you can imagine using these functions. Take time to learn the functions that are considered most important. Once you know them, you can become a jQuery expert. For the exercise in this section, make sure to design your page so that you make it **very apparent** which jQuery function you are using and what you expect it to do.

**IMPORTANT:** For jQuery, you will use jQuery's official documentation to learn these tags. The reason you do this, compared to creating a video for each of these methods, is because it is important to get familiar with reading technical documentation and jQuery's technical documentation is a good place to start. 

Here is the list of recommended functions for you to know well:

* **Effects**: Functions for animation effects.
  * .hide()
  * .show()
  * .toggle()
  * .slideUp()
  * .slideDown()
  * .slideToggle()
  * .fadeOut()
  * .fadeIn()
* **CSS**: Adding or removing a class for an HTML element/DOM.
  * .addClass()
  * .removeClass()
  * .css()
* **Manipulation**: Retrieving or setting value or text in an HTML element.
  * .after()
  * .append()
  * .prepend()
  * .attr()
  * .before()
  * .html()
  * .text()
  * .val()
* **Events**: Functions to handle an event.
  * .click()
  * .on()
  * .live() - deprecated (jQuery 1.7)
  * .hover()

For the **Manipulation** jQuery functions, there are few distinctions to make. The functions `.html()` and `.text()` are different in a key way: `.html()` can be used to insert new HTML markup--AKA, HTML tags. `.text()` is used to get or set the text value of an HTML element. For instance, you could use `.text()` to change the text of a paragraph, but if you want to put an ordered list inside of the paragraph, you need to use `.html()*` to insert the appropriate tags into the paragraph.

Similarly, `.append()` and `.html()` are very similar; they both alter the HTML content of a selected item. However, there is one key difference: the function `.append` will **add** markup to the element in question, whereas **`.html()`** will **overwrite** the markup with the content that is inside the parentheses. 
