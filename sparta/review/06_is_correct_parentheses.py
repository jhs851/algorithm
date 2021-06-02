# 문제링크 https://www.notion.so/5-f51f57c84aef4626b580a5937adabca9#b9d162f860734c48aad924aed7ec71fb

from collections import deque

balanced_parentheses_string = "()))((()"


def get_correct_parentheses(balanced_parentheses_string):
    return


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))
