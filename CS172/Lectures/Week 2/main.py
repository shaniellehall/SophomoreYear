from point import Point
from random import randint

#the main script below this line

if __name__ == "__main__":
    howMany = int(input("How many points do you want? "))
    myPoints = []
    
    for count in range (0, howMany):
        x = randint(0, 50)
        y = randint(0, 50)
        p = Point(x, y)
        myPoints.append(p)
        
    print()
    print(Point.getPointCount(), "random points were created:?")
    for index in range(0, len(myPoints)):
        ptStr = myPoints[index].pointToString()
        print("Point", index + 1, ":", ptStr)
    print