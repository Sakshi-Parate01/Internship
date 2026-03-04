from agents.search_agent import SearchAgent
from agents.calculator_agent import CalculatorAgent

class Router:
    def __init__(self):
        self.search_agent = SearchAgent()
        self.calculator_agent = CalculatorAgent()
    
    def route(self, query: str) -> str:
        query_lower = query.lower()

        if "search" in query_lower:
            return self.search_agent.handle(query)
        elif any(op in query_lower for op in ["+", "-", "*", "/"]):
            return self.calculator_agent.handle(query)
        else:
            return "No suitable agent found."