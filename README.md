# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- In this game you have to guess a secret number, which is randomly generated based on the difficulty. If you have an Easy difficulty, your range is from 1 to 20, Normal difficulty has range from 1 to 50 and Hard difficulty has range from 1 to 100. You can also use hints that can help you see if you guessed higher or lower. 
- [ ] Detail which bugs you found.
  - The main page did not change the range according to difficulty.
  - The range of difficulties were not in the right order.
  - Hints were reversed.
  - After winning, the new game button refreshes only the secret word, and not the game itself.
  - The attemps went into negative.
  - The number of attempts starts from 1 instead of 0.
  - When changing difficulties in the middle of the game, the new game doesn't start, but it continues with the new difficulty.
  - The score calculation is wrong.
  - If the number of attmeps is even, the secret number is converted into string, so if the player guessed the right number in the even attempt, it would either display too low or too high or give an error.
  - When a player enters not a number (a symbol) it says "This is not a number" but it still counts it as attempt. 
- [ ] Explain what fixes you applied.
  - Changed the displayed range on the right side of the web app.
  - Changed the range according to each difficulty.
  - Fixed hints, they are not reversed now.
  - Fixed score calculations.
  - fixed a bug when secret number was converted to string.
  - fixed "Invalid guess" not to count as attempt.

## 📸 Demo

-![!\[alt text\](../pictures/image.png)](pictures/image.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
