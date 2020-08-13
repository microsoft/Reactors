# Microsoft Cognitive Services Reactor Workshop

By the end of this workshop, you will have a basic grasp of how you can implement Microsoft Cognitive Services in your applications. Your hands-on exercises in this workshop will be centered on using Python and Flask in Visual Studio Code to call REST APIs to access Microsoft Cognitive Services. You will also see several different simple and advanced Microsoft Cognitive Services demonstrated.

## What is artificial intelligence?

At root, artificial intelligence (AI) - programs which learn from experience in order to address new situations without explicit instructions - is a tool for amplifying human ingenuity. It is the augmentation of human resourcefulness and inventiveness through the computational power of computers. For this reason, Microsoft believes AI offers incredible opportunities to drive widespread economic and social progress. It provides tremendous tools for meeting medical, educational, and environmental challenges. At the same time, AI supplies tools to help organizations of all sizes solve more mundane problems.

### Examples of AI in action

Let's explore a few implementations of AI in the real world.

#### Wildbook

Microsoft partnered with Wild Me on a project called [Wildbook](http://www.wildbook.org/)®. Wildbook is an open-source framework for wildlife data management seeking to identify and track specific, individual animals from endangered species in the wild. Wildbook uses Microsoft Cognitive Services to do this. AI enables Willdbook not only to detect and identify animals based on their species, but to identify individual animals based on unique differentiators such as the spots on a cheetah or the ridges on a whale’s tail.

### Progressive

Auto insurance provider Progressive may be best known for Flo, its iconic spokesperson. The company wanted to take advantage of customers’ increasing use of mobile channels to interact with its brand. So Progressive [used Microsoft Azure Bot Service](https://customers.microsoft.com/story/progressive-insurance-cognitive-services) and Cognitive Services to quickly and easily build the [Flo Chatbot](https://www.facebook.com/flofromprogressive/) - currently available through Messenger on Flo’s Facebook page - which answers customer questions, provides insurance quotes, and even offers a bit of witty banter in Flo’s popular, well - known style.

As mobile has become a more important channel, Progressive has looked for ways to use it to connect with customers who want easy, personal, and trustworthy digital experiences. The insurer has found the Microsoft Azure Bot Service and Cognitive Services APIs made it easy to adapt and refine the bot and its responses without needing data scientists or to write complex code. The APIs also provide the ability for a knowledge base to grow and learn more over time, so the responses just keep getting better and better.

### Uber

It's important to ride-sharing company Uber the driver behind the wheel matches the driver account on file, both to protect riders and to help ensure the drivers’ accounts haven’t been compromised. Uber decided to add photo-matching technology to an array of screening methods they use.

[Uber turned to Microsoft](https://customers.microsoft.com/story/731196-uber) for the performance, accuracy, and scalability of the Face API in Microsoft Cognitive Services, which can compare photos and return a match within milliseconds, even from a low quality photo. If the match is unsuccessful, the implemented platform is smart enough to notice, and suggest corrective actions. For example, the failure may have been cuased by a reflection from the driver's eyeglasses; the driver would be prompted to remove their glasses and take their picture again.

## Microsoft's goal: democratizing AI

Computers can help people make better decisions through AI. Computers are very good at remembering things—absent a system failure, computers never forget. They are better at probabilistic reasoning than most people, which is powerful for making useful predictions and classification. Finally, computers excel at discerning patterns in data too subtle for people to notice. This "computational intelligence" computers can provide can have a significant impact in almost any field where human intelligence has a role to play. For this reason, Microsoft seeks to combine the capabilities of computers with human capabilities to enable people to achieve more.

Given the power of AI for social, environmental, and economic progress, Microsoft's stance is to use AI to enable and empower everyone. Microsoft is doing this in three main ways:

1. Creating products using AI in innovative ways to enable all users.
2. Building tools developers such as yourselves can use to create (I’ll be showing you how to use some of these tools later)
3. Actively contributing to the global dialog about the ethical implications of AI. Harnessing its potential also requires us to adopt an open and questioning mindset. We have a shared responsibility to ensure the models we build (and the AI experiences they support) are fair, reliable and safe, private and secure, inclusive, transparent, and accountable.

Microsoft is working with technology communities, governments, universities, and organizations on this area of concern through various avenues, including workshops like this one today.

## AI versus ML

Defining each term can be challenging, as they are often used interchangeably. At a high level, AI can be termed as intelligence demonstrated by machines, while machine learning (ML) is the study of algorithms and models which can be used to determine answers based on a given piece of data.

Or, to quote Wikipedia:

[Artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence)

"In computer science, an artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans. Colloquially, the term 'artificial intelligence' is often used to describe machines (or computers) that mimic 'cognitive' functions that humans associate with the human mind, such as 'learning' and 'problem solving'."

[Machine learning](https://en.wikipedia.org/wiki/Machine_learning)

"Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to perform a specific task without using explicit instructions, relying on patterns and inference instead. It is seen as a subset of artificial intelligence. Machine learning algorithms build a mathematical model based on sample data, known as 'training data', in order to make predictions or decisions without being explicitly programmed to perform the task."

### Definitions for our time here

During the course, the term AI will be used synonymously with Cognitive Services. Cognitive Services are a set of pre-trained (or potentially customizable) deep-learning models already created for use in your applications. Machine learning, on the other hand, will represent models you would create and train on your own, which can be used for more advanced or specialized scenarios.

## Limitations of AI

Why doesn’t everyone use deep learning–based AI for every task? Building and training sophisticated deep neural nets takes a great deal of capital investment for powerful computers and a lot of time to train. This is where Microsoft comes in. Microsoft has already done the hard part of building and training the deep learning models; once trained, deep-learning AI models are swift to run. Thus you can easily access the models Microsoft has already built, and focus on building applications without getting bogged down with creating and maintaining your own AI models. With Microsoft Cognitive Services, extremely sophisticated deep neural networks are only an API call away.

## Getting started with the labs

Let's put our understanding of AI to use, implementing a sample application for Contoso Travel. We'll begin by adding the functionality necessary for [reading and translating signs from images](./computer-vision-translator/README.md).
