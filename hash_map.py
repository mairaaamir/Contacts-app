from hash_node import HashNode

class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [None] * self.size

    def _hash(self, key):
        """Simple hashing function"""
        return sum(ord(c) for c in key) % self.size

    def put(self, key, value):
        """Insert or update a key-value pair"""
        index = self._hash(key)
        head = self.buckets[index]

        # Update if key exists
        current = head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next

        # Insert new node at the front
        new_node = HashNode(key, value)
        new_node.next = head
        self.buckets[index] = new_node

    def get(self, key):
        """Retrieve value by key"""
        index = self._hash(key)
        current = self.buckets[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def remove(self, key):
        """Delete a key-value pair"""
        index = self._hash(key)
        current = self.buckets[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.buckets[index] = current.next
                return True
            prev = current
            current = current.next

        return False

    def display(self):
        """Print all contacts"""
        for i, node in enumerate(self.buckets):
            current = node
            while current:
                print(f"Bucket {i}: {current.key} -> {current.value}")
                current = current.next
