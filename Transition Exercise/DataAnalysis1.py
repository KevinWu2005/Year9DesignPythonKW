
#creates a variable data that points at the file and
#is prepared to read from it
data = open("randomDataRAW.txt","r") #Opens file


dataString = data.read() #reads content
print(dataString)

#copy the data from the string into a list
dataList = dataString.split("\n") #converts to list using \n
print(dataList) 

#Cast all list elements into floats
for i in range(0,len(dataList),1): #loops through every element
	dataList[i] = dataList[i].replace(",","") #replaces all commas with nothing
	dataList[i] = float(dataList[i]) #cast element to float

print(dataList)

minimum = min(dataList)
print(minimum)

maximum = max(dataList)
print(maximum)

biggest = 0
for i in range(0,len(dataList),1):
	if biggest < dataList[i]:
		biggest = dataList[i]

print("MAX IS: "+str(biggest))

smallest = biggest
for i in range(0,len(dataList),1):
	if smallest > dataList[i]:
		smallest = dataList[i]

print("MIN IS: "+str(smallest))

value = input("What number do you want to set as upper limit ")
value = float(value)
#write code that uses data analysis
count = 0
for i in range(0, len(dataList),1):
	if(dataList[i] < value):
		count = count+1
		print(dataList[i])

print(count)




