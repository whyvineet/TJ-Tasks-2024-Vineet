# TJ Tasks 2024

## Question 1

This program generates Pascal's Triangle for a given number of rows (`n`).

- **Approach**:
- For each row `i`, print the appropriate number of spaces for alignment.
- For each position in the row, compute the binomial coefficient using the formula: **value = i! // j! * (i-j)!**
- The factorial is computed using a recursive helper function `factorial()`.

---

## Question 2

This function calculates how many distinct ways there are to climb `n` stairs, given that you can climb either 1 or 2 steps at a time.

- **Approach**:
- The approach calculates the number of ways to reach the nth stair by counting the maximum possible 2-steps (i.e., [𝑛/2]) and adding 1 for the case where all steps are 1-steps, as the order of steps doesn't matter. (Note: Here [] represnts the base value of n/2 or we can simply say n//2)

---

## Question 3

This function computes the bitwise AND of all integers between two numbers (`left` and `right`).

- **Approach**:
- The key observation is that the bitwise AND of a range results in a number that shares the common prefix bits between `left` and `right`.
- We right-shift both `left` and `right` until they are equal, keeping track of how many shifts were made.
- Finally, the result is obtained by shifting the common prefix back to the left by the same number of shifts.

---

## Question 4

This function compresses a list of characters by replacing consecutive groups of the same character with the character followed by the group's length.

- **Approach**:
- Traverse the input array and count the consecutive occurrences of each character.
- For groups of more than one character, append the character followed by its count to the array.
- The input array is modified in place, and the function returns the new length of the compressed array.

---

## Question 5



---

## Question 6