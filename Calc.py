n=int(input("Enter First Number --->"))
m=int(input("Enter second Number--->"))
k=input("Enter The Operator-->")
if k=='+':
  print("Sum is->",n+m)
elif k=='-':
  print("Sum is->",n-m)
elif k=='*':
  print("Multiply is-->",n*m)
elif k=='/':
  print("Division is",n/m)
else:
  print("You Entered Wrong Operator")
