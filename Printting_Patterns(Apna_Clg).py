x = "*****"
for i in range(4):
    print(x)
                                               #code for solid rectangle of stars
print("----------------------------------------------------------------------------------------")

for i in range(4):
  for j in range(5):
    if(i==0 or i==(3) or j==0 or j==(4)):
        print("*", end="")
    else:
        print(" ", end="")
  print()
          #code for hallow rectangle
print("----------------------------------------------------------------------------------------")


row = int(input("Enter number of rows="))
col = int(input("Enter number of columns="))
for i in range(row ):
    for j in range(col):
        if(i==0 or i==(row -1) or j==0 or j==(col -1)):
         print("*", end="")
        else:
         print(" ", end="")
    print()


print("----------------------------------------------------------------------------------------")
