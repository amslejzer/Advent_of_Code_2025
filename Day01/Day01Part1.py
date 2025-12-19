CurrentPosition = 50
ZeroCount = 0
PassCount = 0
CurrentPassCount = 0

with open('Day01/Input.txt', 'r') as input:
    for line in input:
        CurrentPassCount = 0
        RotationAmount = int(line[1:])
        if(line[0] == 'L'):
            RotationAmount = RotationAmount * -1
        NewPosition = CurrentPosition + RotationAmount
        if(NewPosition <= 0 and CurrentPosition != 0):
            CurrentPassCount += abs(RotationAmount)//100 + 1
        elif(NewPosition <= 0 and CurrentPosition == 0):
            CurrentPassCount += abs(RotationAmount)//100
        if(NewPosition >= 100):
            CurrentPassCount += NewPosition//100
        #if(NewPosition % 100 == 0):
        #    ZeroCount += 1
        print(f"Start position: {CurrentPosition} | Rotation amount: {RotationAmount} | New position: {NewPosition} | Zero passes: {CurrentPassCount}" )
        CurrentPosition = NewPosition % 100
        PassCount += CurrentPassCount
print(f"Zero Count: {ZeroCount}")
print(f"Pass Count: {PassCount}")