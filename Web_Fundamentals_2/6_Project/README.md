# Web Fundamentals 2 Project

## Background

Find My Neighbors is a community building platform that provides a virtual bullet board that is viewable within a set radius from the user. The company seeks to bring communities closer together by improving communication and visibility within communities. As a member of the development team, a designer has supplied a mock up to be implemented by you, the web developer.

## Key Concepts

- Web Development Process
- Identify page layouts by breaking down page into sections
- Integrating APIs
- Determining the steps necessary to complete the task

## Ethics

Here are some questions to think about:

- When should we ask a user for their location? (right when they get to the site or only when necessary)
- What is the privacy concern when prompting users to use their location?
- How could this data be used to identify a particular individual?
- How will the company manage the information that users are posting to the virtual bulletin board?

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

Create a good foundation by focusing on the structural html before apply any CSS. HTML is equivalent to the bones in our body in the sense that it helps hold everything together, without it we cannot hold form. CSS can then be applied on top of solid HTML foundation to add the final touches. A common developer mistake is too try to fix layout issues with CSS first, which can lead more difficult to maintain code. Lastly improve the functionality by make the page dynamic through use of Javascript.

- [ ] Idenify layout and repeating patterns (to be used for clasification)
- [ ] Create the necessary files and folders (index.html, assets/css/main.css, assets/js/main.js)
- [ ] Create section by section focusing on the html structure first
- [ ] Add style to get layout to match mockup
- [ ] If relevant, hardcode some data onto page before using Javascript to fetch data to continue to focus on styling
- [ ] Create event listeners for button clicks
- [ ] Find the users location
- [ ] Fetch relevant data
- [ ] Loop through data to add content to page

### Deploy

- [Checkout a live version of the site](https://reactor2.z22.web.core.windows.net/)
- [Deployment Instructions](../5_Capstone_Web_Publishing/deploy.md)

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

- [ ] Add a form to allow neighbors to communicate with eachother (posting to the bulletin)
- [ ] Disable the button when finding my location
- [ ] Enable to button after location is found

## Resources

- [Hero Image](https://pixabay.com/photos/residential-aerial-view-aerial-1149514/)
