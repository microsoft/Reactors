# Instructions

### Goal
This directory contains the Bank contract and AssetManager contract from the previous exercises
and most of the Banker contract as well as a migration and a
test. You will need to fill in some details to make the tests pass.


### Steps
- First, run `npm install` to install dependencies.
  - If you don't have
  truffle or truffle-assertions installed globally, you will need to
  add them here as well (`npm install -g truffle` and `npm install -g
  truffle-assertions`).

- Second run, `truffle compile`. There may be compilation errors. 

- **You need to import the Bank and AssetManager contracts into the definition of the Banker contract**. Look for a TODO indicator at the top of the file.

- Run `truffle develop` and then run the `test` command. You should see
  one or more errors. To fix them, look for TODO indicators in the
  **contracts/Banker.sol** file. These will help you figure out what
  is required to make the tests pass.

- If you get stuck, you can find a working version in the or the [Completed_Solutions directory](../../../Completed_Solutions), but try to make it work before looking in those places.
