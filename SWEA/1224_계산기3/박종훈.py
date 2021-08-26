import sys
sys.stdin = open('input.txt')


def icp(x):
    if x == '*' or x == '/':
        return 2
    elif x == '+' or x == '-':
        return 1
    elif x == '(':
        return 3


def isp(x):
    if x == '*' or x == '/':
        return 2
    elif x == '+' or x == '-':
        return 1
    elif x == '(':
        return 0


T = 10

for tc in range(1, T+1):
    N = int(input())
    sik = input()
    stack = []
    postfix = []
    operator = ('+', '-', '*', '/', '(', ')')

    # 중위 표기법 -> 후위 표기법
    for x in sik:
        if x not in operator:  # 피연산자일 때
            postfix.append(int(x))
        else:  # 연산자일 때
            if x == ')':  # 닫는 괄호인 경우 특별 취급
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()  # '(' 없애기
            else:
                if not stack:
                    stack.append(x)
                else:
                    if icp(x) < isp(stack[-1]):  # 우선순위 낮으면
                        while stack and icp(x) <= isp(stack[-1]):  # stack에서 빼내기
                            postfix.append(stack.pop())
                        stack.append(x)  # 다 빼고 넣기
                    elif icp(x) >= isp(stack[-1]):  # 우선순위 같거나 높으면
                        stack.append(x)  # stack에 넣기

    # 후위 표기법 -> 계산
    for y in postfix:
        if y not in operator:
            stack.append(y)
        else:
            b = stack.pop()
            a = stack.pop()
            if y == '+':
                stack.append(a + b)
            elif y == '-':
                stack.append(a - b)
            elif y == '*':
                stack.append(a * b)
            elif y == '/':
                stack.append(a // b)
    else:
        result = stack.pop()

    print(f'#{tc} {result}')
