def uv_div(p):
    # base case
    if not p:
        return ''
    # 카운팅
    open = 0
    close = 0
    for i in range(len(p)):
        if p[i] == '(':
            open += 1
        elif p[i] == ')':
            close += 1
        # uv 나누기
        if open == close:
            u = p[:i+1]
            v = p[i+1:]
            # u가 올바른 괄호 문자열이 아닐 때
            if u[0] == ')' or u[-1] == '(':
                u = u[1:-1]
                u2 = ''
                for j in u:
                    if j == '(':
                        u2 += ')'
                    elif j == ')':
                        u2 += '('
                return '(' + uv_div(v) + ')' + u2
            # u가 올바른 괄호 문자열일 때
            if len(v) != 0:
                return u + uv_div(v)
            else:
                return u

p = input()
print(uv_div(p))