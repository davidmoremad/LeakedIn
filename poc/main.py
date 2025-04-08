from utils import *
from dotenv import load_dotenv
from plugins.phantombuster import PhantomBuster
import json
import datetime

# load .env file
load_dotenv()

def main():

  api_key = os.getenv("PHANTOMBUSTER_API_KEY")
  org_id = os.getenv("PHANTOMBUSTER_ORG_ID")
  pb = PhantomBuster(api_key, org_id)

  print("AGENTS")
  print("-------------------------------------------------------------")
  agents = pb.get_agents()
  for agent in agents:
    print(f"Agent ID: {agent['id']}")
    print(f"Agent Name: {agent['name']}")
    print(f"Agent Script: {agent['script']}")
    print(f"Launch Type: {agent['launchType']}")
    print(f"S3 Folder: {agent['s3Folder']}")
    print("-------------------------------------------------------------")
    
    print("CONTAINERS")
    container_ids = [x['id'] for x in pb.get_containers(agent['id'])['containers']]
    for container_id in container_ids:
      container = pb.get_container(container_id)
      print(f"Container ID: {container['id']}")
      launchedAt = datetime.datetime.fromtimestamp(container['launchedAt'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
      print(f"Container LaunchedAt: {launchedAt}")
      print(f"Container Output: {container.get('output', 'No output')}")
      print(f"Container Result: {container.get('resultObject', 'No result')}")
      print("-------------------------------------------------------------")
    


if __name__ == "__main__":
  main()