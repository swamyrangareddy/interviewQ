import streamlit as st

# Dictionary containing topics and their interview questions with answers
interview_questions = {
    "Python": [
            {"Q1": {
            "question": "Write a Python program to check if a number is even or odd.",
            "answer": """num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")""",
            "explanation": "This program checks if a number is divisible by 2. If the remainder is 0, the number is even; otherwise, it's odd."
        },
        "Q2": {
            "question": "Write a Python function to reverse a string.",
            "answer": """def reverse_string(s):
        return s[::-1]""",
            "explanation": "This function uses slicing to reverse the input string. The slicing feature makes reversing strings concise and efficient."
        },
        "Q3": {
            "question": "How can you find the largest number in a list?",
            "answer": """def find_largest(numbers):
        return max(numbers)""",
            "explanation": "The max() function scans through the list and returns the highest value, making it a straightforward solution."
        },
        "Q4": {
            "question": "Write a program to calculate the factorial of a number.",
            "answer": """def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)""",
            "explanation": "This recursive function multiplies the number by the factorial of (number - 1) until it reaches the base case of 0."
        },
        "Q5": {
            "question": "How do you check if a string is a palindrome?",
            "answer": """def is_palindrome(s):
        return s == s[::-1]""",
            "explanation": "The function compares the input string to its reversed version. If they are the same, it returns True."
        },
        "Q6": {
            "question": "Write a program to count the number of vowels in a given string.",
            "answer": """def count_vowels(s):
        return sum(1 for char in s if char.lower() in 'aeiou')""",
            "explanation": "The function iterates through the string, checking for vowels and summing the matches, ensuring case-insensitivity."
        },
        "Q7": {
            "question": "How do you remove duplicates from a list?",
            "answer": """def remove_duplicates(lst):
        return list(set(lst))""",
            "explanation": "Converting the list to a set removes duplicates, and converting it back to a list ensures the result is in list form."
        },
        "Q8": {
            "question": "Write a program to find the common elements in two lists.",
            "answer": """def common_elements(list1, list2):
        return list(set(list1) & set(list2))""",
            "explanation": "The set intersection operator '&' identifies elements common to both lists, which are then converted back to a list."
        },
        "Q9": {
            "question": "How do you merge two dictionaries in Python?",
            "answer": """dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    merged = {**dict1, **dict2}""",
            "explanation": "Using the dictionary unpacking operator '**', values from dict2 overwrite dict1 in case of duplicate keys."
        },
        "Q10": {
            "question": "Write a program to sort a list of numbers.",
            "answer": """def sort_numbers(numbers):
        return sorted(numbers)""",
            "explanation": "The sorted() function returns a new list containing all elements in ascending order."
        },
        "Q11": {
            "question": "Write a program to find the Fibonacci series up to n.",
            "answer": """def fibonacci(n):
        fib_series = [0, 1]
        while len(fib_series) < n:
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series[:n]""",
            "explanation": "The Fibonacci series starts with 0 and 1. Each subsequent number is the sum of the two preceding numbers."
        },
        "Q12": {
            "question": "Write a Python function to check if a number is prime.",
            "answer": """def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True""",
            "explanation": "The function checks divisors up to the square root of the number, which is computationally efficient for prime checks."
        }
}# Add up to 30 questions and answers
    ],
    "SQL": [{
        # like python questions and answers for SQL with quries and answers
        "Q1": {
            "question": "What is SQL?",
            "answer": "SQL (Structured Query Language) is a domain-specific language used to interact with databases.",
            "explanation": "SQL is used to query and manipulate data stored in databases."
        },        
        "Q2": {
            "question": "What is a database?",
            "answer": "A database is a collection of structured data, typically stored in a relational database management system (RDBMS).",
            "explanation": "Databases are typically used to store and retrieve data in a structured format, such as tables and relations."
        },
        "Q3": {
            "question": "What is a table?",
            "answer": "A table is a collection of rows and columns, where each row represents a record and each column holds a specific type of data.",
            "explanation": "Tables store data in a structured format, with rows representing records and columns representing different attributes."
        },
        "Q4": {
            "question": "What is a primary key?",
            "answer": "A primary key is a unique identifier for each record in a table.",
            "explanation": "Primary keys are used to ensure that each record in a table is unique and can be easily identified."
        },
        "Q5": { 
            "question": "What is a foreign key?",
            "answer": "A foreign key is a field in a table that links to the primary key of another table.",
            "explanation": "Foreign keys establish relationships between tables by referencing the primary key of another table."
        },
        "Q6": {
            "question": "What is a join?",
            "answer": "A join is a SQL operation that combines rows from two or more tables based on a related column between them.",
            "explanation": "Joins are used to retrieve data from multiple tables based on a common column, such as a primary key and foreign key relationship."
        },
        "Q7": {
            "question": "What is a subquery?",
            "answer": "A subquery is a query nested within another query.",
            "explanation": "Subqueries are used to retrieve data from a table based on the results of another query."
        },
        "Q8": {
            "question": "What is a view?",
            "answer": "A view is a virtual table based on a query.",
            "explanation": "Views are used to provide a convenient way to access a subset of data from a table."
        },
        "Q9": {
            "question": "What is a stored procedure?",
            "answer": "A stored procedure is a collection of SQL statements that can be executed as a single unit.",    
            "explanation": "Stored procedures are used to encapsulate and execute complex logic on the database server."
        },
        "Q10": {
            "question": "What is a trigger?",
            "answer": "A trigger is a set of actions that are automatically performed in response to certain events on a table.",
            "explanation": "Triggers are used to enforce data integrity rules or perform actions based on changes to the database."
        }
    },
    ],
    "Excel": [{
        "Q1": {
            "question": "What is Excel?",
            "answer": "Excel is a spreadsheet program used for data analysis, visualization, and management.",
            "explanation": "Excel is a widely used tool for organizing, analyzing, and presenting data in a tabular format."
        },
        "Q2": {
            "question": "What is a formula in Excel?",
            "answer": "A formula in Excel is an expression that performs calculations on values in cells.",
            "explanation": "Formulas can be used to perform mathematical operations, manipulate text, and more."
        },
        "Q3": {
            "question": "What is a chart in Excel?",
            "answer": "A chart in Excel is a graphical representation of data in a spreadsheet.",
            "explanation": "Charts can help visualize data trends, comparisons, and relationships."
        },
        "Q4": {
            "question": "What is a pivot table in Excel?",
            "answer": "A pivot table in Excel is a table that organizes data based on one or more categories.",
            "explanation": "Pivot tables are used to summarize and analyze data in a tabular format."
        },
        "Q5": {
            "question": "What is a macro in Excel?",
            "answer": "A macro in Excel is a collection of statements that perform a specific task or set of tasks.",
            "explanation": "Macros can be used to automate tasks and processes in Excel."
        },
        "Q6": {
            "question": "How do you create a formula in Excel?",    
            "answer": "To create a formula in Excel, start a cell with an equal sign (=) followed by the formula expression.",
            "explanation": "Formulas can include cell references, functions, and operators to perform calculations."
            },
        "Q7": { 
            "question": "How do you create a chart in Excel?",
            "answer": "To create a chart in Excel, select the data you want to visualize, go to the 'Insert' tab, and choose a chart type.",
            "explanation": "Charts can be customized with different styles, colors, and labels to enhance data visualization."
        },
        "Q8": {
            "question": "How do you create a pivot table in Excel?",
            "answer": "To create a pivot table in Excel, select the data you want to analyze, go to the 'Insert' tab, and choose 'PivotTable'.",
            "explanation": "Pivot tables can be used to summarize and analyze large datasets by grouping and aggregating data."
        },
        "Q9": {
            "question": "How do you create a macro in Excel?",
            "answer": "To create a macro in Excel, press Alt + F11 to open the VBA editor, insert a new module, and write the macro code.",
            "explanation": "Macros can be recorded or written manually to automate repetitive tasks in Excel."
        },
        "Q10": {
            "question": "What is the difference between a formula and a chart in Excel?",
            "answer": "A formula is a mathematical expression that performs calculations on values in cells, while a chart is a graphical representation of data in a spreadsheet.",
            "explanation": "Formulas can be used to perform calculations, manipulate text, and more, while charts are used to visualize data trends, comparisons, and relationships."
        }
    },
    ],
    "Pandas": [
        {
        "Q1": {
            "question": "What is Pandas?",
            "answer": "Pandas is a Python library for data manipulation and analysis.",
            "explanation": "Pandas provides data structures and functions to work with structured data, such as tables and time series."
        },
        "Q2": {
            "question": "What is a DataFrame in Pandas?",
            "answer": "A DataFrame in Pandas is a two-dimensional data structure that stores data in rows and columns.",            
            "explanation": "DataFrames are the primary data structure in Pandas and are used to store and manipulate tabular data."
        },
        "Q3": {
            "question": "What is a Series in Pandas?",
            "answer": "A Series in Pandas is a one-dimensional data structure that stores data in a labeled array.",
            "explanation": "Series are used to represent a single column or row of data in a DataFrame."
        },
        "Q4": {
            "question": "What is a MultiIndex in Pandas?",
            "answer": "A MultiIndex in Pandas is a hierarchical index that allows for multiple levels of indexing.",
            "explanation": "MultiIndex is used to create a hierarchical index for a DataFrame, allowing for multiple levels of indexing."
        },
        "Q5": {
            "question": "What is a pivot table in Pandas?",
            "answer": "A pivot table in Pandas is a two-dimensional table that summarizes data based on one or more categories.",
            "explanation": "Pivot tables are used to summarize and analyze data in a tabular format."
        },
        "Q6": {
            "question": "What is a groupby operation in Pandas?",
            "answer": "A groupby operation in Pandas is used to group data based on one or more columns and perform operations on the groups.",
            "explanation": "Groupby operations are used to aggregate data, calculate statistics, and more."
        },
        "Q7": {
            "question": "What is a merge operation in Pandas?",
            "answer": "A merge operation in Pandas is used to combine two DataFrames based on a common column.",
            "explanation": "Merge operations are used to combine data from multiple sources into a single DataFrame."
        },
        "Q8": {
            "question": "What is a pivot table in Pandas?",
            "answer": "A pivot table in Pandas is a two-dimensional table that summarizes data based on one or more categories.",
            "explanation": "Pivot tables are used to summarize and analyze data in a tabular format."
        },
        "Q9": {
            "question": "What is a pivot table in Pandas?",
            "answer": "A pivot table in Pandas is a two-dimensional table that summarizes data based on one or more categories.",
            "explanation": "Pivot tables are used to summarize and analyze data in a tabular format."
        },
        "Q10": {
            "question": "What is a pivot table in Pandas?",
            "answer": "A pivot table in Pandas is a two-dimensional table that summarizes data based on one or more categories.",
            "explanation": "Pivot tables are used to summarize and analyze data in a tabular format."
            }
        },
    ],
    "Power BI": [
        {
        "Q1": {
            "question": "What is Power BI?",
            "answer": "Power BI is a business analytics tool developed by Microsoft that allows users to visualize and analyze data.",
            "explanation": "Power BI is a powerful tool for business users to gain insights from their data."
        },
        "Q2":
            {
            "question": "What are the different types of Power BI reports?",
            "answer": "Power BI reports can be created using various types, including tables, charts, maps, and dashboards.",
            "explanation": "Power BI offers a wide range of report types to suit different data visualization needs."
        },
        "Q3": {
            "question": "What is a Power BI dashboard?",
            "answer": "A Power BI dashboard is a collection of interactive visualizations and widgets that allow users to explore data in a user-friendly way.",
            "explanation": "Dashboards provide a high-level overview of key metrics and insights from the underlying data."
        },
        "Q4": {
            "question": "What is a Power BI dataset?",
            "answer": "A Power BI dataset is a collection of data that can be used to create reports and dashboards.",
            "explanation": "Datasets are the foundation of Power BI reports and dashboards."
        },
        "Q5": {
            "question": "What is Power Query in Power BI?",
            "answer": "Power Query is a data transformation tool in Power BI that allows users to import, transform, and clean data from various sources.",
            "explanation": "Power Query simplifies the process of preparing data for analysis in Power BI."
        },
        "Q6": {
            "question": "What is Power Pivot in Power BI?",
            "answer": "Power Pivot is a data modeling tool in Power BI that allows users to create complex data models and perform advanced data analysis.",
            "explanation": "Power Pivot enables users to perform complex calculations and data analysis on large datasets."
        },
        "Q7": {
            "question": "What is Power View in Power BI?",
            "answer": "Power View is a data visualization tool in Power BI that allows users to create interactive visualizations and dashboards.",
            "explanation": "Power View provides a wide range of visualization options to help users understand their data."
        },
        "Q8": {
            "question": "What is Power BI Desktop?",
            "answer": "Power BI Desktop is a free desktop application that allows users to create Power BI reports and dashboards.",
            "explanation": "Power BI Desktop provides a powerful set of tools for data modeling, visualization, and analysis."
        },
        "Q9": {
            "question": "What is Power BI Service?",
            "answer": "Power BI Service is a cloud-based platform that allows users to share and collaborate on Power BI reports and dashboards.",
            "explanation": "Power BI Service enables users to access and share reports and dashboards from anywhere."
        },
        "Q10": {
            "question": "What is Power BI Embedded?",
            "answer": "Power BI Embedded is a service that allows developers to embed Power BI reports and dashboards into custom applications.",
            "explanation": "Power BI Embedded enables developers to integrate Power BI functionality into their own applications."
        }
    },
            ],
    "Data Analytics": [
        {
        "Q1": {
            "question": "What is Data Analytics?",            
            "answer": "Data Analytics is the process of extracting meaningful insights from data.",
            "explanation": "Data Analytics involves analyzing data to discover patterns, trends, and insights that can inform decision-making."
        },
        "Q2": {
            "question": "What are the steps in a Data Analytics project?",
            "answer": "Data collection, data cleaning, data analysis, data visualization, and reporting.",
            "explanation": "Data Analytics projects typically involve these steps to transform raw data into actionable insights."
        },
        "Q3":
        {
            "question": "What is the difference between Data Analytics and Data Science?",
            "answer": "Data Analytics focuses on analyzing data to find insights, while Data Science involves a broader range of activities, including data collection, modeling, and deployment.",
            "explanation": "Data Analytics is a subset of Data Science, which encompasses a wider range of data-related activities."
        },
        "Q4": {
            "question": "What is a Data Analyst?",
            "answer": "A Data Analyst is a professional who specializes in analyzing data to find insights.",
            "explanation": "Data Analysts use statistical and analytical techniques to interpret data and provide actionable recommendations."
        },
        "Q5": {
            "question": "What is a Business Analyst?",
            "answer": "A Business Analyst is a professional who specializes in analyzing business processes and requirements.",
            "explanation": "Business Analysts use data and analytical tools to identify business needs and recommend solutions."
        },
        "Q6": {
            "question": "What is a Data Engineer?",
            "answer": "A Data Engineer is a professional who specializes in building and maintaining data pipelines.",
            "explanation": "Data Engineers are responsible for designing, building, and maintaining the infrastructure needed to collect, process, and store data."
        },
        "Q7": {
            "question": "What is a Machine Learning Engineer?",
            "answer": "A Machine Learning Engineer is a professional who specializes in building and deploying machine learning models.",
            "explanation": "Machine Learning Engineers are responsible for designing, building, and deploying machine learning models to solve business problems."
        },
        "Q8": {
            "question": "What is a Data Scientist?",
            "answer": "A Data Scientist is a professional who specializes in analyzing and modeling data.",
            "explanation": "Data Scientists use statistical and analytical techniques to extract insights from data and build predictive models."
        },
        "Q9": {
            "question": "What is the CRISP-DM model?",  
            "answer": "CRISP-DM (Cross-Industry Standard Process for Data Mining) is a widely used methodology for data mining projects.",
            "explanation": "The CRISP-DM model outlines a structured approach to data mining projects, including data preparation, modeling, and evaluation."
        },
        "Q10": {
            "question": "What is a Data Warehouse?",
            "answer": "A Data Warehouse is a centralized repository of data that is designed to support business decision-making.",
            "explanation": "Data Warehouses store large amounts of data from various sources and provide a single, unified view of the data."
        }
    },
    ],
    "Data Science": [
        {
        "Q1": {
            "question": "What is Data Science?",
            "answer": "Data Science is a interdisciplinary field that uses statistical and computational methods to extract insights from data.",
            "explanation": "Data Science involves applying advanced statistical and computational techniques to extract insights from data."
        },
        "Q2": {
            "question": "What is a Data Scientist?",
            "answer": "A Data Scientist is a professional who specializes in analyzing and modeling data.",
            "explanation": "Data Scientists use statistical and analytical techniques to extract insights from data and build predictive models."
        },
        "Q3": {
            "question": "What is a Data Mining?",
            "answer": "Data Mining is the process of discovering patterns and insights from large datasets.",
            "explanation": "Data Mining involves using algorithms and statistical techniques to extract useful information from large datasets."
        },
        "Q4": {
            "question": "What is a Data Visualization?",    
            "answer": "Data Visualization is the graphical representation of data to help users understand and interpret information.",
            "explanation": "Data Visualization uses charts, graphs, and other visual elements to communicate data insights effectively."
        },
        "Q5": {
            "question": "What is a Machine Learning?",
            "answer": "Machine Learning is a subset of Data Science that focuses on building models that can learn from data and make predictions.",
            "explanation": "Machine Learning algorithms learn from data and make predictions based on patterns and relationships."
        },
        "Q6": {
            "question": "What is a Deep Learning?",
            "answer": "Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers to learn complex patterns from data.",
            "explanation": "Deep Learning models can learn complex relationships and representations from large datasets."
        },
        "Q7": {
            "question": "What is a Neural Network?",
            "answer": "A Neural Network is a machine learning model inspired by the structure and function of the human brain.",
            "explanation": "Neural Networks consist of interconnected nodes or neurons that process information and learn from data."
        },
        "Q8": {
            "question": "What is a Natural Language Processing (NLP)?",
            "answer": "Natural Language Processing is a branch of artificial intelligence that focuses on the interaction between computers and humans using natural language.",
            "explanation": "NLP enables computers to understand, interpret, and generate human language."
        },
        "Q9": {
            "question": "What is a Data Science?",
            "answer": "Data Science is the interdisciplinary field that uses scientific methods, processes, algorithms, and systems to extract knowledge and insights from data.",
            "explanation": "Data Science involves using data to solve complex problems and make informed decisions."
        },
        "Q10": {
            "question": "What is Data Visualization?",
            "answer": "Data Visualization is the graphical representation of data to help users understand and interpret information.",
            "explanation": "Data Visualization uses charts, graphs, and other visual elements to communicate data insights effectively."
        }
    },
    ]
}

st.title("Interview Questions and Answers")


# Create tabs for topics
tabs = st.tabs(list(interview_questions.keys()))

# Display questions and answers under each tab
for topic, tab in zip(interview_questions.keys(), tabs):
    with tab:
        st.header(f"{topic} Interview Questions")
        for qa in interview_questions[topic]:
            for key,question in qa.items():
                if topic == "Python":
                    st.subheader(f'{key}: {question["question"]}')
                    st.write(f'Answer:')
                    st.code(question["answer"])
                    st.write(f'**Explanation:** {question["explanation"]}')
                    st.markdown("---")  # Horizontal line
                else:
                    st.subheader(f'{key}: {question["question"]}')
                    st.write(f'Answer:')
                    st.write(question["answer"])
                    st.write(f'**Explanation:** ')
                    st.write(question["explanation"])
                    st.markdown("---")  # Horizontal line
