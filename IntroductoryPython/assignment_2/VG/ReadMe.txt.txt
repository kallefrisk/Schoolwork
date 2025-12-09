8. Count Digits
    - Input number
    - Check if number is positive
    - Set counter variables
    - Convert number into string
    - Iterate through every character in string
        * Convert iterated character to integer
        * Check if zero, odd or even and add to corresponding counter
    - Print results

9. Birthday Candles
    - Create a for-loop for computing the amount of missing candles
    - Create another for-loop inside (box-loop) to compute the amount of boxes to buy
    - Make use of variables that add +1 if a condition is met
    - The box-variable is a temporary variable and is reset after every box-loop
    - Print results

13. ABCD
    - Create four for-loops each incrementing sub-integer (a, b, c, d). (A four digit counter)
    - if any sub-integer reaches 10, reset it to 0.
    - Create function for combining four integers into one integer
    - Create funktion for reversing input integer
    - Skip the first iteration. (All zeroes 0000)
    - In the last loop check if abcd*4 = dcba; if true then print result and break

14. Calculating Pi
    - Create a function that approximates π
        - Function creates a random point inside a 1*1 square
        - If said point is inside a quartercircle with radius 1 inside the square:
            * add 1 to inside
        - Then calculate the approximate π value by:
            * Dividing inside with total number of points
            * Multiplying the inside/total ratio with 4
    - Use the function to assign values to pi100, pi10000 and pi1000000
    - Print the results with the amount that the approximation was off

20. Salary revision
    - Input the salaries in one string and split the string at every whitespace
    - Create a new list by converting all the entries in the former list into integers
    - Create a function to calculate the median of the salaries
        * Returns the middle index after sorting or the average of two middle entries if amount of entries is even
    - Create a function to calculate the average of all salaries
        * Returns the sum of all salaries divifed by the amount of entries in the list
    - Create a function to calculate the gap between min and max wage
        * Use methods min and max to get the lowest and highest salary and returns the difference between min and max
    - Print the results

21. Drunken sailor
    - Create a for-loop that iterates for every sailor
        - Create another for-loop that iterates for every step
            * Generate a random number that spans four values
            * Each value represents a step in one of four direction; up, down, left, right
            * For each step in a certain direction add 1 to the counter
            * Check if the sailor is overboard by subtracting the opposite direction
              and if step is within the range of -(raft size) to (raft size)
            * If sailor is overboard; add to overboard and break the loop, otherwise continue
        - After every step loop; reset the step counters
    - Create a function to calculate the ratio of overboard sailors
    - Print results
