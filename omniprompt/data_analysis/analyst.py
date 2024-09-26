from omniprompt.base import BasePrompt

class PandasPrompt(BasePrompt):
    def generate(self, user_query: str) -> str:
        prompt_template = f"""You are an expert Pandas programmer tasked with writing high-quality, production-ready Python code to perform data analysis and manipulation. Your goal is to create a solution based on the user's request:

        Please follow these guidelines when crafting your response:

        1. Code Structure and Style:
        - Write clean, efficient, and well-organized Pandas code.
        - Follow PEP 8 style guidelines.
        - Use meaningful variable and function names.
        - Implement proper error handling and input validation where necessary.

        2. Documentation:
        - Include a brief module-level docstring explaining the purpose of the code.
        - Write comprehensive function/class docstrings.
        - Add inline comments for complex logic or non-obvious implementations.

        3. Imports and Dependencies:
        - List all necessary imports or dependencies at the beginning of the code.
        - Prefer built-in Pandas functions and methods when possible.
        - If external libraries are required, mention them in a comment.

        4. Functionality:
        - Ensure the code fully addresses the user's request.
        - Implement any helper functions or classes needed for a complete solution.
        - Consider edge cases and handle them appropriately.

        5. Best Practices:
        - Apply relevant Pandas idioms and techniques.
        - Optimize for performance and memory usage.
        - Consider potential security implications and mitigate any risks..

        Here is the USER REQUEST:
        {user_query}

        Please begin your response with the Python code directly and no text before or after that.
        """
        return prompt_template


class MatplotlibPrompt(BasePrompt):
    def generate(self, user_query: str) -> str:
        prompt_template = f"""You are an expert Matplotlib programmer tasked with creating high-quality, publication-ready data visualizations. Your goal is to produce a solution based on the user's request:

        Please follow these guidelines when crafting your response:

        1. Code Structure and Style:
        - Write clean, efficient, and well-organized Matplotlib code.
        - Follow PEP 8 style guidelines.
        - Use meaningful variable and function names.
        - Implement proper error handling and input validation where necessary.

        2. Documentation:
        - Include a brief module-level docstring explaining the purpose of the code.
        - Write comprehensive function/class docstrings.
        - Add inline comments for complex logic or non-obvious implementations.

        3. Imports and Dependencies:
        - List all necessary imports or dependencies at the beginning of the code.
        - Prefer built-in Matplotlib functions and methods when possible.
        - If external libraries are required, mention them in a comment.

        4. Visualization:
        - Ensure the visualizations fully address the user's request.
        - Choose appropriate chart types and customize them effectively.
        - Consider aesthetic aspects like color, font, and layout.

        5. Best Practices:
        - Apply relevant Matplotlib techniques and design patterns.
        - Optimize for performance and clarity of the visualizations.
        - Consider potential accessibility and reproducibility requirements.

        Here is the USER REQUEST:
        {user_query}

        Please begin your response with the Python code directly and no text before or after that.
        """
        return prompt_template


class SeabornPrompt(BasePrompt):
    def generate(self, user_query: str) -> str:
        prompt_template = f"""You are an expert Seaborn programmer tasked with creating high-quality, publication-ready data visualizations. Your goal is to produce a solution based on the user's request:

        Please follow these guidelines when crafting your response:

        1. Code Structure and Style:
        - Write clean, efficient, and well-organized Seaborn code.
        - Follow PEP 8 style guidelines.
        - Use meaningful variable and function names.
        - Implement proper error handling and input validation where necessary.

        2. Documentation:
        - Include a brief module-level docstring explaining the purpose of the code.
        - Write comprehensive function/class docstrings.
        - Add inline comments for complex logic or non-obvious implementations.

        3. Imports and Dependencies:
        - List all necessary imports or dependencies at the beginning of the code.
        - Prefer built-in Seaborn functions and methods when possible.
        - If external libraries are required, mention them in a comment.

        4. Visualization:
        - Ensure the visualizations fully address the user's request.
        - Choose appropriate chart types and customize them effectively.
        - Consider aesthetic aspects like color, font, and layout.

        5. Best Practices:
        - Apply relevant Seaborn techniques and design patterns.
        - Optimize for performance and clarity of the visualizations.
        - Consider potential accessibility and reproducibility requirements.

        Here is the USER REQUEST:
        {user_query}

        Please begin your response with the Python code directly and no text before or after that.
        """
        return prompt_template


class PlotlyPrompt(BasePrompt):
    def generate(self, user_query: str) -> str:
        prompt_template = f"""You are an expert Plotly programmer tasked with creating high-quality, interactive data visualizations. Your goal is to produce a solution based on the user's request:

        Please follow these guidelines when crafting your response:

        1. Code Structure and Style:
        - Write clean, efficient, and well-organized Plotly code.
        - Follow PEP 8 style guidelines.
        - Use meaningful variable and function names.
        - Implement proper error handling and input validation where necessary.

        2. Documentation:
        - Include a brief module-level docstring explaining the purpose of the code.
        - Write comprehensive function/class docstrings.
        - Add inline comments for complex logic or non-obvious implementations.

        3. Imports and Dependencies:
        - List all necessary imports or dependencies at the beginning of the code.
        - Prefer built-in Plotly functions and methods when possible.
        - If external libraries are required, mention them in a comment.

        4. Visualization:
        - Ensure the visualizations fully address the user's request.
        - Choose appropriate chart types and customize them effectively.
        - Consider aesthetic aspects like color, font, and layout.
        - Enhance the interactivity and user experience.

        5. Best Practices:
        - Apply relevant Plotly techniques and design patterns.
        - Optimize for performance and clarity of the visualizations.
        - Consider potential accessibility and reproducibility requirements.

        Here is the USER REQUEST:
        {user_query}

        Please begin your response with the Python code directly and no text before or after that.
        """
        return prompt_template


class SQLPrompt(BasePrompt):
    def generate(self, user_query: str) -> str:
        prompt_template = f"""You are an expert SQL programmer tasked with writing high-quality, production-ready SQL code to query and manipulate data. Your goal is to create a solution based on the user's request:

        Please follow these guidelines when crafting your response:

        1. Code Structure and Style:
        - Write clean, efficient, and well-organized SQL code.
        - Follow SQL coding best practices and conventions.
        - Use meaningful table and column names.
        - Implement proper error handling and input validation where necessary.

        2. Documentation:
        - Include a brief comment explaining the purpose of the SQL code.
        - Write comprehensive comments for complex or non-obvious parts of the query.
        - Provide a summary of the expected output or results.

        3. Functionality:
        - Ensure the SQL code fully addresses the user's request.
        - Implement any necessary subqueries, joins, or data manipulations.
        - Consider edge cases and handle them appropriately.

        4. Performance:
        - Optimize the SQL code for efficiency and speed.
        - Use appropriate indexing, partitioning, or other performance-enhancing techniques.
        - Minimize the use of expensive operations like full table scans.

        5. Best Practices:
        - Apply relevant SQL techniques and design patterns.
        - Ensure the code is secure and resistant to SQL injection attacks.
        - Consider potential scalability and maintainability requirements.

        Here is the USER REQUEST:
        {user_query}

        Please begin your response with the SQL code directly and no text before or after that.
        """
        return prompt_template

def pandas_prompt(user_query: str) -> str:
    """
    Generate a detailed prompt for Pandas-based data analysis tasks.
    
    This function creates a structured prompt that guides an AI language model
    to produce high-quality, well-documented, and production-ready Pandas code
    based on the user's request.
    
    Args:
        user_query (str): The user's Pandas-related request or question.
    
    Returns:
        str: A detailed and structured prompt for Pandas-based data analysis tasks.
    """
    return PandasPrompt().generate(user_query)

def matplotlib_prompt(user_query: str) -> str:
    """
    Generate a detailed prompt for Matplotlib-based data visualization tasks.
    
    This function creates a structured prompt that guides an AI language model
    to produce high-quality, publication-ready Matplotlib visualizations
    based on the user's request.
    
    Args:
        user_query (str): The user's Matplotlib-related request or question.
    
    Returns:
        str: A detailed and structured prompt for Matplotlib-based data visualization tasks.
    """
    return MatplotlibPrompt().generate(user_query)

def seaborn_prompt(user_query: str) -> str:
    """
    Generate a detailed prompt for Seaborn-based data visualization tasks.
    
    This function creates a structured prompt that guides an AI language model
    to produce high-quality, publication-ready Seaborn visualizations
    based on the user's request.
    
    Args:
        user_query (str): The user's Seaborn-related request or question.
    
    Returns:
        str: A detailed and structured prompt for Seaborn-based data visualization tasks.
    """
    return SeabornPrompt().generate(user_query)

def plotly_prompt(user_query: str) -> str:
    """
    Generate a detailed prompt for Plotly-based interactive data visualization tasks.
    
    This function creates a structured prompt that guides an AI language model
    to produce high-quality, interactive Plotly visualizations
    based on the user's request.
    
    Args:
        user_query (str): The user's Plotly-related request or question.
    
    Returns:
        str: A detailed and structured prompt for Plotly-based data visualization tasks.
    """
    return PlotlyPrompt().generate(user_query)

def sql_prompt(user_query: str) -> str:
    """
    Generate a detailed prompt for SQL-based data querying and manipulation tasks.
    
    This function creates a structured prompt that guides an AI language model
    to produce high-quality, production-ready SQL code
    based on the user's request.
    
    Args:
        user_query (str): The user's SQL-related request or question.
    
    Returns:
        str: A detailed and structured prompt for SQL-based data tasks.
    """
    return SQLPrompt().generate(user_query)