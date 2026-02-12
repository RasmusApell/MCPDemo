# MCPDemo
## Setup Instructions
### Local
##### Copilot in VSCode
Skapa venv och installera requirements
Kör "Start" i mcp.json filen under .vscode
Paths till venv python och main.py behöver uppdateras

##### Claude Code
claude mcp add local-demo-server /home/rasmus/Repos/MCPDemo/local/venv/bin/python -- /home/rasmus/Repos/MCPDemo/local/main.py
Remove:
claude mcp remove local-demo-server

### Network
##### Starta service på nätverk
Kör main.py
Nu kommer MCP servern vara tillgänglig för alla anslutna till nätet
Eller med docker compose
docker compose build
docker compose up -d
Stoppa:
docker compose down

##### Anslut till Copilot i VSCode
Kan kolla eller starta uppkopling uppkopplingen i .vscode/mcp.json
ctrl + shift + p -> >MCP: Add Server -> http -> http://192.168.1.8:3218/mcp -> namn -> scope
