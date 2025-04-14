# 🏙️ CityStack Agent – Kumbh Nashik 2027

**CityStack Agent** is a small Python-based tool that helps people find civic services like hospitals during large events — starting with the **Kumbh Mela 2027 in Nashik**.

It uses real-time data and can run on local devices, even without internet.

---

## ✨ What It Can Do

- 🔍 Find nearby hospitals in Nashik using real data
- 🛠️ Works with Claude Desktop (or CLI) as a tool
- ⚙️ Built using FastAPI and Python
- 🔗 Can connect to live civic data (ArcGIS)

---

## 🚀 How to Run It

### 1. Clone the Project

```bash
git clone https://github.com/ankushdeore/citystack-agent-kumbh-nashik.git
cd citystack-agent-kumbh-nashik
```

### 2. Set Up the Environment (with [uv](https://astral.sh/uv))

```bash
uv venv
source .venv/bin/activate
uv pip install
```

### 3. Start the Server

```bash
uv run server.py
```

### 4. (Optional) Run Tool Simulator

```bash
uv run simulate_citystack.py
```

---

## 🧪 Example Tool: `find_civic_resource`

Looks up hospitals in Nashik.

**Input:**

```json
{ "resource_type": "hospital" }
```

**Example Output:**

```
Hospital A – Address 1 📍 (20.000000, 73.750000)
Hospital B – Address 2 📍 (20.005000, 73.760000)
```

---

## 📁 Folder Structure

```
citystack-agent-kumbh-nashik/
├── server.py              # Starts the tool server
├── tools/
│   └── find_civic_resource.py
├── simulate_citystack.py  # For testing locally
├── pyproject.toml
├── .gitignore
└── README.md
```

---

## 💻 Claude Desktop Setup

To use this with Claude Desktop, create a `claude_config.json` file:

```json
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
```

Replace the path with your actual project location.

---

## 🌐 Deployment Notes

For cloud platforms like Render or Replit:

- Make sure `server.py` listens on `0.0.0.0` and gets the port from environment:

```python
import os
port = int(os.environ.get("PORT", 8000))
```

- Start command:

```bash
uv run server.py
```

---

## 🛣️ What's Next

Future Scope

- 🚽 Toilet & water finder
- 👮 Nearby police stations
- 📢 Emergency alert system
- 🛐 Cultural site guide 

---

## 🙏 Credits

- **Data**: ArcGIS Open Data (https://www.arcgis.com)
- **Inspiration**: MIT Kumbhathon, CityStack idea, and Decentralized AI research
