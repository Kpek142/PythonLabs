text = input()

words = text.split()

counts = {}

result = []

for word in words:
    seen = counts.get(word, 0) #выведет 0 если слова нет в словаре

    result.append(str(seen))

    counts[word] = seen + 1

print(" ".join(result))