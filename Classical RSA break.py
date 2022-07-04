import math
import time


def factor_finding(num):
    first_factor = 1
    print("The two prime factors of " + str(num) + " are:")
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            first_factor = i
            break

    print(str(first_factor) + " and " + str(int(num / first_factor)))
    return [first_factor, int(num / first_factor)]


def factor_finding_timer(num):
    start_time = time.time()
    factor_finding(num)
    end_time = time.time()
    total_time = round(end_time - start_time, 3)
    print("Execution time: " + str(total_time) + " seconds")


def rsa_key_break(e, n):
    factors = factor_finding(n)
    p = factors[0]
    q = factors[1]
    d = pow(e, -1, (p-1)*(q-1))
    print(f"The public key ({e},{n}) requires the private key to be ({d},{n})")


rsa_key_break(3, 55)
factor_finding_timer(55)

