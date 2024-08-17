import pyexcel as pe
#Reading excel
data = pe.get_sheet(file_name="example.xlsx")
print(data)

#Saving Excel
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"]
]
pe.save_as(array=data, dest_file_name="output.xlsx")

#Accessing
book = pe.get_book(file_name="example.xlsx")
sheet = book["Sheet1"]
print(sheet)

# Convert an Excel file to CSV
pe.convert(file_name="example.xlsx", dest_file_name="output.csv")

# Convert a CSV file to Excel
pe.convert(file_name="example.csv", dest_file_name="output.xlsx")

# Read the Excel file
sheet = pe.get_sheet(file_name="data.xlsx")

# Print all rows
for row in sheet.row:
    print(row)
