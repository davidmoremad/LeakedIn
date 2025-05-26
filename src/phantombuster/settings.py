import requests
import time
from config import API_KEY, API_BASE_URL, ORG_ID, MAX_RETRIES
from src.utils.logger import Logger

class Endpoints:
  ORGS = "orgs/fetch"

  # Scripts - Called Phantoms
  SCRIPTS = "scripts/fetch-all"                               # GET
  SCRIPT = "script/fetch?id={}"                               # GET

  # Agents - Run Phantoms
  AGENTS = "agents/fetch-all"                                 # GET
  AGENT = "agents/fetch?id={}"                                 # GET
  AGENT_OUTPUT = "agents/fetch-output?id={}"                  # GET
  AGENT_LAUNCH = "agents/launch"                              # POST
  AGENT_SAVE = "agents/save"                                  # POST

  # Containers - Execution results
  CONTAINERS = "containers/fetch-all?agentId={}"              # GET
  CONTAINER = "containers/fetch?id={}"                        # GET
  CONTAINER_OUTPUT = "containers/fetch-output?id={}&raw={}"   # GET
  CONTAINER_RESULTS = "containers/fetch-result-object?id={}"  # GET


class PhantomBusterClient:
    logger = Logger()

    def __init__(self, api_key=API_KEY, base_url=API_BASE_URL, org_id=ORG_ID):
        self.api_key = api_key
        self.base_url = base_url
        self.org_id = org_id
        self.session = requests.Session()
        headers = [
            ("X-Phantombuster-Key", self.api_key),
            ("X-PhantomBuster-Org-Id", self.org_id),
            ("Content-Type", "application/json"),
        ]
        self.session.headers.update(headers)
    
    def _request(self, method, endpoint, params=None, data=None, retries=MAX_RETRIES):
        
        url = f"{self.base_url}{endpoint}"
        
        self.logger.info(f"Making {method} request to {url} with params: {params} and data: {data}")
        for attempt in range(retries):
            try:
                response = self.session.request(
                    method=method,
                    url=url,
                    params=params,
                    json=data
                )
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                if attempt == retries - 1:
                    raise e
                time.sleep(2 ** attempt)  # Exponential backoff
    
    def get(self, endpoint, params=None):
        return self._request("GET", endpoint, params=params)
    
    def post(self, endpoint, data=None):
        return self._request("POST", endpoint, data=data)