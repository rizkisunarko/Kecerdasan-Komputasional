import matplotlib.pyplot as plt

cities = [
    ("Denver",39.7420,-104.9915),
    ("Colorado Springs",38.8461,-104.8006),
    ("Telluride",37.9375,-107.8123),
    ("Las Vegas",36.1146,-115.1728),
    ("Grand Canyon",36.0565,-112.1251),
    ("Yellowstone NP",44.4237,-110.5885),
    ("Mount Rushmore",43.9686,-103.3818),
    ("Seattle",47.6080,-122.3352),
    ("Redwood NP",41.2131,-124.0046),
    ("San Diego",32.7157,-117.1610),
    ("Los Angeles",34.0522,-118.2437),
    ("Mount Hood NF",45.4543,-121.9331),
    ("Santa Fe",35.6915,-105.9442),
    ("Chicago",41.8818,-87.6232),
    ("New York City",40.7306,-73.9352)
]

route = [7, 8, 3, 11, 10, 14, 1, 13, 5, 6, 2, 0, 12, 4, 9]

# Put the route coordinates in order
x = []
y = []
names = []

for idx in route:
    names.append(cities[idx][0])
    y.append(cities[idx][1]) # latitude
    x.append(cities[idx][2]) # longitude

# Add the first city at the end to close the loop
x.append(x[0])
y.append(y[0])

plt.figure(figsize=(10, 6))

# Plot the path
plt.plot(x, y, marker='o', linestyle='-', color='b', markersize=6)

# Annotate the cities
for i, name in enumerate(names):
    plt.annotate(name, (x[i], y[i]), textcoords="offset points", xytext=(5,5), ha='left', fontsize=8)

# Add start and end distinct markers
plt.plot(x[0], y[0], marker='s', color='g', markersize=8, label='Start/End')

plt.title("Best Route (TSP) by Genetic Algorithm")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("../media/best_route.png", dpi=300)
print("Saved best_route.png")
