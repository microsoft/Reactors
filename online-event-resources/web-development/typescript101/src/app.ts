import { load } from "dotenv";
import { TextAnalyticsClient, AzureKeyCredential } from "@azure/ai-text-analytics";

load();

const client = new TextAnalyticsClient(
    process.env.CogSvcs_Endpoint,
    new AzureKeyCredential(process.env.CogSvcs_Key)
);

async function getSentiment() {
    const response = await client.analyzeSentiment(['I am fantastic!']);
    console.log(response);
}

getSentiment();

// interface Message {
//     text: string;
// }

// function displayMessage(message: Message) {
//     console.log(message.text);
// }

// let message: Message = {
//     text: 'Hello, world'
// };

// displayMessage(message);
