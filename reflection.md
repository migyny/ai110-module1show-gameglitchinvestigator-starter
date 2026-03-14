# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  - When I ran the game, the visuals looked fine, but when I started playing it, I noticed a lot of bugs and poorly programmed game.
 -----------------------------------------------------------------
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  - When I changed difficulty on the left side, the main page did not change the range according to difficulty, it still had a range between 1 and 100 despite the difficulty. (fixed)
  - The range of difficulties were not in the right order. Normal difficulty had a range between 1 to 100 and a Hard difficulty had a range from 1 to 50. (fixed)
  - Hints were reversed. When I guessed 1 and the secret number was 91, the hint said to go lower, and when i put 99, the hint said go higher. (fixed)
  - After winning, the new game button refreshes only the secret word, and not the game itself, I couldn't fuess anymore.
  - The attemps went into negative, instead of not allowing any new guesses once there was no attmepts.
  - The number of attempts starts from 1 instead of 0, so if a player has 8 attempts, he actually has 7 because the count starts from 1. (fixed)
  - score can go to negative.
  - When changing difficulties in the middle of the game, the new game doesn't start, but it continues with the new difficulty.
  - The score calculation is wrong. When player guess the number that is too high, if it's an even number it adds +5 (when the answer is wrong and it is not supposed to add any points). Wrong guesses should always substract the score. (fixed)
  - If the number of attmeps is even, the secret number is converted into string, so if the player guessed the right number in the even attempt, it would either display too low or too high or give an error. (fixed)
  - When a player enters not a number (a symbol) it says "This is not a number" but it still counts it as attemps. It should not count it as attempt. (fixed)
---------------------------------------------------------------------------------------
------

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  - I used built in VS code Copilot
------------------------
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  - AI correctly refactored logic, moving the functions (check_guess,get_range_for_difficulty, parse_guess, and update_score) from app.py into logic_utils.py. by deleting repetitive functions from app.py. It also fixed bugs that were in this functions but first i went through it to verify if it is correct. One example that it correctly identified why the number that player entered was not matching with secret number, even when the numbers were the same. The problem was that on even attempts the code changed secret number to string.
---------------
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  - When I was generating a pytest for the bug where the number was converted into string, Copilot incorrectly included into the pytest the number of attempts, but in the function that was being checked in pytest didn't use attemps as a variable. I pointed that out to Copilot and it took me some tries and in the end Copilot generated a pytest where he still used attemps but it is unused variable (_attempts), just so I can see how the game should have worked. I just went into the game itself and checked manually if on even attempts the secret number wasn't converted into string.
--------------------

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  - I generated and ran the pytest for all possible cases for the bug I was trying to fix (including edge cases) and then I went to the game and manually checked if the targeted bug was fixed. Sometimes, when the bug was in UI (for exaple the range for guessing number was wrong) I manually fixed it and checked in the game itself, without using pytest.
----------------
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  - I asked Copilot to generate pytest for update_score to see if it worked coorectly (specifically fix the problem where if you guessed too high and it was an even number, the score would add 5 points). Claude generated the pytest, I reviewed if it was correct and accepted the changes, then I ran the pytest for different scenarios and all the tests have been passed. Then I manually checked the fied bug in the web app to ensure it works correctly.
-----------------------------
- Did AI help you design or understand any tests? How?

  - AI helped me uderstand why the secret number (target number) was sometimes wrong even though the number that I entered was correct. On every even numbered attemps the secret number is cast to a string before it is passed to check_guess function. This means that on every even attemps the guess would be false, even if the number player guessed was correct, and if player guess (on even attemps) is bigger than secret number, it would raise a typeerror.

---------------------
 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - The number kept changing when player guessed on even attempts. On even attemps, the secret number is converted to string, so the game compared player's number (int) and secret number (str). And python compares strings alphabetically, so if the guess is 5 (int) and secret number is "5" (string) it would give either "Too Low" or "Too High", even though the player guess is correct.
---------------------------------
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Streamlit is used for building web apps without using HTML, CSS, or javascript. In the ususal python code, your program executes and stops, but if you are using streamlit, you can keep your website running in loop, which waits for user input, and remembers things between inputs. Every time something happens (like you press a button, or change slider) the entire code runs again from the beginning. So for example in this guessing game, if you run the app, there is an empty box to enter value. If the player enters number and presses enter, the entire script runs again from line 1. It;s like for every click you make, everything is rebuilt from the beginning, but with ine small change each time.
-------------------------
- What change did you make that finally gave the game a stable secret number?
  - The secret number kept changing to string if you guessed in an even attmept. There was a line when it would convert it on an even attmepts, so I cempletely deleted that line. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    - I found out about pytest and I think it is very useful if you fixed one problem and want to check specifically the bug that you fixed, focusing only on it. A good habit I found very useful is that I first run pytest, and then verify the bug manually in the web app.
- What is one thing you would do differently next time you work with AI on a coding task?
  - I used to ask broad questions, like "find all the bugs in this code", but when i did it, AI didn't give me all the errors. Now I firt look through the code and web app myself, and then target the issues I found and ask AI to explain them to me.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - AI is definetely a powerful tool, but it doesn't know or account everything. You need to check each promp and AI resopnse carefully. Now I think of AI not as a "coworker", but as a tool, which I have to learn how to use in order to mkae it as efficient as possible. 
