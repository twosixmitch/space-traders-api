import requests
from rich.console import Console

console = Console()

if __name__ == '__main__':
    response = requests.get("https://api.spacetraders.io/v2/")
    console.print_json(data=response.json())

    agent_data = {
        "symbol": "TWO_SIX_MITCH",
        "faction": "COSMIC"
    }
    response = requests.post("https://api.spacetraders.io/v2/register", json=agent_data)
    console.print_json(data=response.json())

    secrets = open("secrets", "r")
    headers = {
        "Authorization": "Bearer " + secrets.readline().strip()
    }

    response = requests.get("https://api.spacetraders.io/v2/my/agent", headers=headers)
    console.print_json(data=response.json())

    response = requests.get("https://api.spacetraders.io/v2/systems/X1-YU85/waypoints/X1-YU85-99640B", headers=headers)
    console.print_json(data=response.json())

    response = requests.get("https://api.spacetraders.io/v2/my/contracts", headers=headers)
    console.print_json(data=response.json())

    response = requests.post("https://api.spacetraders.io/v2/my/contracts/cljkte0626xius60c8mnr70hd/accept", headers=headers)
    console.print_json(data=response.json())

    response = requests.get("https://api.spacetraders.io/v2/systems/X1-YU85/waypoints", headers=headers)
    console.print_json(data=response.json())

    response = requests.get("https://api.spacetraders.io/v2/systems/X1-YU85/waypoints/X1-YU85-34607X/shipyard", headers=headers)
    console.print_json(data=response.json())

    ship_data = {
        "shipType": "SHIP_MINING_DRONE",
        "waypointSymbol": "X1-YU85-34607X"
    }
    response = requests.post("https://api.spacetraders.io/v2/my/ships", headers=headers, data=ship_data)
    console.print_json(data=response.json())

    response = requests.get("https://api.spacetraders.io/v2/my/ships", headers=headers)
    console.print_json(data=response.json())

    response = requests.post("https://api.spacetraders.io/v2/my/ships/TWO_SIX_MITCH-3/orbit", headers=headers)
    console.print_json(data=response.json())

    nav_data = {"waypointSymbol": "X1-YU85-76885D"}
    response = requests.post("https://api.spacetraders.io/v2/my/ships/TWO_SIX_MITCH-3/navigate", headers=headers, data=nav_data)
    console.print_json(data=response.json())

    response = requests.post("https://api.spacetraders.io/v2/my/ships/TWO_SIX_MITCH-3/dock", headers=headers)
    console.print_json(data=response.json())
