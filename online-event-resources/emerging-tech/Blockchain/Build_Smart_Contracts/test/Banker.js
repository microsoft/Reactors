const Banker = artifacts.require("Banker");
const truffleAssert = require('truffle-assertions');

contract('Banker', (accounts) => {

    it('testing joining and starting a game', async () => {
        const c = await Banker.deployed();
        // Can't start a game with less than two players
        await truffleAssert.fails(c.startGame());

        // We'll add two players to the game and then we should be 
        // able to start it. For the tests, accounts[0] plays the
        // role of the Banker, so we start adding users with
        // accounts[1].

        var result = await c.joinGame('User1', {from: accounts[1]});
        truffleAssert.eventEmitted(result, 'PlayerJoined');        
        result = await c.joinGame('User2', {from: accounts[2]});
        truffleAssert.eventEmitted(result, 'PlayerJoined');        
        result = await c.startGame();
        truffleAssert.eventEmitted(result, 'GameStarted');
    });

    it('testing property management on Banker', async() => {
        const c = await Banker.deployed();
        // This should fail because the Banker owns it already and 
        // you can't buy property from yourself.
        await truffleAssert.fails(c.buyProperty("Redmond Reactor"));

        await truffleAssert.passes(c.buyProperty("Redmond Reactor", {from: accounts[1]}));
        // At this point, accounts[1] should be the owner of the property
    });
});
