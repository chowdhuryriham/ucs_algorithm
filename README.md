```markdown
---

# Uniform Cost Search (UCS) Algorithm

## Overview

This project implements the **Uniform Cost Search (UCS)** algorithm to find the shortest path between two cities based on geographical data. The UCS algorithm guarantees finding the least expensive path by exploring nodes in increasing order of cost.

The cities' coordinates and road connections are provided in two CSV files: `cities.csv` and `roads.csv`. The distance between cities is calculated using the **Haversine formula**, which accounts for the Earth's curvature.

## File Structure

```
.
├── ucs.py             # Main Python script implementing UCS algorithm
├── cities.csv         # CSV file with city names and coordinates (latitude, longitude)
├── roads.csv          # CSV file with city connectivity (city pairs with a direct road)
└── README.md          # Project documentation (this file)
```

## Input Files

1. **cities.csv**  
   Format:
   ```
   City,Latitude,Longitude
   CityA,34.052235,-118.243683
   CityB,36.778259,-119.417931
   ```

2. **roads.csv**  
   Format:
   ```
   City1,City2
   CityA,CityB
   CityB,CityC
   ```

## How the UCS Algorithm Works

- **Cost Function:** UCS uses a simple cost function `g(n)` which is the accumulated distance from the start city to the current city.
- **Uninformed Search:** UCS explores the least costly path at each step without any heuristic, ensuring it finds the shortest path if one exists.

### Haversine Formula

The **Haversine formula** calculates the shortest distance between two points on the Earth's surface given their latitude and longitude. The formula is used to calculate the straight-line distance (in kilometers) between cities.

#### Formula:
Given two cities with coordinates `(lat1, lon1)` and `(lat2, lon2)`:

```python
R = 6371.0  # Radius of the Earth in kilometers
phi_1 = math.radians(lat1)
phi_2 = math.radians(lat2)

delta_phi = math.radians(lat2 - lat1)
delta_lambda = math.radians(lon2 - lon1)

a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

distance = R * c  # Distance in kilometers
```

## How to Run the Program

To run the UCS algorithm, follow these steps:

1. **Ensure you have the required CSV files (`cities.csv` and `roads.csv`) in the same folder as the script.**

2. **Run the Python script:**
   Use the following command in your terminal, providing the source city and destination city as arguments.

   ```bash
   python ucs.py <source_city> <destination_city>
   ```

### Example:

```bash
python ucs.py Dalhart San_Antonio
```

### Expected Output:

The program will output the shortest path found along with the total distance in kilometers, like this:

```
Dalhart - Amarillo - Lubbock - San_Antonio
Total Distance - 900.5 km
```

### No Path Found:

If no path exists between the cities, the program will return:
```
Path not found!
```

## Requirements

- Python 3.x
- `csv` module (comes with Python standard library)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
```