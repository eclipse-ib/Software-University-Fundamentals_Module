class Storage:
    storage = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product):
        if len(Storage.storage) < self.capacity:
            Storage.storage.append(product)
        else:
            pass

    def get_products(self):
        return Storage.storage

capacity = int(input())

test_storage = Storage(capacity)

# for i in range(capacity):
#     command = input()
#     product = command
#     test_storage.add_product(product)
#
#
# print(test_storage.get_products())


