class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        for i, (k, _) in enumerate(self.bucket):
            if k == key:
                self.bucket[i] = [key, value]
                return
        self.bucket.append([key, value])

    def delete(self, key):
        if not self.bucket:
            return
        
        found = False
        for i, (k, _) in enumerate(self.bucket):
            if k == key:
                self.bucket[i], self.bucket[-1] = self.bucket[-1], self.bucket[i]
                found = True
                break
        
        if found: self.bucket.pop()


class HashMap:

    def __init__(self):
        self.bucket_size = 1000
        self.buckets = [Bucket() for _ in range(self.bucket_size)]

    def _get_bucket(self, key: int):
        return self.buckets[key % self.bucket_size]

    def put(self, key: int, value: int) -> None:
        bucket = self._get_bucket(key)
        bucket.update(key, value)

    def get(self, key: int) -> int:
        bucket = self._get_bucket(key)
        return bucket.get(key)

    def remove(self, key: int) -> None:
        bucket = self._get_bucket(key)
        bucket.delete(key)