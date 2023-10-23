for element in range(20):                   # 0, 1, 2... 19
    print(element)
    

for element in range(1, 20):                # 1, 2, 3, ... 19
    print(element)
    

my_list = ['Alejandro', 'Santiago', 'Lina']
for element in my_list:
    print(element)                          # Alejandro, Santiago, Lina


my_tuple = (12, 24, 36, 48, 60, 72)
for element in my_tuple:
    print(element)                          # 12, 24, 36, 48, 60, 72
    
    
product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 24,
}

for element in product:
    print(element)                          # name, price, stock
    
for key in product:
    print(key, " --> ", product[key])       # name --> Camisa, price --> 100, stock --> 24
    
for key, value in product.items():
    print(key, ' --> ', value)              # name --> Camisa, price --> 100, stock --> 24
    

people = [
    {'name': 'Alejandro', 'age': 25},
    {'name': 'Santiago', 'age': 18},
    {'name': 'Lina', 'age': 28},
]

for person in people:
    print('Name: ', person['name'])         # Name: Alejandro, Name: Santiago, Name: Lina