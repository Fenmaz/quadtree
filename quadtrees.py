class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


class Box:
    def __init__(self, center, half_x, half_y):
        if type(center) != Point:
            raise TypeError("center variable must be type Point")
        self.center = center
        self.half_x = half_x
        self.half_y = half_y

    def contains(self, point):
        if type(point) != Point:
            raise TypeError("point variable must be type Point")
        if abs(point.x - self.center.x) <= self.half_x and abs(point.y - self.center.y) <= self.half_y:
            return True
        return False

    def intersects(self, another):
        if self.center.x + self.half_x < another.center.x - another.half_x or another.center.x + another.half_x \
                < self.center.x - self.half_x:
            return False
        if self.center.y + self.half_y < another.center.y - another.half_y or another.center.y + another.half_y \
                < self.center.y - self.half_y:
            return False
        return True

    def get_corners(self):
        top_left = (self.center.x - self.half_x, self.center.y - self.half_y)
        bottom_right = (self.center.x + self.half_x, self.center.y + self.half_y)
        return top_left, bottom_right

    def get_all_corners(self):
        (x1, y1), (x2, y2) = self.get_corners()
        return (x1, y1), (x1, y2), (x2, y2), (x2, y1)

    def __str__(self):
        return "Top left: {0} | Bottom right: {1}".format(*self.get_corners())


class QuadTrees:
    def __init__(self, box):
        if type(box) != Box:
            raise TypeError("box variable must be type Box")
        self.box = box

        self.point = None

        self.nw = None
        self.ne = None
        self.sw = None
        self.se = None

    def has_point(self):
        if self.point is None:
            return False
        return True

    def subdivide(self):
        quarter_x = self.box.half_x / 2
        quarter_y = self.box.half_y / 2
        x = self.box.center.x
        y = self.box.center.y

        nw_center = Point(x - quarter_x, y - quarter_y)
        nw_box = Box(nw_center, quarter_x, quarter_y)
        self.nw = QuadTrees(nw_box)

        ne_center = Point(x + quarter_x, y - quarter_y)
        ne_box = Box(ne_center, quarter_x, quarter_y)
        self.ne = QuadTrees(ne_box)

        sw_center = Point(x - quarter_x, y + quarter_y)
        sw_box = Box(sw_center, quarter_x, quarter_y)
        self.sw = QuadTrees(sw_box)

        se_center = Point(x + quarter_x, y + quarter_y)
        se_box = Box(se_center, quarter_x, quarter_y)
        self.se = QuadTrees(se_box)

    def insert(self, point):
        if type(point) != Point:
            raise TypeError("point variable must be type Point")

        if not self.box.contains(point):
            return False

        if not self.has_point():
            self.point = point
            return True

        if self.nw is None:
            self.subdivide()

        for tree in (self.nw, self.ne, self.sw, self.se):
            if tree.insert(point):
                return True

        return False

    def find_point(self, point):
        if self.point == point:
            return True
        if self.nw is None:
            return False
        return self.nw.find_points(point) or self.ne.find_points(point) \
            or self.sw.find_points(point) or self.se.find_points(point)

    def query_box(self, box):
        results = []

        if not self.box.intersects(box):
            return results

        if self.has_point() and box.contains(self.point):
            results.append(self.point)

        if self.nw is None:
            return results

        results += self.nw.query_box(box)
        results += self.ne.query_box(box)
        results += self.sw.query_box(box)
        results += self.se.query_box(box)

        return results

    def get_children(self):
        if self.nw is None:
            return []
        return [self.nw, self.ne, self.sw, self.se]

    def get_box(self):
        return self.box

    def __str__(self):
        base = "{0} | Point: {1}".format(self.box, self.point)
        if self.nw is None:
            return base
        return base + "\n{0} \n{1} \n{2} \n{3}".format(self.nw, self.ne, self.sw, self.se)
