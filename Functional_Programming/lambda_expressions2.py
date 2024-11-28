a = [(0,2),(4,4),(10,-1),(5,3)]

a.sort(key=lambda x: x[1], reverse=False) #In this the sorting happens as per the lambda function where the sorting item x gets filtered using the x[1] value i.e. second element of each tuple item in the list a
print(a)