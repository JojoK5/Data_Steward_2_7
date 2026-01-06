#importing pandas library to open excel files
import pandas as pd 

#importing Path from pathlib to handle file paths
from pathlib import Path

#importing matplotlib to create plots
import matplotlib.pyplot as plt 

folder = Path(__file__).parent #getting the current folder path
file_path = folder / "data_python.xlsx" 
df = pd.read_excel(file_path) #reading the excel file 

#printing the first 5 rows of the file to verify it opened correctly
print(df.head())

#---------
#using a function with interface df
def summary_data(df):
    total=0 #initializing total variable to 0
    all_values_sum = df["data"].sum() # Total of every value in the column "data"
    mean_value = df["data"].mean()    # The average value
    
    print("The total sum of all values is:", all_values_sum) #printing the total sum of all values
    print("The mean value is:", mean_value) #printing the mean value
    
    for value in df["data"]:
        if value<15: #checking if the value in the column "data" is less than 15
            total += value #adding the value to total if condition is met
            
    difference = all_values_sum - total # Difference between total and filtered sum
    
    return total, all_values_sum, mean_value, difference

# Calling the function and getting the results

result, total_sum, average, diff = summary_data(df)

#printing the result
print(f"Sum of values < 15: {result}")
print(f"Total sum of all data: {total_sum}")
print(f"The average value is: {average:.2f}")
print(f"The difference between the total sum and the sum of values < 15 is: {diff}")

new_array = [value for value in df["data"] if value > 10]
print("New array with values greater than 10:", new_array) #printing the new array

#----------
#Making a summary diagram and comparing individual values to the conditional calculated total

plt.figure(figsize=(10,6)) #setting the figure size
plt.bar(df.index, df["data"], color="purple", label='Individual Values') #creating a bar plot
plt.axhline(y=result, color='b', linestyle='--', label='Sum of values < 15') #adding a horizontal line for the sum
plt.xlabel('Row Number (position)')
plt.ylabel('Value')
plt.title('Individual Data vs. Calculated Total')
plt.legend()    
plt.savefig('my_summary_diagram.png') #saving the plot as a PNG file
plt.show() #displaying the plot

#close the diagram window to get the print statement below and get the file location:
print(f"Analysis complete. File saved at: {Path('my_summary_diagram.png').resolve()}")