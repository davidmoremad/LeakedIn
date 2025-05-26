import argparse
# from src.phantombuster.script_service import ScriptService
from src.phantombuster.agent_service import AgentService
from src.phantombuster.container_service import ContainerService
from src.utils.csv_utils import CSVExporter
from src.utils.logger import Logger

def parse_arguments():
    parser = argparse.ArgumentParser(description="Run PhantomBuster scripts and export data")
    parser.add_argument("--url", required=True, help="LinkedIn URL to scrape")
    parser.add_argument("--agent-id", required=True, help="PhantomBuster agent ID")
    parser.add_argument("--output", default=None, help="Output CSV filename")
    parser.add_argument("--timeout", type=int, default=300, help="Timeout in seconds")
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    # Initialize services
    agent_service = AgentService()
    container_service = ContainerService()
    csv_exporter = CSVExporter()
    
    logger = Logger()
    logger.info("Starting PhantomBuster agent execution")
    
    # Launch the agent with the LinkedIn URL
    launch_result = agent_service.launch_agent(args.agent_id, args.url)
    if not launch_result:
        print("Failed to launch agent")
        return
    
    print(f"Agent launched successfully. Waiting for completion (timeout: {args.timeout}s)")
    
    # Wait for agent to complete
    completed = agent_service.wait_for_agent_completion(
        args.agent_id, 
        timeout=args.timeout
    )
    
    if not completed:
        print("Agent did not complete within the timeout period")
        return
    
    print("Agent execution completed. Fetching results...")
    
    # Get latest container results
    results = container_service.get_latest_container_results(args.agent_id)
    
    if not results:
        print("No results found")
        return
    
    print("Data retrieved successfully. Exporting to CSV...")
    
    # Export results to CSV
    output_file = csv_exporter.export_data(results, args.output)
    
    if output_file:
        print(f"Data exported successfully to: {output_file}")
    else:
        print("Failed to export data")

if __name__ == "__main__":
    main()