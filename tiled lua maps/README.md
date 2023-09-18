simple 2d lua game

video demo: https://youtu.be/1Ps8yUCjdbE

description:

Loading Libraries and Map:
The love.load() function is the entry point of the game where all the initial setup happens. You are using several external libraries to enhance your game:
anim8: A library for animating sprites.
sti: Simple Tiled Implementation, for loading and handling Tiled maps created in the Tiled Map Editor.
windfield: A physics library for collision handling and object movement.
You set a default graphics filter to make pixel art graphics appear crisp.
Entities and Characters:
You define various entities and characters in your game:
healingspot: An object representing a healing spot, created as a rectangle collider at a specific position.
bombs: An array representing bombs in the game. Each bomb has properties like position, radius, damage, and a timer for explosion.
enemy: An enemy character with attributes such as position, collider, speed, health points (hp), and a sprite for rendering.
player: The main player character, with properties similar to the enemy, but also includes animations for different directions of movement.
Collision Detection:
The function checkCollision(enemy, player) checks if the player collides with the enemy. If a collision occurs, the player's health points (player.hp) are decreased based on the enemy's damage value.

Game Logic and Update:
The love.update(dt) function handles the game's logic and is called each frame before drawing. Here are the key elements:

There is a gameOver flag to check if the player's health reaches zero, indicating the game is over.
The player's movement is controlled by the keyboard arrow keys (W, A, S, D). The direction is calculated based on the keys pressed and the player's speed, and the player's animation is updated accordingly.
A timer (bombTimer) is used to spawn new bombs at regular intervals. The bombs move towards the player, and if they collide, the player's health decreases.
The enemy (enemy) follows the player's position using a simple direction calculation and adjusts its linear velocity to move towards the player.
The Windfield physics library handles collision detection between entities and walls in the game map.
Drawing and Rendering:
The love.draw() function is responsible for rendering the game's graphics. The key elements include:
Rendering the map loaded from Tiled using gameMap:draw().
Displaying "Game Over" if the gameOver flag is set, with an option to restart the game by pressing the 'R' key.
Displaying the player's and enemy's health points (player.hp and enemy.hp) on the screen.
Drawing the player and enemy sprites at their respective positions with the appropriate animations.
Rendering the bombs as small sprites and removing them if they explode or hit the player.

Overall, the code demonstrates a basic 2D game with a player character and an enemy, along with bomb mechanics, collision detection, and health management. The game map is created using the Tiled Map Editor, and physics handling is facilitated by the Windfield library. With further development, this code can serve as a foundation to create a more complex and engaging 2D game in Lua with the LÖVE framework. I really enjoyed doing this, it took me a lot of hours even it's a pretty simple game, but it help me to realise
how to do thins better and more effective, i'll definitely keep working on it just for fun. 