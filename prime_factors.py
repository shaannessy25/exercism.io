
# Compute the prime factors of a given natural number. A prime number is only evenly
# divisible by itself and 1. Note that 1 is not a prime number.
 
#  Start with input: 60
# Divide by first divisor 2 until remainder not equal to 0 or 1
# if it is no longer then divide by next divisor 3 until remainder = 0
# Divide by next divisor until remainder is equal to 1
# if number is odd then div
# 
# output: 2,2,3,5




def find_prime(Number):
    for i in range(2, Number + 1):
        if(Number % i == 0):
            isprime = 1
            for j in range(2, (i //2 + 1)):
                if(i % j == 0):
                    isprime = 0
                    break
                
            if (isprime == 1):
                print(" %d is a Prime Factor of a Given Number %d" %(i, Number))


def main():
    Number = Number = int(input(" Please Enter any Number: "))
    print(find_prime(Number))


if __name__ == "__main__":
    main()