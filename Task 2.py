import random

class Server:
    def __init__(self, server_id):
        self.server_id = server_id
        self.load = random.randint(-100, 200)
        
    #define thresholds to classify tasks as underloaded, balanced or overloaded
    def get_status(self):
        if self.load < 0:
            return "Incorrect Load"
        elif 0 <= self.load <= 40:
            return "underloaded"
        elif 40 < self.load <= 50:
            return "balanced"
        else:
            return "overloaded"

    def __str__(self):
        return f"Server{self.server_id} has a load of {self.load} and its status is {self.get_status()}"

class ServerManager:
    def __init__(self, num_servers=5):
        self.servers = [Server(str(i + 1)) for i in range(num_servers)]

    def display(self):
        print("\nServer Statuses:")
        for server in self.servers:
            print(server)

    def scan_and_balance(self):
        underloaded = []
        overloaded = []

        print("\nScanning Servers:")
        for server in self.servers:
            print(server)
            status = server.get_status()
            if status == "underloaded":
                underloaded.append(server)
            elif status == "overloaded":
                overloaded.append(server)

        if overloaded and underloaded:
            print("\nBalancing Load:")
            for ol_server in overloaded:
                while underloaded:
                    ul_server = underloaded.pop()
                    load_to_move = min(ol_server.load - 50, 50 - ul_server.load)

                    ol_server.load -= load_to_move
                    ul_server.load += load_to_move

                    print(f"Moving {load_to_move} from Server{ol_server.server_id} to Server{ul_server.server_id}")
                    print(f"New load of Server{ol_server.server_id}: {ol_server.load}")
                    print(f"New load of Server{ul_server.server_id}: {ul_server.load}")

                    if ul_server.get_status() != "Underloaded":
                        break

                    if ol_server.get_status() != "Overloaded":
                        break
        else:
            print("\nNo balancing needed as no servers are both overloaded and underloaded")

def run_code():
    manager = ServerManager()
    print("Initial Server Status:")
    manager.display()

    manager.scan_and_balance()

    manager.display()

run_code()