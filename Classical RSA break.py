# A simple script which returns the privat RSA key if given a valid public key. A classical brute force method is used to find the factors of N
import math
import time


# A function which calculates the factors of the number "num"
def factor_finding(num):
    first_factor = 1
    print("The two prime factors of " + str(num) + " are:")
    # Check for every number smaller then "num" if it is a factor
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            first_factor = i
            # Since only one factor needs to be found, the other numbers can be skiped
            break
    # Print both factors and return them as a list
    print(str(first_factor) + " and " + str(int(num / first_factor)))
    return [first_factor, int(num / first_factor)]


# A function which times the call of factor_finding for a number "num"
# This function was only used to compare the runtime of the brute force method to Shor's algorithm
def factor_finding_timer(num):
    # Create a timestamp as the start time
    start_time = time.time()
    # Call the function factor_finding for "num"
    factor_finding(num)
    # Create a timestamp as the end time and calculate the diffrence to the start time
    end_time = time.time()
    total_time = round(end_time - start_time, 3)
    # Print the total time needed
    print("Execution time: " + str(total_time) + " seconds")


# A function which takes a public RSA key and returns the corresponding private key
def rsa_key_break(e, n):
    # Find the factors of n by using the function factor_finding
    factors = factor_finding(n)
    p = factors[0]
    q = factors[1]
    # Calculate d of the private key by using all information gathered
    d = pow(e, -1, (p-1)*(q-1))
    # Print the public and private key pair
    print(f"The public key ({e},{n}) requires the private key to be ({d},{n})")

# Calls the function above to calculate the corresponding private key to the public key (3, 55)
rsa_key_break(3, 55)
# Measure the time it takes to find both factors of 55 when using the brute force method
factor_finding_timer(55)
