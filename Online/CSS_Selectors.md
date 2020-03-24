# CSS Selectors
CSS (Cascading Style Sheets) apply style, formatting, and layout to a page. Items to style are identified by a selector. 

## Common Selectors
The three common selectors are:
- Element
- Class name
- ID

You can find a [CodePen example on common selectors here](https://codepen.io/GeekTrainer/pen/OJVwXgL?editors=1100).

## Scoring
But what happens when multiple selectors try to apply to one element?

`Tag Name < Class Name < ID Else last write`

You can find a [CodePen example on scoring here](https://codepen.io/sguthals/pen/xxGyzab?editors=1100)

## Combinators
You can make style changes to elements based on the hierarchy of the HTML too, with combinators. This includes:  
`parent child` - All children  
`parent > child`- Only a direct child  
`sibling1 ~ sibling2` - Any sibling   
`sibling1 + sibling2`- Only an adjascent sibling  

You can find a [CodePen example on combinators here](https://codepen.io/GeekTrainer/pen/eYNjdZj?editors=1100)

## Psuedo Classes
Style is applied to elements based on the state or location of the element. The style for this is:  
`element:psuedo-class`  

And some examples include:  
`a:visited` - style applied to links that have been visited by this person before  
`a:hover` - style applied to links that are hovered over  

You can find a [CodePen example on psuedo-classes here](https://codepen.io/GeekTrainer/pen/abOjmVr?editors=1100)

## Psuedo Elements
Style is applied to elements based on their content. The style for this is:  
`element::psuedo-element`  

And some examples include:  
`p::first-letter` - style applied to the first letter of any paragraph  
`p::selection` - style applied to text that is selected by the user  

You can find a [CodePen example on psuedo-elements here](https://codepen.io/GeekTrainer/pen/oNXMzJb?editors=1100)

## Attribute Filters
Style is applied to elements based on the values. This style for this is:  
`element[attribute=value]`

And some examples inlude:  
`a[href$="pdf"]` - any link that ends in ".pdf"  
`a[href^="https"]` - any link that starts with "https"  

You can find a [CodePen example on attribute filters here](https://codepen.io/GeekTrainer/pen/KKpBNYw?editors=1100)

# Resources
[CSS Wikipedia Page](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)  
[CSS Combinators W3 Schools Page](https://www.w3schools.com/css/css_combinators.asp)  
[CSS Psuedo-Classes W3 Schools Page](https://www.w3schools.com/css/css_combinators.asp)  
[CSS Psuedo-Elements W3 Schools Page](https://www.w3schools.com/css/css_pseudo_elements.asp)  

## CodePen examples
[Common Selectors](https://codepen.io/GeekTrainer/pen/OJVwXgL?editors=1100)   
[Scoring](https://codepen.io/sguthals/pen/xxGyzab?editors=1100)  
[Combinators](https://codepen.io/GeekTrainer/pen/eYNjdZj?editors=1100)  
[Psuedo-Classes](https://codepen.io/GeekTrainer/pen/abOjmVr?editors=1100)  
[Psuedo-Elements](https://codepen.io/GeekTrainer/pen/oNXMzJb?editors=1100)  
[Attribute Filters](https://codepen.io/GeekTrainer/pen/KKpBNYw?editors=1100)  
