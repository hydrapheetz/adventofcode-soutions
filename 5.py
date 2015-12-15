import re
from collections import Counter, OrderedDict
problem_input = open("input_5.txt", "r").readlines()

class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

def niceness_test(inp):
    bad_pairs = ["ab", "cd", "pq", "xy"]
    
    if (any(map(lambda x: x in inp, bad_pairs))):
        return False

    vowel_count = 0
    for i in inp:
        if (i in ["a", "e", "i", "o", "u"]):
            vowel_count = vowel_count + 1
    
    if (vowel_count < 3):
        return False

    repeating_letters = False
    for (current, adj) in zip(inp, inp[1:]):
        if (current == adj):
            repeating_letters = True

    if (repeating_letters == False):
        return False


    return True # all other tests passed

def take(count, string):
    return string[0:count]

def niceness_2(inp):
    #pairs = [i for i in filter(lambda x: x > 1, OrderedCounter([i for i in map(lambda x: x[0]+x[1], zip(inp, inp[1:]))]).values())]
    pairs = (re.search(r'(..).*\1',inp) is not None)
    cluster = (re.search(r'(.).\1',inp) is not None)
    return (cluster and pairs)
assert niceness_test("ugknbfddgicrmopn") == True
assert niceness_test("aaa") == True
assert niceness_test("jchzalrnumimnmhp") == False
assert niceness_test("haegwjzuvuyypxyu") == False
assert niceness_test("dvszwmarrgswjxmb") == False

print(len([i for i in filter(lambda x: x == True, (niceness_test(i) for i in problem_input))]))

assert niceness_2("qjhvhtzxzqqjkmpb") == True
assert niceness_2("xxyxx") == True
assert niceness_2("uurcxstgmygtbstg") == False
assert niceness_2("ieodomkazucvgmuy") == False
print(len([i for i in filter(lambda x: x == True, (niceness_2(i) for i in problem_input))]))
