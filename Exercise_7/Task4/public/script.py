#!/usr/bin/env python3

def evolve(world, steps):
    # raise Errors for wrong inputs
    if type(world) != tuple or type(steps) != int:
        raise Warning("The input-type is wrong!")

    if world == ():
        raise Warning("The world is empty!")

    if steps < 1:
        raise Warning("The steps needs to be a positive integer!")

    for l in world:
        if type(l) != str:
            raise Warning("A line in the input-world is not a string!")

    for l in world[0]:
        if l != "-":
            raise Warning("Your first line doesn't consist only of - !")

    if not any("-" in l for l in world):
        raise Warning("The world-input is invalid!")

    if not any("|" in l for l in world):
        raise Warning("The world-input is invalid!")

    for l in world[-1]:
        if l != "-":
            raise Warning("Your last line doesn't consist only of - !")

    len_world = len(world[0])
    if len_world <= 2:
        raise Warning("The input-world needs to be at least 2 characters long!")
    for l in world[1:]:
        if len(l) != len_world:
            raise Warning("The lines in the input-world don't have the same length!")

    for l in world[1:-1]:
        if l[0] != "|" or l[-1] != "|":
            raise Warning("Every line in the input-world needs to start and end with a | !")

    count = 0
    copy = world

    for line_count, line in enumerate(copy[1:-1]):

        for index, c in enumerate(line[1:-1]):

            if not (c == " " or c == "#"):
                raise Warning("Every column needs to start or end with a - !")

            count = 0
            count += world[line_count].count("#", index, index + 3)
            count += (world[line_count + 1][index] + world[line_count + 1][index + 2]).count("#")
            count += world[line_count + 2].count("#", index, index + 3)

            if c == "#":
                if count <= 1:
                    line = "".join(line[:index + 1] + " " + line[index + 2:])
                if count >= 4:
                    line = "".join(line[:index + 1] + " " + line[index + 2:])
            if c == " " and count == 3:
                line = "".join(line[:index + 1] + "#" + line[index + 2:])

        y = list(copy)
        y[line_count + 1] = line
        copy = tuple(y)

    if steps != 1:
        steps -= 1
        copy = evolve(copy, steps)[0]

    for l in copy:
        count += l.count("#")

    return copy, count


field = (
    "--------------",
    "|            |",
    "|   ###      |",
    "|   #        |",
    "|    #       |",
    "|            |",
    "--------------"
)
steps = 4

result, alive_cells = evolve(field, steps)

#print(f"Game of Life after {steps} moves:")
#for row in result:
#    print(row)
#print(f"{alive_cells} are alive.")