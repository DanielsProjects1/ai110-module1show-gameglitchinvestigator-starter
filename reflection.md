# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---

 1. The game seems to not know when you've started a new game.
 2. The hints themselves are incorrect. They give me the opposite of what the actual hint should be.
 For example, if the answer is 90 and my guess is 50, the hint the program gives me is to go lower instead of higher like it should be.
 3. Normal and Hard mode seem to be switched. Easy mode gives you a 1/20 chance to get the correct guess, but then Normal gives you a 1/100 chance and Hard gives youa 1/50 chance. The logical progression should be Normal gives you a 1/50 chance and Hard gives you a 1/100 chance.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).


My answer:

I used Copilot to help me debug most of the project, then I switched to Claude Code because I had used up my chats on Copilot for the month.
One example of an AI suggestion that was correct and that I did not catch when testing the program on my own was that the game state did not reset after the player started a new game. I verified this by running the program, successfully guessing the number the first time, and then starting a new game. The state; the number of attempts, the players history of guesses for the current game, and the secret number did not update when a new game was started.
An example of an AI suggestion that was misleading was that attempts were incremented when the player's input was invalid (was not a number). This was true, however, I did not consider this a bug because that is still an attempt regardless of whether the guess was a number or not.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

My answers:

I decided whether a bug was really fixed based on whether it passed the tests I had Copilot creat for it in test_game_logic.py. 
One of these tests were checking whether get_range_for_difficulty function returned the right range for each difficulty.
Copilot helped me create this test after I told it to swap the ranges returned to the function for values "Normal" and "Hard", then add a test for this function in test_game_logic.py and run it.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

My answer: Basically, Streamlit resets your entire script after every interaction, and session state is how you can preserve the memory of the app across reruns during a given user session.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

Using Copilot/Claude Code to speed up my debugging process by having it look for any bugs in the program, so that any bugs that I failed to catch, the AI catches it and gives me fixes for it.

- What is one thing you would do differently next time you work with AI on a coding task?

Give the AI more efficient prompts telling it what to do.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

I now no longer believe that all AI generated code is buggy. I can use AI to generate fixed code for me for small portions of my program that had bugs in them.
