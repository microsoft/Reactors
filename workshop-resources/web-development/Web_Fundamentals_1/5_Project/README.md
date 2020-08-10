# Web Fundamentals 1 Project

## Background

Contoso offers high resolution 3D printing services. The company prints custom designs in a variety of materials and finishes. To place an order, customers only need to upload a file, customize the order, and add shipping and payment information. As a member of the development team, a designer has supplied a mockup for you, the web developer, to implement.

## Key concepts

- Web development process
- Identify page layouts by breaking page into sections

## Accessiblity

The web was designed to be avilable for everyone regardless of their condition. Not everyone can access the web the same way. Depending on the situation, a user could have a permanent, temporary, or conditional disability. A user could be accessing the web through various devices, connection speeds, and locations that could affect their experience on the web. In some cases, accessibility for all is required by law. To provide equal access and opportunity to people with diverse abilities, it is important as developers to keep accessibility in mind when developing applications. It is up to you the developer to make the web an accessible place.

Some tips to get started on building a more accessible web:

- Use semantic HTML.
- Use alt tags to describe an image `<img src="" alt="Image description goes here">`.
- Add caption tags `<caption></caption>` to tables.
- Use keyboard navigation.
- Use Accessible Rich Internet Applications (ARIA) properties to define roles for objects.
- You can learn more tips at [Accessible U, University of Minnesota](https://accessibility.umn.edu/your-role/web-developers).

## Ethics

Here are some questions to think about:

- What kind of materials are being used in the product?
- Do these products need warning labels?
- What is the environmental impact of these products depending on the material being use?
- Are there file types that should be prohibited, such as weapons?

---

## The web development proccess

Web development is an iterative process throughout the lifetime of a product. The process can be broken into the following steps:

> Design -> Develop -> Deploy -> Iterate

1. Design: Generate a blueprint for the work to be done.
2. Develop: Write necessary code to implement the design.
3. Deploy: Push code to a server to be viewed by anyone.
4. Iterate: Repeat as necessary.

### Design

Depending on the size of the team, the developer can also play the role of the designer. In larger teams, there is often a dedicated designer for the product. In the design stage, developers should:

- [ ] Gather requirements and assets (ie, wireframes).
- [ ] If something is unclear, ask questions before writing code.
- [ ] Create a plan (implement it top-to-bottom).

### Develop

Create a good foundation by focusing on the structural HTML before applying CSS. HTML is equivalent to the bones in our body in the sense that it holds everything together; without it, we cannot hold the form of the website together. CSS can be applied on top of a solid HTML foundation to add the final touches. A common developer mistake is too try to fix layout issues with CSS first, which can make it more difficult to maintain code. Some guidelines for the development stage:

- [ ] Idenify layout and repeating patterns (to be used for clasification).
- [ ] Create the necessary files (index.html, main.css).
- [ ] Code section by section, focusing on the HTML structure first, and using common body tags and forms as discussed in [Part 2. HTML: Common Body Tags](../2_HTML/common_body_tags.md) and [Part 2. HTML: Forms](../2_HTML/forms.md).
- [ ] Add style to match layouts to the mockups by using CSS Selectors, as discussed in [Part 3. CSS: CSS Selectors](../3_CSS_CSS3/css_selectors.md).
- [ ] Continue building the page by styling elements or text, as discussed in [Part 3. CSS: Styling Elements](../3_CSS_CSS3/styling_elements.md) and [Part 3. CSS: Styling Text](../3_CSS_CSS3/styling_text.md).

### Deploy

What does it mean to deploy code? In short, our code will be copied to a server and sent to clients, as discussed in [Part 1. Web Basics: The Request and Response Cycle](../1_Web_Basics/req_resp.md). When thinking about deployment:

- [Check out a live version of the site](https://reactor1.z5.web.core.windows.net).
- Follow the deployment instructions from [Part 4. Capstone Deployment](../4_Capstone_Deployment/deploy.md).

### Iterate

Depending on the length of the project, a developer might also be responsible for maintaining the application over a period of time. During this maintenance, you can expect to tackle the following tasks:

- Add new features.
- Add new pages.
- A/B test different colors/user flows.

---

## Key takeaways

- Review requirements before coding.
- Break pages into manageable sections.

## Bonus

- Improve user experience by breaking steps into multiple pages so users don't have to scroll.
- Add cost calculation to order.
- Add about and contact pages.

## Resources

- [Hero Image](https://pixabay.com/photos/3d-printer-printing-technology-791205/)
