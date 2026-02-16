## Snake-game  
A simple yet addictive implementation of the classic Snake game i built with Python

## Structure  
snake-game/  
├── main.py          -Game initialization  
├── snake.py         -Snake class and movement logic  
├── food.py          -Food class  
├── scoreboard.py    -Score tracking and display  
├── highscore.txt        ### NEW - auto-generated  
└── README.md        -This file

## 🚀 Getting Started  
Prerequisites  
- Python 3
- Turtle module (comes pre-installed with Python)

## Installation
 
1. Clone the repository:

```bash
git clone https://github.com/yourusername/snake-game.git
cd snake-game
```

1. Run the game:

```bash
python main.py
```

## 🎯 How to Play  
1. Use the Arrow Keys to control the snake:  
   - ⬆️ Up Arrow: Move Up  
   - ⬇️ Down Arrow: Move Down  
   - ⬅️ Left Arrow: Move Left  
   - ➡️ Right Arrow: Move Right  
2. Guide the snake to eat the red food dots  
3. Each food dot increases:  
   - Your score by 1 point  
   - The snake's length by 1 square part  
4. Avoid:  
   - Colliding with the walls  
   - Colliding with your own tail  
5. Try to beat your high score!

## 🔄 Update: High Score Persistence Added to Snake Game!

📁 New File: highscore.txt  
· Initially contains 0  
· Updates in real-time when you beat your record  
· Simple text format for easy viewing/modification  

🔧 Updated File: scoreboard.py

The scoreboard now features file I/O operations:
· .read() and 
· .write()