# Recursive
def appendAtFront(x, L):
    return [x + element for element in L]

def bitBinary(n):
    if n == 0:
        return []
    
    if n == 1:
        return ["0", "1"]
    
    return (appendAtFront("0", bitBinary(n-1))) + (appendAtFront("1", bitBinary(n-1)))

# Iterative
# def bitBinary(n):
#     if n == 0: return []
#     if n == 1: return ["0", "1"]

#     return [digit + bitstring for digit in bitBinary(1) for bitstring in bitBinary(n-1)]

print(bitBinary(5))
