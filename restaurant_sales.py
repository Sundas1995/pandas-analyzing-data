import pandas as pd
csv_file_path = r'D:\Work\DAproject\restaurant_sales.csv'
df = pd.read_csv(csv_file_path)

#Display the first few rows of the dataset
print('First few rows of the dataset')
print(df.head())

#Display Column Names
print('Display Column names')
print(df.columns)

#Number of rows and columns
print(df.shape)

#Basic information about the dataset
print(df.info())

#Statistical summery of numeric columns
print('Statistical summary')
print(df.describe())

#checking for missing values
print('----------------------------------')
print(df.isnull().sum())
print()

mode_value = df['transaction_type'].mode()[0]
df['transaction_type'].fillna(mode_value, inplace=True)
#handling missing values 
print('Replacing missing values with mode')
print(df.isnull().sum())

#checking for duplicates
duplicate_rows = df.duplicated()
print('Duplicates:')
print(df[duplicate_rows])

#outliers
print('Outliers:')
for column in ['item_price', 'quantity', 'transaction_amount']:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    print(f"Potential outliers for {column}:")
    print(outliers)

    
#datatypes
print('Datatypes of columns')
print(df.dtypes)

# Replace '-' with '/'
df['date'] = df['date'].str.replace('-', '/')

# Convert to datetime
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')
print(df['date'].head())

#checking datatypes now
print(df.dtypes)
print(df[df['date'].isna()])


#unique values
unique_values = df['time_of_sale'].unique()
print(unique_values)
unique_values = df['received_by'].unique()
print(unique_values)
unique_values= df['transaction_type'].unique()
print(unique_values)
unique_values = df['item_type'].unique()
print(unique_values)

#save the modifications in a new file
df.to_csv('D:/Work/DAproject/cleaned_data.csv',index=False)
