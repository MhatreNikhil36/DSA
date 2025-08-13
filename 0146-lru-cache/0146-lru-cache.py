class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {}
        self.stack = []
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.lru:
            # Move the accessed key to the top of the stack
            self.stack.remove(key)
            self.stack.append(key)
            return self.lru[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            # Update existing key's value and move it to the top of the stack
            self.lru[key] = (value, len(self.stack))
            self.stack.remove(key)
            self.stack.append(key)
        else:
            # Add new key-value pair
            if len(self.stack) >= self.cap:
                # Remove the least recently used key from the stack and dictionary
                lru_key = self.stack.pop(0)
                del self.lru[lru_key]
            # Add the new key to the top of the stack and dictionary
            self.lru[key] = (value, len(self.stack))
            self.stack.append(key)
