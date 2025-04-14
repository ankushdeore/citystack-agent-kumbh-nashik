# 🏙️ CityStack Agent — Kumbh Nashik 2027

**`citystack-agent-kumbh-nashik`** is a lightweight AI MCP (Model Context Protocol) server that supports decentralized, citizen-centric tools for the **Kumbh Mela 2027** in Nashik. It leverages real-time civic data to provide **urban intelligence at the edge** — locally, offline-ready, and privacy-first.

> 🧠 Part of the CityStack initiative, inspired by MIT Kumbhathon and Decentralized AI research at MIT Media Lab.

---

## ✨ Features

- ✅ `find_civic_resource`: Fetch real-time civic data (e.g. hospitals in Nashik)
- 🌐 Live integration with ArcGIS public APIs
- ⚙️ FastAPI-based MCP tool server
- 🔌 Plug-and-play with Claude Desktop or edge device deployments

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/citystack-agent-kumbh-nashik.git
cd citystack-agent-kumbh-nashik

2. Install Dependencies (with uv)

uv venv
source .venv/bin/activate
uv pip install

3. Run the MCP Server

uv run server.py

4. Simulate Tool Locally (optional)

uv run simulate_citystack.py

🧪 Tool Overview
find_civic_resource

Fetches hospitals in Nashik from live civic data.

Input:

{ "resource_type": "hospital" }

Output Example:

Hospital A – Address 1 📍 (20.000000, 73.750000)
Hospital B – Address 2 📍 (20.005000, 73.760000)

📁 Project Structure

citystack-agent-kumbh-nashik/
├── server.py                  # Main MCP server
├── tools/
│   └── find_civic_resource.py
├── simulate_citystack.py     # CLI testing
├── pyproject.toml
├── .gitignore
└── README.md

🧠 Claude Desktop Integration

To integrate with Claude Desktop, create a claude_config.json file:

{
  "mcpServers": {
    "citystack-kumbh": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/yourname/path/to/citystack-agent-kumbh-nashik",
        "run",
        "server.py"
      ]
    }
  }
}

    🔄 Replace the path with your actual local directory.

🚀 Deployment Notes

For platforms like Render, Replit, or Fly.io:

    Ensure server.py binds to 0.0.0.0 and uses:

import os
port = int(os.environ.get("PORT", 8000))

    Start command:

uv run server.py

🔭 Roadmap

Future Scope:

    🚽 Toilet & water finder

    👮 Safety hub locator

    📢 Emergency broadcaster

    🛐 Cultural site explorer 

## 🙏 Acknowledgements

- **Data:** ArcGIS Open Data APIs (https://www.arcgis.com)  
- **Inspiration:** MIT Media Lab, Kumbhathon initiative, and Decentralized AI research  
- **Vision:** Inspired by the CityStack sandbox — a prototyping space for AI-first civic infrastructure for large-scale events like Kumbh Mela 2027.
