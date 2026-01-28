# Setup instructions

### Local
##### Copilot in VSCode
Kör "Start" i mcp.json filen under .vscode

##### Copilot CLI


##### Claude Code
claude mcp add local-demo-server /home/rasmus/Repos/MCPDemo/local/venv/bin/python -- /home/rasmus/Repos/MCPDemo/local/main.py
Remove:
claude mcp remove local-demo-server

### Network
##### Starta service på nätverk
Kör main.py
Nu kommer MCP servern vara tillgänglig för alla anslutna till nätet
Eller med docker
docker build -t mcp-demo-server MCPDemo/network
docker run -d -p 3218:3218 --name mcp-demo mcp-demo-server

docker logs mcp-demo
docker stop mcp-demo
docker rm mcp-demo

##### Anslut till Copilot i VSCode
Kan kolla uppkopplingen i .vscode/mcp.json
ctrl + shift + p -> >MCP: Add Server -> http -> http://192.168.1.8:3218/mcp -> namn -> scope

##### Copilot CLI


##### Claude Code


### Public

