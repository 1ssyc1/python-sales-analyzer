import csv

# Open and read our spreadsheet
with open('sales_data.csv', mode='r') as file:
    reader = csv.DictReader(file)

    total_sales = 0
    count = 0

    print("--- Reading Spreadsheet Data ---")
    for row in reader:
        sale_amount = int(row['Sales'])
        total_sales += sale_amount
        count += 1
        print(f"Month: {row['Month']} | Item: {row['Product']} | Sales: {sale_amount}")

    average_sales = total_sales / count
    print("--------------------------------")
    print(f"Total Sales across all months: {total_sales}")
    print(f"Average Monthly Sales: {average_sales}")