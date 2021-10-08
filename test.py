import requests
base = "http://127.0.0.1:5000/"

data = [{"model_id": 1245, "count": 3, "name": "fiat", "color": "pink", "price": 2000},
        {"model_id": 1269, "count": 3, "name": "ciaz", "color": "magenta", "price": 4000}]
# print(base+"car/"+str(data[0]["model_id"]))
# for i in range(len(data)):
#     response = requests.put(base+"car/"+str(data[i]["model_id"]), data[i])
#     print(response.json())
# input()


# response = requests.get(base+"car/"+str(1248))
# print(response.json())

# response = requests.delete(base+"car/"+str(1248))
# print(response.json())

# response = requests.get(base+"car/"+str(1248))
# print(response.json())

# response = requests.put(base+"car/"+str(1269), data[1])
# print(response.json())
# json
# response = requests.get(base+"car/"+str(1543))
# print(response.json())

# response = requests.patch(base+"car/"+str(1248), {'price': 80000,'count':69})
# print(response.json())

# response = requests.delete(base+"car/"+str(1248))
# print(response)

# response = requests.delete(base+"car/"+str(1243), count=10)
# print(response.json())

# response = requests.delete(base+"car/"+str(1225))
# print(response.json())

