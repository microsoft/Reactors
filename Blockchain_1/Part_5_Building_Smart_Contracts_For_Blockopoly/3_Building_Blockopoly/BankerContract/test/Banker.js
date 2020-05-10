const Banker = artifacts.require("Banker");
const truffleAssert = require('truffle-assertions');

// This test handles the majority of the game-specific rules. At this
// point, the tests accumulate state between the it clauses. Usually
// tests reset the state, but it seemed easier to isolate the tests
// this way.

contract('Banker', (accounts) => {

    it('testing stopping an unstarted game of Banker', async() => {
        const c = await Banker.deployed();

        // This will fail because the game hasn't started yet
        await truffleAssert.fails(c.stopGame());
    });

    it('testing starting an unstarted game of Banker', async () => {
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

        // The banker should be initialized to a large default pile
        // of cash. Game players are assigned much less.

        var balance = await c.getBalance(accounts[0]);
        assert.equal(100000, balance.toNumber());
        balance = await c.getBalance(accounts[1]);
        assert.equal(1000, balance.toNumber(), 'Player 1 got initial 1000');
        balance = await c.getBalance(accounts[2]);
        assert.equal(1000, balance.toNumber(), 'Player 2 got initial 1000');
    });

    it('testing double-starting a game on Banker', async() => {
        const c = await Banker.deployed();

        // This will fail because the game has already started.
        await truffleAssert.fails(c.startGame());
    });

    it('testing player join a game on Banker', async() => {
        const c = await Banker.deployed();

        // This player should not have joined yet and there should
        // be room in the game. For now, we are allowing players to
        // join after the game has started. If we want to disallow
        // that, the tests will have to be refactored but that 
        // won't be hard.
        var result = await c.joinGame('User3', {from: accounts[3]});
        truffleAssert.eventEmitted(result, 'PlayerJoined');
    });

    it('testing player double-join a game on Banker', async() => {
        const c = await Banker.deployed();

        // This should fail because User1 joined earlier.
        await truffleAssert.fails(c.joinGame('User1', {from: accounts[1]}));
    });

    it('testing player remaining players join a game on Banker', async() => {
        const c = await Banker.deployed();

        // Fill in the remaining slots so the game fills up.
        await c.joinGame('User4', {from: accounts[4]});
        await c.joinGame('User5', {from: accounts[5]});
        await c.joinGame('User6', {from: accounts[6]});

        // At this point, we can't add a seventh player.
        await truffleAssert.fails(c.joinGame('User7', {from: accounts[7]}));
    });

    it('testing property management on Banker', async() => {
        const c = await Banker.deployed();

        // The Banker adds a dozen or so Reactor properties in its 
        // constructor. We could verify all of them, but for now we
        // are just verifying three of them.

        var reactors = [
            "Redmond Reactor",
            "Seattle Reactor",
            "San Francisco Reactor"
        ];
        var available;
        
        // Make sure each of these properties is available.

        reactors.forEach(element => async() => {
            available = await c.isPropertyAvailable(element);
            assert.equal(true, available, 
                element + " Property is available");
        });

        // There is no Frankfurt Reactor so this property should not
        // exists but shouldn't cause any trouble.

        available = await c.isPropertyAvailable("Frankfurt Reactor");
        assert.equal(false, available, 
            "Frankfurt Reactor Property is not available");

        // This should fail because the Banker owns it already and 
        // you can't buy property from yourself.
        await truffleAssert.fails(c.buyProperty("Redmond Reactor"));
        
        // Make sure all of the players we are expecting to be there are
        var numPlayers = await c.getNumberOfPlayers();
        assert.equal(6, numPlayers.toNumber(), "There are six players");
        
        // At this point, accounts[1] should have money in the bank and it
        // should be enough to buy the Redmond Reactor property from the
        // Banker. We send the message as accounts[1] so the buyer and 
        // seller aren't the same and this should therefore work.

        var result = await c.buyProperty("Redmond Reactor", {from: accounts[1]});

        // At this point, accounts[1] should be the owner of the property
        
        var owner = await c.getPropertyOwner("Redmond Reactor");
        assert.equal(owner, accounts[1], "Property Transfer Occurred");
    });

    it('testing stopping a game on Banker', async() => {
        const c = await Banker.deployed();

        // Stop the game we have been using
        var result = await c.stopGame();
        truffleAssert.eventEmitted(result, 'GameStopped');
        await truffleAssert.fails(c.stopGame());
    });
});
