def best_calculator(numerator, denumerator, n):
    result = ""
    assert n > 0
    while True:
        if numerator > denumerator:
            value = numerator / denumerator
            result += str(value)
            numerator -= (value*denumerator)
            if numerator == 0:
                return float(result)
            elif "." not in result:
                result += "."
            if len(result[result.index("."):]) == n+1:
                return float(result)
            increase = False
        else:
            if "." not in result:
                result += "0."
            elif increase:
                result += "0"
            numerator *= 10
            increase = True
            if len(result[result.index("."):]) == n+1:
                return float(result)

        