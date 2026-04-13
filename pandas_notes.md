# pandas_notes

## Overview
This document collects pandas notes from:
- `031.pandas day 2.ipynb`
- `032.pandas class 3.ipynb`
- `033.pandas 4.ipynb`
- `034.pandas class homework discussed.ipynb`
- `035.pandas and numpy.ipynb`
- `topic-wise/5. Pandas Class 23-25/9. iNeuron Pandas 23 - 25 Class.ipynb`

`pandas` is a Python library for data analysis, providing `Series` and `DataFrame` as primary data structures.

## 1. Importing pandas
```python
import pandas as pd
```

## 2. Reading data
### CSV files
```python
df = pd.read_csv('./data/sample-csv/titanic.csv')
```

### Common CSV options
- `header=None` → no header row
- `names=[...]` → custom column names
- `sep='|'` or `sep='\t'` → specify delimiter
- `skiprows=[1, 3]` → skip specific rows

### Remote CSV
```python
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
```

### Excel files
```python
df = pd.read_excel('./data/sample-excel/LUSID Excel - Manage Orders.xlsx')
```

### Read all sheets
```python
xls = pd.ExcelFile('./data/sample-excel/LUSID Excel - Manage Orders.xlsx')
print(xls.sheet_names)
for sheet in xls.sheet_names:
    sheet_df = pd.read_excel('./data/sample-excel/LUSID Excel - Manage Orders.xlsx', sheet_name=sheet)
```

### HTML tables
```python
import requests
import re
url = 'https://www.basketball-reference.com/leagues/NBA_2015_totals.html'
headers = {'User-Agent': 'Mozilla/5.0'}
res = requests.get(url, headers=headers)
html = re.sub('<!--|-->', '', res.text)
df_list = pd.read_html(html)
df = df_list[0]
```

### JSON data
```python
df = pd.read_json('https://api.github.com/repos/pandas-dev/pandas/issues')
```

## 3. Inspecting DataFrames
```python
df.head(5)
df.tail(5)
df.columns
df.dtypes
df.info()
df.describe()
```

## 4. Selecting columns
```python
a = df['name']              # Series
sub_df = df[['name', 'location_id', 'id']]  # DataFrame
```

## 5. Row and column selection
```python
df.loc[0:4, ['order_id','order_date','ship_date']]
df.iloc[1:6, 3:6]
```

## 6. Missing values
```python
df.isnull().sum()
missing_rows = df[df['Age'].isnull()]

df.fillna(value='sudh')
df.fillna(value=df['Age'].mean())
```

### Drop missing values
```python
df.dropna(axis=1)
df.dropna(axis=0, how='all')
df.dropna(thresh=3)
```

## 7. Creating and modifying columns
```python
df['ineuron'] = 'sudh'
df['New'] = df['SibSp'] + df['Parch']
df['sales'] = df['sales'].str.replace(',', '').astype(int)
```

## 8. String operations
```python
df['cabin_Number'] = df['Cabin'].str.replace('([A-Za-z]+)', '')
df['cabin_Letter'] = df['Cabin'].str.extract('([A-Za-z]+)')
```

## 9. Filtering and conditions
```python
df[df['Age'] < 25]
df[(df['Survived'] == 0) & (df['Age'] < 40)]
df[df['Name'].str.startswith('S')]
```

## 10. Grouping and aggregation
```python
df.groupby('Pclass')['Pclass'].count()
df.groupby('Survived').describe()['PassengerId']
df1.groupby(['contact', 'y']).count()
```

Examples:
- number of male/female passengers
- survived vs casualties
- count by ticket class
- average rating and weekly summaries

## 11. Concatenation and merging
### Concatenation
```python
df2 = pd.concat([df2, df3])
df2 = pd.concat([df2, df3], axis=1)
```

### Merge
```python
df_left = pd.merge(df4, df5, how='left', on='emp_id')
df_right = pd.merge(df4, df5, how='right', on='emp_id')
```

### Merge with different keys
```python
pd.merge(df6, df7, left_on='emp_id1', right_on='emp_id2', how='inner')
```

### Join with index
```python
df2 = df2.set_index('age')
df3 = df3.set_index('age')
df2.join(df3, how='inner')
```

## 12. DataFrame creation from dictionaries
```python
data = {
    'name': ['sudh', 'krish', 'hitesh', 'tulesko'],
    'salary': [100, 200, 300, 400],
    'mail_id': ['sudh@ineuron.ai', 'krish@ineuron.ai', 'hitesh@ineuron.ai', 'tulesko@ineuron.ai'],
    'addr': ['blr', 'blr', 'blr', 'mum']
}
df = pd.DataFrame(data)
```

## 13. Exporting data
```python
df.to_csv('NBA.csv', index=False)
```

## 14. Useful pandas notes from iNeuron class
- `pd.read_html()` is useful for scraping HTML tables.
- Use raw strings for Windows file paths: `r'.\data\sample-csv\taxonomy.csv'`.
- `pd.ExcelFile(...).sheet_names` lists worksheet names.
- `pd.read_csv()` supports remote URLs directly.
- Use `.str` functions for string extraction and replacement.

## 15. Practice tasks
1. Count male vs female passengers
2. Count survivors and casualties
3. Find the oldest passenger name
4. Count passengers by class
5. Count names starting with a specific letter
6. Create a new column from existing columns
7. Filter on age and survival conditions
8. Separate text and numeric parts from a cabin field
9. Analyze bank dataset with age, housing, loan, and campaign metrics
10. Group by education or contact method and count

---
Generated from the selected pandas notebooks listed above.
