from omniprompt.base import BasePrompt

class CoderPrompt(BasePrompt):
    def generate(self, user_query: str, language: str) -> str:
        prompt_template = f"""You are an expert {language} programmer tasked with writing high-quality, production-ready {language} code. Your goal is to create a solution based on the user's request:

        Please follow these guidelines when crafting your response:

        1. Code Structure and Style:
        - Write clean, efficient, and well-organized code.
        - Follow appropriate style guidelines for {language}.
        - Use meaningful variable and function names.
        - Implement proper error handling and input validation where necessary.

        2. Documentation:
        - Include a brief module-level docstring explaining the purpose of the code.
        - Write comprehensive function/class docstrings.
        - Add inline comments for complex logic or non-obvious implementations.

        3. Imports and Dependencies:
        - List all necessary imports or dependencies at the beginning of the code.
        - Prefer standard libraries or built-in features of {language} when possible.
        - If external libraries are required, mention them in a comment.

        4. Functionality:
        - Ensure the code fully addresses the user's request.
        - Implement any helper functions or classes needed for a complete solution.
        - Consider edge cases and handle them appropriately.

        5. Best Practices:
        - Apply relevant design patterns or idioms commonly used in {language}.
        - Optimize for readability and maintainability.
        - Consider potential security implications and mitigate any risks.

        Here is the USER REQUEST:
        {user_query}

        Please begin your response with the {language} code directly and no text before or after that.
        """
        return prompt_template


class CodeRefinerPrompt(BasePrompt):
    def generate(self, user_code: str, language: str) -> str:
        prompt_template = f"""You are an experienced {language} developer tasked with improving and refining the provided code. Your goal is to enhance the code while maintaining its original functionality.

        Please follow these guidelines when refining the code:

        1. Code Quality:
        - Ensure the code follows proper style guidelines for {language}.
        - Remove any redundant or unnecessary code.
        - Simplify the logic wherever possible without affecting functionality.

        2. Optimization:
        - Improve the efficiency of the code by optimizing algorithms, loops, or data structures.
        - Ensure the code handles large data sets or complex operations efficiently.
        - Consider the time and space complexity of the code.

        3. Readability and Maintainability:
        - Improve variable and function names to make the code more understandable.
        - Add meaningful comments to explain complex or non-obvious parts of the code.
        - Ensure the code is modular and well-structured for future maintainability.

        4. Testing and Validation:
        - Make sure the code works correctly and passes all edge cases.

        Here is the provided code that needs refinement:
        {user_code}

        Please begin your response with the refined {language} code directly and no text before or after that.
        """
        return prompt_template


class CodeOptimizerPrompt(BasePrompt):
    def generate(self, user_code: str, language: str) -> str:
        prompt_template = f"""You are an expert {language} programmer tasked with optimizing the provided code for performance and efficiency. Your goal is to enhance its execution speed and reduce resource usage without changing the functionality.

        Please follow these guidelines when optimizing the code:

        1. Performance Improvements:
        - Analyze the code for performance bottlenecks.
        - Optimize expensive operations such as loops, recursive functions, and data processing steps.
        - Consider more efficient algorithms or data structures where applicable.

        2. Memory Usage:
        - Minimize memory usage by optimizing data structures or using more memory-efficient approaches.
        - Avoid unnecessary memory allocation or copying of data.

        3. Time Complexity:
        - Aim to reduce the time complexity of the code where possible (e.g., reducing O(n^2) to O(n log n) or O(n)).
        - Explain the changes made and how they improve time or space complexity.

        4. Code Integrity:
        - Ensure that the optimized code produces the same results as the original.

        5. Documentation:
        - Explain any changes in the logic or approach clearly in the code comments.
        - If necessary, refactor the code for better readability after optimization.

        Here is the provided code for optimization:
        {user_code}

        Please begin your response with the optimized {language} code directly and no text before or after that.
        """
        return prompt_template


class CodeErrorCorrectorPrompt(BasePrompt):
    def generate(self, user_code: str, code_error: str, language: str) -> str:
        prompt_template = f"""You are a skilled {language} programmer responsible for identifying and fixing errors in the following code. Your goal is to ensure the code runs correctly and efficiently.

        Please follow these guidelines when correcting the code:

        1. Bug Identification and Fixing:
        - Review the code for syntax errors, logical errors, and runtime exceptions.
        - Fix any issues that may cause the code to crash or behave unexpectedly.

        2. Validation:
        - Ensure all edge cases are properly handled.
        - Consider potential input validation or error handling improvements.

        3. Code Quality:
        - Follow proper style guidelines to maintain clean and readable code.
        - Add meaningful comments explaining any non-trivial changes.

        Here is the provided code with errors:
        {user_code}

        Here is the error that this code encountered:
        {code_error}

        Please begin your response with the corrected {language} code directly and no text before or after that.
        """
        return prompt_template


def coder_prompt(user_query: str, language: str) -> str:
    """
    Generate a detailed prompt for coding tasks in the specified language.
    
    This function creates a structured prompt that guides an AI language model
    to produce high-quality, well-documented, and production-ready code
    based on the user's request.
    
    Args:
        user_query (str): The user's coding request or question.
        language (str): The programming language for the task.
    
    Returns:
        str: A detailed and structured prompt for coding tasks.
    """
    return CoderPrompt().generate(user_query, language)


def code_refiner_prompt(user_code: str, language: str) -> str:
    """
    Generate a detailed prompt to refine existing code in the specified language.
    
    This function creates a prompt that guides an AI language model
    to improve and clean up the provided code while maintaining functionality.
    
    Args:
        user_code (str): The user's existing code.
        language (str): The programming language of the code.
    
    Returns:
        str: A detailed and structured prompt for code refinement.
    """
    return CodeRefinerPrompt().generate(user_code, language)


def code_optimizer_prompt(user_code: str, language: str) -> str:
    """
    Generate a detailed prompt for code optimization in the specified language.
    
    This function creates a prompt that guides an AI language model
    to optimize the provided code for performance, efficiency, and resource usage.
    
    Args:
        user_code (str): The user's existing code.
        language (str): The programming language of the code.
    
    Returns:
        str: A detailed and structured prompt for code optimization.
    """
    return CodeOptimizerPrompt().generate(user_code, language)


def code_error_corrector_prompt(user_code: str, code_error: str, language: str) -> str:
    """
    Generate a detailed prompt for code error correction in the specified language.
    
    This function creates a prompt that guides an AI language model
    to identify and fix errors in the provided code, ensuring it runs correctly.
    
    Args:
        user_code (str): The user's code with errors.
        code_error (str): The error encountered in the code.
        language (str): The programming language of the code.
    
    Returns:
        str: A detailed and structured prompt for code error correction.
    """
    return CodeErrorCorrectorPrompt().generate(user_code, code_error, language)