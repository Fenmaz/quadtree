from quadtrees import QuadTrees, Box, Point
from PIL import Image, ImageDraw


def inp(filename):
    f = open("{}.txt".format(filename), "r")
    line = f.readline().split()
    bounds = tuple(map(int, line))

    points = []
    for line in f:
        map_int = map(int, line.split())
        points.append(Point(map_int.__next__(), map_int.__next__()))

    return bounds, points


def make_quadtree(bounds):
    half_x = bounds[0] / 2
    half_y = bounds[1] / 2
    center = Point(half_x, half_y)
    box = Box(center, half_x, half_y)
    return QuadTrees(box)


def draw_tree(filename, tree):
    im = Image.open("{}.png".format(filename))
    d = ImageDraw.Draw(im)

    def draw_box(t):
        corners = list(t.get_box().get_all_corners())
        corners.append(corners[0])
        d.line(corners, fill=(0, 0, 0), width=5)
        # print("Drawing {}".format(t.get_box()))
        for child in t.get_children():
            draw_box(child)

    draw_box(tree)
    im.save("{}Boxed.png".format(filename))


def main():
    filename = input()
    bounds, points = inp(filename)
    tree = make_quadtree(bounds)
    for point in points:
        tree.insert(point)

    output = "{}Tree.txt".format(filename)
    f = open(output, "w")
    f.write("{}".format(tree))

    draw_tree(filename, tree)

if __name__ == '__main__':
    main()
