pages = [['baby', 'first grade', 'eight grade', 'party with friends'], ['prom', 'wedding']]

result = "-----------\n"
for row in range(len(pages)):
    for col in range(len(pages[row])):
        result += "[]"
    result += "\n-----------\n"

print(result)