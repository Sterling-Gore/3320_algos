D = ["dog", "sled", "bed"]
s= "dogsled"

def in_d(stri):
    if stri in D:
        return True
    return False

cache = {}
cache[0] = True
def CBF(i):
    if i not in cache:
        cache[i] = any(CBF(k) and in_d(s[k:i]) for k in range(i))
        # for k in range(i):
        #     if CBF(k) and in_d(s[k:i]) == True:
        #         cache[i] = True
    return cache[i]

print(CBF(len(s)))
