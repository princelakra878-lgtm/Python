travels = ["Delhi", "Mumbai", "Jaipur", "Goa"]

count = len(travels)
print("Total trips:", count)

distances = [250, 500, 300, 450]  # in kilometers

total_distance = sum(distances)
print("Total distance:", total_distance, "km")

from collections import Counter

travels = ["Delhi", "Mumbai", "Delhi", "Goa", "Mumbai", "Delhi"]

counts = Counter(travels)
print(counts)