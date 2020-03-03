# Forms

Forms are one of the most important HTML tags you will learn. They are responsible for all the data exchange between the user (front-end) and the server (back-end). So it's very important that you have a good understanding of how to build them.

A form's job is to take in user input and send it to the back-end to be processed. A form is declared by using the `<form>` tag, which will have attributes action and method that decide where the form information gets sent, and how it gets sent respectively. W3Schools has a [great collection of information about forms](https://www.w3schools.com/htmL/html_forms.asp).

## Labels and inputs

Collecting information is done through the use of several types of controls, including radio buttons, textboxes, and dropdown lists. One of the keys to creating a form is adding `label`s. A `label` allows you to, well, label an item. This allows someone to tap on the label text itself to interact with the control (such as a textbox). It also provides better guidance to a screen reader. Use labels whenever you're creating a form.

``` html
<!-- Create a label for a textbox called name -->
<label for="name">Name</label>
<input type="text" id="name" />
```

## Textboxes

The most basic type of information we collect from users is text information. But not all text is created the same. Sometimes we want passwords, email addresses, or simply text. Fortunately, we have several options at our disposal to ensure we're getting the right information.

Almost all textboxes are indicated by using the `input` element with a different `type` attribute, where the value of `type` indicates the type of textbox we're creating.

Input controls are also typically decorated with `id` and `name` attributes. `id` indicates the id of the item used by the page for [anchors](../common_body_tabs.md#anchors), CSS and JavaScript. `name` indicates the name of the item for the server when the information in the form is processed.

### Text

The textbox is ubiquitous. As you would expect, it allows someone to type in some amount of text. A textbox applies no rules by default, it's simply text. You indicate you wish to accept text by using the `type="text"` attribute on an `input` tag.

``` html
<label for="first_name">First Name:</label>
<input type="text" id="first_name" name="first_name">
<label for="last_name">Last Name:</label>
<input type="text" id="last_name" name="last_name">
```

### Passwords

The password type allows you to request, as you might expect, a password.

> **NOTE**: The password field **does not** automatically encrypt the password. It will shield the value from being displayed, but will not protect it while being sent over the internet. To ensure security, you will need to make sure your page is accessed using [TLS/SSL](#securing-forms).

``` html
<label for="password">Password</label>
<input type="password" id="password" name="password">
```

### Other types

Because of the various types of text commonly used requested in forms, [HTML5](https://en.wikipedia.org/wiki/HTML5) includes [several options beyond simply "text"](https://www.w3schools.com/html/html_form_input_types.asp). One of the most common is `email`, which indicates you're requesting an email address.

When you use the `email` type, the browser will automatically validate the input to ensure it's an email address. in addition, on-screen keyboards will automatically update to include characters like **@** to make it easier for the user to enter the appropriate value.

``` html
<label for="email">Email:</label>
<input type="text" id="email" name="email">
```

## Lists of options

### Single selection

If you need the user to select one item from a list of options, you can present a set of radio buttons or a dropdown list. The difference between these two controls is how they are displayed to the user.

#### Radio buttons

Radio buttons show all of the options to the user, allowing them to select the item they wish to choose by "putting the dot" next to the item they want. Because all choices are displayed, radio buttons are best when there's a relatively limited number of options, typically fewer than five.

Radio buttons do not include text automatically; you will need to ensure text is displayed next to the radio button; this is typically done by using a `label` tag.

You create the group of items from which the user can select one item by ensuring each item in the group has the same name. In our example, all items share the name of **gender**.

``` html
<label for="male">Male</label>
<input type="radio" id="male" name="gender" value="male">
<label for="female">Female</label>
<input type="radio" id="female" name="gender" value="female">
<label for="decline">Prefer not to say</label>
<input type="radio" id="non-binary" name="gender" value="non-binary">
<label for="decline">Prefer not to say</label>
<input type="radio" id="decline" name="gender" value="decline">
```

#### Dropdown lists

Dropdown lists also allow a choice of one from a group of items. The difference is in the display; a dropdown list will only show the available list of options when the user opens the list, typically by clicking on it. In addition, the dropdown list automatically enables paging/scrolling as necessary. As such, it's perfect for a longer list of options, such as a list of US states.

``` html
<label for="home_state">Please select your home state</label>
<select name="home_state" id="home_state">
    <option value="AL">Alabama</option>
    <option value="AK">Alaska</option>
    <option value="AZ">Arizona</option>
    <option value="AR">Arkansas</option>
    <option value="CA">California</option>
    <option value="CO">Colorado</option>
    <option value="CT">Connecticut</option>
</select>
```

### Multiple selection

If you need to allow the user to select multiple items from the list of choices, you can use either checkboxes or multiple select lists.

#### Checkboxes

Checkboxes, similar to radio buttons display all the options to the user. As a result, they're also best if the list of options is relatively short. But, unlike radio buttons, checkboxes allow the user to choose multiple items.

``` html
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

#### Multiple select list

While a dropdown list offered paging and scrolling for longer lists, it only allows the selection of one item. If you wish to allow the user to select multiple items, you can add the `multiple` attribute to the `select` element we saw previously. By default, the first four items will be displayed, and scrolling enabled for the remainder of the items.

When using a multiple select, it's best to let the user know they can select multiple items by using the Control or Command key, as it's not always clear how to interact with the element.

``` html
<label for="home_state">Please select your home state</label>
<select name="home_state" id="home_state" multiple="multiple">
    <option value="AL">Alabama</option>
    <option value="AK">Alaska</option>
    <option value="AZ">Arizona</option>
    <option value="AR">Arkansas</option>
    <option value="CA">California</option>
    <option value="CO">Colorado</option>
    <option value="CT">Connecticut</option>
</select>
```

> **NOTE**: Why the `multiple="multiple"`? Some variations of HTML want attributes to be a key/value pair. As a result, you will see many HTML developers use syntax such as `multiple="multiple"`. It's worth noting the core HTML specification allows you to just add `multiple`.

## Buttons

When the user is ready to send the information for processing, they usually click on a button. There's two main ways to create a button to send the information to the server for processing, `<input type="submit">` or `<button type="submit">`. While the syntax is a little different between the two tags, there is no difference in what's being created. You may find you like the `button` tag since it's a little more intuitive.

The core difference in syntax is in how you indicate the text to be displayed to the user. If you're using an `input` tag, the text to be displayed is held inside the `value` attribute. If you're using a `button` tag, the text to be displayed is between the two tags.

``` html
<input type="submit" value="Submit">
<button type="submit">Submit</button>
```

## Securing forms

As highlighted when we were talking about passwords, information is sent across the internet in clear text. Not only does this mean the information can be read by others, it could also be modified. As such, there's a compelling argument to be made [all traffic should be encrypted](https://blog.codinghorror.com/lets-encrypt-everything/).

Encryption is handled seamlessly through the use of Transport Layer Security, or TLS. TLS is the successor to Secure Sockets Layer or SSL. You will frequently see web encryption indicated as TLS/SSL or just SSL, even though TSL is the standard and what is almost always being used.

When SSL is enabled for your forms, their URLs start with **https://** instead of **http://**. All forms should be encrypted with SSL, if not your entire site. If you are using [Azure to host your website](https://azure.microsoft.com/services/app-service/), you have the ability to use SSL for all shared domains (yourname.azurewebsites.net), or can upload a certificate for custom domains.

## What you've learned

There is a lot going on with forms. The best way to get good at creating forms is to create a lot of them. It's an important skill for a developer to be able to make forms and use the data somehow after a user has entered something. Making forms with validation rules can help insure that you have good data from your users. Let's solidify our new skill with an activity where we create a registration form.

NEXT: [Activity: Registration Page](./registration_assignment.md)
