result = 0

with open("Day02/Input.txt", "r") as inputFile:
    inputText = inputFile.read()
inputRanges = inputText.split(',')
for line in inputRanges:
    floor = int(line.split('-')[0])
    ceiling = int(line.split('-')[-1])
    for i in range(floor, ceiling+1):
        productID = str(i)
        middle = len(productID) // 2
        firstHalf = productID[:middle]
        secondHalf = productID[middle:]
        if firstHalf == secondHalf:
            #print(f"First Half: {firstHalf} | Second Half: {secondHalf}")
            result += i

print(result)