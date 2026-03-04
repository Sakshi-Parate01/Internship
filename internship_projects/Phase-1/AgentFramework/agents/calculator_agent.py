import re
from agents.base_agent import Agent
class CalculatorAgent(Agent):
    def handle(self, query: str) -> str:
        try:
            expression = re.findall(r"\d+|\+|\-|\*|\/", query)
            expression = "".join(expression)
            result = eval(expression)
            return f"Result: {result}"
        except Exception:
            return "Invalid calculation input."

