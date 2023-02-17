
food = ['rice', 'beans']
food.append('broccoli')
print(food)

food.extend(['bread','pizza'])
print(food)

print(food[0])
print(food[1])
print(food[4])

breakfastString=('eggs, fruit, orange juice')
breakfast=breakfastString.split(',')
print(breakfast)
print(len(breakfast))

MyList=[]
while True:
    MyEntry = input ("Enter a number of type 'stop' to end: ")
    if MyEntry == "stop":
        break
    MyList.append(int(MyEntry))

if MyList:
    print("Minimum: ", min(MyList))
    print("Maximum: ", max(MyList))
    print("Average: ", sum(MyList) / len(MyList))
else:
    print("End")
