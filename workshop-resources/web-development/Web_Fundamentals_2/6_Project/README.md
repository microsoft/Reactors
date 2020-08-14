# Web Fundamentals 2 Project

## Background

Contoso is an on-demand job searching platform that provides a list of available jobs at the click of a button. The company's mission is to empower people by bringing jobs to users with a single touch. As a member of the development team, a designer has supplied a mockup for you, the web developer, to implement.

## Key concepts

- Understanding the web development process.
- Identifying page layouts by breaking page into sections.
- Integrating APIs.
- Determining the steps necessary to complete the task.

## Ethics

Here are some questions to think about:

- How should you filter and order the data that is returned from the API?
- How will Contoso manage the information that companies post on the platform?

---

## The web development proccess

Web development is an iterative process throughout the lifetime of a product. The process can be broken into the following steps:

> Design -> Develop -> Deploy -> Iterate

1. Design: Generate a blueprint for the work to be done.
2. Develop: Write necessary code to implement the design.
3. Deploy: Push code to a server to be viewed by anyone.
4. Iterate: Repeat, as necessary.

### Design

Depending on the size of the team, the developer can also play the role of the designer. In larger teams, there is often a dedicated designer for the product. In the design stage, developers should:

- [ ] Gather requirements and assets (ie, wireframes).
- [ ] If something is unclear, ask questions before writing code.
- [ ] Create a plan (implement it top-to-bottom).
- [ ] Write pseudo code in plain english and walk through the necessary steps to build the product.

### Develop

Create a good foundation by focusing on the structural HTML before applying CSS. HTML is equivalent to the bones in our body in the sense that it holds everything together; without it, we cannot hold the form of the website together. CSS can be applied on top of a solid HTML foundation, and then JavaScript can be added to make a page dynamic. A common developer mistake is to try to fix layout issues with CSS first, which can make it more difficult to maintain code. Some guidelines for the development stage:

- [ ] Identify layout and repeating patterns (to be used for classification).
- [ ] Create the necessary files (index.html, main.css).
- [ ] Code section by section, focusing on the HTML structure first, and using common body tags and forms as discussed in [Part 1. HTML: Common HTML Body Tags](../1_HTML/common_body_tags.md) and forms from [Part 1. HTML: Forms](../1_HTML/forms.md).
- [ ] Add style to match layouts to the mockups by using CSS Selectors, as discussed in [Part 2. Cascading Style Sheets (CSS)](../2_CSS_CSS3/css_selectors.md).
- [ ] If relevant, focus on HTML and CSS to hardcode the page before using JavaScript to fetch data.
- [ ] Create Document Object Model (DOM) event listeners for button clicks, as discussed in [Part 3. JavaScript: The Document Object Model (DOM)](../3_Javascript/the_dom.md).
- [ ] Fetch relevant data from an API, as discussed in [Part 4. jQuery and APIs: API](../4_JQuery_APIs/api.md)
- [ ] Loop through data to add content to page.

### Deploy

- [ ] [Check out a live version of the site](https://reactor1.z5.web.core.windows.net).
- [ ] Follow the deployment instructions from [Part 5. Capstone Project: Pubish/Deploy Your Files to Azure Storage](../5_Capstone_Web_Publishing/deploy.md).

### Iterate

Depending on the length of the project, a developer might also be responsible for maintaining the application over a period of time. During this maintenance, you can expect to tackle the following tasks:

- Add new features.
- Add new pages.
- A/B test different colors/user flows.

---

## Key takeaways

- Review requirements before coding.
- Break pages into manageable sections.
- Check pseudo code to find weaknesses in the algorithm and help you plan out steps.

## Value-added features

- [ ] Sort the job postings by title.
- [ ] Add a form so users can filter job postings for easily.

## Resources

- [Hero Image](https://pixabay.com/photos/residential-aerial-view-aerial-1149514/)
