S = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>'
def write16(val):
    string = ''
    places = []
    while val >= 1:
        leftover = val % 16
        val >>= 4
        string = S[leftover] + string
    return string
def write64(val):
    string = ''
    places = []
    while val >= 1:
        leftover = val % 64
        val >>= 6
        string = S[leftover] + string
    return string