# Web Fundamentals 2 Project

## Background

Contoso is an on demand job searching platform that provides a list of available jobs at the click of a button. The company's mission is to empower people by brining jobs to the users with a single touch. As a member of the development team, a designer has supplied a mock up to be implemented by you, the web developer.

## Key Concepts

- Web Development Process
- Identify page layouts by breaking down page into sections
- Integrating APIs
- Determining the steps necessary to complete the task

## Ethics

Here are some questions to think about:

- How should you filters and order the data that is returned from the API?
- How will Contoso manage the information that companies post on the platform?

---

## The Web Development Proccess

Web development is an iterative process that is repeated throughout the lifetime of a product. The process can be broken down into the following steps:

> Design -> Develop -> Deploy -> Iterate

1. Design - Generate a blueprint for the work to be done
2. Develop - Write necessary code to implement the design
3. Deploy - Push code to a server to be viewed by anyone
4. Iterate - Repeat as necessary

### Design

Depending on the size of the team, the developer can also play the role of the designer. In some larger teams there is a dedicated designer for the product.

- [ ] Gather requirements and assets (wireframes, images)
- [ ] Ask questions if something is unclear before writing code
- [ ] Create plan (implement top to bottom)
- [ ] Psuedo code in plain english and you walk through the necessary steps to build the product

### Develop

Create a good foundation by focusing on the structural html before apply any CSS. HTML is equivalent to the bones in our body in the sense that it helps hold everything together, without it we cannot hold form. CSS can then be applied on top of a solid HTML foundation to add the final touches. A common developer mistake is too try to fix layout issues with CSS first, which can lead more difficult to maintain code. Lastly improve the functionality by make the page dynamic through use of Javascript.

- [ ] Idenify layout and repeating patterns (to be used for clasification)
- [ ] Create the necessary files and folders (index.html, assets/css/main.css, assets/js/main.js)
- [ ] Code section by section focusing on the html structure first using common body tags as duscussed in [Part 1. HTML: Common Body Tags](../1_HTML/common_body_tags.md) and forms from [Part 1. HTML: Forms](../1_HTML/forms.md)
- [ ] Add style to get layout to match mockup using CSS Selectors as disccussed in [Part 2. CSS: CSS Selectors](../2_CSS_CSS3/css_selectors.md)
- [ ] If relevant, hardcode some data onto page before using Javascript to fetch data to continue to focus on html and css
- [ ] Create DOM event listeners for button clicks as discussed in [Part 3. Javascript: The DOM](../3_Javascript/the_dom.md)
- [ ] Fetch relevant data from an api as discussed in [Part 4. JQuery + APIs: API](../4_JQuery_APIs/api.md)
- [ ] Loop through data to add content to page

### Deploy

- [Checkout a live version of the site](https://reactor2.z22.web.core.windows.net/)
- Follow deployment instructions from [Part 5. Capstone Web Publishing](../5_Capstone_Web_Publishing/deploy.md)

### Iterate

Depending on the length of the project a developer might also get the task of maintaining the application over a period of time. During this maintenance one can expect to see the following kind of tasks:

- Add new features
- Add new pages
- A/B Testing different colors / user flows

---

## Key Takeaways

- Review requirements before coding
- Break pages into manageable sections
- Pseudo code to find weaknesses in the algorithm, it also helps plan out the steps

## Bonus

- [ ] Sort the job postings by title
- [ ] Add a form for the user to type in so they can filter the job postings

## Resources

- [Hero Image](https://pixabay.com/photos/residential-aerial-view-aerial-1149514/)
