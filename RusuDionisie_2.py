import pulp

# Definim matricea de costuri pentru fiecare transport
costs = [[20, 23, 20, 15, 24, 17],
         [29, 15, 16, 19, 29, 22],
         [6, 11, 10, 9, 8, 7],
         [14, 21, 18, 25, 22, 14],
         [21, 24, 21, 16, 25, 18]]

# Definim capacitatea fiecarui transport
capacity = [340, 310, 260, 200, 250]

# Definim cerintele de livrare pentru fiecare client
demand = [160, 180, 140, 240, 250, 280]

# Definim numarul de transporturi si numarul de clienti
num_trucks = len(capacity)
num_customers = len(demand)

# Cream problema de optimizare
prob = pulp.LpProblem("Linear Transportation Problem", pulp.LpMinimize)

# Cream variabilele de decizie
x = [[pulp.LpVariable(f"x{i},{j}", lowBound=0) for j in range(num_customers)] for i in range(num_trucks)]

# Adaugam functia obiectiv care minimizeaza costurile totale de transport
prob += sum(costs[i][j] * x[i][j] for i in range(num_trucks) for j in range(num_customers))

# Adaugam constrangerile de capacitate pentru fiecare transport
for i in range(num_trucks):
    prob += sum(x[i][j] for j in range(num_customers)) <= capacity[i]

# Adaugam constrangerile de cerere pentru fiecare client
for j in range(num_customers):
    prob += sum(x[i][j] for i in range(num_trucks)) >= demand[j]

# Rezolvam problema
status = prob.solve()

# Verificam rezultatul
assert status == pulp.LpStatusOptimal

# Afisam valorile optime pentru variabilele de decizie
for i in range(num_trucks):
    for j in range(num_customers):
        print(f"x{i},{j} = {x[i][j].value()}")

# Afisam valoarea functiei obiectiv (costul total minim)
print(f"Costul total minim: {pulp.value(prob.objective)}")
