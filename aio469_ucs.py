import math
import csv
import heapq
import sys

# Haversine Formula
def haversine(lat1, lon1, lat2, lon2):
    R = 6371000 #radius of earth in meters
    
    phi_1= math.radians(lat1)
    phi_2= math.radians(lat2)

    delta_phi = math.radians(lat1-lat2)
    delta_lambda= math.radians(lon2-lon1)

    #a = sin²(ΔlatDifference/2) + cos(lat1).cos(lt2).sin²(ΔlonDifference/2)
    a= math.sin(delta_phi/2.0)**2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda/2.0) **2

    #c = 2.atan2(√a, √(1−a))
    c= 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))

    #d = R.c
    d= (R * c)/1000.0 # Distance in KM 
    return d

#load cities.csv
def retrieve_cities(path):
    cities = {}
    with open(path, mode = 'r') as file:
        reader=csv.reader(file)
        for row in reader:
            city, lat, lon = row[0], float(row[1]), float(row[2])
            cities[city] = (lat,lon)
    return cities

#load roads.csv
def retrieve_roads(path, cities):
    roads = {}
    with open(path, mode = 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            city1, city2 = row[0], row[1]
            #calculating the distance 
            if city1 in cities and city2 in cities:
                lat1, lon1 = cities[city1]
                lat2, lon2 = cities[city2]
                distance = haversine(lat1, lon1, lat2, lon2)

                #adding road to roads dictionary
                #considering bidirectional
                if city1 not in roads:
                    roads[city1] = []

                if city2 not in roads:
                    roads[city2] = []

                roads[city1].append((city2,distance))
                roads[city2].append((city1,distance))
            else:
                print(f"Data is missing for {city1} or {city2}")

    return roads

# ucs Algorithm
def ucs(cities, roads, start, goal):

    
    search_queue = [(0, start, [])]

    #converts search_queue to a min-heap, meaning smallest element at front
    heapq.heapify(search_queue)

    #keep track of cities (or nodes) that have already been explored
    explored = set()

    while search_queue:
        cost, city, path = heapq.heappop(search_queue)

        if city in explored:
            continue

        path = path+ [city]

        if city == goal:
            return path, cost
        
        explored.add(city)

        for neighbor, distance in roads.get(city, []):
            if neighbor not in explored:
                total_cost = distance + cost
                heapq.heappush(search_queue,(total_cost,neighbor,path))

    return None, None

def main():
    start_city = sys.argv[1]
    goal_city = sys.argv[2]

    cities = retrieve_cities("cities.csv")
    roads = retrieve_roads("roads.csv", cities)

    if start_city not in cities or goal_city not in cities:
        print("City not found!")

    path, distance = ucs(cities, roads, start_city, goal_city)

    if path:
        print(" - ".join(path))
        print(f"Total Distance - {distance:.2f} km")
    else:
        print("Path not found!")

if __name__ == "__main__":
    main()