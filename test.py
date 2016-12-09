from quadtrees import QuadTrees, Point, Box

center = Point(10, 10)
box = Box(center, 10, 10)
tree = QuadTrees(box)
for i in range(10):
    tree.insert(Point(i, i))
print(tree)
