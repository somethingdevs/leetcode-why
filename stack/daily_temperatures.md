## 739. Daily Temperatures

### Brute Force

```python
def daily_temperatures(temps):
    result = [0] * len(temps)
    for i in range(len(temps)):
        for j in range(i, len(temps)):
            if temps[j] > temps[i]:
                result[i] = j - i
                break
    return result
```

### Main idea - Monotonic Stack

### How to solve this?

A more efficient way to solve this problem is to use a stack. The idea is to traverse the list of temperatures once and
use the stack to keep track of temperatures that have not yet found a warmer day. Here’s a brief overview of how you can
implement this method:

1. **Initialize**: Create an empty stack that will store indices of the temperature list, and an output array
   initialized with zeros (since some days might not have a warmer temperature following them).

2. **Iterate Over Temperatures**: Go through each temperature in the list:
    - While the stack is not empty and the current temperature is greater than the temperature at the index at the top
      of the stack:
        - Pop the index from the stack. This represents a day where the current day is the next warmer day.
        - Calculate the difference between the current index and the popped index, and update the corresponding position
          in the output array with this difference.
    - Push the current index onto the stack.

3. **Output**: After processing all temperatures, the output array will contain the number of days one has to wait until
   a warmer temperature for each day.