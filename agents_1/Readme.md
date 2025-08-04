
##to create a empty agent folder
   adk create google_release_notes_agent
   

##gcloud commands for deployment
#Artifact Registry
gcloud artifacts repositories create container-images-registry 
  --repository-format=docker 
  --location=asia-south1
  --description="Repository for remote MCP servers"
  --project="agentic-ai-solution"

gcloud builds submit --region=asia-south1 --tag asia-south1-docker.pkg.dev/agentic-ai-solution/container-images-registry/mcp-usage:v1 

asia-south1-docker.pkg.dev/agentic-ai-solution/container-images-registry
