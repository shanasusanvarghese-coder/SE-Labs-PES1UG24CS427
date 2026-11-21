# Implementation Notes

### 1. Numeric rank comparison
Each card has a numeric rank from 2 to 14 (Jack=11, Queen=12, King=13, Ace=14). The game compares these numbers, avoiding incorrect alphabetical/string comparisons.

### 2. Consecutive-win streak
A correct guess increments the streak and awards points equal to the new streak count. An incorrect guess resets the streak and subtracts one point, without allowing the score to fall below zero.

### 3. Tie handling
When the drawn card has the same numeric rank as the previous card, the result is PUSH. Neither score nor streak changes.

### 4. Side-by-side reveal
After each guess, the previous and new cards are shown together for 900 milliseconds. Further guesses are ignored during this reveal.
