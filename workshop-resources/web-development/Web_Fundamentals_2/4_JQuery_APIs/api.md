# Application Programming Interface (API)

APIs define a set of rules in which you can interact with a particular application. For web developers, the useful URLs previously discussed are specifically designed to be used by other developers or web pages. With a set of governing principles on how an API should be designed, developers can access information in very logical steps.

For example, pretend you have a huge database of Pokemon and want to allow other developers to access this database to create cool Pokemon applications like a Pokedex. You can create a series of URLs that map to important information in a predictable manner. These developers will need to read the documentation of your API to learn how to properly interact with your URLs and get predictable results. This is exactly what PokeAPI did. Take a look at the [PokeAPI documentation](http://pokeapi.co/).

## Every API is different

Even though every API is designed with a set of governing principles in mind, every API you interact with will be different. It is up to the developer who wrote the program to specify the protocols needed to interact with that API. Some APIs will let you access information as long as you ask for it in the URL. Some APIs will give you better information if you submit more data through a form. Some APIs will only allow you to request a certain URL a limited number of times per day. Some APIs will require you to sign up on their website to receive an authenticity token to pass with every API request you make.

APIs are usually web URLs where you can pass information either in the URL or by posting a form to the URL and the server returns JSON (or other similar data formats). Later, you will create your own API, but in essence, this is all you need to build an API: if a URL takes data and outputs JSON (or other similar formats), you have created an API. 

Take a look at some of the APIs listed below:

* [LinkedIn](https://developer.linkedin.com/docs/rest-api#)
* [Open Weather Map](http://openweathermap.org/api)
* [GitHub](https://developer.github.com/v3/)
* [Twitter](https://dev.twitter.com/rest/public)

Although you must interact with each API differently, notice how they are all collections of URLs that you can use as long as you follow the protocols that the developer has specified in the documentation.

## Benefits

* Speed (for developers): Instead of creating all code from scratch, you can utilize APIs of other web services to build apps more easily. There are many useful APIs available.
* Cross development (for managers/developers): APIs allow experts and developers of different languages (PHP, Ruby, Python, etc.) to work together efficiently. For example, let's say you had a team of Java developers who built an app in Java and you had another team of PHP developers who built an app in PHP. Say you had another team of JavaScript developers who built their app in Node. What could you do if you wanted these three apps to work together to send data back and forth? You could either have everyone migrate to one language (not recommended) or have three teams build APIs (URLs where you can submit/retrieve information) so that these three apps can work together to communicate information!
* Wider audience reach (for marketers): APIs allows marketers to promote their product/services to a wider audience of developers. Then, these developers can build applications that use the API to reach an even wider audience of consumers and developers. For companies who want to reach a wider audience, like LinkedIn, Microsoft, Twitter, and Google, APIs make it easy for developers to use their services to build these brands.
