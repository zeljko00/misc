def plusOne(digits):
    pos = len(digits) - 1
    inc = int((1 + digits[pos]) / 10)
    digits[pos] = (1 + digits[pos]) % 10
    pos -= 1
    while inc > 0 and pos >= 0:
        temp=inc
        inc = int((inc + digits[pos]) / 10)
        digits[pos] = (temp + digits[pos]) % 10
        pos -= 1
    if pos < 0 and inc > 0:
        return [inc] + digits
    else:
        return digits

plusOne([8,9,9,9])