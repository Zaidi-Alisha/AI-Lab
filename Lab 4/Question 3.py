import heapq
from datetime import datetime, timedelta
from collections import defaultdict

class DeliveryPoint:
    def __init__(self, id, location, time_window, service_time=10):
        self.id = id
        self.location = location
        self.time_window = time_window
        self.service_time = timedelta(minutes=service_time)
        self.time_window_width = (time_window[1] - time_window[0]).total_seconds()
        
    def __lt__(self, other):
        return self.time_window_width < other.time_window_width

class DeliveryOptimizer:
    def __init__(self, depot_location, current_time=None):
        self.depot = depot_location
        self.current_time = current_time or datetime.now()
        self.delivery_points = []
        
    def add_delivery_point(self, delivery_point):
        self.delivery_points.append(delivery_point)
        
    def distance(self, a, b):
        return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5
    
    def time_to_travel(self, a, b, speed=30):
        distance_km = self.distance(a, b) / 1000  
        return timedelta(hours=distance_km/speed)
    
    def greedy_best_first_search(self):
        if not self.delivery_points:
            return []
        
        unvisited = []
        for point in self.delivery_points:
            time_urgency = point.time_window_width
            dist_from_depot = self.distance(self.depot, point.location)
            priority = time_urgency + dist_from_depot * 0.1  
            heapq.heappush(unvisited, (priority, point))
        
        route = []
        current_location = self.depot
        current_time = self.current_time
        total_distance = 0
        
        while unvisited:
            _, next_point = heapq.heappop(unvisited)
            
            travel_time = self.time_to_travel(current_location, next_point.location)
            arrival_time = current_time + travel_time
            
            window_start, window_end = next_point.time_window
            
            if arrival_time > window_end:
                print(f"Warning: Cannot deliver to {next_point.id} on time (arrival at {arrival_time})")
                continue
              
            wait_time = max(timedelta(0), window_start - arrival_time)
            
            route.append({
                'point': next_point.id,
                'location': next_point.location,
                'arrival_time': arrival_time + wait_time,
                'departure_time': arrival_time + wait_time + next_point.service_time,
                'travel_time': travel_time,
                'wait_time': wait_time
            })
            
            total_distance += self.distance(current_location, next_point.location)
            current_location = next_point.location
            current_time = arrival_time + wait_time + next_point.service_time
        
        return_distance = self.distance(current_location, self.depot)
        total_distance += return_distance
        route.append({
            'point': 'DEPOT',
            'location': self.depot,
            'arrival_time': current_time + self.time_to_travel(current_location, self.depot),
            'travel_time': self.time_to_travel(current_location, self.depot),
            'total_distance': total_distance
        })
        
        return route

if __name__ == "__main__":
    depot = (0, 0)
    now = datetime.now()
    optimizer = DeliveryOptimizer(depot, now)
    
    optimizer.add_delivery_point(DeliveryPoint(
        id="A",
        location=(3000, 4000),
        time_window=(now + timedelta(minutes=30), now + timedelta(hours=1))
    ))
    
    optimizer.add_delivery_point(DeliveryPoint(
        id="B",
        location=(1500, 1500),
        time_window=(now + timedelta(minutes=15), now + timedelta(minutes=45))
    ))
    
    optimizer.add_delivery_point(DeliveryPoint(
        id="C",
        location=(5000, 1000),
        time_window=(now + timedelta(hours=1), now + timedelta(hours=2))
    ))
    
    optimizer.add_delivery_point(DeliveryPoint(
        id="D",
        location=(2000, 5000),
        time_window=(now + timedelta(minutes=45), now + timedelta(hours=1, minutes=30))
    ))
    
    optimized_route = optimizer.greedy_best_first_search()
    
    print("Optimized Delivery Route:")
    print(f"{'Point':<5} {'Location':<12} {'Arrival Time':<25} {'Travel Time':<15} {'Wait Time':<15}")
    for stop in optimized_route[:-1]:
        print(f"{stop['point']:<5} {str(stop['location']):<12} "
              f"{stop['arrival_time'].strftime('%Y-%m-%d %H:%M:%S'):<25} "
              f"{str(stop['travel_time']):<15} {str(stop['wait_time']):<15}")
    
    print(f"\nTotal distance: {optimized_route[-1]['total_distance']:.2f} meters")
    print(f"Return to depot at: {optimized_route[-1]['arrival_time'].strftime('%Y-%m-%d %H:%M:%S')}")
