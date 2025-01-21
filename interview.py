import streamlit as st

# Dictionary containing topics and their interview questions with answers
interview_questions = {
    "Python": [
        {"question": "What is Python?", "answer": "Python is an interpreted, high-level programming language."},
        {"question": "Explain Python's key features.", "answer": "Python has dynamic typing, garbage collection, and supports multiple programming paradigms."},
        {"question": "What are the different data types in Python?", "answer": "Integers, floats, strings, lists, tuples, dictionaries, etc."},
        {"question": "What is a function in Python?", "answer": "A function is a reusable block of code that performs a specific task."},
        {"question": "What is a class in Python?", "answer": "A class is a blueprint for creating objects with predefined attributes and methods."},
        {"question": "What is a module in Python?", "answer": "A module is a file containing Python code that can be imported and used in other Python programs."},
        {"question": "What is a package in Python?", "answer": "A package is a collection of related modules that are organized in a directory hierarchy."},
        {"question": "What is PEP 8?", "answer": "PEP 8 is the Python Enhancement Proposal that provides guidelines for writing clean and readable Python code."},
        {"question": "What is a virtual environment in Python?", "answer": "A virtual environment is a self-contained directory that contains a Python installation for a specific project."},
        {"question": "How do you install external packages in Python?", "answer": "Using pip, the Python package manager, e.g., pip install numpy."},
        {"question": "What is a lambda function in Python?", "answer": "A lambda function is an anonymous function defined using the lambda keyword."},
        {"question": "What is list comprehension in Python?", "answer": "List comprehension is a concise way to create lists in Python."},
        {"question": "What is a decorator in Python?", "answer": "A decorator is a design pattern that allows you to add new functionality to an existing object without modifying its structure."},
        {"question": "What is a generator in Python?", "answer": "A generator is a function that returns an iterator object using the yield keyword."},
        {"question": "What is the difference between a list and a tuple in Python?", "answer": "Lists are mutable, while tuples are immutable."},
        {"question": "What is the difference between '==' and 'is' in Python?", "answer": "'==' compares the values of two objects, while 'is' compares the identities of two objects."},
        {"question": "What is the difference between 'append()' and 'extend()' in Python?", "answer": "'append()' adds an element to a list, while 'extend()' adds elements from an iterable."},
        {"question": "What is the difference between 'remove()' and 'pop()' in Python?", "answer": "'remove()' deletes an element by value, while 'pop()' deletes an element by index."},
        {"question": "What is the difference between 'deep copy' and 'shallow copy' in Python?", "answer": "A deep copy creates a new object and recursively copies the objects found in the original, while a shallow copy creates a new object and references the objects found in the original."},
        {"question": "What is the difference between 'global' and 'nonlocal' in Python?", "answer": "'global' is used to declare global variables, while 'nonlocal' is used to declare variables in nested functions."},
        {"question": "What is the difference between 'iterable' and 'iterator' in Python?", "answer": "An iterable is an object that can be iterated over, while an iterator is an object that generates the next value in a sequence."},
        {"question": "What is the difference between 'map()' and 'filter()' in Python?", "answer": "'map()' applies a function to all the items in an input list, while 'filter()' creates a list of elements for which a function returns true."},
        {"question": "What is the difference between 'sort()' and 'sorted()' in Python?", "answer": "'sort()' sorts a list in place, while 'sorted()' returns a new sorted list."},
        {"question": "What is the difference between '==', 'is', and 'in' in Python?", "answer": "'==' compares the values of two objects, 'is' compares the identities of two objects, and 'in' checks for membership in a sequence."},
        {"question": "What is the difference between 'args' and 'kwargs' in Python?", "answer": "'args' is used to pass a variable number of non-keyword arguments to a function, while 'kwargs' is used to pass a variable number of keyword arguments to a function."},
        {"question": "What is the difference between 'super()' and 'self' in Python?", "answer": "'super()' is used to access the parent class of a child class, while 'self' is used to access the current instance of a class."},
        {"question": "What is the difference between 'instance method', 'class method', and 'static method' in Python?", "answer": "An instance method operates on an instance of a class, a class method operates on the class itself, and a static method does not operate on either the instance or the class."},
        {"question": "What is the difference between 'list comprehension' and 'map()' in Python?", "answer": "List comprehension is a concise way to create lists, while map() applies a function to all the items in an input list."},
        {"question": "What is the difference between 'deepcopy()' and 'copy()' in Python?", "answer": "'deepcopy()' creates a new object and recursively copies the objects found in the original, while 'copy()' creates a new object and references the objects found in the original."},
        {"question": "What is the difference between 're.match()' and 're.search()' in Python?", "answer": "'re.match()' matches the pattern at the beginning of the string, while 're.search()' matches the pattern anywhere in the string."},
        # Add up to 30 questions and answers
    ],
    "SQL": [
        {"question": "What is SQL?", "answer": "SQL (Structured Query Language) is used to communicate with databases."},
        {"question": "What are the different types of JOINs in SQL?", "answer": "INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN, CROSS JOIN, etc."},
        {"question": "What is a primary key in SQL?", "answer": "A primary key is a unique identifier for each record in a table."},
        {"question": "What is a foreign key in SQL?", "answer": "A foreign key is a field that links two tables together."},
        {"question": "What is a subquery in SQL?", "answer": "A subquery is a query nested within another query."},
        {"question": "What is a view in SQL?", "answer": "A view is a virtual table based on the result set of a SELECT statement."},
        {"question": "What is a stored procedure in SQL?", "answer": "A stored procedure is a set of SQL statements that can be executed on the database."},
        {"question": "What is a trigger in SQL?", "answer": "A trigger is a set of SQL statements that are automatically executed when a specified event occurs."},
        {"question": "What is normalization in SQL?", "answer": "Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity."},
        {"question": "What is denormalization in SQL?", "answer": "Denormalization is the process of adding redundant data to a database to improve read performance."},
        {"question": "What is an index in SQL?", "answer": "An index is a data structure that improves the speed of data retrieval operations on a database table."},
        {"question": "What is a constraint in SQL?", "answer": "A constraint is a rule that enforces data integrity in a database."},
        {"question": "What is the difference between 'HAVING' and 'WHERE' in SQL?", "answer": "'HAVING' is used with GROUP BY to filter groups, while 'WHERE' is used to filter rows."},
        {"question": "What is the difference between 'UNION' and 'UNION ALL' in SQL?", "answer": "'UNION' removes duplicate rows, while 'UNION ALL' retains duplicate rows."},
        {"question": "What is the difference between 'TRUNCATE' and 'DELETE' in SQL?", "answer": "'TRUNCATE' removes all rows from a table, while 'DELETE' removes specific rows based on a condition."},
        {"question": "What is the difference between 'CHAR' and 'VARCHAR' in SQL?", "answer": "'CHAR' is a fixed-length data type, while 'VARCHAR' is a variable-length data type."},
        {"question": "What is the difference between 'NULL' and 'NOT NULL' in SQL?", "answer": "'NULL' allows a column to have no value, while 'NOT NULL' requires a column to have a value."},
        {"question": "What is the difference between 'GROUP BY' and 'ORDER BY' in SQL?", "answer": "'GROUP BY' groups rows based on a column, while 'ORDER BY' sorts rows based on a column."},
        {"question": "What is the difference between 'COUNT(*)' and 'COUNT(column)' in SQL?", "answer": "'COUNT(*)' counts all rows in a table, while 'COUNT(column)' counts non-null values in a column."},
        {"question": "What is the difference between 'INNER JOIN' and 'OUTER JOIN' in SQL?", "answer": "'INNER JOIN' returns rows that have matching values in both tables, while 'OUTER JOIN' returns all rows from both tables."},
        {"question": "What is the difference between 'LIKE' and 'IN' in SQL?", "answer": "'LIKE' is used to search for a specified pattern in a column, while 'IN' is used to specify multiple values in a WHERE clause."},
        {"question": "What is the difference between 'UNIQUE' and 'PRIMARY KEY' in SQL?", "answer": "'UNIQUE' allows null values and multiple occurrences, while 'PRIMARY KEY' does not allow null values and enforces uniqueness."},
        {"question": "What is the difference between 'HAVING' and 'WHERE' in SQL?", "answer": "'HAVING' is used with GROUP BY to filter groups, while 'WHERE' is used to filter rows."},
        {"question": "What is the difference between 'UNION' and 'UNION ALL' in SQL?", "answer": "'UNION' removes duplicate rows, while 'UNION ALL' retains duplicate rows."},
        {"question": "What is the difference between 'TRUNCATE' and 'DELETE' in SQL?", "answer": "'TRUNCATE' removes all rows from a table, while 'DELETE' removes specific rows based on a condition."},
        {"question": "What is the difference between 'CHAR' and 'VARCHAR' in SQL?", "answer": "'CHAR' is a fixed-length data type, while 'VARCHAR' is a variable-length data type."},
        {"question": "What is the difference between 'NULL' and 'NOT NULL' in SQL?", "answer": "'NULL' allows a column to have no value, while 'NOT NULL' requires a column to have a value."},
        {"question": "What is the difference between 'GROUP BY' and 'ORDER BY' in SQL?", "answer": "'GROUP BY' groups rows based on a column, while 'ORDER BY' sorts rows based on a column."},
        {"question": "What is the difference between 'COUNT(*)' and 'COUNT(column)' in SQL?", "answer": "'COUNT(*)' counts all rows in a table, while 'COUNT(column)' counts non-null values in a column."},
        {"question": "What is the difference between 'INNER JOIN' and 'OUTER JOIN' in SQL?", "answer": "'INNER JOIN' returns rows that have matching values in both tables, while 'OUTER JOIN' returns all rows from both tables."},
        # Add up to 30 questions and answers
    ],
    "Excel": [
        {"question": "What is Excel?", "answer": "Excel is a spreadsheet application developed by Microsoft."},
        {"question": "How do you create a pivot table?", "answer": "Select data, go to Insert > PivotTable, and configure the fields."},
        {"question": "How do you create a chart?", "answer": "Select data, go to Insert > Chart, and configure the chart."},
        {"question": "What is a VLOOKUP?", "answer": "VLOOKUP is a function used to search for a value in a table and return a corresponding value."},
        {"question": "What is an IF function?", "answer": "IF is a function used to perform conditional logic in Excel."},
        {"question": "What is conditional formatting?", "answer": "Conditional formatting is a feature that highlights cells based on specified conditions."},
        {"question": "What is a named range?", "answer": "A named range is a range of cells with a specific name."},
        {"question": "What is a data validation?", "answer": "Data validation is a feature that restricts the type of data that can be entered in a cell."},
        {"question": "What is a formula?", "answer": "A formula is an expression that performs calculations on values in a worksheet."},
        {"question": "What is a function?", "answer": "A function is a predefined formula that performs specific calculations."},
        {"question": "What is a macro?", "answer": "A macro is a set of instructions that automates tasks in Excel."},
        {"question": "What is a filter?", "answer": "A filter is a feature that displays only the rows that meet specified criteria."},
        {"question": "What is a slicer?", "answer": "A slicer is a visual control that filters data in a pivot table or chart."},
        {"question": "What is a sparkline?", "answer": "A sparkline is a small chart that provides a visual representation of data in a cell."},
        {"question": "What is a table?", "answer": "A table is a range of cells with structured data that can be sorted and filtered."},
        {"question": "What is a worksheet?", "answer": "A worksheet is a single page in an Excel workbook."},
        {"question": "What is a workbook?", "answer": "A workbook is a file that contains one or more worksheets."},
        {"question": "What is the difference between a workbook and a worksheet?", "answer": "A workbook is a file that contains one or more worksheets, while a worksheet is a single page in an Excel workbook."},
        {"question": "What is the difference between a chart and a pivot table?", "answer": "A chart is a visual representation of data, while a pivot table is a summary of data."},
        {"question": "What is the difference between a formula and a function?", "answer": "A formula is an expression that performs calculations on values in a worksheet, while a function is a predefined formula that performs specific calculations."},
        {"question": "What is the difference between a filter and a slicer?", "answer": "A filter displays only the rows that meet specified criteria, while a slicer filters data in a pivot table or chart."},
        {"question": "What is the difference between a named range and a table?", "answer": "A named range is a range of cells with a specific name, while a table is a range of cells with structured data that can be sorted and filtered."},
        {"question": "What is the difference between a sparkline and a chart?", "answer": "A sparkline is a small chart that provides a visual representation of data in a cell, while a chart is a visual representation of data."},
        {"question": "What is the difference between a workbook and a worksheet?", "answer": "A workbook is a file that contains one or more worksheets, while a worksheet is a single page in an Excel workbook."},
        {"question": "What is the difference between a chart and a pivot table?", "answer": "A chart is a visual representation of data, while a pivot table is a summary of data."},
        {"question": "What is the difference between a formula and a function?", "answer": "A formula is an expression that performs calculations on values in a worksheet, while a function is a predefined formula that performs specific calculations."},
        {"question": "What is the difference between a filter and a slicer?", "answer": "A filter displays only the rows that meet specified criteria, while a slicer filters data in a pivot table or chart."},
        {"question": "What is the difference between a named range and a table?", "answer": "A named range is a range of cells with a specific name, while a table is a range of cells with structured data that can be sorted and filtered."},
        {"question": "What is the difference between a sparkline and a chart?", "answer": "A sparkline is a small chart that provides a visual representation of data in a cell, while a chart is a visual representation of data."},
        {"question": "What is the difference between a workbook and a worksheet?", "answer": "A workbook is a file that contains one or more worksheets, while a worksheet is a single page in an Excel workbook."},
        # Add up to 30 questions and answers
    ],
    "NumPy": [
        {"question": "What is NumPy?", "answer": "NumPy is a library for numerical computing in Python."},
        {"question": "How do you create a NumPy array?", "answer": "Using the numpy.array() function."},
        {"question": "What is the difference between a NumPy array and a Python list?", "answer": "NumPy arrays are homogeneous and support vectorized operations, while Python lists are heterogeneous and do not support vectorized operations."},
        {"question": "What is a vectorized operation?", "answer": "A vectorized operation applies an operation to each element in an array without the need for explicit loops."},
        {"question": "What is a universal function (ufunc) in NumPy?", "answer": "A ufunc is a function that operates element-wise on NumPy arrays."},
        {"question": "What is broadcasting in NumPy?", "answer": "Broadcasting is a mechanism that allows NumPy to perform operations on arrays of different shapes."},
        {"question": "What is the difference between a filter and a slicer?", "answer": "A filter displays only the rows that meet specified criteria, while a slicer filters data in a pivot table or chart."},
        {"question": "What is the difference between a named range and a table?", "answer": "A named range is a range of cells with a specific name, while a table is a range of cells with structured data that can be sorted and filtered."},
        {"question": "What is the difference between a sparkline and a chart?", "answer": "A sparkline is a small chart that provides a visual representation of data in a cell, while a chart is a visual representation of data."},
        {"question": "What is the difference between a workbook and a worksheet?", "answer": "A workbook is a file that contains one or more worksheets, while a worksheet is a single page in an Excel workbook."},
        {"question": "What is the difference between a chart and a pivot table?", "answer": "A chart is a visual representation of data, while a pivot table is a summary of data."},
        {"question": "What is the difference between a formula and a function?", "answer": "A formula is an expression that performs calculations on values in a worksheet, while a function is a predefined formula that performs specific calculations."},
        {"question": "What is the difference between a filter and a slicer?", "answer": "A filter displays only the rows that meet specified criteria, while a slicer filters data in a pivot table or chart."},
        {"question": "What is the difference between a named range and a table?", "answer": "A named range is a range of cells with a specific name, while a table is a range of cells with structured data that can be sorted and filtered."},
        {"question": "What is the difference between a sparkline and a chart?", "answer": "A sparkline is a small chart that provides a visual representation of data in a cell, while a chart is a visual representation of data."},
        {"question": "What is the difference between a workbook and a worksheet?", "answer": "A workbook is a file that contains one or more worksheets, while a worksheet is a single page in an Excel workbook."},
        {"question": "What is the difference between a chart and a pivot table?", "answer": "A chart is a visual representation of data, while a pivot table is a summary of data."},
        {"question": "What is the difference between a formula and a function?", "answer": "A formula is an expression that performs calculations on values in a worksheet, while a function is a predefined formula that performs specific calculations."},
        {"question": "What is the difference between a filter and a slicer?", "answer": "A filter displays only the rows that meet specified criteria, while a slicer filters data in a pivot table or chart."},
        {"question": "What is the difference between a named range and a table?", "answer": "A named range is a range of cells with a specific name, while a table is a range of cells with structured data that can be sorted and filtered."},
        {"question": "What is the difference between a sparkline and a chart?", "answer": "A sparkline is a small chart that provides a visual representation of data in a cell, while a chart is a visual representation of data."},
        {"question": "What is the difference between a workbook and a worksheet?", "answer": "A workbook is a file that contains one or more worksheets, while a worksheet is a single page in an Excel workbook."},
        {"question": "What is the difference between a chart and a pivot table?", "answer": "A chart is a visual representation of data, while a pivot table is a summary of data."},
        {"question": "What is the difference between a formula and a function?", "answer": "A formula is an expression that performs calculations on values in a worksheet, while a function is a predefined formula that performs specific calculations."},
        {"question": "What is the difference between a filter and a slicer?", "answer": "A filter displays only the rows that meet specified criteria, while a slicer filters data in a pivot table or chart."},
        {"question": "What is the difference between a named range and a table?", "answer": "A named range is a range of cells with a specific name, while a table is a range of cells with structured data that can be sorted and filtered."},
        {"question": "What is the difference between a sparkline and a chart?", "answer": "A sparkline is a small chart that provides a visual representation of data in a cell, while a chart is a visual representation of data."},
        {"question": "What is the difference between a workbook and a worksheet?", "answer": "A workbook is a file that contains one or more worksheets, while a worksheet is a single page in an Excel workbook."},
        {"question": "What is the difference between a chart and a pivot table?", "answer": "A chart is a visual representation of data, while a pivot table is a summary of data."},
        {"question": "What is the difference between a formula and a function?", "answer": "A formula is an expression that performs calculations on values in a worksheet, while a function is a predefined formula that performs specific calculations."},
        # Add up to 30 questions and answers
    ],
    "Pandas": [
        {"question": "What is Pandas?", "answer": "Pandas is a Python library for data manipulation and analysis."},
        {"question": "How do you create a DataFrame in Pandas?", "answer": "Using the pandas.DataFrame() function."},
        {"question": "What is a DataFrame in Pandas?", "answer": "A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types."},
        {"question": "What is a Series in Pandas?", "answer": "A Series is a 1-dimensional labeled data structure with a single type."},
        {"question": "How do you read data from a CSV file in Pandas?", "answer": "Using the pandas.read_csv() function."},
        {"question": "How do you select rows and columns in a DataFrame?", "answer": "Using the .loc[] and .iloc[] methods."},
        {"question": "How do you filter rows in a DataFrame?", "answer": "Using boolean indexing."},
        {"question": "How do you group data in a DataFrame?", "answer": "Using the .groupby() method."},
        {"question": "How do you merge two DataFrames in Pandas?", "answer": "Using the .merge() method."},
        {"question": "How do you handle missing values in a DataFrame?", "answer": "Using the .dropna() and .fillna() methods."},
        {"question": "How do you create a new column in a DataFrame?", "answer": "By assigning a value to a new column name."},
        {"question": "How do you rename columns in a DataFrame?", "answer": "Using the .rename() method."},
        {"question": "How do you sort values in a DataFrame?", "answer": "Using the .sort_values() method."},
        {"question": "How do you apply a function to a DataFrame?", "answer": "Using the .apply() method."},
        {"question": "How do you pivot a DataFrame in Pandas?", "answer": "Using the .pivot() method."},
        {"question": "How do you melt a DataFrame in Pandas?", "answer": "Using the .melt() method."},
        {"question": "What is the difference between .loc[] and .iloc[] in Pandas?", "answer": ".loc[] is label-based, while .iloc[] is integer-based."},
        {"question": "What is the difference between .groupby() and .pivot_table() in Pandas?", "answer": ".groupby() groups data based on one or more columns, while .pivot_table() creates a spreadsheet-style pivot table."},
        {"question": "What is the difference between .merge() and .join() in Pandas?", "answer": ".merge() is more flexible and can merge on any column, while .join() merges on the index."},
        {"question": "What is the difference between .dropna() and .fillna() in Pandas?", "answer": ".dropna() removes missing values, while .fillna() fills missing values with a specified value."},
        # Add up to 30 questions and answers
    ],
    "Power BI": [
        {"question": "What is Power BI?", "answer": "Power BI is a business analytics tool developed by Microsoft."},
        {"question": "How do you create a report in Power BI?", "answer": "Import data, drag fields into visuals, and customize the visuals."},
        {"question": "What is a data model in Power BI?", "answer": "A data model is a collection of tables and relationships in Power BI."},
        {"question": "What is a measure in Power BI?", "answer": "A measure is a calculation based on the data in a Power BI report."},
        {"question": "What is a visualization in Power BI?", "answer": "A visualization is a graphical representation of data in a Power BI report."},
        {"question": "What is a dashboard in Power BI?", "answer": "A dashboard is a collection of visuals from multiple reports in Power BI."},
        {"question": "What is a slicer in Power BI?", "answer": "A slicer is a visual control that filters data in a report."},
        {"question": "What is a filter in Power BI?", "answer": "A filter is a condition that restricts the data displayed in a report."},
        {"question": "What is a drill-through in Power BI?", "answer": "A drill-through is a feature that allows users to navigate from a summary report to a detailed report."},
        {"question": "What is a bookmark in Power BI?", "answer": "A bookmark is a snapshot of a report page that can be saved and revisited."},
        {"question": "What is a theme in Power BI?", "answer": "A theme is a set of predefined styles that can be applied to a report."},
        {"question": "What is a gateway in Power BI?", "answer": "A gateway is a feature that allows users to navigate between reports."},
        {"question": "What is a dataflow in Power BI?", "answer": "A dataflow is a collection of data entities that can be reused in multiple reports."},
        {"question": "What is a workspace in Power BI?", "answer": "A workspace is a container for reports, dashboards, and datasets in Power BI."},
        {"question": "What is a Power BI service?", "answer": "The Power BI service is a cloud-based platform for sharing and collaborating on Power BI reports."},
        {"question": "What is the difference between a report and a dashboard in Power BI?", "answer": "A report is a single page with visuals, while a dashboard is a collection of visuals from multiple reports."},
        {"question": "What is a Power BI desktop?", "answer": "The Power BI desktop is a desktop application for creating and editing Power BI reports."},
        {"question": "What is the difference between a slicer and a filter in Power BI?", "answer": "A slicer is a visual control that filters data in a report, while a filter is a condition that restricts the data displayed in a report."},
        {"question": "What is the difference between a drill-through and a drill-down in Power BI?", "answer": "A drill-through allows users to navigate from a summary report to a detailed report, while a drill-down allows users to view more detailed data within a visual."},
        {"question": "What is the difference between a bookmark and a snapshot in Power BI?", "answer": "A bookmark is a snapshot of a report page that can be saved and revisited, while a snapshot is a static image of a report page."},
        # Add up to 30 questions and answers
    ],
    "Data Analytics": [
        {"question": "What is Data Analytics?", "answer": "Data Analytics involves analyzing raw data to find trends and insights."},
        {"question": "What are the types of Data Analytics?", "answer": "Descriptive, Diagnostic, Predictive, and Prescriptive Analytics."},
        {"question": "What is a data scientist?", "answer": "A data scientist is a professional who specializes in analyzing and modeling data."},
        {"question": "What is the CRISP-DM model?", "answer": "CRISP-DM (Cross-Industry Standard Process for Data Mining) is a widely used methodology for data mining projects."},
        {"question": "What is the difference between Data Analytics and Data Science?", "answer": "Data Analytics focuses on analyzing data to find insights, while Data Science involves analyzing data to build models and make predictions."},
        {"question": "What is the difference between structured and unstructured data?", "answer": "Structured data is organized and can be easily processed, while unstructured data is not organized and requires more processing."},
        {"question": "What is the difference between a data analyst and a data scientist?", "answer": "A data analyst focuses on analyzing data to find insights, while a data scientist focuses on analyzing data to build models and make predictions."},
        {"question": "What is the difference between a data warehouse and a data lake?", "answer": "A data warehouse is a structured repository for data, while a data lake is a repository for raw data in its native format."},
        {"question": "What is the difference between data mining and machine learning?", "answer": "Data mining is the process of discovering patterns in data, while machine learning is the process of building models that can learn from data."},
        {"question": "What is the difference between supervised and unsupervised learning?", "answer": "Supervised learning uses labeled data to train a model, while unsupervised learning uses unlabeled data."},
        {"question": "What is the difference between classification and regression?", "answer": "Classification predicts categories or labels, while regression predicts continuous values."},
        {"question": "What is the difference between overfitting and underfitting?", "answer": "Overfitting occurs when a model is too complex and learns noise in the data, while underfitting occurs when a model is too simple and cannot capture the underlying patterns."},
        {"question": "What is the difference between precision and recall?", "answer": "Precision is the ratio of true positives to the sum of true positives and false positives, while recall is the ratio of true positives to the sum of true positives and false negatives."},
        {"question": "What is the difference between a data engineer and a data analyst?", "answer": "A data engineer focuses on building and maintaining data pipelines, while a data analyst focuses on analyzing data to find insights."},
        {"question": "What is the difference between a data lake and a data warehouse?", "answer": "A data lake is a repository for raw data in its native format, while a data warehouse is a structured repository for data."},
        {"question": "What is the difference between a data scientist and a machine learning engineer?", "answer": "A data scientist focuses on analyzing data to build models and make predictions, while a machine learning engineer focuses on building and deploying machine learning models."},
        {"question": "What is the difference between a data analyst and a business analyst?", "answer": "A data analyst focuses on analyzing data to find insights, while a business analyst focuses on analyzing business processes and requirements."},
        {"question": "What is the difference between a data scientist and a statistician?", "answer": "A data scientist focuses on analyzing data to build models and make predictions, while a statistician focuses on analyzing data to draw inferences and make decisions."},
        {"question": "What is the difference between a data scientist and a data engineer?", "answer": "A data scientist focuses on analyzing data to build models and make predictions, while a data engineer focuses on building and maintaining data pipelines."},
        {"question": "What is the difference between a data scientist and a machine learning engineer?", "answer": "A data scientist focuses on analyzing data to build models and make predictions, while a machine learning engineer focuses on building and deploying machine learning models."},

        # Add up to 30 questions and answers
    ],
    "Data Science": [
        {"question": "What is Data Science?", "answer": "Data Science is an interdisciplinary field that uses data for insights and decision-making."},
        {"question": "What are the steps in a data science project?", "answer": "Data collection, cleaning, analysis, modeling, and deployment."},
        {"question": "What is a data scientist?", "answer": "A data scientist is a professional who specializes in analyzing and modeling data."},
        {"question": "What is a data engineer?", "answer": "A data engineer is a professional who specializes in building and maintaining data pipelines."},
        {"question": "What is a machine learning engineer?", "answer": "A machine learning engineer is a professional who specializes in building and deploying machine learning models."},
        {"question": "What is a data analyst?", "answer": "A data analyst is a professional who specializes in analyzing data to find insights."},
        {"question": "What is a business analyst?", "answer": "A business analyst is a professional who specializes in analyzing business processes and requirements."},
        {"question": "What is a statistician?", "answer": "A statistician is a professional who specializes in analyzing data to draw inferences and make decisions."},
        {"question": "What is a data scientist?", "answer": "A data scientist is a professional who specializes in analyzing and modeling data."},
        {"question": "What is the CRISP-DM model?", "answer": "CRISP-DM (Cross-Industry Standard Process for Data Mining) is a widely used methodology for data mining projects."},
        {"question": "What is a data pipeline?", "answer": "A data pipeline is a set of processes that move data from one place to another."},
        {"question": "What is a machine learning model?", "answer": "A machine learning model is a mathematical model that can learn from data and make predictions."},
        {"question": "What is a data warehouse?", "answer": "A data warehouse is a large repository of data that is used for reporting and analysis."},
        {"question": "What is a data lake?", "answer": "A data lake is a large repository of data that is used for storage and processing."},
        {"question": "What is a data visualization?", "answer": "A data visualization is a graphical representation of data that helps to understand and communicate insights."},
        {"question": "What is a data mining?", "answer": "Data mining is the process of discovering patterns and insights in large datasets."},
        {"question": "What is a data cleaning?", "answer": "Data cleaning is the process of removing or correcting errors and inconsistencies in data."},
        {"question": "What is a data analysis?", "answer": "Data analysis is the process of analyzing data to find insights and make decisions."},
        {"question": "What is a data modeling?", "answer": "Data modeling is the process of creating a model of data to represent the structure and relationships of data."},
        {"question": "What is a data mining?", "answer": "Data mining is the process of discovering patterns and insights in large datasets."},
        # Add up to 30 questions and answers
    ],
}

st.title("Interview Questions and Answers")

# Create tabs for topics
tabs = st.tabs(list(interview_questions.keys()))

# Display questions and answers under each tab
for topic, tab in zip(interview_questions.keys(), tabs):
    with tab:
        st.header(f"{topic} Interview Questions")
        for qa in interview_questions[topic]:
            st.subheader(f'Q. {qa["question"]}')
            st.write(f'A. {qa["answer"]}')
            st.markdown("---")  # Horizontal line
