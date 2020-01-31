# The Request and Response Cycle

As we know now, the web is simply an interconnected network of computers that interact and communicate with each other. But how exactly do they communicate? What a great question! The most common and basic way computers communicate with each other is through the **request and response cycle**. Earlier, we talked about how there are generally two types of computers involved in this process: the **client** and the **server**.

## The Request

As you might have guessed, the request and response cycle begins with the client making a request by entering an address into a web browser. Once the request is on its way, the first stop it makes is at the **Domain Name Server (DNS)**.

## The DNS

The actual address of a web page is an IP address which looks like a series of four period-separated numbers. Let's say I own a house on 123 Main Street and I chose to name my house Breezy Acres. The actual IP address of a web page is equivalent to my street address, and the name Breezy Acres is equivalent to the domain name you typed into the browser. So the **DNS** reads the URL and routes your request to the proper IP address.

## The Response

Once the **server** receives the client's request, given that the server approves the request, a **response** is prepared on the server-side. There are many different ways the server can prepare a response for the client (querying a database, handling logic, executing algorithms, etc) but we'll cover that in more detail in the next section on Full Stack Development. An important thing to note here is that although the response can be prepared in many different ways, it will _always_ be some combination of **HTML, CSS, and JavaScript**!

![Client Server](../images/client-server.jpg)

## What you've learned

In this section we covered how the HTTP Request and Response cycle works and how the response is made up of HTML, CSS, and JavaScript. We also quickly discussed how the DNS system works and how it interprets URLs to return the data you request from specific websites.

NEXT: [Full Stack Web Development](./full_stack.md)
