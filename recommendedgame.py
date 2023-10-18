import json

with open('datacov.json', 'r') as file :
    datacov = json.load(file)

inp = 'Brass: Birmingham'
covgame = datacov[0].index(inp)+1
recommended = [i for i in datacov[covgame] if 0 <= float(i)]
recommended.sort(reverse=True)
recommended.pop(0)
while len(recommended) > 10 :
    recommended.pop()
recommendedgame = [datacov[0][datacov[covgame].index(i)] for i in recommended]
print(recommendedgame)
