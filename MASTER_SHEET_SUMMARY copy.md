# 📚 COMPREHENSIVE MASTER SHEET - iNeuron Classes Learning Path

**Created:** April 14, 2026  
**Total Notebooks:** 650+  
**Organized by:** Learning Progression, Topics, and Concepts

---

## 📖 TABLE OF CONTENTS

1. [Curriculum Overview](#curriculum-overview)
2. [Python Fundamentals](#python-fundamentals)
3. [Object-Oriented Programming](#object-oriented-programming)
4. [Data Structures & Algorithms](#data-structures--algorithms)
5. [Database Management](#database-management)
6. [Data Analysis & Visualization](#data-analysis--visualization)
7. [Machine Learning](#machine-learning)
8. [Deep Learning & Neural Networks](#deep-learning--neural-networks)
9. [Natural Language Processing](#natural-language-processing)
10. [Time Series Analysis](#time-series-analysis)
11. [Web Development & APIs](#web-development--apis)
12. [Practice Tasks & Projects](#practice-tasks--projects)
13. [Quick Reference Guide](#quick-reference-guide)

---

## 🎯 CURRICULUM OVERVIEW

### Learning Path Structure

```
Level 1: PYTHON BASICS
├── Basic Syntax & Concepts (Classes 0-5)
├── Control Flow (Classes 6-9)
├── Functions (Class 10)
├── File Handling (Class 11)
├── Exception Handling (Classes 13-14)
└── Logging & Debugging (Classes 15-16)

Level 2: OBJECT-ORIENTED PROGRAMMING
├── Classes & Objects (Class 10)
├── Inheritance (Class 17)
├── Polymorphism & Encapsulation (Classes 18-20)
├── Advanced OOP Concepts
└── Design Patterns

Level 3: DATA STRUCTURES & ALGORITHMS
├── Lists, Tuples, Sets (Classes 5-6)
├── Dictionaries (Class 6)
├── Iterators & Generators (Class 12)
├── Map, Filter, Reduce, Zip (Class 28)
└── Algorithm Design

Level 4: DATABASE MANAGEMENT
├── SQL Fundamentals (Classes 25-26)
├── SQLite & SQL Operations (Class 28)
├── MongoDB (Classes 27, 21-22)
└── Database Design & Queries

Level 5: DATA ANALYSIS
├── NumPy Arrays (Classes 26-27)
├── Pandas DataFrames (Classes 23-25, 29-35)
├── Data Cleaning & Manipulation
└── Exploratory Data Analysis (EDA)

Level 6: DATA VISUALIZATION
├── Matplotlib (Class 28-29)
├── Seaborn (Class 29)
├── Plotly & Interactive Graphs
└── Advanced Visualization Techniques

Level 7: MACHINE LEARNING
├── Linear & Logistic Regression
├── Classification Algorithms (SVM, Decision Trees, etc.)
├── Clustering (K-Means)
├── Model Evaluation & Tuning
└── Feature Engineering

Level 8: DEEP LEARNING
├── Neural Networks Basics
├── Convolutional Neural Networks (CNN)
├── Recurrent Neural Networks (RNN/LSTM)
├── Transfer Learning
└── Object Detection

Level 9: SPECIALIZED TOPICS
├── Natural Language Processing (NLP)
├── Time Series Analysis
├── Web Scraping
├── API Development
└── GUI Development (Tkinter)
```

---

## 📝 PYTHON FUNDAMENTALS

### Level: Beginner | Time: 5-10 hours

#### **1. Basic Syntax & Concepts**
**Notebooks:** 000.python basic, 001.python basic  
**Key Topics:**
- Print statements and output formatting
- Variable declaration and assignment
- Data types: int, float, str, bool
- Type conversion and casting
- Comments and documentation

**Key Concepts:**
```
- Variables: Dynamic typing in Python
- Data Types: int, float, str, bool, None
- Operators: Arithmetic, Comparison, Logical
- String Formatting: f-strings, format(), %
- Input/Output: input(), print()
```

#### **2. Control Flow - Conditionals**
**Notebooks:** 021.if else for loop, 2-Control Flow/Conditionalstatements  
**Key Topics:**
- If-else-elif statements
- Nested conditionals
- Comparison operators
- Logical operators (and, or, not)
- Ternary operator

**Key Concepts:**
```
if condition:
    # execute if true
elif another_condition:
    # execute if another true
else:
    # execute if all false

# Ternary operator:
value_if_true if condition else value_if_false
```

#### **3. Control Flow - Loops**
**Notebooks:** 002.whileloop, 003.Forloop, 022.for loops while loop, 2-Control Flow/Loops  
**Key Topics:**
- While loops and conditions
- For loops with range()
- Loop control: break, continue, pass
- Nested loops
- Looping through lists and strings

**Key Concepts:**
```
# While loop
while condition:
    # execute code
    if exit_condition:
        break

# For loop
for item in iterable:
    if skip_condition:
        continue
    # process item

# Range usage
for i in range(start, end, step)
```

#### **4. String & List Manipulation**
**Notebooks:** 004.python string and list manipulation, 005.list manipulation, 1-Python Basics/1.0-basic  
**Key Topics:**
- String indexing and slicing
- String methods: split(), join(), strip(), replace()
- List creation and indexing
- List methods: append(), extend(), insert(), remove(), pop()
- List comprehension
- String concatenation and formatting

**Key Concepts:**
```
# String operations
s = "Hello World"
s[0]        # Indexing
s[1:5]      # Slicing
s.upper()   # Methods
s.split()   # String to list

# List operations
lst = [1, 2, 3, 4]
lst.append(5)
lst[2:]     # Slicing
[x*2 for x in lst]  # List comprehension
```

#### **5. Data Structures - Tuples, Sets, Dictionaries**
**Notebooks:** 006.Tuples set dict, 3.2-Tuples, 3.3-Sets, 3.4-Dictionaries, 2-Python List Dictionary Sets  
**Key Topics:**
- Tuple creation and immutability
- Tuple unpacking
- Set operations: union, intersection, difference
- Set methods and properties
- Dictionary creation and access
- Dictionary methods: keys(), values(), items()
- Nested dictionaries

**Key Concepts:**
```
# Tuples (immutable)
t = (1, 2, 3)
a, b, c = t  # Unpacking

# Sets (unique, unordered)
s = {1, 2, 3}
s.add(4)
s1 | s2      # Union

# Dictionaries (key-value pairs)
d = {'name': 'John', 'age': 30}
d['name']    # Access
d.get('age')  # Safe access
d.update({'city': 'NYC'})
```

---

## 🏗️ OBJECT-ORIENTED PROGRAMMING

### Level: Intermediate | Time: 8-12 hours

#### **1. Classes & Objects Basics**
**Notebooks:** 010.class and object, 8.1-oops, 1-Python Basics/1.0-basic  
**Key Topics:**
- Class definition and instantiation
- Constructor (__init__)
- Instance variables and methods
- Class variables
- Object attributes and behavior

**Key Concepts:**
```python
class Dog:
    species = "Canis familiaris"  # Class variable
    
    def __init__(self, name, age):  # Constructor
        self.name = name  # Instance variable
        self.age = age
    
    def bark(self):  # Instance method
        return f"{self.name} says Woof!"

dog = Dog("Buddy", 3)
print(dog.bark())
```

#### **2. Inheritance**
**Notebooks:** 8.2-inheritance, Advance Python Series- Inheritance--OOPS  
**Key Topics:**
- Parent and child classes
- Method overriding
- super() function
- Multiple inheritance
- Method Resolution Order (MRO)

**Key Concepts:**
```python
class Animal:
    def speak(self):
        return "Some sound"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Multiple Inheritance
class Pet(Animal, Guardian):
    pass

# super() to access parent class
super().speak()
```

#### **3. Polymorphism**
**Notebooks:** 8.3-Polymorphism  
**Key Topics:**
- Method overriding
- Operator overloading
- Duck typing
- Polymorphic functions
- isinstance() and type checking

**Key Concepts:**
```python
# Polymorphic function
def animal_sound(animal):
    return animal.speak()

# Works with any class that has speak() method
cat_sound = animal_sound(cat)
dog_sound = animal_sound(dog)
```

#### **4. Encapsulation & Access Modifiers**
**Notebooks:** 8.4-Encapsulation, Advance Python Series- Public Private And Protected  
**Key Topics:**
- Public, private, protected members
- Double underscore naming convention
- Property decorators (@property)
- Getters and setters
- Data hiding principles

**Key Concepts:**
```python
class Person:
    def __init__(self, name):
        self._name = name  # Protected
        self.__account = 12345  # Private
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
```

#### **5. Abstraction**
**Notebooks:** 8.5-Abstraction  
**Key Topics:**
- Abstract classes and methods
- ABC module
- Interface design
- Abstract method implementation
- Concrete vs abstract classes

**Key Concepts:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
```

#### **6. Magic Methods & Operator Overloading**
**Notebooks:** 8.6-magicmethods, 8.7-OperatorOverloading, Advance Python Series-Magic Methods In Classes  
**Key Topics:**
- __str__ and __repr__
- Arithmetic operators (__add__, __sub__)
- Comparison operators (__eq__, __lt__)
- __len__, __getitem__, __setitem__
- __enter__, __exit__ (context managers)

**Key Concepts:**
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):  # Overload +
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __len__(self):
        return (self.x**2 + self.y**2)**0.5
```

#### **7. Advanced OOP Concepts**
**Notebooks:** Class Methods In Python, Static Methods In Python  
**Key Topics:**
- Class methods (@classmethod)
- Static methods (@staticmethod)
- Decorators (@decorator)
- Method types and usage
- Composition vs Inheritance

**Key Concepts:**
```python
class MyClass:
    count = 0
    
    def __init__(self):
        MyClass.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @staticmethod
    def static_method():
        return "Static method"
    
    @property
    def read_only(self):
        return "Cannot modify"
```

---

## 📊 DATA STRUCTURES & ALGORITHMS

### Level: Intermediate | Time: 6-10 hours

#### **1. Advanced List Operations**
**Notebooks:** 3.1-Lists, 3.1.1-ListExamples  
**Key Topics:**
- List methods and operations
- Slicing and negative indexing
- List comprehension vs loops
- Sorting and ordering
- List manipulation algorithms

**Key Concepts:**
```python
# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
matrix = [[i+j for j in range(3)] for i in range(3)]

# List unpacking
a, b, c = [1, 2, 3]
first, *middle, last = [1, 2, 3, 4, 5]

# Sorting
sorted_list = sorted(lst)
lst.sort(reverse=True)
sorted(lst, key=lambda x: x['age'])
```

#### **2. Functional Programming**
**Notebooks:** 4.3-Lambda, 4.4-Mapsfunction, 4.5-filterfunction, 028.SQLLITE map reduce filter zip, Python Zip Function-Parallel Iteration  
**Key Topics:**
- Lambda functions
- map() function
- filter() function
- reduce() function
- zip() function
- Functional programming paradigm

**Key Concepts:**
```python
# Lambda functions
square = lambda x: x**2
square(5)  # 25

# map() - Apply function to all items
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))

# filter() - Keep items that pass test
evens = list(filter(lambda x: x % 2 == 0, numbers))

# reduce() - Accumulate values
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)

# zip() - Parallel iteration
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

#### **3. Iterators & Generators**
**Notebooks:** 012.iterator generator, 9.1-Iterators, 9.2-Generators, Python- Iterators Vs Generators  
**Key Topics:**
- Iterator protocol (__iter__, __next__)
- Iterating over sequences
- Generator functions (yield)
- Generator expressions
- Lazy evaluation
- StopIteration exception

**Key Concepts:**
```python
# Iterator class
class CountUp:
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        raise StopIteration

# Generator function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Generator expression
gen = (x**2 for x in range(5))
```

#### **4. Decorators**
**Notebooks:** 9.3-Decorators, Python Decorators  
**Key Topics:**
- Function decorators
- Decorator syntax and usage
- Nested decorators
- Decorators with arguments
- Use cases and applications

**Key Concepts:**
```python
# Simple decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something before")
        result = func(*args, **kwargs)
        print("Something after")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    return f"Hello {name}"

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(times=3)
def greet():
    print("Hi!")
```

---

## 📂 FILE HANDLING & I/O

### Level: Beginner-Intermediate | Time: 3-5 hours

#### **1. File Operations**
**Notebooks:** 011.file system, 6.1-fileoperation, 6.2-filepath, 008.Function and files  
**Key Topics:**
- Opening and closing files
- Reading files (read, readline, readlines)
- Writing to files (write, writelines)
- Appending to files
- File modes (r, w, a, x, b, +)
- Context managers (with statement)
- File paths and navigation

**Key Concepts:**
```python
# Traditional file handling
f = open('file.txt', 'r')
content = f.read()
f.close()

# With context manager (recommended)
with open('file.txt', 'r') as f:
    content = f.read()
    lines = f.readlines()

# Writing to file
with open('file.txt', 'w') as f:
    f.write("Hello World")

# File modes
# 'r' - Read (default)
# 'w' - Write (overwrites)
# 'a' - Append
# 'x' - Create
# 'b' - Binary
# '+' - Read and write
```

#### **2. Exception Handling & Logging**
**Notebooks:** 013.Exception handling class 1, 014.Exception handling class 2, 015.logging, 016.logging, 7.1-exception, 009.logging and debugging, 12.1-logging, 12.2-multiplelogger  
**Key Topics:**
- Try-except blocks
- Exception types and hierarchy
- Multiple exceptions
- Finally block
- Custom exceptions
- Logging module configuration
- Log levels and formatters
- File logging and handlers

**Key Concepts:**
```python
# Exception handling
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Cannot divide by zero: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("Success!")
finally:
    print("Cleanup")

# Custom exceptions
class CustomError(Exception):
    pass

raise CustomError("Something went wrong")

# Logging
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='log.txt'
)
logging.info("Info message")
logging.error("Error occurred")
```

---

## 🗄️ DATABASE MANAGEMENT

### Level: Intermediate | Time: 10-15 hours

#### **1. SQL Fundamentals**
**Notebooks:** 025.SQL basic, 026.sql day 2  
**Key Topics:**
- SQL basics and syntax
- SELECT statements
- WHERE, ORDER BY, GROUP BY
- Joins (INNER, LEFT, RIGHT, FULL)
- Aggregate functions (COUNT, SUM, AVG)
- CREATE, INSERT, UPDATE, DELETE
- Indexes and optimization

**Key Concepts:**
```sql
-- SELECT with filtering
SELECT * FROM users WHERE age > 18;

-- Joins
SELECT users.name, orders.order_id
FROM users
INNER JOIN orders ON users.id = orders.user_id;

-- Aggregate functions
SELECT department, COUNT(*) as count, AVG(salary)
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;

-- CREATE TABLE
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    email VARCHAR(100) UNIQUE
);
```

#### **2. SQLite & Database Operations**
**Notebooks:** 11.1-sqlite, 028.SQLLITE map reduce filter zip, TaskSQLite/  
**Key Topics:**
- SQLite database creation
- Running SQL queries from Python
- CRUD operations
- Database connections
- Cursor and execute methods
- Database design patterns

**Key Concepts:**
```python
import sqlite3

# Connect to database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

# Insert data
cursor.execute('INSERT INTO users VALUES (1, "John", 30)')

# Query data
cursor.execute('SELECT * FROM users')
results = cursor.fetchall()

# Update
cursor.execute('UPDATE users SET age = 31 WHERE name = "John"')

# Commit and close
conn.commit()
conn.close()
```

#### **3. MongoDB & NoSQL**
**Notebooks:** 027.mongodb class 1, MongoDB/ subdirectory, Advance Python Series/ MongoDB tasks  
**Key Topics:**
- MongoDB basics and BSON/JSON
- Document structure
- Collections and databases
- CRUD operations with PyMongo
- Querying and filtering
- Indexes in MongoDB
- Aggregation pipeline

**Key Concepts:**
```python
from pymongo import MongoClient

# Connect
client = MongoClient('mongodb://localhost:27017/')
db = client['mydb']
collection = db['users']

# Insert
collection.insert_one({'name': 'John', 'age': 30})
collection.insert_many([...])

# Query
user = collection.find_one({'name': 'John'})
users = collection.find({'age': {'$gt': 25}})

# Update
collection.update_one({'name': 'John'}, {'$set': {'age': 31}})

# Delete
collection.delete_one({'name': 'John'})

# Aggregation
pipeline = [
    {'$match': {'age': {'$gt': 25}}},
    {'$group': {'_id': '$city', 'count': {'$sum': 1}}}
]
results = collection.aggregate(pipeline)
```

---

## 📈 DATA ANALYSIS & VISUALIZATION

### Level: Intermediate-Advanced | Time: 15-20 hours

#### **1. NumPy - Numerical Computing**
**Notebooks:** 10.1-numpy, 3-Numpy Tutorial, 035.pandas and numpy, 036.numpy day 2, 036.numpy_recorded  
**Key Topics:**
- NumPy arrays creation and manipulation
- Array indexing and slicing
- Mathematical operations
- Broadcasting
- Array reshaping
- Statistical functions
- Linear algebra operations

**Key Concepts:**
```python
import numpy as np

# Array creation
arr = np.array([1, 2, 3])
arr = np.arange(0, 10, 2)
arr = np.linspace(0, 1, 5)
arr = np.ones((3, 3))
arr = np.zeros(10)

# Indexing and slicing
arr[0]      # First element
arr[1:4]    # Slice
arr[-1]     # Last element

# Operations
arr + 5
arr * 2
np.sqrt(arr)
np.mean(arr)

# Broadcasting
matrix = np.array([[1, 2], [3, 4]])
matrix + np.array([10, 20])

# Reshaping
arr.reshape((2, 5))
arr.flatten()
```

#### **2. Pandas - Data Manipulation**
**Notebooks:** 10.2-pandas, 10.3-datamanipulation, 10.4-readdata, 4- Pandas tutorial, 029.Pandas, 031.pandas day 2, 032.pandas class 3, 033.pandas 4, 034.pandas class homework discussed, Pandas.ipynb  
**Key Topics:**
- Series and DataFrames
- Data loading (CSV, Excel, JSON)
- Data cleaning and handling missing values
- Data filtering and selection
- Grouping and aggregation
- Merging and joining DataFrames
- Time series indexing

**Key Concepts:**
```python
import pandas as pd

# DataFrame creation
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
})

# Loading data
df = pd.read_csv('data.csv')
df = pd.read_excel('data.xlsx')

# Data exploration
df.head()       # First 5 rows
df.info()       # Data types and nulls
df.describe()   # Statistical summary

# Filtering
df[df['age'] > 25]
df.loc[0, 'name']
df.iloc[0, 1]

# Data cleaning
df.dropna()     # Remove null values
df.fillna(0)    # Fill null values
df.drop_duplicates()

# Grouping and aggregation
df.groupby('city')['age'].mean()
df.groupby('city').agg({'age': 'mean', 'salary': 'sum'})

# Merging
pd.merge(df1, df2, on='id')
pd.concat([df1, df2])
```

#### **3. Matplotlib - Static Visualization**
**Notebooks:** 10.5-matplotlib, 4.5-Matplotlib  
**Key Topics:**
- Line plots, scatter plots, bar plots
- Histograms and distributions
- Box plots and violin plots
- Pie charts
- Subplots and figure layout
- Labels, titles, legends, grids
- Customization: colors, styles, markers

**Key Concepts:**
```python
import matplotlib.pyplot as plt

# Basic plot
plt.plot([1, 2, 3], [1, 4, 9])
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Title')
plt.show()

# Scatter plot
plt.scatter(x, y, color='red', marker='o')

# Bar plot
plt.bar(categories, values, color='blue')

# Histogram
plt.hist(data, bins=20, edgecolor='black')

# Subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(x, y)
axes[0, 1].scatter(x, y)

# Customization
plt.plot(x, y, color='red', linestyle='--', marker='o', linewidth=2)
plt.grid(True, alpha=0.3)
plt.legend(['Series 1', 'Series 2'])
```

#### **4. Seaborn - Statistical Visualization**
**Notebooks:** 10.6-seaborn, 5- Seaborn  
**Key Topics:**
- Seaborn scatter plots and line plots
- Categorical plots (bar, box, violin)
- Distribution plots
- Correlation heatmaps
- Pair plots and relationships
- Color palettes and theming

**Key Concepts:**
```python
import seaborn as sns

# Load datasets
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')

# Scatter plot with hue
sns.scatterplot(x='total_bill', y='tip', hue='sex', data=tips)

# Regression plot
sns.regplot(x='total_bill', y='tip', data=tips)

# Categorical plots
sns.barplot(x='day', y='total_bill', data=tips)
sns.boxplot(x='day', y='total_bill', hue='sex', data=tips)
sns.violinplot(x='day', y='total_bill', data=tips)

# Distribution
sns.histplot(tips['total_bill'], kde=True)
sns.kdeplot(tips['total_bill'], fill=True)

# Relationships
sns.pairplot(iris)
sns.jointplot(x='petal_length', y='petal_width', data=iris)

# Heatmap
corr = iris.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
```

#### **5. Plotly - Interactive Visualization**
**Notebooks:** 039.plotly  
**Key Topics:**
- Interactive plots with Plotly
- 3D visualizations
- Scatter plots with hover information
- Line charts and bar charts
- Bubble charts
- Maps and geographic visualization
- Animations and interactions

**Key Concepts:**
```python
import plotly.express as px
import plotly.graph_objects as go

# Scatter plot
fig = px.scatter(df, x='age', y='salary', color='city', size='experience')

# Line plot
fig = px.line(df, x='date', y='sales', title='Sales Over Time')

# Bar chart
fig = px.bar(df, x='product', y='revenue', barmode='group')

# 3D scatter
fig = px.scatter_3d(df, x='x', y='y', z='z', color='category')

# Box plot
fig = px.box(df, x='day', y='total_bill', points='all')

# Show
fig.show()
```

#### **6. Exploratory Data Analysis (EDA)**
**Notebooks:** EDA.ipynb  
**Key Topics:**
- Data profiling and summary statistics
- Missing value analysis
- Outlier detection
- Correlation analysis
- Feature distributions
- Data quality checks

**Key Concepts:**
```python
# Complete EDA workflow
import pandas as pd
import numpy as np
import seaborn as sns

# 1. Load and overview
df = pd.read_csv('data.csv')
print(df.head())
print(df.info())
print(df.describe())

# 2. Missing values
print(df.isnull().sum())
sns.heatmap(df.isnull(), cbar=False)

# 3. Distributions
df.hist(figsize=(10, 8))
sns.distplot(df['column_name'])

# 4. Correlations
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')

# 5. Relationships
sns.pairplot(df)
sns.scatterplot(x='col1', y='col2', hue='category', data=df)
```

---

## 🤖 MACHINE LEARNING

### Level: Advanced | Time: 30-40 hours

#### **1. Regression Models**
**Topics:**
- Linear Regression
- Multiple Linear Regression
- Polynomial Regression
- Ridge, Lasso, ElasticNet regression
- Evaluation metrics (MSE, RMSE, R², MAE)

**Key Concepts:**
```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Linear regression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

# Ridge regression (L2 regularization)
from sklearn.linear_model import Ridge
model = Ridge(alpha=1.0)
model.fit(X_train, y_train)

# Lasso regression (L1 regularization)
from sklearn.linear_model import Lasso
model = Lasso(alpha=0.1)
model.fit(X_train, y_train)
```

#### **2. Classification Models**
**Topics:**
- Logistic Regression
- Decision Trees
- Random Forests
- Support Vector Machines (SVM)
- Naive Bayes
- K-Nearest Neighbors (KNN)
- Gradient Boosting (XGBoost, LightGBM)

**Key Concepts:**
```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# Decision Tree
model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)

# Random Forest
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# SVM
model = SVC(kernel='rbf', C=1.0)
model.fit(X_train, y_train)

# Evaluation
accuracy = accuracy_score(y_test, predictions)
conf_matrix = confusion_matrix(y_test, predictions)
print(classification_report(y_test, predictions))
```

#### **3. Clustering**
**Topics:**
- K-Means clustering
- Hierarchical clustering
- DBSCAN
- Silhouette analysis
- Elbow method

**Key Concepts:**
```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X)

# Elbow method
inertias = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)

# Silhouette score
score = silhouette_score(X, clusters)
```

#### **4. Feature Engineering**
**Topics:**
- Feature selection
- Feature scaling and normalization
- Dimensionality reduction (PCA)
- Encoding categorical variables
- Polynomial features
- Feature importance

**Key Concepts:**
```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, f_classif

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dimensionality reduction
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Categorical encoding
encoder = LabelEncoder()
X['category_encoded'] = encoder.fit_transform(X['category'])

# Feature selection
selector = SelectKBest(f_classif, k=5)
X_selected = selector.fit_transform(X, y)
```

#### **5. Model Evaluation**
**Topics:**
- Cross-validation
- Hyperparameter tuning
- Grid search and random search
- ROC curves and AUC
- Precision, recall, F1-score

**Key Concepts:**
```python
from sklearn.model_selection import cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.metrics import roc_curve, auc, roc_auc_score

# Cross-validation
scores = cross_val_score(model, X, y, cv=5)

# Grid search
params = {'max_depth': [3, 5, 7], 'min_samples_split': [2, 5, 10]}
grid = GridSearchCV(DecisionTreeClassifier(), params, cv=5)
grid.fit(X_train, y_train)

# Random search
random_search = RandomizedSearchCV(model, params, cv=5, n_iter=10)

# ROC curve
fpr, tpr, _ = roc_curve(y_test, predictions)
auc_score = auc(fpr, tpr)
```

---

## 🧠 DEEP LEARNING & NEURAL NETWORKS

### Level: Advanced | Time: 40-50 hours

#### **1. Neural Networks Basics**
**Topics:**
- Perceptron and activation functions
- Forward and backward propagation
- Loss functions
- Gradient descent optimization
- Neural network architecture

**Key Concepts:**
```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Sequential model
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(input_dim,)),
    layers.Dropout(0.2),
    layers.Dense(32, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])

# Compile
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train
history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Predict
predictions = model.predict(X_test)
```

#### **2. Convolutional Neural Networks (CNN)**
**Topics:**
- Convolution operations
- Pooling layers
- CNN architecture design
- Transfer learning
- Pre-trained models (VGG, ResNet, Inception)

**Key Concepts:**
```python
# CNN architecture
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])

# Transfer learning
base_model = tf.keras.applications.VGG16(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False

model = keras.Sequential([
    base_model,
    layers.Flatten(),
    layers.Dense(256, activation='relu'),
    layers.Dense(10, activation='softmax')
])
```

#### **3. Recurrent Neural Networks (RNN, LSTM, GRU)**
**Topics:**
- Sequential data processing
- LSTM cells and gates
- GRU architecture
- Sequence-to-sequence models
- Attention mechanisms

**Key Concepts:**
```python
# LSTM model
model = keras.Sequential([
    layers.LSTM(128, activation='relu', input_shape=(seq_length, input_dim), return_sequences=True),
    layers.Dropout(0.2),
    layers.LSTM(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])

# GRU model
model = keras.Sequential([
    layers.GRU(128, activation='relu', input_shape=(seq_length, input_dim)),
    layers.Dense(32, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])

# Bidirectional RNN
model = keras.Sequential([
    layers.Bidirectional(layers.LSTM(64, return_sequences=True)),
    layers.Flatten(),
    layers.Dense(num_classes, activation='softmax')
])
```

#### **4. Object Detection**
**Topics:**
- YOLO (You Only Look Once)
- R-CNN family
- Anchor boxes and bounding boxes
- Non-maximum suppression
- Detectron2

---

## 📝 NATURAL LANGUAGE PROCESSING

### Level: Advanced | Time: 20-30 hours

#### **1. NLP Fundamentals**
**Topics:**
- Tokenization and preprocessing
- Stemming and lemmatization
- TF-IDF and word embeddings
- Word2Vec and GloVe
- Text normalization

**Key Concepts:**
```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Preprocessing
text = "Natural Language Processing is great!"
tokens = word_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]

# Stemming
stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in tokens]

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
```

#### **2. Text Classification**
**Topics:**
- Sentiment analysis
- Spam detection
- Topic classification
- Hate speech detection

**Key Concepts:**
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# TF-IDF vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(texts)

# Classification
model = MultinomialNB()
model.fit(X, labels)
predictions = model.predict(X_test)
```

#### **3. RNN & LSTM for NLP**
**Topics:**
- Sequence-to-sequence models
- RNN text generation
- Machine translation
- Name entity recognition

---

## ⏰ TIME SERIES ANALYSIS

### Level: Advanced | Time: 15-20 hours

#### **1. Time Series Fundamentals**
**Topics:**
- Time series components (trend, seasonality, noise)
- Stationarity testing
- ACF and PACF plots
- Lag features

#### **2. ARIMA & SARIMA**
**Topics:**
- ARIMA models
- SARIMA for seasonal data
- Auto-ARIMA
- Forecasting and evaluation

**Key Concepts:**
```python
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima

# Auto-ARIMA
model = auto_arima(data, seasonal=False)

# ARIMA
model = ARIMA(data, order=(p, d, q))
result = model.fit()
forecast = result.forecast(steps=10)

# SARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
model = SARIMAX(data, order=(p, d, q), seasonal_order=(P, D, Q, s))
```

#### **3. Deep Learning for Time Series**
**Topics:**
- LSTM for forecasting
- CNN-LSTM hybrid models
- Attention mechanisms

---

## 🌐 WEB DEVELOPMENT & APIs

### Level: Intermediate-Advanced | Time: 10-15 hours

**Topics:**
- REST APIs with Flask
- HTTP methods and status codes
- JSON handling
- API authentication
- Web scraping
- Streamlit web apps

**Key Concepts:**
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'data': [1, 2, 3]})

@app.route('/api/data', methods=['POST'])
def create_data():
    data = request.json
    return jsonify({'status': 'success'}), 201

# Streamlit
import streamlit as st

st.title('My App')
name = st.text_input('Enter name:')
if st.button('Submit'):
    st.write(f'Hello {name}')
```

---

## 💻 GUI DEVELOPMENT

### Level: Intermediate | Time: 5-10 hours

**Notebooks:** gui tkinter task/  
**Topics:**
- Tkinter widgets
- Layout managers (pack, grid, place)
- Event handling
- Canvas and drawing
- Dialogs and file operations

**Key Concepts:**
```python
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title('My App')
root.geometry('400x300')

# Label
label = tk.Label(root, text='Hello World')
label.pack(pady=10)

# Entry
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Button
def click():
    name = entry.get()
    messagebox.showinfo('Info', f'Hello {name}')

button = tk.Button(root, text='Submit', command=click)
button.pack(pady=10)

root.mainloop()
```

---

## 📋 PRACTICE TASKS & PROJECTS

### Root Directory Tasks

1. **Python Basics Practice** (023.practice problem python basic)
   - Basic syntax exercises
   - Control flow problems
   - Function writing challenges

2. **Titanic Task** (classTask_MongoDB_SQLite/titanic task/)
   - Dataset: Titanic passenger survival
   - Goal: Predict survival using classification
   - Skills: EDA, feature engineering, model building

3. **Bank Task** (classTask_MongoDB_SQLite/BankTask/)
   - Multiple Python assignments
   - Database operations
   - Data analysis workflows

4. **MongoDB & SQLite Tasks** (classTask_MongoDB_SQLite/)
   - Data insertion and querying
   - Schema design
   - CRUD operations

5. **Plotly Task** (classTask_MongoDB_SQLite/plotly task/)
   - Interactive visualizations
   - Dashboard creation

6. **Resume Parsing** (classTask_MongoDB_SQLite/resume parsing/)
   - NLP text extraction
   - Information retrieval

---

## 🚀 QUICK REFERENCE GUIDE

### Essential Python Commands

```python
# Data types
type(var)                  # Check type
isinstance(var, int)       # Type checking
len(collection)            # Length

# String operations
s.upper(), s.lower()       # Case conversion
s.split(), s.join()        # Split/join
s.strip(), s.replace()     # Trim/replace
f"Value: {var}"            # F-string

# List operations
lst.append(), lst.extend()  # Add items
lst.pop(), lst.remove()    # Remove items
lst[start:end:step]        # Slicing
sorted(lst), lst.sort()    # Sorting

# Dictionary operations
d.get(key, default)        # Safe access
d.keys(), d.values()       # Keys/values
d.items()                  # Key-value pairs
d.update()                 # Merge dictionaries

# Set operations
s.add(), s.remove()        # Add/remove
s1 | s2                    # Union
s1 & s2                    # Intersection
s1 - s2                    # Difference
```

### Pandas Commands Cheatsheet

```python
# Read/Write
pd.read_csv(), pd.read_excel()
df.to_csv(), df.to_excel()

# Data exploration
df.head(), df.tail()
df.info(), df.describe()
df.shape, df.dtypes

# Selection
df['column']               # Select column
df.loc[row, col]           # Label-based
df.iloc[row_num, col_num]  # Index-based
df[df['col'] > value]      # Filtering

# Manipulation
df.drop(), df.rename()
df.fillna(), df.dropna()
df.sort_values(), df[['col1', 'col2']]

# Grouping & aggregation
df.groupby('col').sum()
df.groupby('col').agg({'col2': 'mean'})
df.value_counts()

# Merging
pd.merge(df1, df2, on='key')
pd.concat([df1, df2])
```

### Matplotlib & Seaborn Quick Plot

```python
# Matplotlib
plt.plot(x, y)
plt.scatter(x, y)
plt.bar(x, y)
plt.hist(data)
plt.title(), plt.xlabel(), plt.ylabel()
plt.show()

# Seaborn
sns.scatterplot(x=, y=, data=)
sns.lineplot(x=, y=, data=)
sns.barplot(x=, y=, data=)
sns.boxplot(x=, y=, data=)
sns.heatmap(data, annot=True)
sns.pairplot(df)
```

### Scikit-Learn Workflow

```python
# Data splitting
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Model training
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Evaluation
from sklearn.metrics import accuracy_score, classification_report
accuracy = accuracy_score(y_test, predictions)
```

### TensorFlow/Keras Quick Build

```python
import tensorflow as tf
from tensorflow.keras import layers, models

# Build model
model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(input_size,)),
    layers.Dropout(0.2),
    layers.Dense(32, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])

# Compile
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate
loss, accuracy = model.evaluate(X_test, y_test)

# Predict
predictions = model.predict(X_test)
```

---

## 📊 Learning Progress Tracker

### Suggested Learning Order (90 Days)

**WEEKS 1-2: Python Fundamentals**
- Basic syntax, variables, data types
- Control flow (if-else, loops)
- String and list operations
- Start: Classes 000-003, 021-022

**WEEKS 3-4: Data Structures**
- Tuples, sets, dictionaries
- List comprehension
- Functional programming (map, filter, reduce, zip)
- Start: Classes 005-006, 028

**WEEKS 5-6: Functions & OOP Basics**
- Function definition and tools
- Classes and objects
- Basic inheritance
- Start: Class 007, 008, 010, 017

**WEEKS 7-8: Advanced Python**
- Exception handling
- Logging and debugging
- Iterators and generators
- Decorators
- Start: Classes 009, 013-016, 012

**WEEKS 9-10: Databases**
- SQL fundamentals
- SQLite operations
- MongoDB basics
- Start: Classes 025-027

**WEEKS 11-12: NumPy & Pandas**
- NumPy arrays and operations
- Pandas DataFrames
- Data cleaning and manipulation
- Start: Classes 026-027, 029-035

**WEEKS 13: Data Visualization**
- Matplotlib basics
- Seaborn statistical plots
- Plotly interactive visualizations
- Start: Classes 028-029, 039

**WEEKS 14-15: Machine Learning**
- Regression and classification
- Model evaluation
- Feature engineering
- Tree-based models
- Complete ML subdirectory notebooks

**WEEKS 16+: Deep Learning & Specializations**
- Neural networks and CNNs
- NLP and text processing
- Time series analysis
- Advanced topics

---

## 🔗 File Organization Reference

```
iNeuron Classes/
├── MASTER_SHEET_SUMMARY.md (This file)
├── Root Notebooks (Classes 000-039)
├── Complete-Python-Bootcamp-main/
│   ├── 1-Python Basics
│   ├── 2-Control Flow
│   ├── 3-Data Structures
│   ├── 4-Functions
│   ├── 5-Modules
│   ├── 6-File Handling
│   ├── 7-Exception Handling
│   ├── 8-Class And Objects
│   ├── 9-Advance Python Concepts
│   ├── 10-Data Analysis With Python
│   ├── 11-Working With Databases
│   ├── 12-Logging In Python
│   ├── 14-Streamlit
│   └── 15-Memory Management
├── Machine-Learning-in-90-days-master/
│   └── Section 1- Python Crash Course (45+ notebooks)
├── topic-wise/ (200+ specialized notebooks)
├── classTask_MongoDB_SQLite/ (150+ task notebooks)
├── data/ (Datasets and supporting files)
└── python/ (Additional Python resources)
```

---

## ✅ Study Tips & Best Practices

1. **Code Along**: Don't just read - run every code example
2. **Practice**: Complete practice problems after each section
3. **Project-Based**: Work on real projects (Titanic, Bank, etc.)
4. **Incremental Learning**: Master basics before advanced topics
5. **Debugging**: Learn to use print(), logging, and debuggers
6. **Documentation**: Read official docs of libraries
7. **Communities**: Engage with Python communities
8. **Review**: Regularly review concepts you learned earlier
9. **Apply**: Apply concepts to real-world problems
10. **Track Progress**: Document what you learn

---

## 📚 Key Resources Summary

| Topic | Key Notebooks | Key Libraries | Concepts |
|-------|---------------|---------------|----------|
| Python Basics | 000-006 | Built-in | Variables, loops, functions |
| OOP | 010, 017-020 | Built-in | Classes, inheritance, methods |
| Data Structures | 005-006, 3.x | Built-in | Lists, dicts, sets, tuples |
| NumPy | 035, 10.1, 3-NumPy | NumPy | Arrays, operations, algebra |
| Pandas | 029-035, 10.2-4, 4- | Pandas | DataFrames, groupby, merge |
| Matplotlib | 037-028, 10.5, 4.5 | Matplotlib | Plots, subplots, customization |
| Seaborn | 038, 10.6, 5- | Seaborn | Statistical plots, heatmaps |
| ML | topic-wise/ML | scikit-learn | Models, evaluation, tuning |
| DL | topic-wise/DL | TensorFlow/Keras | NNs, CNNs, RNNs |
| Databases | 025-027 | SQL/MongoDB | Queries, operations, design |
| NLP | topic-wise/NLP | NLTK, spacy | Tokenization, classification |
| Web | topic-wise/API | Flask, Streamlit | APIs, apps, scraping |

---

## 🎓 Certification Path

Upon completing this learning path, you'll be ready for:

- ✅ Python Developer Certification
- ✅ Data Science Professional Certificate
- ✅ Machine Learning Specialist
- ✅ Deep Learning Engineer
- ✅ Natural Language Processing Specialist
- ✅ Full Stack Data Science Developer

---

**Last Updated:** April 14, 2026  
**Total Learning Hours:** 150-200 hours (estimated)  
**Difficulty Progression:** Beginner → Advanced  
**Hands-on Projects:** 15+ practical projects included

---

*This master sheet is a comprehensive guide to your iNeuron learning journey. Update it as you progress through the course!*
