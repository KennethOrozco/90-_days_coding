# projects = [
#     ("Task Manager", "Python"),
#     ("Portfolio", "JavaScript"),
#     ("Data Analyzer", "Python"),
#     ("Website", "HTML")
# ]

# for index, (name, language) in  enumerate(projects, start=1):
#     print(f"{index}. {name} - {language}")
# products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
# prices = [1200, 25, 75, 300]
# quantities = [2, 10, 5, 3]

# for product, price, quantity in zip(products, prices, quantities):
#     result = price*quantity
#     print(f"{product}: ${price} x {quantity} = ${result}")
# def calculate_average(*scores):
#     if not  scores:
#         return 0
#     average = sum(scores)/len(scores)
#     return average

# print(calculate_average())

# def create_profile(**kwargs):
#     return kwargs

# profile1 = create_profile(
#     name="Alex",
#     age=24
# )
# profile2 = create_profile(
#     name="Jordan",
#     language="Python",
#     experience=3
# )
# profile3 = create_profile()

# print(profile1)
# print(profile2)
# print(profile3)
# def create_project(name, **details):
#     details["name"] = name
#     return details

# print (create_project("Task Manager", language="Python", complete=True, lines=250))
