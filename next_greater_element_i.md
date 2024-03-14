## 150. Next Greater Element I

### Brute Force

    Basically use two for loops and keep checking if its greater than it or not and thats pretty much it.    

```python
def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    result = [-1] * len(nums1)

    for i in range(len(nums1)):
        start = nums2.index(nums1[i])
        for j in range(start, len(nums2)):
            if nums1[i] < nums2[j]:
                result[i] = nums2[j]
                break
    return result
```

### How to solve - Monotonic Stack

Okay but the actual way to solve it is basically,

- You traverse the second array in reverse and keep the stack on the
  side to help you.
    - You look at the last element and then you go does the stack have an element greater than this, if it
      does then you add that to the next_greater_list dictionary.
    - If not, then keep popping the stack
    - Also, append the stack at the bottom.

- Now, you should have a dictionary that basically gives you all the greater elements, check that and you should be good
  to go
