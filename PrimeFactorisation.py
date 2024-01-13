compositeNumber = 12163892746


def findPrimeFactors(prime_number):
    flag = True
    divisor = 2
    factors =[]
    while flag:
        if prime_number % divisor == 0:
            prime_number /=divisor
            factors.append(divisor)
        if prime_number == 1:
            flag = False
        if prime_number % divisor !=0:
            divisor +=1 
    return factors
    
algorithm = findPrimeFactors(compositeNumber)
print(algorithm)
