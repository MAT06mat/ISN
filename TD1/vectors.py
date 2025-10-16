class Vector:
    coords = ()
    
    def __init__(self, *coords):
        self.coords = coords
    
    def __compatible_vector(self, obj):
        if not isinstance(obj, Vector):
            raise ValueError(f"Can't do operation on Vector and {type(obj)}")
        
        if len(self.coords) != len(obj.coords):
            raise ValueError("Vectors haven't the same number of dimensions")
    
    def __add__(self, obj):
        self.__compatible_vector(obj)
        new_coords = [self.coords[i] + obj.coords[i] for i in range(len(self.coords))]
        return Vector(*new_coords)
    
    def __sub__(self, obj):
        self.__compatible_vector(obj)
        new_coords = [self.coords[i] - obj.coords[i] for i in range(len(self.coords))]
        return Vector(*new_coords)
    
    def scalaire(self, obj):
        self.__compatible_vector(obj)
        new_coords = [self.coords[i] * obj.coords[i] for i in range(len(self.coords))]
        return sum(new_coords)
    
    def __mul__(self, obj):
        if isinstance(obj, (int, float)):
            new_coords = [obj * coord for coord in self.coords]
            return Vector(*new_coords)
        self.__compatible_vector(obj)
        if len(self.coords) != 3:
            raise ValueError("Vectorial product only work in 3 dimensions")
            
        x, y, z = self.coords
        a, b, c = obj.coords
        
        new_coords = [
            y*c - z*b,
            z*a - x*c,
            x*b - y*a,
        ]
        
        return Vector(*new_coords)
        
    
    def __eq__(self, obj):
        return self.coords == obj.coords
    
    def __repr__(self):
        return f'Vector{self.coords}'

# DEMO

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 0)

print(f"{v1=} {v2=}")
print(f"{v1+v2=}")
print(f"{v1-v2=}")
print(f"{v1*2=}")
print(f"{v1*v2=}")

    



