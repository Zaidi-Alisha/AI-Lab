class Hospital:
    def __init__(self):
        self.location = "Medicine Storage"
        self.medicine_cart = {}
        self.patients = {
            "Room 1": {"medicine": "Panadol", "id": "8493"},
            "Room 2": {"medicine": "Calpol", "id": "0284"},
            "Room 3": {"medicine": "Augmentin", "id": "7264"}
        }

    def move(self, location):
        print(f"Moving to {location}")
        self.location = location

    def collect(self):
        print("Collecting medicines:")
        for room, details in self.patients.items():
            self.medicine_cart[room] = details["medicine"]
        print("Medicines have been collected")

    def deliver(self):
        for room, details in self.patients.items():
            self.move(room)
            print(f"Id of patient in {room}")
            if details["id"] == f"P{room.split()[1]}":
                print(f"Patient is present in records. Delivering {details['medicine']} to {room}.")
            else:
                print(f"There is no match! Staff has been asked to check {room}")
        print("Deliveries are done")

    def perform(self):
        self.move("Medicine Storage")
        self.collect()
        self.deliver()

robot = Hospital()
robot.perform()
