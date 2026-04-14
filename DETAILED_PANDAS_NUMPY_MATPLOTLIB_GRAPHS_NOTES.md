# Comprehensive Guide: Pandas, NumPy, Matplotlib & Graphs

---

## TABLE OF CONTENTS
1. [PANDAS - Data Analysis & Manipulation](#pandas)
2. [NUMPY - Numerical Computing](#numpy)
3. [MATPLOTLIB - Static Visualization](#matplotlib)
4. [GRAPHS & ADVANCED VISUALIZATION](#graphs)
5. [PLOTLY - Interactive Visualization](#plotly)
6. [Best Practices & Tips](#best-practices)

---

# PANDAS - Data Analysis & Manipulation {#pandas}

## Overview
Pandas is a powerful Python library for data manipulation and analysis, providing data structures for efficiently storing and manipulating large datasets.

### Key Data Structures
- **Series**: 1D labeled array (like a column)
- **DataFrame**: 2D labeled table (like a spreadsheet)
- **Index**: Labels for rows and columns

---

## 1. READING DATA

### From CSV Files
```python
import pandas as pd

# Basic read
df = pd.read_csv('file.csv')

# With options
df = pd.read_csv('file.csv', 
                  sep=',',           # Specify separator
                  header=0,          # Row number to use as column names
                  index_col=0,       # Set index column
                  encoding='utf-8')  # File encoding
```

### From Excel Files
```python
df = pd.read_excel('file.xlsx', sheet_name=0)  # Sheet index or name
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')
```

### From Other Formats
```python
# JSON
df = pd.read_json('file.json')

# HTML (reads all tables)
tables = pd.read_html('file.html')
df = tables[0]  # First table

# SQL Database
import sqlite3
conn = sqlite3.connect('database.db')
df = pd.read_sql_query("SELECT * FROM table_name", conn)

# Remote sources
df = pd.read_csv('https://example.com/data.csv')
```

---

## 2. INSPECTING DATA

### Basic Information
```python
# View first/last rows
df.head()      # First 5 rows
df.head(10)    # First 10 rows
df.tail()      # Last 5 rows
df.tail(10)    # Last 10 rows

# Basic statistics
df.describe()     # Statistical summary
df.info()         # Data types, non-null counts, memory usage
df.shape          # (rows, columns) tuple
df.columns        # Column names
df.index          # Row indices
df.dtypes         # Data types of each column

# Value information
df['column_name'].value_counts()      # Count unique values
df['column_name'].unique()            # Get unique values list
df.isnull().sum()                     # Count missing values per column
df.isnull()                           # Boolean mask of missing values
df.duplicated().sum()                 # Count duplicate rows
```

---

## 3. DATA SELECTION & INDEXING

### Using loc (Label-based)
```python
# Select by row label
df.loc[0]                    # First row

# Select by row and column labels
df.loc[0, 'column_name']     # Specific cell
df.loc[0:5, 'column_name']   # Rows 0-5, specific column

# Select multiple columns
df.loc[:, ['col1', 'col2']]  # All rows, specific columns

# Boolean indexing with loc
df.loc[df['age'] > 25]       # Rows where age > 25
df.loc[df['age'] > 25, 'name']  # Names of people over 25
```

### Using iloc (Position-based)
```python
# Select by integer position
df.iloc[0]                 # First row
df.iloc[0:5]               # Rows 0-4 (5 not included)
df.iloc[0:5, 0:3]          # First 5 rows, first 3 columns
df.iloc[[0, 2, 4]]         # Rows at positions 0, 2, 4
df.iloc[5:11]              # Rows at positions 5-10

# Horizontal selection
df.iloc[[5]].plot(kind='barh')  # Specific row as horizontal bar
```

### Boolean Indexing
```python
# Filter based on condition
mask = df['age'] > 25
df[mask]                    # Rows where condition is True

# Multiple conditions
df[(df['age'] > 25) & (df['city'] == 'NYC')]    # AND
df[(df['age'] > 25) | (df['age'] < 18)]         # OR
df[~mask]                   # NOT condition
```

### Direct Column Access
```python
df['column_name']           # Get entire column (Series)
df[['col1', 'col2']]        # Get multiple columns (DataFrame)
df.column_name              # Attribute access (if no spaces in name)
```

---

## 4. DATA CREATION & MODIFICATION

### Creating DataFrames
```python
# From dictionary
data = {'name': ['Alice', 'Bob'], 'age': [25, 30]}
df = pd.DataFrame(data)

# From numpy array
import numpy as np
df = pd.DataFrame(np.random.randn(10, 3), 
                  columns=['A', 'B', 'C'])

# With custom index
df = pd.DataFrame(np.random.randn(1000),
                  columns=['data'],
                  index=pd.date_range('2022/03/26', periods=1000))
```

### Adding & Modifying Columns
```python
# Add new column with constant value
df['new_col'] = 5

# Add column with formula
df['total'] = df['price'] * df['quantity']

# Add column with function
df['square'] = df['numbers'].apply(lambda x: x**2)

# Rename columns
df.rename(columns={'old_name': 'new_name'}, inplace=True)

# Drop columns
df.drop('column_name', axis=1, inplace=True)  # axis=1 for columns
df.drop(columns=['col1', 'col2'], inplace=True)
```

### Creating Calculated Columns
```python
# Using conditions
df['category'] = df['age'].apply(
    lambda x: 'Adult' if x >= 18 else 'Minor'
)

# Using vectorized operations (faster)
df['is_adult'] = df['age'] >= 18
```

---

## 5. DATA CLEANING

### Handling Missing Values
```python
# Identify missing values
df.isnull()               # Boolean mask of NaN values
df.notnull()              # Inverse of isnull()
df.isnull().sum()         # Count NaN per column

# Remove missing values
df.dropna()               # Drop rows with any NaN
df.dropna(how='all')      # Drop rows where all values are NaN
df.dropna(subset=['col1', 'col2'])  # Drop if NaN in specific columns
df.dropna(axis=1)         # Drop columns with NaN values

# Fill missing values
df.fillna(0)              # Fill with constant value
df.fillna({'col1': 0, 'col2': 'Unknown'})  # Fill specific columns
df.fillna(method='ffill')  # Forward fill (use previous value)
df.fillna(method='bfill')  # Backward fill (use next value)
df['col'].fillna(df['col'].mean())  # Fill with mean/median
```

### String Operations
```python
# Convert to lowercase/uppercase
df['name'] = df['name'].str.lower()
df['name'] = df['name'].str.upper()

# String methods
df['name'].str.len()          # Get length
df['name'].str.startswith('A')  # Check start
df['name'].str.contains('text')  # Check contains
df['name'].str.replace('old', 'new')  # Replace text

# Split strings
df[['first', 'last']] = df['name'].str.split(' ', expand=True)

# Extract with regex
df['numbers'] = df['text'].str.extract(r'(\d+)', expand=False)
```

### Removing Duplicates
```python
df.drop_duplicates()           # Remove exact duplicate rows
df.drop_duplicates(subset=['col1', 'col2'])  # Based on specific columns
df.drop_duplicates(keep='first')  # Keep first occurrence
df.drop_duplicates(keep='last')   # Keep last occurrence
df.duplicated().sum()          # Count duplicates
```

---

## 6. DATA GROUPING & AGGREGATION

### Group By Operations
```python
# Basic grouping
grouped = df.groupby('category')
grouped.sum()              # Sum for each group
grouped.mean()             # Average for each group
grouped.count()            # Count for each group
grouped.describe()         # Statistics for each group

# Multiple groupby
df.groupby(['category', 'region']).sum()

# Custom aggregation
df.groupby('category').agg({
    'price': 'sum',
    'quantity': 'mean',
    'name': 'count'
})

# Multiple aggregations same column
df.groupby('category')['price'].agg(['sum', 'mean', 'count'])
```

### Value Counts
```python
# Count occurrences
df['category'].value_counts()      # Counts in descending order
df['category'].value_counts(sort=False)
df['category'].value_counts(normalize=True)  # As proportions

# Multiple columns
df.groupby(['col1', 'col2']).size()
```

---

## 7. MERGING & JOINING DATA

### Merge (SQL-like joins)
```python
# Inner join (default)
result = pd.merge(df1, df2, on='key_column', how='inner')

# Different join types
result = pd.merge(df1, df2, on='key', how='left')    # Left join
result = pd.merge(df1, df2, on='key', how='right')   # Right join
result = pd.merge(df1, df2, on='key', how='outer')   # Full outer join

# Merge on different column names
result = pd.merge(df1, df2, left_on='id1', right_on='id2')

# Merge on index
result = pd.merge(df1, df2, left_index=True, right_index=True)
```

### Concatenate
```python
# Stack vertically (rows)
result = pd.concat([df1, df2])         # By default axis=0
result = pd.concat([df1, df2], axis=1)  # Stack horizontally (columns)
result = pd.concat([df1, df2], ignore_index=True)  # Reset index

# Append (deprecated, use concat)
df1 = df1.append(df2)
```

---

## 8. EXPORTING DATA

### Save to Different Formats
```python
# To CSV
df.to_csv('output.csv', index=False)

# To Excel
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)

# To JSON
df.to_json('output.json')

# To SQL Database
df.to_sql('table_name', conn, if_exists='replace')

# To HTML
df.to_html('output.html')

# To Clipboard
df.to_clipboard()
```

---

## 9. Advanced DataFrame Operations

### Pivot Tables
```python
# Basic pivot
pivot = df.pivot_table(
    values='amount',
    index='category',
    columns='region',
    aggfunc='sum'
)

# Multiple aggregations
pivot = df.pivot_table(
    values=['amount', 'quantity'],
    index='category',
    aggfunc={'amount': 'sum', 'quantity': 'mean'}
)
```

### Sorting
```python
# Sort by values
df.sort_values(by='column_name')
df.sort_values(by='column_name', ascending=False)

# Sort by multiple columns
df.sort_values(by=['col1', 'col2'])

# Sort by index
df.sort_index()
```

### Apply Functions
```python
# Apply to entire column
df['revenue'] = df['price'].apply(lambda x: x * 1.1)

# Apply to entire DataFrame
df.apply(lambda row: row['a'] + row['b'], axis=1)

# Apply custom function
def custom_func(x):
    if x > 100:
        return 'High'
    else:
        return 'Low'

df['category'] = df['price'].apply(custom_func)
```

---

# NUMPY - Numerical Computing {#numpy}

## Overview
NumPy is the fundamental package for numerical computing in Python, providing support for arrays and matrices along with mathematical functions.

---

## 1. ARRAY CREATION

### Basic Array Creation
```python
import numpy as np

# From lists
arr = np.array([1, 2, 3, 4])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Predefined arrays
np.zeros(5)              # [0. 0. 0. 0. 0.]
np.ones(5)               # [1. 1. 1. 1. 1.]
np.zeros((3, 4))         # 2D array of zeros (3x4)
np.ones((3, 4))          # 2D array of ones (3x4)
np.eye(5)                # Identity matrix (5x5)

# Sequence generation
np.arange(0, 10)         # [0 1 2 3 4 5 6 7 8 9]
np.arange(0, 10, 2)      # [0 2 4 6 8]
np.linspace(0, 1, 5)     # Evenly spaced: [0.   0.25 0.5  0.75 1.  ]
np.logspace(0, 3, 4)     # Logarithmically spaced

# Random arrays
np.random.rand(5)        # 5 random floats between 0-1
np.random.randn(5)       # 5 random normal distribution
np.random.randint(0, 10, 5)  # 5 random integers 0-9
```

---

## 2. ARRAY PROPERTIES

### Shape and Dimensions
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

arr.shape      # (2, 3) - 2 rows, 3 columns
arr.ndim       # 2 - number of dimensions
arr.size       # 6 - total elements
arr.dtype      # dtype('int64') - data type
arr.nbytes     # Memory usage in bytes

arr.T          # Transpose (flip rows/columns)
arr.flatten()  # Convert to 1D array
```

### Data Types
```python
arr = np.array([1, 2, 3], dtype=np.int32)
arr = np.array([1.0, 2.0], dtype=np.float64)
arr = np.array(['a', 'b'], dtype=str)

# Type conversion
arr.astype(float)
arr.astype(int)
arr.astype(str)
```

---

## 3. RESHAPING & RESIZING

### Reshape Operations
```python
arr = np.arange(12)        # [0 1 2 3 4 5 6 7 8 9 10 11]

arr.reshape(3, 4)          # 3x4 matrix
arr.reshape(2, 2, 3)       # 2x2x3 3D array
arr.reshape(-1)            # Flatten (automatic size)
arr.reshape(-1, 4)         # Unknown rows, 4 columns

# Non-modifying reshape
new_arr = np.reshape(arr, (3, 4))
```

### Resizing
```python
# Resize with repetition
arr = np.arange(4)
np.resize(arr, 8)          # [0 1 2 3 0 1 2 3]

# Repeating elements
np.repeat(arr, 3)          # [0 0 0 1 1 1 2 2 2 3 3 3]
np.tile(arr, 3)            # [0 1 2 3 0 1 2 3 0 1 2 3]
```

---

## 4. MATHEMATICAL OPERATIONS

### Element-wise Operations
```python
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Arithmetic
a + b           # [6 8 10 12]
a - b           # [-4 -4 -4 -4]
a * b           # [5 12 21 32]
a / b           # Element-wise division
a ** 2          # [1 4 9 16] - power
a % 2           # Modulo

# Scalar operations
a + 5           # Add 5 to each element
a * 2           # Multiply each element by 2
10 - a          # [9 8 7 6]
```

### Mathematical Functions
```python
a = np.array([1, 2, 3, 4])

# Basic functions
np.sqrt(a)      # Square root
np.exp(a)       # Exponential (e^x)
np.log(a)       # Logarithm
np.sin(a)       # Trigonometric functions
np.cos(a)
np.tan(a)

# Rounding
np.round(a * 0.5)      # Round to nearest integer
np.floor(a * 0.5)      # Round down
np.ceil(a * 0.5)       # Round up

# Absolute value
np.abs([-1, -2, 3])    # [1 2 3]
```

### Aggregation Functions
```python
a = np.array([1, 2, 3, 4, 5])

# Single value aggregations
np.sum(a)          # Sum all elements
np.mean(a)         # Average
np.std(a)          # Standard deviation
np.var(a)          # Variance
np.min(a)          # Minimum value
np.max(a)          # Maximum value

# 2D array aggregation
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
np.sum(arr_2d)              # Sum all: 21
np.sum(arr_2d, axis=0)      # Sum columns: [5 7 9]
np.sum(arr_2d, axis=1)      # Sum rows: [6 15]

# Cumulative operations
np.cumsum(a)               # [1 3 6 10 15]
np.cumprod(a)              # [1 2 6 24 120]
```

---

## 5. BROADCASTING

### How Broadcasting Works
Broadcasting allows operations on arrays of different shapes following these rules:
1. If arrays have different ranks, pad the smaller with 1s
2. Arrays compatible if dimensions match or one is 1
3. Missing dimensions treated as 1

### Examples
```python
a = np.array([[1, 2, 3], [4, 5, 6]])    # Shape: (2, 3)
b = np.array([1, 2, 3])                 # Shape: (3,)

# b is broadcast to (1, 3) then to (2, 3)
result = a + b
# [[2 4 6]
#  [5 7 9]]

# Scalar broadcasting
a + 10              # Adds 10 to all elements

# Column/Row broadcasting
a = np.array([[1], [2], [3]])           # Shape: (3, 1)
b = np.array([1, 2, 3])                 # Shape: (3,)
a + b               # Result: (3, 3)
```

---

## 6. INDEXING & SLICING

### 1D Array Indexing
```python
arr = np.array([10, 20, 30, 40, 50])

arr[0]              # 10 (first element)
arr[-1]             # 50 (last element)
arr[1:4]            # [20 30 40] (indices 1, 2, 3)
arr[:3]             # [10 20 30] (first 3)
arr[2:]             # [30 40 50] (from index 2 onwards)
arr[::2]            # [10 30 50] (every 2nd element)
```

### 2D Array Indexing
```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr[0]              # [1 2 3] - first row
arr[0, 1]           # 2 - row 0, column 1
arr[1:3]            # Rows 1 and 2
arr[:, 0]           # [1 4 7] - first column
arr[:, 1:3]         # All rows, columns 1-2
arr[1:3, 1:3]       # 2x2 subarray
```

### Fancy Indexing
```python
arr = np.array([10, 20, 30, 40, 50])

# Using list of indices
arr[[0, 2, 4]]              # [10 30 50]

# Boolean indexing
mask = arr > 25
arr[mask]                   # [30 40 50]

# 2D fancy indexing
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
arr_2d[[0, 2]]              # Rows 0 and 2
arr_2d[[0, 2], [1, 0]]      # arr_2d[0,1] and arr_2d[2,0]
```

---

## 7. MEMORY & VIEWS

### Copies vs Views
```python
original = np.array([1, 2, 3, 4, 5])

# View (doesn't copy data)
view = original[1:4]
view[0] = 99  # Modifies original!

# Copy (independent data)
copy = original[1:4].copy()
copy[0] = 99  # Doesn't affect original

# Check if view or copy
view.base is original       # True if view
copy.base is original       # Likely False
```

### Memory Layout
```python
arr = np.arange(12).reshape(3, 4)
arr.flags                   # Check memory flags
arr.strides                 # Memory strides
np.shares_memory(arr, copy)  # Check if shares memory
```

---

## 8. LINEAR ALGEBRA

### Matrix Operations
```python
import numpy.linalg as la

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
np.dot(A, B)                # Matrix product
A @ B                       # @ operator (Python 3.5+)

# Transpose
A.T

# Determinant
la.det(A)

# Inverse
la.inv(A)

# Rank
la.matrix_rank(A)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = la.eig(A)

# Solving linear equations (Ax = b)
x = la.solve(A, np.array([1, 2]))
```

### Vector Operations
```python
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Dot product
np.dot(v1, v2)              # 1*4 + 2*5 + 3*6 = 32

# Cross product
np.cross(v1, v2)

# Vector norm
la.norm(v1)                 # Magnitude of vector
```

---

# MATPLOTLIB - Static Visualization {#matplotlib}

## Overview
Matplotlib is a plotting library for creating static, animated, and interactive visualizations in Python.

---

## 1. BASIC SETUP & CONFIGURATION

### Import and Basic Structure
```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Figure and Axes
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])

# Or simpler (implicit figure/axes)
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
```

### Figure Sizing
```python
# Set figure size
plt.figure(figsize=(12, 6))    # Width=12, Height=6 inches
plt.figure(figsize=(40, 10))   # Large figure
plt.figure(dpi=100)            # Resolution

# In pandas (returns matplotlib axes)
df.plot(figsize=(40, 10))
```

---

## 2. PANDAS PLOTTING

### Line Plots
```python
df = pd.DataFrame(np.random.randn(100), 
                  columns=['value'],
                  index=pd.date_range('2022/01/01', periods=100))

# Simple line plot
df.plot()
df.plot(figsize=(40, 10))
df['column'].plot()

# Line plot options
df.plot(figsize=(15, 6), 
        color='blue',
        linewidth=2,
        linestyle='--',
        alpha=0.7)
```

### Bar Plots
```python
# Vertical bar chart
df.plot(kind='bar', figsize=(15, 6))

# Horizontal bar chart
df.plot(kind='barh', figsize=(15, 6))

# With specific rows
df.iloc[5:11].plot(kind='bar', figsize=(40, 10))

# Multiple series bars
df[['col1', 'col2']].plot(kind='bar', figsize=(15, 6))
```

### Histogram
```python
# Basic histogram
df.plot(kind='hist', figsize=(40, 10))

# Single column histogram
df['column'].plot(kind='hist', orientation='horizontal')

# Styled histogram
df.hist(figsize=(40, 10), color='green', alpha=0.9)

# With bins
df['column'].plot(kind='hist', bins=20)
```

### Box Plot
```python
# Box plot
df.plot(kind='box', figsize=(40, 10))

# Horizontal box plot
df.plot(kind='box', figsize=(40, 10), vert=False)

# Colored box plot
df.plot(kind='box',
        figsize=(40, 10),
        color={'boxes': 'green', 'whiskers': 'red'},
        vert=False)
```

### Area Plot
```python
# Stacked area plot
df.plot(kind='area', figsize=(40, 10), stacked=True)

# Non-stacked area plot with transparency
df.plot(kind='area', figsize=(40, 10), alpha=0.4, stacked=False)
```

### Scatter Plot
```python
# Basic scatter
df.plot.scatter(x='col1', y='col2', figsize=(10, 6))

# With color mapping
dfi.plot.scatter(x='SepalLengthCm', y='PetalLengthCm',
                c='SepalWidthCm',        # Color by column
                s=dfi['PetalWidthCm']*500,  # Size by column
                figsize=(40, 10))
```

### Hexbin Plot
```python
# Hexagonal binning (for dense data)
df.plot.hexbin(x='col1', y='col2', 
              gridsize=10,
              C='col3',                 # Color by column
              figsize=(10, 6))
```

### Pie Chart
```python
# Pie chart for entire DataFrame
df.plot(kind='pie')

# Single row as pie
row = df.drop(columns=['Species']).iloc[0]
row.plot(kind='pie', figsize=(40, 10))
```

---

## 3. PLOT CUSTOMIZATION

### Colors and Styles
```python
# Color specification
plt.plot([1, 2, 3], color='red')       # By name
plt.plot([1, 2, 3], color='#FF0000')   # By hex
plt.plot([1, 2, 3], color='0.5')       # By gray value (0-1)
plt.plot([1, 2, 3], 'r-')              # Shorthand: red, solid line

# Line styles
'-'   # Solid line
'--'  # Dashed line
'-.'  # Dash-dot
':'   # Dotted

# Markers
'o'   # Circle
's'   # Square
'^'   # Triangle
'*'   # Star
'+'   # Plus
'x'   # X mark
```

### Transparency and Width
```python
# Transparency (alpha)
df.plot(alpha=0.7)         # 70% opaque
df.plot(alpha=0.4)         # 40% opaque

# Line width
df.plot(linewidth=2)
df.plot(lw=1.5)

# Marker size
plt.scatter([1, 2, 3], [1, 4, 9], s=100)  # Size in points
```

### Labels and Titles
```python
plt.plot([1, 2, 3], [1, 4, 9])
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('Plot Title')
plt.legend(['Series 1', 'Series 2'])

# With DataFrame
ax = df.plot()
ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.set_title('Time Series')
```

---

# GRAPHS & ADVANCED VISUALIZATION {#graphs}

## 1. INTERACTIVE VISUALIZATION WITH CUFFLINKS

### Setup
```python
import cufflinks as cf
import plotly.graph_objects as go

cf.go_offline()  # Use offline mode
```

### 2D Interactive Plots
```python
# Interactive line/area plot
df.iplot()

# Scatter plot
df.iplot(x='col1', y='col2', mode='markers', kind='scatter')

# Multiple series
df.iplot(kind="scatter", mode='markers', size=10)
```

### 3D Interactive Plots
```python
# 3D Scatter plot
df.iplot(kind='scatter3d', 
         x='SepalLengthCm', 
         y='SepalWidthCm', 
         z='PetalLengthCm')

# 3D Bubble plot
df.iplot(kind='bubble3d',
         x='SepalLengthCm',
         y='SepalWidthCm',
         z='PetalLengthCm',
         size='PetalWidthCm')
```

### Bubble Charts
```python
# 2D Bubble
df.iplot(kind='bubble',
         x='SepalLengthCm',
         y='PetalLengthCm',
         size='SepalWidthCm')
```

### Scatter Matrix
```python
# Pairwise scatter plots
df.scatter_matrix()
```

---

## 2. MATPLOTLIB ADVANCED PLOTTING

### Creating Multiple Subplots
```python
import matplotlib.pyplot as plt

# 2x2 grid
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot([1, 2, 3])
axes[0, 1].bar([1, 2, 3], [1, 4, 9])
axes[1, 0].scatter([1, 2, 3], [1, 4, 9])
axes[1, 1].hist([1, 1, 2, 2, 2, 3, 3, 3, 3])

plt.tight_layout()  # Adjust spacing
plt.show()
```

### Combining Plots
```python
# Add multiple series to same plot
plt.figure(figsize=(12, 6))
plt.plot(df['col1'], label='Series 1')
plt.plot(df['col2'], label='Series 2')
plt.legend()
plt.show()
```

---

## 3. STATISTICAL VISUALIZATION WITH SEABORN

### Installation
```python
import seaborn as sns
import matplotlib.pyplot as plt
```

### Relationship Plots
```python
df = pd.read_csv('data.csv')

# Scatter plot with regression line
sns.relplot(data=df, x='col1', y='col2', kind='scatter')

# With hue (color by category)
sns.relplot(data=df, x='col1', y='col2', hue='category')

# With style and size
sns.relplot(data=df, x='col1', y='col2', 
           hue='category', style='type', size='value')

# Faceted plots
sns.relplot(data=df, x='col1', y='col2',
           col='category')  # Separate plots per category
```

### Categorical Plots
```python
# Box plot
sns.catplot(data=df, x='category', y='value', kind='box')

# Violin plot
sns.catplot(data=df, x='category', y='value', kind='violin')

# Strip plot
sns.catplot(data=df, x='category', y='value', kind='strip')

# Bar plot
sns.catplot(data=df, x='category', y='value', kind='bar')
```

### Distribution Plots
```python
# Histogram with KDE
sns.distplot(df['column'])

# Kernel Density Estimate
sns.kdeplot(data=df, x='column')

# 2D KDE
sns.kdeplot(data=df, x='col1', y='col2')
```

### Pair Plots
```python
# Pairwise relationships
sns.pairplot(df)

# With hue
sns.pairplot(df, hue='category')

# With different plot kinds
sns.pairplot(df, diag_kind='hist', plot_kws={'alpha': 0.6})
```

### Themes
```python
# Set theme
sns.set_theme(style="darkgrid")
sns.set_theme(style="whitegrid")
sns.set_theme(style="dark")

# Color palettes
sns.set_palette("husl")
sns.set_palette("Set2")
```

---

# PLOTLY - Interactive Visualization {#plotly}

## Overview
Plotly provides interactive web-based visualizations with hover information, zooming, and panning capabilities.

---

## 1. SETUP & BASIC PLOTS

### Installation and Import
```python
import plotly.express as px
import plotly.graph_objects as go
import cufflinks as cf

# For offline viewing
cf.go_offline()
```

### 2D Plots
```python
# Line plot
fig = px.line(df, x='date', y='value', title='Line Plot')
fig.show()

# Scatter plot
fig = px.scatter(df, x='col1', y='col2', 
                title='Scatter Plot',
                color='category')
fig.show()

# Bar chart
fig = px.bar(df, x='category', y='value',
            title='Bar Chart')
fig.show()
```

### 3D Plots
```python
# 3D Scatter
fig = px.scatter_3d(df, x='col1', y='col2', z='col3',
                   color='category')
fig.show()

# 3D Surface
z_data = np.random.randn(10, 10)
fig = go.Figure(data=[go.Surface(z=z_data)])
fig.show()
```

---

## 2. CUFFLINKS INTEGRATION WITH PANDAS

### Basic Usage
```python
import cufflinks as cf
cf.go_offline()

# Line plot from DataFrame
df.iplot()

# Scatter plot
df.iplot(kind='scatter', x='col1', y='col2', mode='markers')

# Bubble chart
df.iplot(kind='bubble', x='col1', y='col2', size='col3')

# 3D scatter
df.iplot(kind='scatter3d', x='col1', y='col2', z='col3')

# 3D bubble
df.iplot(kind='bubble3d', x='col1', y='col2', z='col3',
        size='col4')

# Scatter matrix
df.scatter_matrix()
```

---

# BEST PRACTICES & TIPS {#best-practices}

## Data Analysis Workflow

### 1. Data Loading & Exploration
```python
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data.csv')

# Quick exploration checklist
print(df.shape)              # Understand size
print(df.info())             # Check data types
print(df.head())             # Look at sample
print(df.describe())         # Statistical summary
print(df.isnull().sum())     # Check missing values
print(df.duplicated().sum()) # Check duplicates
```

### 2. Data Cleaning
```python
# Handling missing values
df.fillna(df.mean())         # Fill with mean
df.dropna()                  # Remove rows

# Remove duplicates
df.drop_duplicates()         # Keep first
df.drop_duplicates(keep='last')  # Keep last

# Convert data types
df['date'] = pd.to_datetime(df['date'])
df['category'] = df['category'].astype('category')
```

### 3. Data Transformation
```python
# Create new columns
df['ratio'] = df['A'] / df['B']

# Normalize/Standardize
df_norm = (df - df.mean()) / df.std()

# One-hot encoding
df_encoded = pd.get_dummies(df, columns=['category'])

# Binning
df['age_group'] = pd.cut(df['age'], bins=[0, 18, 65, 100],
                         labels=['Child', 'Adult', 'Senior'])
```

### 4. Data Analysis
```python
# Groupby analysis
df.groupby('category').sum()
df.groupby(['cat1', 'cat2']).agg({'val': 'mean'})

# Pivot tables
pivot = df.pivot_table(values='amount', index='date',
                       columns='category', aggfunc='sum')

# Correlation
df.corr()                    # Correlation matrix
df['col1'].corr(df['col2'])  # Correlation between columns
```

### 5. Visualization
```python
# Start simple
df.plot()  # Quick overview

# Explore relationships
df.plot(kind='scatter', x='A', y='B')

# Compare groups
df.groupby('category')['value'].mean().plot(kind='bar')

# Time series
df.set_index('date').plot()

# Distribution
df['value'].plot(kind='hist', bins=50)
```

---

## Performance Tips

### Pandas Optimization
```python
# Use appropriate data types to save memory
df['small_int'] = df['small_int'].astype('int8')  # Instead of int64
df['category'] = df['category'].astype('category')

# Vectorized operations (much faster than loops)
# Bad:
result = []
for val in df['column']:
    result.append(val * 2)

# Good:
result = df['column'] * 2

# Use query for complex filtering
df.query('age > 25 and salary > 50000')  # Faster than loc/boolean

# Use groupby efficiently
df.groupby('category', as_index=False)['value'].transform('mean')
```

### NumPy Optimization
```python
# Pre-allocate arrays
result = np.empty(1000)  # Instead of appending

# Use vectorized functions
result = np.sqrt(arr)    # Instead of loop with math.sqrt

# Avoid copies
view = arr[1:4]          # View (no copy)
copy = arr[1:4].copy()   # Copy (when needed)

# Use appropriate dtypes
arr = np.array([1, 2, 3], dtype=np.int32)  # Smaller than int64
```

### Matplotlib Optimization
```python
# Set figure size once
fig, ax = plt.subplots(figsize=(12, 6))

# Use ax instead of plt for more control
ax.plot(data)
ax.set_title('Title')
ax.set_xlabel('X')

# Reduce data points for large datasets
df.sample(n=1000).plot()  # Plot sample instead of all data
```

---

## Common Mistakes to Avoid

### 1. Pandas
```python
# WRONG: Modifying copy, not original
df_copy = df  # This is a view, not a copy
df_copy['col'] = 'value'  # Modifies original!

# RIGHT: Make explicit copy
df_copy = df.copy()

# WRONG: Not handling missing values
df.groupby('cat').mean()  # NaN values affect results

# RIGHT: Handle them first
df.dropna().groupby('cat').mean()

# WRONG: Chaining operations inefficiently
result = df[df['a'] > 5][df['b'] < 10]  # Multiple passes

# RIGHT: Combine conditions
result = df[(df['a'] > 5) & (df['b'] < 10)]
```

### 2. NumPy
```python
# WRONG: Matrix multiplication with *
A * B  # Element-wise, not matrix multiplication

# RIGHT: Use @ or np.dot
A @ B  # Matrix multiplication
np.dot(A, B)

# WRONG: Broadcasting confusion
a = np.array([1, 2, 3])  # Shape: (3,)
b = np.array([[1], [2]])  # Shape: (2, 1)
# Result shape will be (2, 3) due to broadcasting

# RIGHT: Understand broadcasting rules
```

### 3. Matplotlib
```python
# WRONG: Overlapping plots
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.show()  # May overlap

# RIGHT: Manage figure/axes explicitly
fig, ax = plt.subplots()
ax.plot(x1, y1, label='Series 1')
ax.plot(x2, y2, label='Series 2')
ax.legend()
plt.show()

# WRONG: Large text on small figure
plt.figure()  # Default size too small
plt.title('Title', fontsize=20)  # Text too big

# RIGHT: Set appropriate figure size
plt.figure(figsize=(12, 6))
plt.title('Title', fontsize=12)
```

---

## Quick Reference - Common Operations

### Pandas Quick Ref
| Operation | Code |
|-----------|------|
| Load CSV | `df = pd.read_csv('file.csv')` |
| First rows | `df.head()` |
| Info | `df.info()` |
| Statistics | `df.describe()` |
| Filter rows | `df[df['col'] > 5]` |
| Select columns | `df[['col1', 'col2']]` |
| Group by | `df.groupby('cat').sum()` |
| Pivot | `df.pivot_table(...)` |
| Merge | `pd.merge(df1, df2, on='key')` |
| Sort | `df.sort_values(by='col')` |
| Fill NaN | `df.fillna(0)` |
| Save CSV | `df.to_csv('file.csv')` |

### NumPy Quick Ref
| Operation | Code |
|-----------|------|
| Create array | `np.array([1, 2, 3])` |
| Zeros | `np.zeros(5)` |
| Random | `np.random.rand(5)` |
| Range | `np.arange(0, 10)` |
| Reshape | `arr.reshape(3, 3)` |
| Sum | `np.sum(arr)` |
| Mean | `np.mean(arr)` |
| Element-wise | `arr1 + arr2` |
| Matrix mult | `arr1 @ arr2` |
| Transpose | `arr.T` |
| Index | `arr[1:4]` |
| Boolean index | `arr[arr > 5]` |

### Matplotlib Quick Ref
| Operation | Code |
|-----------|------|
| Line plot | `df.plot()` |
| Bar chart | `df.plot(kind='bar')` |
| Scatter | `df.plot.scatter(x='col1', y='col2')` |
| Histogram | `df.plot(kind='hist')` |
| Box plot | `df.plot(kind='box')` |
| Figure size | `plt.figure(figsize=(12, 6))` |
| Title | `plt.title('Title')` |
| Labels | `plt.xlabel('X')` |
| Legend | `plt.legend()` |
| Subplots | `fig, axes = plt.subplots(2, 2)` |
| Colors | `color='red'` |
| Alpha | `alpha=0.7` |

---

## Resources and Next Steps

### Topics to Explore Further
- Statistical Analysis (SciPy)
- Machine Learning (scikit-learn)
- Advanced Plotting (Plotly Dash, Bokeh)
- Time Series Analysis (statsmodels)
- Natural Language Processing (NLTK, spaCy)

### Useful Documentation Links
- Pandas: https://pandas.pydata.org/docs/
- NumPy: https://numpy.org/doc/
- Matplotlib: https://matplotlib.org/
- Plotly: https://plotly.com/python/
- Seaborn: https://seaborn.pydata.org/

---

**Document Created**: Comprehensive study guide covering Pandas, NumPy, Matplotlib, and Graph Visualization
**Last Updated**: 2026
**Total Topics**: 50+ with 200+ code examples

