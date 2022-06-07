def calculator(expression):
    allowed_sign = '+-/*'
    if not any(sign in expression for sign in allowed_sign):
        raise ValueError(f'Expression should be contain some one sign {allowed_sign}')
    for sign in allowed_sign:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)  # if not int value can be TypeError
                if sign == '+':
                    return left + right
                elif sign == '-':
                    return left - right
                elif sign == '*':
                    return left * right
                elif sign == '/':
                    return left / right
            except (ValueError, TypeError):
                raise ValueError('Expression should be contain 2 int numbers and one sign')


if __name__ == '__main__':
    print(calculator('2+3'))
