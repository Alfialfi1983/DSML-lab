print("containers:sets")
num1={100,110,120}
print("set 'num1':",num1)
num1.add(90)
print("'num1' after inserting 90:",num1)
num1.update([50,60,70])
print("'num1' after inserting multiple elements:",num1)
num1.remove(60)
print("'num1' after removing 60:",num1)
print("set comprehension and set operation")
n1={x for x in range(10)}
print("n1=",n1)
n2={x for x in range(10) if x%2!=0}
print("n2=",n2)
print("n1 union n2:",n1| n2)