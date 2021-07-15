from itertools import permutations


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def solution(numbers):
    n = len(numbers)
    answer = set()

    for i in range(1, n + 1):
        permutation_array = map(''.join, permutations(numbers, i))

        for permutation in permutation_array:
            permutation = int(permutation)

            if is_prime(permutation):
                answer.add(permutation)

    return len(answer)


print(solution("011"))
