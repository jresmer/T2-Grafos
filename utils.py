def nextl(l : list):

    l.pop(0)

def split_st(s : str) -> (str, str):

    for i in range(len(s)):

        if s[i] == " ":
            return s[:i], s[i+1:]
        
def split_nd(s : str) -> [str, str, str]:

    r = []
    i, j, counter = -1, 0, 0

    while counter < 2:
        i += 1

        if s[i] == " ":
            r.append(s[j:i])
            j = i
            counter += 1

    r.append(s[i:])

    return r
