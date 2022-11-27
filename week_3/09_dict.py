class Dict:
    def __init__(self) :
        self.items = [None] * 8

    def put(self, key, value) :

        hash_num = hash(key)
        idx = hash_num % len(self.items)
        self.items[idx] = value

        return

    def get(self, key):

        hash_num = hash(key)
        idx = hash_num % len(self.items)

        return self.items[idx]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))
