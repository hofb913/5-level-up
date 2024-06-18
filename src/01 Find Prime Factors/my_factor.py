def get_prime_factors(n):
    factors =[]
    tstF = 2

    while tstF <= n:
        if n % tstF == 0:
            factors.append(tstF)
            n = n // tstF
        else:
            tstF += 1
    
    return(factors)

print(f'Prime factors for 630: {get_prime_factors(630)}')
print(f'Prime factors for 13: {get_prime_factors(13)}')
