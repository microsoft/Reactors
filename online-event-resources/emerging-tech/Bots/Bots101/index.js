const fetch = require('node-fetch');
const restify = require('restify');

const server = restify.createServer();
server.listen(process.env.PORT || process.env.port || 3978, () => {
    console.log('server up!!');
});

const botbuilder = require('botbuilder');
const { BotAdapter } = require('botbuilder');
const adapter = new botbuilder.BotFrameworkAdapter();

adapter.onTurnError = (context, error) => { console.log(error); };

// it's all about one route
server.post('/api/messages', (req, res) => {
    adapter.processActivity(req, res, async (context) => {
        // find what the user said
        switch (context.activity.type) {
            case 'message':
                await handleMessage(context);
                break;
            case 'conversationUpdate':
                // was a member added?
                await welcomeMessage(context);
                break;
        }
    });
});

async function welcomeMessage(context) {
    if (context.activity.membersAdded) {
        await context.sendActivity('I can search GitHub to find users for you.');
        await context.sendActivity('Just tell me what you want to search for!');
    }
}

async function handleMessage(context) {
    await context.sendActivity({
        type: 'typing'
    });

    const text = context.activity.text;
    const encodedText = encodeURIComponent(text);
    const response = await fetch('https://api.github.com/search/users?q=' + encodedText);
    const json = await response.json();

    await context.sendActivity(`I found ${json.total_count} users.`);

    const firstUser = json.items[0];
    await context.sendActivity(`The first person is named ${firstUser.login}`);

    const card = botbuilder.CardFactory.heroCard(
        firstUser.login,
        [{ url: firstUser.avatar_url }]
    );

    await context.sendActivity({
        type: 'message',
        attachments: [card]
    });
}
