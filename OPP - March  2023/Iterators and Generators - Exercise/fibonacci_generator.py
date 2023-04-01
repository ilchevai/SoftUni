def fibonacci():
    first_num = 0
    second_num = 1
    i = 0

    while True:
        if i <= 1:
            next_num = i
        else:
            next_num = first_num + second_num
            first_num = second_num
            second_num = next_num

        yield next_num
        i = i + 1


generator = fibonacci()
for i in range(5):
    print(next(generator))