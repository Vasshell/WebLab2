import math


class Sphere:

    def __init__(self, x=0, y=0, z=0, r=1):
        self.XCoordinate = x
        self.YCoordinate = y
        self.ZCoordinate = z
        self.Radius = r

    def get_volume(self):
        return 4 / 3 * math.pi * self.Radius ** 3

    def get_square_(self):
        return 4 * math.pi * self.Radius ** 2

    def get_radius_(self):
        return self.Radius

    def get_center_(self):
        return self.XCoordinate, self.YCoordinate, self.ZCoordinate

    def set_radius_(self, r):
        self.Radius = r

    def set_center(self, x, y, z):
        self.XCoordinate = x
        self.YCoordinate = y
        self.ZCoordinate = z

    def is_point_inside(self, x, y, z):
        if (self.XCoordinate - x) ** 2 + (self.YCoordinate - y) ** 2 + (self.ZCoordinate - z) ** 2 <= self.Radius ** 2:
            return True
        return False


MySphere = Sphere(22, 30, 25, 10)
BadShpere = Sphere()
print(MySphere.get_volume())
print(MySphere.get_square_())
print(MySphere.get_radius_())
print(MySphere.get_center_())
print(MySphere.set_center(100,200,300))
print(MySphere.set_radius_(1))
print(MySphere.get_radius_())
print(MySphere.get_center_())
print(MySphere.is_point_inside(0.5, 0.5, -0.5))
print(BadShpere.get_center_())
print(BadShpere.get_radius_())
print(BadShpere.is_point_inside(0.5, 0.5, -0.5))

