# Wanderer game, new edition

As previous version, this one also contains of files ```game.py``` and ```main.py```. Game has all classes that are needed for game to functionate properly, and in main there is a main function and all the objects are created to play the game

The main idea of the game is that you wander in a lost village, and it has a whole new storyline and the boss that you need to kill

## Class Entity

Creates an object that represents an alive creature that is present in a game and can interract with the player

## Class Villager

Sublass to Entity, a friendly mob that helps player to go through his adventure

## Class Enemy

Subclass of Entity, an unfriendly creature that can kill you, and your goal is to clear the village from them

## Class Boss

Subclass of Enemy, an  unfriendly creature that is stronger that regular enemy and after killing it you finish the game

## Class Place

Class that represents some kind of area where some kind of action takes place

## Class Item

Class that represents an object that gives different advantages for a player

## Class Weapon

Subclass of Item that represents an Item with which the player can fight

## Class Healer

Subclass of Item that can heal a player
