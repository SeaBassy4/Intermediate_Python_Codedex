import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

 
try:
    with open('packing_list.csv', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
    
    

except FileNotFoundError:
    print("packing_list.csv file not found, create a new one.")
    

with open('packing_list.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    
