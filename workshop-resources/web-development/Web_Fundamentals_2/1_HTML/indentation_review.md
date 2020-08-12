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

By analyzing the HTML, you'll notice that there is an opening HTML tag on the second line that does not close until the end of the HTML document. This means that every element inside of those HTML tags should be indented once, as they are children elements of the HTML tag. The same is true for the title tag, which is nested in the head element. Likewise, the H1 tag and the p tag are children elements of the body tag and grandchildren of the HTML tag. Now let's look at the second example:

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

NEXT: After you've completed this activity, go to the next section called [Common HTML Body Tags](./common_body_tags.md).
