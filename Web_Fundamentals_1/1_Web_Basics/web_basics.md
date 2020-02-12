# Web Basics

## How the Web Works

So what is this magical Web? We use it every day, but we may not fully understand exactly what it is and how it works. As future awesome web developers and general humans who use the internet daily, it's important that we lay a concrete foundation. Simply put, the Internet is a large **network of computers that are connected** and can communicate together. The Web is made up of computers that we call **clients** and **servers**.

![Web Image](../images/web.jpg)

**Clients** are the typical Web user's Internet-connected devices (for example, the computer you are on right now connected to your Wi-Fi!) and web browsers on those devices (e.g. Edge on Windows, Safari on Mac, or Silk on Kindle).  

**Servers** are computers that store web pages or applications. They are computers, just like the machine you are on right now, without the keyboard, trackpad, or screen. When a **client** wants to access a web page (like Bing or LinkedIn), a copy of the web page is downloaded from the server onto the client machine to be displayed in the user's web browser.

In simpler words, the client makes a **request** and the server answers back with a **response**. But we'll get into the request-response cycle in a little bit.

## So What Actually Happens

Let's say you want to learn more about clients and servers (because I'm sure you do!) so you open a browser and type into the address bar www.bing.com.

1. Your browser goes to the Domain Name Server or DNS (think of this like an address book or phone book) and finds the _real_ address of the Bing server that the website lives on (the **IP address** which is a series of four period-separated numbers like 52.33.229.159).
2. The browser sends an **HTTP request** message to Bing's servers asking it to send a copy of the website back to you, the client.
3. Provided that you are not violating any security protocols and you have the proper permissions, Bing's servers approve the client's request and responds by sending the website's files back to the browser as a series of small chunks called data packets.
4. The browser assembles the small chunks into a complete website and displays the Bing homepage to you.

And there you have it! Nothing magic to it!

## What is a URL

While surfing the web you have likely heard the term URL thrown around. URL stands for Uniform Resource Locator and this is a reference to a resource that is on the web. As users, we enter in a URL and expect to get a resource back. When we enter in the URL of www.linkedin.com we expect to get LinkedIn's homepage back as a resource that was located. There are two parts to a given URL; HTTP is the protocol identifier, www.linkedin.com is the resource name.

## What is an IP address

"IP Address" is probably another one of those tech buzzwords you may have heard here and there. It may look and sound intimidating, but an IP address is simply one computer's unique identifying address.  IP addresses allow the location of literally billions of digital devices that are connected to the Internet to be pinpointed and differentiated from other devices! Just like how your home needs a unique mailing address to send you a letter, a remote computer needs your unique IP address to communicate with your computer. So why is it that we type in something like www.linkedin.com, instead of LinkedIn's actual IP address (which is currently 144.2.12.1, but may change from time to time)? It would be extremely difficult for any reasonable person to remember the actual IP address of all of their favorite websites, so we point the IP address to a domain name. When you type in www.linkedin.com, your web browser visits something called the DNS (Domain Name Server), which acts like a phone book. The DNS finds the domain name of www.linkedin.com, matches it with the correct IP address, and sends the request to LinkedIn's servers!

## What is a localhost

It’s a name and address used by a web browser to find a web server on your computer. The difference between localhost and any other URL like www.linkedin.com is that localhost traffic never travels on a network. Data is transmitted in your computer - hence the word "local". Your computer has many different network ports, which are used to give different access rights to different hosted files. Your localhost is unique in that it is assigned to the loopback network interface, which is a fancy way of saying that you are giving access and getting access to the hosted files on your computer. Your machine is both the client and the server! Translated into an IP address, a localhost is always designated as 127.0.0.1.

Localhost is the perfect tool for developers building web applications because it allows you to view your web page during the development process all the way up until it is ready for production.

![Local Host Image](../images/localhost.jpg)

## What you've learned

In this section you learned about servers and clients and how they use a protocol called HTTP to connect. You also learned with how IP addresses and URLs work together and what it means to run a localhost on your home computer. In the next section we will discuss the HTTP Request and Response Cycle.

Next: [Request and Response Cycle.](./req_resp.md)
