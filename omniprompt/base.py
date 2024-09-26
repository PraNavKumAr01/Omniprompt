from abc import ABC, abstractmethod

class BasePrompt(ABC):
    @abstractmethod
    def generate(self, user_query: str) -> str:
        """
        Generate a prompt based on the user query.
        
        Args:
            user_query (str): The user's input or question.
        
        Returns:
            str: The generated prompt.
        """
        pass