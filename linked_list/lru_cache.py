class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.order = []

    def get(self, key: int) -> int:
        if key in self.hash_map:
            self.order.remove(key)
            self.order.append(key)
            return self.hash_map[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.hash_map[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.hash_map) >= self.capacity:
                lru_key = self.order.pop(0)
                del self.hash_map[lru_key]
            self.hash_map[key] = value
            self.order.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Example driver code:
if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)  # Cache is {1=1}
    lRUCache.put(2, 2)  # Cache is {1=1, 2=2}
    print(lRUCache.get(1))  # Returns 1
    lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, Cache is {1=1, 3=3}
    print(lRUCache.get(2))  # Returns -1 (not found)
    lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, Cache is {4=4, 3=3}
    print(lRUCache.get(1))  # Returns -1 (not found)
    print(lRUCache.get(3))  # Returns 3
    print(lRUCache.get(4))  # Returns 4
