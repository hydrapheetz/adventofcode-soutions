house_map = {}

problem_input = open("input_3.txt", "r").read()
#problem_input = "^v^v^v^v^v"

def process_map():
    global house_map
    coords = (0,0)
    for house in problem_input:
        presents = house_map.setdefault(coords, 0)
        house_map[coords] = presents+1
        if (house == "v"):
            coords = (coords[0], coords[1]+1)
            house_map.setdefault(coords, 0)
            house_map[coords] = presents+1
        elif (house == ">"):
            coords = (coords[0]+1, coords[1])
            house_map.setdefault(coords, 0)
            house_map[coords] = presents+1
        elif (house == "<"):
            coords = (coords[0]-1, coords[1])
            house_map.setdefault(coords, 0)
            house_map[coords] = presents+1
        elif (house == "^"):
            coords = (coords[0], coords[1]-1)
            house_map.setdefault(coords, 0)
            house_map[coords] = presents+1

def process_robo():
    global house_map
    coords = (0,0)
    robo_coords = (0,0)
    robo_move = False
    presents = house_map.setdefault(coords, 0)
    robo_presents = house_map.setdefault(robo_coords,0)
    house_map[coords] = presents+1
    house_map[robo_coords] = presents+1
    for house in problem_input:
        if (house == "v"):
            if (not robo_move):
                coords = (coords[0], coords[1]+1)
                house_map.setdefault(coords, 0)
                house_map[coords] = presents+1
            else:
                robo_coords = (robo_coords[0], robo_coords[1]+1)
                house_map.setdefault(robo_coords,0)
                house_map[robo_coords] = presents+1
        elif (house == ">"):
            if (not robo_move):
                coords = (coords[0]+1, coords[1])
                house_map.setdefault(coords, 0)
                house_map[coords] = presents+1
            else:
                robo_coords = (robo_coords[0]+1, robo_coords[1])
                house_map.setdefault(robo_coords, 0)
                house_map[robo_coords] = presents+1
        elif (house == "<"):
            if (not robo_move):
                coords = (coords[0]-1, coords[1])
                house_map.setdefault(coords, 0)
                house_map[coords] = presents+1
            else:
                robo_coords = (robo_coords[0]-1, robo_coords[1])
                house_map.setdefault(robo_coords, 0)
                house_map[robo_coords] = presents+1
        elif (house == "^"):
            if (not robo_move):
                coords = (coords[0], coords[1]-1)
                house_map.setdefault(coords, 0)
                house_map[coords] = presents+1
            else:
                robo_coords = (robo_coords[0], robo_coords[1]-1)
                house_map.setdefault(robo_coords, 0)
                house_map[robo_coords] = presents+1

        robo_move = (not robo_move)

process_map()
print(len(house_map.values()))
house_map = {}
# problem_input = "^v^v^v^v^v"
process_robo()
print(house_map.keys())
print(len(house_map.values()))
