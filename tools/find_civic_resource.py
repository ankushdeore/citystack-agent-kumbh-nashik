import httpx
import random
from mcp.server.fastmcp import FastMCP

# 🧠 In-memory cache to reduce API calls
cache = {}

# 🔐 Adds slight coordinate noise for privacy
def add_noise(lat, lon):
    if lat is None or lon is None:
        return lat, lon
    lat += random.uniform(-0.001, 0.001)
    lon += random.uniform(-0.001, 0.001)
    return round(lat, 6), round(lon, 6)

# 🛠️ Register the MCP tool
def register_tool(mcp: FastMCP):
    @mcp.tool()  # ✅ No unsupported keyword arguments
    async def find_civic_resource(resource_type: str) -> str:
        resource_type = resource_type.lower()

        if "hospital" in resource_type:
            if resource_type in cache:
                return cache[resource_type]

            url = "https://services3.arcgis.com/xDMb8Us7jzsHQ7bn/arcgis/rest/services/Nashik_Hospitals/FeatureServer/0/query"
            params = {
                "where": "1=1",
                "outFields": "Hospitals_Name,Address,Lat,Lon",
                "f": "json"
            }

            try:
                async with httpx.AsyncClient() as client:
                    response = await client.get(url, params=params, timeout=10)
                    response.raise_for_status()
                    data = response.json()
                    features = data.get("features", [])
                    if not features:
                        return "No hospitals found in the dataset."

                    hospitals = []
                    for feature in features[:10]:  # Limit to 10 results
                        attr = feature.get("attributes", {})
                        name = attr.get("Hospitals_Name", "Unknown")
                        address = attr.get("Address", "No address listed")
                        lat, lon = add_noise(attr.get("Lat"), attr.get("Lon"))
                        location = f"📍 ({lat}, {lon})" if lat and lon else ""
                        hospitals.append(f"{name} - {address} {location}")

                    result = "\n".join(hospitals)
                    cache[resource_type] = result
                    return result

            except Exception as e:
                return f"Error fetching hospital data: {e}"

        return f"Resource type '{resource_type}' is not supported yet."
