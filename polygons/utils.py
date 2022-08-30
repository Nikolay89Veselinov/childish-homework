import math


def if_right(x1, y1, x2, y2, x3, y3):
    a = ((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2))
    b = ((x1 - x3) * (x1 - x3)) + ((y1 - y3) * (y1 - y3))
    c = ((x2 - x3) * (x2 - x3)) + ((y2 - y3) * (y2 - y3))

    if ((a == (b + c) and a != 0 and b != 0 and c != 0) or
        (b == (a + c) and a != 0 and b != 0 and c != 0) or
        (c == (a + b) and a != 0 and b != 0 and c != 0)):
        return True
    return False


def is_equilateral(x1, y1, x2, y2, x3, y3):
    a = ((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1))
    b = ((x3 - x2) * (x3 - x2)) + ((y3 - y2) * (y3 - y2))
    c = ((x3 - x1) * (x3 - x1)) + ((y3 - y1) * (y3 - y1))

    if a == b and b == c and c == a:
        return True
    return False


def get_triangle_id(query, func):
    triangles_id = []

    for x in query:
        obj = func(
            x.vertices.values()[0]['x'], x.vertices.values()[0]['y'],
            x.vertices.values()[1]['x'], x.vertices.values()[1]['y'], x.vertices.values()[2]['x'],
            x.vertices.values()[2]['y']
        )
        if not obj:
            triangles_id.append(x.id)

    return triangles_id


def distance2D(xA,yA,xB,yB):
    return math.sqrt((xA-xB)*(xA-xB)+(yA-yB)*(yA-yB))