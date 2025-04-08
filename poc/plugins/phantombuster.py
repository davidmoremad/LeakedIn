# PhantomBuster Wrapper
import requests
from utils import setup_logger

class PhantomBuster(object):

  # Base URL
  BASE_URL = "https://api.phantombuster.com/api/v2/"

  # Endpoints
  ORGS = "orgs/fetch"
  AGENTS = "agents/fetch-all"
  AGENT = "agent/fetch?id={}"
  AGENT_OUTPUT = "agents/fetch-output?id={}"
  SCRIPTS = "scripts/fetch-all"
  SCRIPT = "script/fetch?id={}"
  CONTAINERS = "containers/fetch-all?agentId={}"
  CONTAINER = "containers/fetch?id={}"
  CONTAINER_OUTPUT = "containers/fetch-output?id={}&raw={}"
  CONTAINER_RESULTS = "containers/fetch-result-object?id={}"

  def __init__(self, api_key, org_id=None):
    """
    Initialize the PhantomBuster class with the API key.
    """
    self.api_key = api_key
    self.headers = {
      "X-Phantombuster-Key-1": self.api_key,
      "Content-Type": "application/json"
    }
    self.logger = setup_logger("PhantomBuster")
    self.logger.info("PhantomBuster initialized.")


  # ORGS
  # -------------------------------------------------------------

  def get_orgs(self):
    """
    Fetch all organizations.
    """
    url = self.BASE_URL + self.ORGS
    response = requests.get(url, headers=self.headers)
    if response.status_code == 200:
      self.logger.info("Fetched organizations successfully.")
      return response.json()
    else:
      self.logger.error(f"Failed to fetch organizations: {response.status_code}")
      return None
    
  def set_org(self, org_id):
    """
    Set the organization ID for the instance.
    """
    self.org_id = org_id
    self.logger.info(f"Organization ID set to {org_id}.")


  # AGENTS
  # -------------------------------------------------------------
    
  def get_agents(self):
    """
    Fetch all agents.
    """
    url = self.BASE_URL + self.AGENTS
    response = requests.get(url, headers=self.headers)
    if response.status_code == 200:
      self.logger.info("Fetched agents successfully.")
      return response.json()
    else:
      self.logger.error(f"Failed to fetch agents: {response.status_code}")
      return None
    
  def get_agent(self, agent_id):
    """
    Fetch a specific agent by ID.
    """
    url = self.BASE_URL + self.AGENT.format(agent_id)
    response = requests.get(url, headers=self.headers)
    if response.status_code == 200:
      self.logger.info(f"Fetched agent {agent_id} successfully.")
      return response.json()
    else:
      self.logger.error(f"Failed to fetch agent {agent_id}: {response.status_code}")
      return None
    
  def get_agent_last_output(self, agent_id):
    """
    Fetch the output of a specific agent by ID.
    """
    url = self.BASE_URL + self.AGENT_OUTPUT.format(agent_id)
    response = requests.get(url, headers=self.headers)
    if response.status_code == 200:
      self.logger.info(f"Fetched agent {agent_id} output successfully.")
      return response.json()
    else:
      self.logger.error(f"Failed to fetch agent {agent_id} output: {response.status_code}")
      return None

  
  # CONTAINERS
  # -------------------------------------------------------------

  def get_containers(self, agent_id):
    """
    Fetch all containers for a specific agent.
    """
    url = self.BASE_URL + self.CONTAINERS.format(agent_id)
    response = requests.get(url, headers=self.headers)
    if response.status_code == 200:
      self.logger.info(f"Fetched containers for agent {agent_id} successfully.")
      return response.json()
    else:
      self.logger.error(f"Failed to fetch containers for agent {agent_id}: {response.status_code}")
      return None
    
  def get_container(self, container_id):
    """
    Fetch a specific container by ID.
    """
    url = self.BASE_URL + self.CONTAINER.format(container_id)
    response = requests.get(url, headers=self.headers)
    if response.status_code == 200:
      self.logger.info(f"Fetched container {container_id} successfully.")
      return response.json()
    else:
      self.logger.error(f"Failed to fetch container {container_id}: {response.status_code}")
      return None
    
  def get_container_output(self, container_id, raw=False):
    """
    Fetch the output of a specific container by ID.
    If raw=True, returns the txt output. Else returns JSON.
    """
    url = self.BASE_URL + self.CONTAINER_OUTPUT.format(container_id, str(raw).lower())
    response = requests.get(url, headers=self.headers)
    if response.status_code == 200:
      self.logger.info(f"Fetched container {container_id} output successfully.")
      return response.json()
    else:
      self.logger.error(f"Failed to fetch container {container_id} output: {response.status_code}")
      return None
    
  def get_container_results(self, container_id):
    """
    Fetch the results of a specific container by ID.
    """
    url = self.BASE_URL + self.CONTAINER_RESULTS.format(container_id)
    response = requests.get(url, headers=self.headers)
    if response.status_code == 200:
      self.logger.info(f"Fetched container {container_id} results successfully.")
      return response.json()
    else:
      self.logger.error(f"Failed to fetch container {container_id} results: {response.status_code}")
      return None


  # SCRIPTS
  # -------------------------------------------------------------

  def get_scripts(self):
    """
    Fetch all scripts.
    """
    url = self.BASE_URL + self.SCRIPTS
    response = requests.get(url, headers=self.headers)
    if response.status_code == 200:
      self.logger.info("Fetched scripts successfully.")
      return response.json()
    else:
      self.logger.error(f"Failed to fetch scripts: {response.status_code}")
      return None
    
