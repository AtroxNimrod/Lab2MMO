import itertools
import math

# Numărul total de orașe
num_cities = 5

# Numele orașelor
city_names = ["Chisinau", "Ialoveni", "Criuleni", "Floresti", "Soroca"]

# Distanțele dintre orașe
distances = [[0, 10, 15, 20, 30],
             [10, 0, 35, 25, 40],
             [15, 35, 0, 30, 50],
             [20, 25, 30, 0, 60],
             [30, 40, 50, 60, 0]]

# Lista tuturor permutărilor posibile de orașe
permutations = list(itertools.permutations(range(num_cities)))

# Găsim distanța minimă parcursă
min_distance = float("inf")
best_permutation = None
for permutation in permutations:
  distance = 0
  for i in range(len(permutation)):
    city_1 = permutation[i]
    city_2 = permutation[(i+1) % num_cities]
    distance += distances[city_1][city_2]
  if distance < min_distance:
    min_distance = distance
    best_permutation = permutation

# Afișăm drumul parcurs
print("Drumul parcurs este:")
for i in range(len(best_permutation)):
  city_1 = city_names[best_permutation[i]]
  city_2 = city_names[best_permutation[(i+1) % num_cities]]
  print(f"{city_1} -> {city_2} ({distances[best_permutation[i]][best_permutation[(i+1) % num_cities]]} km)")

print("Distanța minimă parcursă este:", min_distance, "km")