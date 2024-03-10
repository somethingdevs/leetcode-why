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