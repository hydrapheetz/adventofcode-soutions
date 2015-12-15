problem_input = open("input_2.txt", "r").readlines()
def paper_order():
    for present in problem_input:
        (w, l, h) = map(int, present.split("x"))
        yield sum([2*l*w, 2*w*h, 2*h*l, min([l*w, w*h, h*l])])

def ribbon_order():
    for present in problem_input:
        (w, l, h) = map(int, present.split("x"))
        biggest_sides = sorted((w,l,h))[:2]
        yield sum([biggest_sides[0]+biggest_sides[0]+biggest_sides[1]+biggest_sides[1], w*l*h])

print(sum((i for i in paper_order())))
print(sum((i for i in ribbon_order())))
