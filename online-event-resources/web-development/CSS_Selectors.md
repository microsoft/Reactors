# CSS Selectors
Cascading Style Sheets (CSS) apply style, formatting, and layout to a page. Items to style are identified by a selector. 

## Common Selectors:
The three common selectors are:
- Element
- Class name
- ID

Here is a [CodePen example on common selectors](https://codepen.io/GeekTrainer/pen/OJVwXgL?editors=1100).

## Scoring:
But what happens when multiple selectors try to apply to one element?

`Tag Name < Class Name < ID Else last write`

Here is a [CodePen example on scoring](https://codepen.io/sguthals/pen/xxGyzab?editors=1100).

## Combinators:
You can make style changes to elements based on the hierarchy of the HTML with combinators. This includes:  
`parent child`: All children  
`parent > child`: Only a direct child  
`sibling1 ~ sibling2`: Any sibling   
`sibling1 + sibling2`: Only an adjacent sibling  

Here is a [CodePen example on combinators](https://codepen.io/GeekTrainer/pen/eYNjdZj?editors=1100).

## Pseudo classes:
Style is applied to elements based on the state or location of the element. The style for this is:  
`element:pseudo-class`  

And some examples include:  
`a:visited`: Style applied to links that have been visited by this person before.  
`a:hover`: Style applied to links that are hovered over.  

Here is a [CodePen example on pseudo-classes](https://codepen.io/GeekTrainer/pen/abOjmVr?editors=1100).

## Pseudo elements:
Style is applied to elements based on their content. The style for this is:  
`element::pseudo-element`  

And some examples include:  
`p::first-letter`: Style applied to the first letter of any paragraph.  
`p::selection`: Style applied to text that is selected by the user.  

Here is a [CodePen example on pseudo-elements](https://codepen.io/GeekTrainer/pen/oNXMzJb?editors=1100).

## Attribute filters:
Style is applied to elements based on the values. This style for this is:  
`element[attribute=value]`

And some examples inlude:  
`a[href$="pdf"]`: Any link that ends in ".pdf".  
`a[href^="https"]`: Any link that starts with "https".  

Here is a [CodePen example on attribute filters](https://codepen.io/GeekTrainer/pen/KKpBNYw?editors=1100).

# Resources:
[CSS Wikipedia Page](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)  
[CSS Combinators W3 Schools Page](https://www.w3schools.com/css/css_combinators.asp)  
[CSS Pseudo-Classes W3 Schools Page](https://www.w3schools.com/css/css_combinators.asp)  
[CSS Pseudo-Elements W3 Schools Page](https://www.w3schools.com/css/css_pseudo_elements.asp)  

## CodePen examples:
[Common Selectors](https://codepen.io/GeekTrainer/pen/OJVwXgL?editors=1100)   
[Scoring](https://codepen.io/sguthals/pen/xxGyzab?editors=1100)  
[Combinators](https://codepen.io/GeekTrainer/pen/eYNjdZj?editors=1100)  
[Pseudo-Classes](https://codepen.io/GeekTrainer/pen/abOjmVr?editors=1100)  
[Pseudo-Elements](https://codepen.io/GeekTrainer/pen/oNXMzJb?editors=1100)  
[Attribute Filters](https://codepen.io/GeekTrainer/pen/KKpBNYw?editors=1100)  
[From the Stream](https://codepen.io/sguthals/pen/MWwPXXL?editors=1100)
