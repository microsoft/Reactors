# Activity: Debugging jQuery

Learning how to write correct code is important, obviously. However, learning how to spot errors and debug code is an invaluable skill as well. 

## Instructions
For this assignment, you will [clone this GitHub repo](https://github.com/Codingdojo-Trey/Debugging-jQuery/tree/error_version) and find the coding errors.

* This is a mock landing page for a pizza business. 
* There are five mistakes in the jQuery/JavaScript code for you to find. The errors are mostly syntax errors, but there is one key piece of coding missing that specifically relates to jQuery. Find the coding error first. 
* Check the code line by line. A few errors may be hard to spot, but that is on purpose.
* When you have corrected all the code errors, test the page to verify the code is working the way it should.

**Note:** The correct version of the code is contained in another branch of this repository. Don't clone it or look at it unless you are really struggling. 

The command syntax to clone a specific branch from GitHub is:
`git clone -b *branch name* *url to repository*`

So, for this activity, the command you will run to clone the error_version of this repository will be:
`git clone -b error_version https://github.com/Codingdojo-Trey/Debugging-jQuery.git`

## Results
Once you have located and corrected all five errors, the website should perform as follows:

(To see the finished result, go to [CodePen](https://codepen.io/dannyooooo/pen/jOEpaxR).)

* When the "Tell us!" survey button is clicked, the page displays a message box with the text specified in the code.
* When either of the images is clicked, the image should slide up and disappear. When either of the small headers underneath each picture is clicked, the header slides down and the image reappears.
* When the text within the red div is hovered over, it turns white. This includes the bulleted list of items and the headers.
* When the link "Click here to order!" in the red div is clicked, the page displays a message box.

NEXT: [Getting Data from an API](./json_html.md)
