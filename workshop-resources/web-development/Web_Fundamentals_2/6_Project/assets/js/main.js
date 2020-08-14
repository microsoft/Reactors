// Verify that the JavaScript is properly linked by logging in to the console.
// console.log("main.js")

// Step 0: Setup
document.addEventListener("DOMContentLoaded", () => {
  /*
    First thing to do is wait until HTML finishes loading before running JavaScript.
    This is especially important when using the document.querySelector function.
    If the HTML element you are trying to select is not yet loaded,
    you won't be able to find the element on the page.
  */

  // Create event listener for the button to find jobs.
  document
    .querySelector("#find-jobs")
    .addEventListener("click", appendJobsToPage)
})

/* Functions */

// Function 1 appendJobsToPage
async function appendJobsToPage() {
  // Using an async function, you can wait for the data to return before proceeding with the code execution.
  // Step 1: fetch the data.
  const postsData = await getPostsData()
  const usersData = await getUsersData()

  // Step 2: remove tip element because you have your post and user data.
  const tip = document.querySelector("#tip")
  tip.remove()

  // Step 3: Select the postings element in preparation for appending the posts to the page.
  const postings = document.querySelector("#postings")

  // Step 4: Loop through each post.
  for (post of postsData) {
    // Log the post to inspect the object in the browser console.
    // console.log(`post: `, post)

    // Step 5: Find the user who created the post.
    let user = usersData.filter((user) => user.id === post.userId)
    /*
      Because the filter function returns an array of matching users, you can set the
      user variable equal to the user in the first position of the array.
    */
    if (user.length === 1) {
      user = user[0]
    } else {
      // If you don't find the user,
      // throw an error.
      throw new Error("No user found")
    }

    // Log the user to inspect the object in the browser console.
    // console.log(`user: `, user)

    // Now that you have a user, you can build the HTML.

    // Step 6: Use JavaScript create the HTML.
    // The example HTML you will build can be found in the index.html file.

    // Create a div element to hold your job posting.
    const divNode = document.createElement("div")
    divNode.className = "job-post"

    // Create an H3 element to hold the job title.
    const h3Node = document.createElement("h3")
    // Using template literals, you can create a string that includes some text and the post title.
    const jobTitle = document.createTextNode(`Job Title: ${post.title}`)
    // Add the text node to the H3 element.
    h3Node.appendChild(jobTitle)
    // Add the H3 node to the div element.
    divNode.appendChild(h3Node)

    // Repeat for each element.

    const h4Node = document.createElement("h4")
    const company = document.createTextNode(`Company: ${user.company.name}`)
    h4Node.appendChild(company)
    divNode.appendChild(h4Node)

    const h5Node = document.createElement("h5")
    const descriptionLabel = document.createTextNode("Description:")
    h5Node.appendChild(descriptionLabel)
    divNode.appendChild(h5Node)

    const pDescriptionNode = document.createElement("p")
    const descriptionText = document.createTextNode(post.body)
    pDescriptionNode.appendChild(descriptionText)
    divNode.appendChild(pDescriptionNode)

    const pContactNode = document.createElement("p")
    const contactLabel = document.createTextNode("Contact: ")
    pContactNode.appendChild(contactLabel)

    const aNode = document.createElement("a")
    const contactText = document.createTextNode(user.name)
    aNode.appendChild(contactText)
    aNode.href = `mailto:${user.email}`
    pContactNode.appendChild(aNode)

    const moreDetailsText = document.createTextNode(" for more details.")
    pContactNode.appendChild(moreDetailsText)
    divNode.appendChild(pContactNode)

    // Step 7: Append HTML to the page.
    postings.appendChild(divNode)
  }
  // End of for loop

  // Done!
  // By now, the page should have the code for each post that was returned by the API.
  // Confirm this in your browser and inspect the HTML to verify that the JavaScript-generated HTML is valid.
}

/* Function 2 getUsersData */
async function getUsersData() {
  // Fetch users using the browser fetch API.
  const usersResponse = await fetch(
    "https://jsonplaceholder.typicode.com/users",
    {
      mode: "cors",
      headers: { "Access-Control-Allow-Origin": "*" },
    }
  )
  // Convert the response into JSON.
  const usersData = await usersResponse.json()

  // Log the data to see how it appears.
  // console.log(`usersData: `, usersData)

  return usersData
}

/* Function 3 getPostsData */
async function getPostsData() {
  // Fetch posts using the browser fetch API.
  const postsResponse = await fetch(
    "https://jsonplaceholder.typicode.com/posts",
    {
      mode: "cors",
      headers: { "Access-Control-Allow-Origin": "*" },
    }
  )
  // Convert the response into JSON.
  const postsData = await postsResponse.json()

  // Log the data to see how it appears.
  // console.log(`postsData: `, postsData)

  return postsData
}
