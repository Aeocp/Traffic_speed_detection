def createLine():
  numLine = int(input("Enter number of counting line :"))
  x = []
  y = []
  for l in range(numLine):
    print("Enter the beginning and ending of the line (0-1) (x,y) :")
    print("Line",l+1)
    Bp = input("Beginning Point :").split(",")
    x.append((Bp[0]))
    y.append((Bp[1]))
    Ep = input("Ending Point :").split(",")
    x.append(Ep[0])
    y.append(Ep[1])
  return numLine,x,y

def createLine2():
  numLine = int(input("Enter number of counting line :"))
  x = []
  y = []
  for l in range(numLine):
    print("Enter the beginning and ending of the line (0-1) (x,y) :")
    print("Line",l+1)
    Bp = input("Enter line position :").split(",")
    x.append((Bp[0]))
    y.append((Bp[1]))
    x.append((Bp[2]))
    y.append((Bp[2]))
  return numLine,x,y

def createLineSpeed():
  numLine = int(input("Enter number of counting line :"))
  x1 = []
  y1 = []
  x2 = []
  y2 = []
  print("Enter the beginning and ending of the line (0-1) (x,y) :")
  Bp = input("First Point Line1 :").split(",")
  x.append((Bp[0]))
  y.append((Bp[1]))
  Ep = input("End Point Line1:").split(",")
  x.append(Ep[0])
  y.append(Ep[1])
  Bp = input("First Point Line2 :").split(",")
  x2.append((Bp[0]))
  y2.append((Bp[1]))
  Ep = input("End Point Line2:").split(",")
  x2.append(Ep[0])
  y2.append(Ep[1])
  return x1,y1,x2,y2
