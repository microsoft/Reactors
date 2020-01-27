# Forms
Forms are one of the most important HTML tags you will learn. They are responsible for all the data exchange between the user (front-end) and the server (back-end). So it's very important that you have a good understanding of how to build them.

A form's job is to take in user input and send it to the back-end to be processed. A form is declared by using the `<form>` tag, which will have attributes action and method that decide where the form information gets sent, and how it gets sent respectively. [Learn more about forms and attributes here.](https://www.w3schools.com/htmL/html_forms.asp)

Taking in the input is done by using input fields, usually designated by the `<input>` tag. Depending on the type of information required, the way in which we take in the information may be different. This is sometimes designated by a type attribute, and other times by a different tag. Each input will typically also have a label (`<label>`) that is the name of the field. To make sure that a specific label is linked/associated to a specific input element, we must add corresponding for attribute on the label with input's id attribute. Including a label tag around the input field is a convention that allows us to click on the label to focus on the input field.

A name attribute also will typically go hand in hand with your input tags. They are used mainly for sending form data that the user enters in your form. You need the name attribute to reference that field in your form in other parts of your HTML.

Let's look at what input types would be used in the following circumstances:

When the user needs to enter a short amount of text, such as an email address or name.
The appropriate input type here is text.
```
<label for="first_name">First Name:</label>
<input type="text" id="first_name" name="first_name">
<label for="last_name">Last Name:</label>
<input type="text" id="last_name" name="last_name">
<label for="email">Email:</label>
<input type="text" id="email" name="email">
```

A password field.
The appropriate input type here is password.
```
<label for="password">Password</label>
<input type="password" id="password" name="password">
```

When the user can choose only 1 option from a variety of options. A good example is a gender selector.
One appropriate input type here is radio buttons.

```
<label for="male">Male</label>
<input type="radio" id="male" name="gender" value="male">
<label for="female">Female</label>
<input type="radio" id="female" name="gender" value="female">
<label for="decline">Prefer not to say</label>
<input type="radio" id="decline" name="gender" value="decline">
Another option is a dropdown menu, which uses <select> and <option> tags.

<select name="gender">
    <option value="male">Male</option>
    <option value="female">Female</option>
    <option value="decline">Prefer not to say</option>
</select>
```

When the user can choose multiple things from a variety of options, such as choosing their favorite 3 colors from 5 options.
The appropriate input type here is checkboxes.

```
<label for="blue">Blue</label>
<input type="checkbox" id="blue" name="color" value="blue">
<label for="green">Green</label>
<input type="checkbox" id="green" name="color" value="green">
<label for="red">Red</label>
<input type="checkbox" id="red" name="color" value="red">
<label for="black">Black</label>
<input type="checkbox" id="black" name="color" value="black">
<label for="purple">Purple</label>
<input type="checkbox" id="purple" name="color" value="purple">
```

When the user might want to enter longer text. This can be used in forums for comments, or for user profile descriptions.
In this case we use the ```<textarea>``` tag.

```<textarea name="description"></textarea>```

When a form needs to submit more than just user input. 
Input type hidden is similar to text fields, except they do not show on the page and users can not enter anything into them. This is useful for the back-end authentication and passing data. 
```
<input type="hidden" name="id" value="7">
```

Finally, to create a submit button:
The appropriate input type is submit.

```
<input type="submit" value="Submit">
```

Let's look at a sample full registration form:
```
<form action="process.php" method="post">
    <p>Please Register</p>
    <label for="first_name">First Name:</label>
    <input type="text" id="first_name" name="first_name">
   
    <label for="last_name">Last Name:</label>
    <input type="text" id="last_name" name="last_name">
   
    <label for="email">Email:</label>
    <input type="text" id="email" name="email">
   
    <p>Select your gender:</p>
    <label for="male">Male</label>
    <input type="radio" id="male" name="gender" value="male">
   
    <label for="female">Female</label>
    <input type="radio" id="female" name="gender" value="female">
    
    <label for="decline">Prefer not to say</label>
    <input type="radio" id="decline" name="gender" value="decline">
   
    <p>Select 3 of your favorite colors:</p>
    <label for="blue">Blue</label>
    <input type="checkbox" id="blue" name="color" value="blue">
    
    <label for="green">Green</label>
    <input type="checkbox" id="green" name="color" value="green">
   
    <label for="red">Red</label>
    <input type="checkbox" id="red" name="color" value="red">
    
    <label for="black">Black</label>
    <input type="checkbox" id="black" name="color" value="black">
   
    <label for="purple">Purple</label>
    <input type="checkbox" id="purple" name="color" value="Purple">
    
    <p>Say a few words about yourself:</p>
    <textarea name="description"></textarea>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password">
   <label for="pw_confirm">Password Confirmation:</label>
   <input type="password" id="pw_confirm" name="password_confirmation">
   
   <input type="submit" value="Click here to register">
</form>
```
Other label-input Declaration
Most CSS frameworks (especially on Twitter Bootstrap), use the label-input pairing shown above, but you may encounter a different format on how the label-input set is being declared. Below is an example:
```
<form>    
    <p>Please Register</p>
    <label>
        Name:<input type="text" name="name">
    </label>
    <p>Select your gender:</p>
    <label>
       Male<input type="radio" name="gender" value="male"> 
    </label>
    <label>
       Female<input type="radio" name="gender" value="female">
    </label>
    <label>
       Prefer not to say<input type="radio" name="gender" value="decline">
    </label>
    <p>For security, enter your password.</p>
    <label>
        Password:<input type="password" name="password">
    </label>
    <input type="submit" value="Click here to register">
</form>
```
Notice that the input element is now nested inside the label element and we no longer need to link the two using the label's for attribute and the input's id attribute.

#### NEXT: [Activity: Registration Page](./registration_assignment.md)


