S = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>'
def int2hex(val):
    string = ''
    places = []
    while val >= 1:
        leftover = val - (val // 16 * 16)
        val //= 16
        string = S[leftover] + string
    return string
def int2b64(val):
    string = ''
    places = []
    while val >= 1:
        leftover = val - (val // 64 * 64)
        val //= 64
        string = S[leftover] + string
    return string
def 