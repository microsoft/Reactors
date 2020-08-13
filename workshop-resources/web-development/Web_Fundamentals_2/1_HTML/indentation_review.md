# Indentation Review

This is such an important concept to understand for the rest of your development life that we will be reviewing the last activity together.

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

By analyzing our HTML, we notice that we have an opening HTML tag on our second line that does not close till the end of our HTML document. This means every single element inside of those HTML tags should be indented over once as they are all children elements of the HTML tag. The same is applied for the title tag which is nested in the head element. Likewise, for the h1 tag and the p tag, they are both children elements of the body tag and grandchildren of the HTML tag. Now let's cover the second example.

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

Review this code and apply the parent, sibling and child relationships to understand this content a little easier.

NEXT: [After you've completed this activity go on to the next section, "Common Body Tags"](./common_body_tags.md)
