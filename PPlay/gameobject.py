<<<<<<< HEAD
"""The most basic game class"""
class GameObject():
    """Creates a GameObject in X, Y co-ords, with Width x Height"""
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

    def collided(self, obj):
        # Module import
        from . import collision
        
        return collision.Collision.collided(self, obj)
=======
"""The most basic game class"""
class GameObject():
    """Creates a GameObject in X, Y co-ords, with Width x Height"""
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

    def collided(self, obj):
        # Module import
        from . import collision
        
        return collision.Collision.collided(self, obj)
>>>>>>> 1c73ac2717b15f72afa3c2c99444a2543c94e074
