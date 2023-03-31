class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number

    def repeat(self):
        if len(self.sequence) <= self.number:
            for char in self.sequence:
                yield char
        else:
            for _ in range(self.number):
                for char in self.sequence:
                    yield char


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')