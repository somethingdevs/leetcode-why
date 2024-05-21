## 88. Merge Sorted Array

### Main idea - Two pointers

#### Bruteforce

Copying second array to empty part of the first array and then just sort

```python
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1[m:m + n] = nums2
    nums1.sort()
```

But since, its not that easy we need to do something else

### Reasoning - FIll in the first array from behind.
