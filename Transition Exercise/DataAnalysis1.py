
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