

def dec_to_bin(decimal_number: int) -> str:
    if decimal_number == 0:
        return '0'
    
    _n = decimal_number
    _bin_number = ''
    while _n > 0:
        _bin_number = str(_n % 2) + _bin_number
        _n = _n // 2

    return _bin_number

def power_of_two(power: int) -> int:
    i = 0
    res = 1
    while i < power:
        res <<= 1
        i += 1
    return res

if __name__ == '__main__':
    # x = dec_to_bin(40)
    # print(x)

    print(power_of_two(2))