v = int(input())
p_1 = int(input())
p_2 = int(input())
h = float(input())
debit_from_pipe = (p_1 + p_2) * h

if debit_from_pipe <= v:
    pool =  debit_from_pipe * 100 / v
    pipe_1 = (p_1 * h) * 100 / debit_from_pipe
    pipe_2 = (p_2 * h) * 100 / debit_from_pipe
    print(f"The pool is {pool}% full. Pipe 1: {pipe_1:.2f}%. Pipe 2: {pipe_2:.2f}%.")
else:
    over_liters = abs(v - debit_from_pipe)
    print(f"For {h} hours the pool overflows with {over_liters} liters.")

