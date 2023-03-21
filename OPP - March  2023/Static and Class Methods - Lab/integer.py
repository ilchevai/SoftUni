from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(int(float_value))

        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        roman_numb = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        int_numb = 0

        for i in range(len(value)):
            if roman_numb[value[i]] > roman_numb[value[i - 1]]:
                int_numb += roman_numb[value[i]] - 2 * roman_numb[value[i - 1]]
            else:
                int_numb += roman_numb[value[i]]

        return cls(int_numb)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            return cls(int(value))

        return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))




