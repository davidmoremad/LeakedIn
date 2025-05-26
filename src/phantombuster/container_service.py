from src.phantombuster.settings import Endpoints, PhantomBusterClient

class ContainerService:
    def __init__(self):
        self.client = PhantomBusterClient()
    
    def get_all_containers(self, agent_id):
        """Fetch all containers for an agent"""
        endpoint = Endpoints.CONTAINERS.format(agent_id)
        return self.client.get(endpoint)
    
    def get_container_details(self, container_id):
        """Get details for a specific container"""
        endpoint = Endpoints.CONTAINER.format(container_id)
        return self.client.get(endpoint)
    
    def get_container_output(self, container_id, raw=True):
        """Get output logs for a container"""
        endpoint = Endpoints.CONTAINER_OUTPUT.format(container_id, str(raw).lower())
        return self.client.get(endpoint)
    
    def get_container_results(self, container_id):
        """Get result data from a container"""
        endpoint = Endpoints.CONTAINER_RESULTS.format(container_id)
        return self.client.get(endpoint)
    
    def get_latest_container_results(self, agent_id):
        """Get results from the latest container of an agent"""
        containers = self.get_all_containers(agent_id)
        if not containers or len(containers) == 0:
            return None
            
        # Sort containers by launchTime (descending)
        containers.sort(key=lambda c: c.get("launchTime", 0), reverse=True)
        latest_container = containers[0]
        
        return self.get_container_results(latest_container["id"])