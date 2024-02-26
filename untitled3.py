#importing important libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# reading csv file
kaggle_raw_data = pd.read_csv('./HRDataset_v14.csv')

# preprocessing raw data
# select coloums which are important

columns_to_use = ['Employee_Name','EmpID','Salary','Position','DeptID','Sex','MaritalDesc','MarriedID','GenderID']
selected_data = kaggle_raw_data[columns_to_use]

print(selected_data.head())

# function for histogram plot
def histogram_plot():
  plt.hist(selected_data['MaritalDesc'])
  plt.xlabel("Marital Status")
  plt.ylabel("Count")
  plt.title("Histogram of Marital Status")
  plt.show()

# function for Bar chart
def plot_bar_chart():
  selected_data['DeptID'].value_counts().plot(kind="bar")
  plt.xlabel("DeptID")
  plt.ylabel("Number of people in DeptID")
  plt.title("Bar Chart of Department ID")
  plt.show()

# function for Pie chart
def plot_pie_chart():
  selected_data['Position'].value_counts().plot(kind="pie", autopct="%1.1f%%")
  plt.title("Pie Chart of Position")
  plt.show()

print("1. Histogram Plot")
print("2. Bar Chart")
print("3. Pie Chart")
num = int(input("Enter any number from 1 to 3: "))
if num==1:
  histogram_plot()
elif num==2:
  plot_bar_chart()
elif num==3:
  plot_pie_chart()
else:
  print("Invalid Number")

# Line graph
#sorting data based on Salary
sorted_data = sorted(zip(selected_data['Salary'], selected_data['Position']), key=lambda x: x[1])

# Extract sorted lists
x = [data[1] for data in sorted_data]
y = [data[0] for data in sorted_data]

def line_graph():
  plt.plot(x, y, label='Position vs Salary')
  plt.xlabel('Position')
  plt.ylabel('Salary')
  plt.title('Line Graph')
  plt.legend()
  plt.show()

def scatter_graph():
  plt.scatter(x, y, label='Position vs Salary')
  plt.xlabel('Position')
  plt.ylabel('Salary')
  plt.title('Scatter Graph')
  plt.legend()
  plt.show()

print("1. Line Graph")
print("2. Scatter graph")
num = int(input("Enter any number from 1 or 2: "))
if num == 1:
  line_graph()
elif num == 2:
  scatter_graph()
else:
  print("Invalid Number")

def heatmap_plot():
    sns.heatmap(selected_data.corr(), annot=True)
    plt.title('Correlation Heatmap')
    plt.show()

def corner_plot():
    sns.pairplot(selected_data)
    plt.suptitle('Corner Plot')
    plt.show()

def box_plot():
    sns.boxplot(
        x=selected_data['Employee_Name'],
        y=selected_data['GenderID'],
        showmeans=True,
        data=selected_data
    )
    plt.title(f'Box Plot of gender by name')
    plt.show()

def violin_plot():
    sns.violinplot(
        x=selected_data['Employee_Name'],
        y=selected_data['GenderID'],
        showmeans=True,
        data=selected_data
    )
    plt.title(f'Violin Plot of gender by name')
    plt.show()

print("1. Heatmap")
print("2. Corner plot")
print("3. Box plot")
print("4. Violin plot")
num = int(input("Enter any number from 1 to 4: "))
if num == 1:
  heatmap_plot()
elif num == 2:
  corner_plot()
elif num == 3:
  box_plot()
elif num == 4:
  violin_plot()
else:
  print("Invalid Number")

print(selected_data.describe())

# Calculate the correlation matrix
correlation_matrix = selected_data.corr()

# Print the correlation matrix
print(correlation_matrix)

