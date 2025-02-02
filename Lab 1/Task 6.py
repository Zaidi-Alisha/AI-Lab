#Fires are represented by @#
class Fire_Fighter_Robot:
    def __init__(self):
        self.grid = {
            'a': 'safe ', 'b': 'safe ', 'c': '@#',
            'd': 'safe', 'e': '@#', 'f': 'safe ',
            'g': 'safe', 'h': 'safe', 'j': '@#'
        }
        self.path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
        self.position = 'a'

    def display(self):
        print("\nGrid:")
        print(f"{self.grid['a']} {self.grid['b']} {self.grid['c']}")
        print(f"{self.grid['d']} {self.grid['e']} {self.grid['f']}")
        print(f"{self.grid['g']} {self.grid['h']} {self.grid['j']}")

    def movement(self):
        for room in self.path:
            self.position = room
            print(f"\nMoving to room {room}")
            if self.grid[room] == '@#':
                print(f"There's a fire in room {room}. Putting out the fire")
                self.grid[room] = ' '
            else:
                print(f"There is no fire in room {room}")
            self.display()

    def process(self):
        print("Starting the movement of the robot to find and extinguish fires")
        self.display()
        self.movement()
        print("\nRooms after finishing the task:")
        self.display()

# Running the firefighting robot simulation
robot = Fire_Fighter_Robot()
robot.process()
