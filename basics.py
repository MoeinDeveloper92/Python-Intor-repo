import pandas as pd
#bellow we create a data frame
data = {'name':['Moein',"Darya","Mohsen"],
'age':[30,25,35],
'Country':["Iran","Germany","USA"]}

df = pd.DataFrame(data)

#bellow we print out the data
print((df))