from typing import Dict

class dictionary_iter:
    def __init__(self, dictionary: Dict):
        self.dictionary = list(dictionary.items())
        self.iterator = -1
    def __iter__(self):
        return self

    def __next__(self):
        if self.iterator == len(self.dictionary) - 1:
            raise StopIteration

        self.iterator += 1

        return self.dictionary[self.iterator]

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)