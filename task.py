# Write a function that receives two sequences: A and B of integers and returns one sequence C.
# Sequence C should contain all elements from sequence A (maintaining the order) except those,
# that are present in sequence B p times, where p is a prime number.

A = [2, 3, 9, 2, 5, 1, 3, 7, 10]

B = [2, 1, 3, 4, 3, 10, 6, 6, 1, 7, 10, 10, 10]

C = [2, 9, 2, 5, 7, 10]


def get_primes(max_num):
    primes = []
    for i in range(2, max_num+1):
        is_num_prime = True
        for prime in primes:
            if i % prime == 0:
                is_num_prime = False
                break
        if is_num_prime:
            primes.append(i)
    return primes


def expose_specific_elements(list1, list2):
    primes = get_primes(len(list2))
    new_list = []
    for number in list1:
        if number in list2:
            quantity = list2.count(number)
            if quantity in primes:
                continue
        new_list.append(number)

    return new_list


print(expose_specific_elements(A, B))
