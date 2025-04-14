import httpx
from mcp.server.fastmcp import FastMCP

def register_tool(mcp: FastMCP):
    @mcp.tool()
    async def find_civic_resource(resource_type: str) -> str:
        resource_type = resource_type.lower()
        if "hospital" in resource_type:
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
                    for feature in features[:5]:  # Limit to 5 hospitals
                        attr = feature.get("attributes", {})
                        name = attr.get("Hospitals_Name", "Unknown")
                        address = attr.get("Address", "No address listed")
                        lat = attr.get("Lat")
                        lon = attr.get("Lon")
                        location = f"📍 ({lat}, {lon})" if lat and lon else ""
                        hospitals.append(f"{name} - {address} {location}")
                    return "\n".join(hospitals)

            except Exception as e:
                return f"Error fetching hospital data: {e}"
        else:
            return f"Resource type '{resource_type}' is not supported yet."
