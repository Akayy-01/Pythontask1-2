#TASK 1
radius=float(input("Input the radius of circle\n"))          
a=(radius*radius)*3.14
print("The area of circle with radius",radius,"is:",a)

#TASK 2
fn=input("Input the filename:")
f=fn.split(".")
print("Extension of the file is:" +f[-1])
