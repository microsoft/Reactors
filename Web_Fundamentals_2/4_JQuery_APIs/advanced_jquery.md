# Advanced jQuery

## Dynamic Content, Callbacks, and Traversing

If you want to learn how to use APIs and AJAX effectively, you must understand how dynamic content behaves with jQuery. What exactly is dynamic content anyway? Dynamic content is HTML code that you generate after the page loads. The tricky part with dynamic content is that it will not follow the same jQuery rules you set for your original content unless you tell it to. In this section, you will learn how to master this difficult art! In addition to this, you will learn about traversing through HTML elements, which is how we reference HTML elements relative to their containing, or neighboring elements.

## Introducing Dynamic Content

With the use of  .html() and .append(), you have the ability to add new HTML content for any page you make. This is called dynamic content. The rules for adding jQuery listeners onto your dynamic content are a little tricky because at first, your browser doesn't know that the content is even there.

## .on()

The most effective way to add event handlers to any dynamically rendered HTML content is to use the `.on()` method. The `.on()` method works a little differently than the jQuery commands you have practiced up to this point. So how does `.on()` work? We must attach the `.on()` function to something within a selector. However, what you pass into the selector is not what you want to attach the event to. What goes into the selector is the element that contains the relevant HTML element(s) you want to attach an event listener to. You can think of the element you select as the sphere of detection for the event you want to listen for.  

Here's an example:

`$(document).on('click', 'button', function(){alert('you clicked a button!')});`

So, the 'sphere of detection' of this instance of `.on()` is paired with the selector for the whole document. That means that the following parameters of the function will be applied to everything contained in the entire document. This is the widest scope that you can use on a jQuery function. If you want your scope to be smaller, you can select a different element in the selector.

The `.on()` function takes up to 4 parameters and we will show you how they mesh with our example above:

The event: Are you waiting for a click? A submit? Keydown? In this case, we are looking for a click.

Data you wish to pass to the handler (this is not required and seldom used). We're not using it here!

The target: i.e. the element you are trying to target. Here we are targeting a button. So now our search is narrowed down listening for a button to be clicked.

The function you want to run: Just the stuff you want to attach! In our case, we are just going to alert to the screen that we clicked a button-- every time a button is clicked.
Every time the event you specified in the first item (1) happens, the function searches the document for the target(s) you specified in the third item (3). If the action was triggered by the correct element, the code you put in the fourth item (along with any information you passed from the optional second item) will be executed.

The really neat thing about this .on() function is that every time the event happens in the corresponding target, the relevant parts of the document get scanned in real time. Thus, any new element added after page load will be detected and the code will run. Pretty great, huh? Using this method, the code we need to accomplish the same goal as the previous tab would be the following:

```javascript
 $(document).ready(function(){
     $('button').click(function(){
         $('div').append('<h3>I am a dynamically generated h3 </h3>');
      });
     $(document).on('click', 'h3', function(){
         alert('You clicked me!');
     });
 });
 ```

## Scope

Since we first must assign the scope of where our `.on()` function will look, this invites a question: why not just always use document? Using `$(document).on()` will assure us that no item can accidentally pass through detection. Well, think about it like this: if we tell you that one of your friends has a message for you, but you must figure out which friend has it -- that might take a while to figure out.  If, instead, we say: one of your friends who lives on a particular street in Mountain View has a message for you -- that would take a lot less time. Same concept with being more specific in your selector for the `.on()` method; the more searching of the document the `.on()` function has to do, the slower your code will run. Selecting $(document) for everything in an average website won't slow down your performance at all, but if you have tens of thousands of dynamic HTML elements that you are trying to add handlers to, using a more specific selector can make a huge difference between your website crashing or working. This will apply to anyone interested in game development, where thousands of operations per second are the norm.

Also, another great reason to judge the scope of your detection carefully is that you may not want all dynamic HTML elements to have the same functionality. Consider the following code:

```javascript
 <script>
  $(document).ready(function(){
   $('button').click(function(){
    $('div').append('<h3>I am a new content</h3>');
   });
   $(document).on('mouseover', 'h3', function(){
    $(this).css('color', 'pink');
   });
  });
 </script>
 <body>
  <button>Click me for new content!</button>
  <div class='a'>
   <h3>I am old content</h3>
  </div>
  <div class='b'>
   <h3>I am old content</h3>
  </div>
 </body>
```

## Note: for this function, 'mouseover' takes the place of 'hover'

If you run the code, you will notice that both divs will have dynamic content generated when the button is clicked. When any h3 on the page is hovered over, it will turn pink. Perhaps you want to change the functionality a little bit so that only the divs in the class 'a' div have this functionality. We can make this change quite easily using the selector correctly.

Observe:

```javascript
<script>
  $(document).ready(function(){
   $('button').click(function(){
    $('div').append('<h3>I am a new content</h3>');
   });
   $('div.a').on('mouseover', 'h3', function(){
    $(this).css('color', 'pink');
   });
  });
</script>
<body>
  <button>Click me</button>
  <div class="a">
   <h3>I am old content</h3>
  </div>
  <div class="b">
   <h3>I am old content</h3>
  </div>
</body>
```

Now you can see the usefulness of this technique!

## Callbacks

The recommended way to attach handlers to dynamic HTML content is by using callbacks. A callback is nothing more than a function that we tell some other function to run at some specific later time. In order to attach event handlers to dynamic HTML content, I need to run my jQuery code for the dynamic content after the content is created. In other words, I must wait until that dynamic content is created before I can attach any event listener to it. One way to do this is to attach the event handler in the same function that creates the dynamic content. This is a concept more easily demonstrated than described, so make sure to type along with the video.

## Defining a callback

Consider the following portion of a web page:

```html
<script>
    $(document).ready( function() {
        $('h3').click( function() { alert('You clicked an H3!'); });
    });
</script>
<body>
    <div>
        <h3>Click me to see a message!</h3>
    </div>
</body>
```

Naturally, this function just triggers an alert any time an h3 tag is clicked. So what happens if we dynamically generate some new HTML by adding some more jQuery and HTML? When first learning jQuery, the different nested `({ })` marks can be very confusing (and error-prone!), so for clarity, we will indent the following example code a bit differently. Once you are comfortable with jQuery callbacks, you can revert to a more compact style.

```html
<script>
    $(document).ready(
        function() {
            $('h3').click(
                function() {
                    alert('You clicked an H3!');
                }
            );
            $('button').click(
                function() {
                    $('div').append('<h3>I am a dynamically generated H3</h3>');
                }
            );
        }
    );
</script>
<body>
    <div>
        <button>Click me to add a new H3 tag!</button>
        <h3>Click me to see a message!</h3>
    </div>
</body>
```

If you try to run this code in your browser, you may be disappointed when you click on the dynamically generated h3, because it won't show any message.

The point to observe here is that the jQuery we have written is specifically applied to elements that already exist at the time of page load! Even further, try right-clicking and going to View Page Source. You shouldn't be able to see any of the `h3` tags you made by clicking the button. This is why dynamically rendered content must be dealt with separately than the statically rendered content -- because the browser doesn't really know that the dynamic content exists. So let's define our callback now:

```javascript
<script>
    $(document).ready( function() {
        $('h3').click( function() {
            alert('You clicked an H3!');
        });
        $('button').click( function() {
            $('div').append('<h3>I am a dynamically generated H3</h3>');
            $('h3').click( function() {
                alert('You clicked an H3!');   // **** here it is!
            });
        });
    });
</script>
<body>
    <div>
        <button>Click me to add a new H3 tag!</button>
        <h3>Click me to see a message!</h3>
    </div>
</body>
```

Notice that all we did was restate the original jQuery code for new content after that new content was created. That's all it takes! There is your first callback. Now even a dynamically generated h3 element should be sending you a message. Why does this work? This works because as soon as we created content, we gave the browser instructions to the code we just declared! This is exactly the same process that happens for the static (page load) content; the handlers get attached as soon as the page content is created!

One last thing: note this repeats the code, which is something developers dislike doing. Following the principle Don't Repeat Yourself (DRY), let's DRY out our code. Here is the convention we use to achieve this:

```html
<script>
    function attach_h3_handlers() {
        $('h3').click( function() { alert('You clicked an H3!'); });
    }
    $(document).ready( function() {
        attach_h3_handlers();
        $('button').click( function() {
            $('div').append('<h3>I am a dynamically generated H3</h3>');
            attach_h3_handlers();
        });
    });
</script>
<body>
    <div>
        <button>Click me to add a new H3 tag!</button>
        <h3>Click me to see a message!</h3>
    </div>
</body>
```

Notice all we did was just define a function that did exactly what the original code did. This allows us to just call the function instead of rewriting the code, which is a big time-saver! Another thing to note: we defined our function outside our `$(document).ready()` function but called it within the `$(document).ready()` function. Take a moment to think about why this worked.

Here's why: by calling the function within the `.ready()` tags, we told our browser to search all of our JavaScript for a function of that name and execute it. Pretty sweet, huh? That is part of the beauty of functions in JavaScript. When the browser/interpreter reads a statement that invokes a function, the entire document is scanned for a function of that name, meaning it could be defined on a latter segment of the page and the interpreter/browser will still be able to find it.
