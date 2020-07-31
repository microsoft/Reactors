# Instructions

### Goal
This directory contains the Bank contract and AssetManager contract from the previous exercises, along with most of the Banker contract as well as a migration and a
test. You will need to fill in some details to make the tests pass.


### Steps
1. To install dependencies, run `npm install`.
  - If you don't have truffle or truffle-assertions installed globally, you will need to
  add them here: `npm install -g truffle` and `npm install -g
  truffle-assertions`.

2. Run `truffle compile`. There may be compilation errors. 

**You need to import the Bank and AssetManager contracts into the definition of the Banker contract**. Look for a TODO indicator at the top of the file.

3. Run `truffle develop`, and then run the `test` command. You should see
  one or more errors. To fix them, look for TODO indicators in the
  **contracts/Banker.sol** file. These will help you figure out what
  is required to make the tests pass.

  - If you get stuck, you can find a working version in the or the [Completed_Solutions directory](../../../Completed_Solutions), but try truffle before using these other options.
