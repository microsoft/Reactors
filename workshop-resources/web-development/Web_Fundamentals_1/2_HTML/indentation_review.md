# Indentation Review

We will review the last activity together because this is an important concept to understand for your development work.

``` html
<!DOCTYPE html>
<html>
  <head>
    <title>Basic I</title>
  </head>
  <body>
    <h1>What language do you love?</h1>
    <p>I love HTML!</p>
  </body>
</html>
```

By analyzing our HTML, we notice that we have an opening HTML tag on our second line that does not close until the end of our HTML document. This means every element inside of those HTML tags should be indented once, as they are children elements of the HTML tag. The same is true for the title tag, which is nested in the head element. Likewise, the h1 tag and the p tag are children elements of the body tag and grandchildren of the HTML tag. Now let's cover the second example.

``` html
<!DOCTYPE html>
<html>
    <head>
        <title>Basic II</title>
    </head>
    <body>
        <table>
            <thead>
                <tr>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Email</th>
                    <th>Password</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Brendan</td>
                    <td>Stanton</td>
                    <td>brendanrocks@gmail.com</td>
                    <td>FakePassword123</td>
                </tr>
            </tbody>
        </table>
        <h1>Here is a list of my favorite things:</h1>
        <ul>
            <li>Food</li>
            <li>Bandwidth</li>
            <li>Coffee</li>
            <li>Beach</li>
        </ul>
    </body>
</html>
```

Review this code and apply the parent, sibling, and child relationships to understand this content a little easier.

## What you learned
By reviewing the activity, you learned the importance of proper indentation and formatting in your HTML code. You learned that by doing so, you are also making the job easier for the next person who may work on a page after you. 


NEXT: After you've completed this activity, go to the next section called [Common HTML Tags Used in the Body of Web Pages](./common_body_tags.md).
