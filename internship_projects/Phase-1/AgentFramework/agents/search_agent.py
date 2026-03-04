from agents.base_agent import Agent
class SearchAgent(Agent):
    def handle(self, query: str) -> str:
        keyword = query.replace("search", "").strip()
        
        if not keyword:
            return "Please provide something to search."
        return f"Simulated search result for '{keyword}'"