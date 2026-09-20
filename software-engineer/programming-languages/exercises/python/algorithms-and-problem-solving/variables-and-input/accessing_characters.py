characters = 'Python'
indices = [0, 1, 5, 19, 20]

for i in indices:
    if i < len(characters):
        print(characters[i])
    else:
        print(f"Index {i} is out of range")
