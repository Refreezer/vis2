from math import *
from StateTable import StateTable


class CustomTrianglesProvider:
    triangles = []


isonumber = 0.1


def calctriangles():
    def f(x, y, z):
        # return x**2/10 + y**2/8 + z**2/7
        # return (x ** 2 + y ** 3 * sin(z / 10)) / 30
        return cos(y) + exp(x)

    start, h, end = StateTable.start, StateTable.h, StateTable.end

    n = int((end - start) / h)
    print(n)

    x = start
    cubes = []
    for i in range(n):
        y = start
        for j in range(n):
            z = start
            for k in range(n):
                cube = []
                for sign1 in range(0, 2, 1):
                    for sign2 in range(0, 2, 1):
                        r = range(0, 2, 1)

                        if sign2 % 2:
                            r = range(1, -1, -1)

                        for sign3 in r:
                            cube.append((round(x + h * sign1, 2), round(y + h * sign2, 2), round(z + h * sign3, 2)))

                cubes.append(cube)
                z += h
            y += h
        x += h

    print(len(cubes))
    grid_values = dict()

    for cube in cubes:
        for i in range(len(cube)):
            grid_values[(cube[i][0], cube[i][1], cube[i][2])] = f(cube[i][0], cube[i][1], cube[i][2])

    table = StateTable.UsedTriangleVertex()

    for j in range(len(cubes)):
        vs = [grid_values[vx] for vx in cubes[j]]

        cubeindex = 0

        i = 0
        for value in vs:
            if value > isonumber:
                cubeindex |= 2 ** i

            i += 1

        if StateTable.Edges()[cubeindex] == 0:
            continue

        vertlist = [0] * 12
        for i in range(12):
            if StateTable.Edges()[cubeindex] & (2 ** i):
                id1, id2 = StateTable.VertexMapping(i)
                vertlist[i] = StateTable.LinearInterp(isonumber, cubes[j][id1], cubes[j][id2], vs[id1],
                                                      vs[id2])

        i = 0
        while table[cubeindex][i] != -1:
            CustomTrianglesProvider.triangles.append((vertlist[table[cubeindex][i]], vertlist[table[cubeindex][i + 1]],
                                                      vertlist[table[cubeindex][i + 2]]))

            i += 3

