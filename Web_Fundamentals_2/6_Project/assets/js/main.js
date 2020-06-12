// First verify that the Javascript is properly linked by logging to the console.
console.log("main.js")

// TODO
// [ ] List numerical steps(1, 2, 3, 4, 5) and indicate above function declaration

// First thinkg we should do is wait until html is done loading before running our Javascript
// This is especially important when using the document.querySelector function
// because if the html we are trying to select an element that is not yet loaded
// we will not be able to find the element
document.addEventListener("DOMContentLoaded", () => {
  // Create event listener for the button prompting the user if we can check their location
  document
    .querySelector("#find-my-location")
    .addEventListener("click", findMyLocation)
})

// Functions
// Javascript hoisting will bring this function to the top allowing us to declare it here

// Define a function that get's the user's location
// This function will be called when the button is clicked
function findMyLocation() {
  // Verify the function is executing properly
  // Feel free to comment this out or remove it
  // Logging allows the developer to get instant feedback from their code during development
  console.log("Finding location")

  // Select the status element so that we can update the text
  const status = document.querySelector("#status")

  // Using the browser navigator api we can check the location of the device
  if (!navigator.geolocation) {
    // If geolocation is not supported, set the text to unsupported
    status.textContent = "Geolocation is not supported by your browser"
  } else {
    // If geolocation is supported, set the status to locating
    status.textContent = "Locating…"

    // Request the user's location
    // Pass the success function and error function callbacks
    navigator.geolocation.getCurrentPosition(success, error)
  }
}

// Function is called we there is an error while retrieving current location
function error() {
  status.textContent = "Unable to retrieve your location"
}

// Function is called when we are able to successfully get the current position
// Params: a success
function success(position) {
  // Log the position to see what the object looks like
  console.log(`position: `, position)

  // Extract the latitude and longitutde
  const latitude = position.coords.latitude
  const longitude = position.coords.longitude

  // Select the status element
  const status = document.querySelector("#status")

  // Update the text to display the coordinates
  status.textContent = `Latitude: ${latitude}, Longitude ${longitude}`

  // Call the function to fetch and add posts to the bullet board
  appendPostsToBulletinBoard()
}

// Using an async function we can wait for the data to return before proceeding with the code execution
async function appendPostsToBulletinBoard() {
  const [postsData, usersData] = await getData()

  // Select the bulletin element in preparation for appending the posts
  const bulletin = document.querySelector("#bulletin")

  // Loop through each post
  for (post of postsData) {
    // Log the post to see what it looks like
    console.log(`post: `, post)

    // Find the user in the user list
    let user = usersData.filter((user) => user.id === post.userId)
    // Since the filter function returns an array of matching users we can set the
    if (user.length === 1) {
      user = user[0]
    } else {
      // If we don't find the user
      // throw an error
      throw new Error("No user found")
    }

    // Log the user to see what it looks like
    console.log(`user: `, user)

    // Now that we have a user we can build the html
    // create an a tag to link to a user profile page
    const aTag = document.createElement("a")
    // set the href to the page
    aTag.href = `http://jsonplaceholder.typicode.com/users/${user.id}`
    // set the target as blank to open a link in a new tab
    aTag.target = "_blank"

    // create the text node for the userName
    const userName = document.createTextNode(user.name)
    // appending it to the a tag
    aTag.appendChild(userName)

    // create another text node for the post information
    // user template literals we can create a string the the post title
    const userPost = document.createTextNode(` posted: ${post.title}`)

    // Create a paragraph node to be appended into the bulletin board
    const paragraphNode = document.createElement("p")
    // first add the a tag
    paragraphNode.appendChild(aTag)
    // then add the user's post
    paragraphNode.appendChild(userPost)

    // lastly add the paragraph to the bullet
    bulletin.appendChild(paragraphNode)

    // After clicking the find my location button
    // inspect the page to confirm that our html was added properly
    // you should observe the p tag with two children, the a tag and text
  }
}

// TODO
// Break this up into two separate functions so that each function returns a separate array
// Return a nested array will probably be confusing for people new to Javascript

// Function for getting user and post data
// Returns a nested array with data we fetched
async function getData() {
  // After finding the users location we can use the browser's fetch api to get the list of users and posts

  // Fetch users
  const usersResponse = await fetch(
    "https://jsonplaceholder.typicode.com/users",
    {
      mode: "cors",
      headers: {
        "Access-Control-Allow-Origin": "*",
      },
    }
  )
  // Convert the response into json
  const usersData = await usersResponse.json()

  // Fetch posts
  const postsResponse = await fetch(
    "https://jsonplaceholder.typicode.com/posts",
    {
      mode: "cors",
      headers: {
        "Access-Control-Allow-Origin": "*",
      },
    }
  )
  // Convert the response into json
  const postsData = await postsResponse.json()

  // Log the data to see what it looks like
  console.log(`postsData: `, postsData)
  console.log(`usersData: `, usersData)

  return [postsData, usersData]
}

// TODO
// Template for function comments

/**
 * Returns x raised to the n-th power.
 *
 * @param {number} x The number to raise.
 * @param {number} n The power, must be a natural number.
 * @return {number} x raised to the n-th power.
 */
