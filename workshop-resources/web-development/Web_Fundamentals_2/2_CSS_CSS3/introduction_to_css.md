# What Is CSS?

Cascading Style Sheets (CSS) is a style sheet language that web developers use to define styles in a document (like a web page) that are written in a markup language like HTML. CSS is one of the foundational blocks of the web, along with JavaScript and HTML.

The term "cascading" refers to the priority scheme that determines which style rule applies if more than one rule matches a particular element. This cascading priority scheme is predictable.

A style sheet is used to define how content is presented, including layout, fonts, backgrounds, colors, and even transparency of a document. Essentially, it is a list of rules. Each rule (or "rule-set") consists of one or more selectors (the items to modify) and a declaration block (how the items should be modified).

## Getting started with CSS/CSS3
There are three ways of attaching CSS to a document:  inline, internal, and external. Inline and internal CSS are considered bad practices because they're not very reusable, and can cause inconsistent results. We will only use external style sheets, linked from the HTML document that is using the `<head>` tag.

> **NOTE**: CSS uses a priority scheme to determine which style rules apply if more than one rule matches a particular element. In this scheme, priorities (or "weights") cascade and are assigned to rules so that the results are predictable.

If you don't remember how to add a link to your ```<head>``` tag, refer back to the [HTML module](../1_HTML/README.md).


NEXT: [CSS Selectors](./css_selectors.md)
