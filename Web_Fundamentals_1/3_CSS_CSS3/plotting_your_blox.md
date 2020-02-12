# Plotting Your Blocks: Activity

Try to duplicate the image below by adjusting the CSS code provided. Use **margins** and **paddings** to adjust the spaces between divisions and use the **display** property to be able to put each block in its proper place. You may need additional CSS properties.

![Blocks Diagram](../images/position-blocks.png)

## Here's the HTML code

```html
<!DOCTYPE html>
<html lang="en">
   <head>
      <title>Position Practice</title>
      <link rel="stylesheet" type="text/css" href="style.css">
   </head>
   <body>
       <div id="wrapper">
         <div id="header"></div>
         <div id="navigation"></div>
         <div id="main_content">
            <div class="subcontents"></div>
            <div class="subcontents"></div>
            <div class="subcontents"></div>
            <div id="advertisement"></div>
         </div>
      </div><!-- end of wrapper -->
   </body>
</html>
```

## And CSS

```css
/*CSS reset settings here*/
*{
 margin: 0px;
 padding: 0px;
}
#wrapper{
 width: 950px;
 background-color: silver;
 margin: 0px auto;
}
#header{
 min-height: 150px;
 background-color: green;
}
#navigation{
 min-height: 300px;
 width: 200px;
 background-color: blue;
}
#main_content{
 min-height: 400px;
 width: 700px;
 background-color: red;
}
.subcontents{
 min-height: 200px;
 width: 210px;
 background-color: yellow;
}
#advertisement{
 min-height: 120px;
 width: 660px;
 background-color: purple;
}
```

While you do this activity, please use min-height as well as vertical align to give minimum height to the division and also to vertically align some of the inline-blocks. Also, please do NOT use float (use display:inline-block instead).

[Or, you can complete the activity online at Codepen](https://codepen.io/dannyooooo/pen/100311ce217467fbcf13862a5090012b)

## What you learned

This is one of the essential activities of the workshop. Being able to use margins, padding, and borders to layout your webpages is an important skill. If you don’t get this the first time, don’t be discouraged, keep working at it. You can keep using the pot in your box template to create the base for your other static HTML pages. We finished with the section and now will go on to Do our capstone project and deployed it on Azure.

 NEXT: [Part 4. Capstone + Deployment with Azure](../4_Capstone_Deployment)
