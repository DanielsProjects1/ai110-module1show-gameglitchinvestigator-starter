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

The game's purpose was essentially just for the player to guess a number until they hit a certain amount of attempts, track the history of their guesses, give them hints if their guess was lower or higher than the secret number, and allow them to guess again after they get it right or run out of attempts.

- [ ] Detail which bugs you found.

The bugs I found were:
1. The game failed to start a new game.
2. The ranges of Normal and Hard difficulties were swapped.
3. The hints given were the opposite of what they should be.
4. The number range was hard coded in someplaces and failed to update when the difficulty was changed.

- [ ] Explain what fixes you applied.

I used Copilot or Claude Code to fix all of these bugs. It restarted the state of the game every time a new game was started, updated the range everywhere when the difficulty was changed, update the secret number to be within the range when the difficulty was changed, corrected the hints when the guess number did not equal the secret number, swapped the ranges for Normal and Hard difficulties, and finally set the session_state status to playing when a new game began.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
![alt text](<Screenshot 2026-03-22 at 11.28.22 PM.png>)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
