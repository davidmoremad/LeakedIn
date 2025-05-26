import time
from src.phantombuster.settings import Endpoints, PhantomBusterClient


class AgentService:
    def __init__(self):
        self.client = PhantomBusterClient()
    
    def get_all_agents(self):
        """Fetch all agents"""
        return self.client.get(Endpoints.AGENTS)
    
    def get_agent_details(self, agent_id):
        """Get details for a specific agent"""
        endpoint = Endpoints.AGENT.format(agent_id)
        return self.client.get(endpoint)
    
    def get_agent_output(self, agent_id):
        """Get output for a specific agent"""
        endpoint = Endpoints.AGENT_OUTPUT.format(agent_id)
        return self.client.get(endpoint)
    
    def launch_agent(self, agent_id, argument=None):
        """Launch an agent with optional arguments"""
        payload = {"id": agent_id}
        if argument:
            payload["argument"] = argument
        return self.client.post(Endpoints.AGENT_LAUNCH, data=payload)
    
    def save_agent(self, agent_data):
        """Create or update an agent"""
        return self.client.post(Endpoints.AGENT_SAVE, data=agent_data)
    
    def wait_for_agent_completion(self, agent_id, timeout=300, check_interval=10):
        """Wait for an agent to complete execution"""
        start_time = time.time()
        while time.time() - start_time < timeout:
            agent_details = self.get_agent_details(agent_id)
            status = agent_details.get("lastEndType")
            
            if status == "finished":
                return True
            elif status in ["error", "stopped"]:
                return False
                
            time.sleep(check_interval)
        
        return False  # Timeout