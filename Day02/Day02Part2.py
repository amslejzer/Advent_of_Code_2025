result = 0

with open("Day02/Input.txt", "r") as inputFile:
    inputText = inputFile.read()
inputRanges = inputText.split(',')
for line in inputRanges:
    floor = int(line.split('-')[0])
    ceiling = int(line.split('-')[-1])
    for id in range(floor, ceiling+1):
        productID = str(id)
        for i in range(1, ((len(productID) // 2) + 1)):
            pattern = productID[:i]
            occurrence_count = productID.count(pattern)
            if(occurrence_count == len(productID) / len(pattern)):
                result += id
                break

print(result)