
command = input()
prime = 0
no_prime = 0

while command != "stop":
    num = int(command)
    if num < 0:
        print(f"Number is negative.")
    else:
        num_is_prime = True
        for number in range(2, num):
            if num % number == 0:
                num_is_prime = False
        if num_is_prime:
            prime += num
        else:
            no_prime += num
    command = input()
print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {no_prime}")



