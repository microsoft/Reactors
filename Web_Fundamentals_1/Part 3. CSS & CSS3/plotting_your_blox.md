# Plotting Your Blocks: Activity

Try to duplicate the image below by adjusting the CSS code provided. Use **_margins_** and **_paddings_** to adjust the spaces between divisions and use the **_display_** property to be able to put each block in its proper place. You may need additional CSS properties.

![](http://s3.amazonaws.com/General_V88/boomyeah/company_209/chapter_2135/handouts/chapter2135_3264_position-blocks.png)

##### Here's the HTML code:
```
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

##### And CSS:

```
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

##### [Or, you can complete the activity online: Click Here](https://codepen.io/dannyooooo/pen/100311ce217467fbcf13862a5090012b)


#### NEXT: [Part 4. Capstone + Deployment with Azure](https://github.com/daniel-dc-cd/web-fundamentals-1/tree/master/Part%204.%20%20Capstone%20%2B%20Deployment)
