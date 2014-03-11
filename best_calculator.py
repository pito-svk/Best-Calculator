def best_calculator(numerator, denumerator, n=10):
    assert n > 0
    result = ""
    minus = ""
    if (numerator < 0  and denumerator > 0) or (numerator > 0 and denumerator < 0):
        minus += "-"
    if numerator == 0:
        return 0
    numerator = abs(numerator)
    denumerator = abs(denumerator)
    while True:
        if numerator >= denumerator:
            value = numerator / denumerator
            result += str(value)
            numerator -= (value*denumerator)
            if numerator == 0:
                return  minus +result
            elif "." not in result:
                result += "."
            increase = False
        else:
            if "." not in result:
                result += "0."
            elif increase:
                result += "0"
            numerator *= 10
            increase = True
        if len(result[result.index("."):]) == n+1:
            return minus + result

