# https://www.codewars.com/kata/5262119038c0985a5b00029f

def is_prime(n):
    if n <= 1 or n % n**0.5 == 0 : return False
    i = 2
    while (i < n**0.5):
        if n % i == 0: return False
        i += 1
    return True
