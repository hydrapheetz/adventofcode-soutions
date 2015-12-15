import hashlib
problem_input = "ckczppom"

def mine(inp):
    return hashlib.md5(inp.encode("utf-8")).hexdigest()

start = 1
while True:
    h = mine(problem_input + str(start))
    if (h.startswith("000000")):
        print(start)
        break
    else:
        start = start + 1
