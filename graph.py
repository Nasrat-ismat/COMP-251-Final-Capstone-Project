class HashMap:
    def __init__(self, capacity=8):
        self.capacity = max(8, capacity)
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        hash_value = 0
        for ch in key:
            hash_value = (31 * hash_value + ord(ch)) % self.capacity
        return hash_value

    def _load_factor(self):
        return self.size / self.capacity

    def _resize(self):
        old_items = []
        for bucket in self.buckets:
            for item in bucket:
                old_items.append(item)

        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for key, value in old_items:
            self.insert(key, value)

    def insert(self, key, value):
        if self._load_factor() > 0.7:
            self._resize()

        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        for i, (old_key, _) in enumerate(bucket):
            if old_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1

    def search(self, key):
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        for old_key, value in bucket:
            if old_key == key:
                return value
        return None

    def delete(self, key):
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        for i, (old_key, value) in enumerate(bucket):
            if old_key == key:
                del bucket[i]
                self.size -= 1
                return value
        return None

    def keys(self):
        keys_list = []
        for bucket in self.buckets:
            for key, _ in bucket:
                keys_list.append(key)
        return keys_list

    def items(self):
        items_list = []
        for bucket in self.buckets:
            for item in bucket:
                items_list.append(item)
        return items_list
