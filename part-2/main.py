import requests
from rich.console import Console

console = Console()

if __name__ == '__main__':
    # response = requests.get("https://api.spacetraders.io/v2/")
    # console.print_json(data=response.json())

    # agent_data = {
    #     "symbol": "TWO_SIX_MITCH",
    #     "faction": "COSMIC"
    # }
    # response = requests.post("https://api.spacetraders.io/v2/register", json=agent_data)
    # console.print_json(data=response.json())

    secrets = open("secrets", "r")
    headers = {
        "Authorization": "Bearer " + secrets.readline().strip()
    }

    # response = requests.get("https://api.spacetraders.io/v2/my/agent", headers=headers)
    # console.print_json(data=response.json())

    current_waypoint = "X1-JF24-06790Z"
    sector = "X1"
    system = "X1-JF24"

    # response = requests.get(
    #     f"https://api.spacetraders.io/v2/systems/{system}/waypoints/{current_waypoint}", headers=headers
    # )
    # console.print_json(data=response.json())

    # response = requests.get("https://api.spacetraders.io/v2/my/contracts", headers=headers)
    # console.print_json(data=response.json())

    # contract_id = "clkeu56ffjwo8s60cz5zy6dux"
    # response = requests.post(f"https://api.spacetraders.io/v2/my/contracts/{contract_id}/accept", headers=headers)
    # console.print_json(data=response.json())

    # List all waypoints
    # response = requests.get(f"https://api.spacetraders.io/v2/systems/{system}/waypoints", headers=headers)
    # console.print_json(data=response.json())

    # shipyard_waypoint = "X1-JF24-73757X"
    # response = requests.get(
    #     f"https://api.spacetraders.io/v2/systems/{system}/waypoints/{shipyard_waypoint}/shipyard", headers=headers
    # )
    # console.print_json(data=response.json())

    # ship_data = {
    #     "shipType": "SHIP_MINING_DRONE",
    #     "waypointSymbol": shipyard_waypoint
    # }
    # response = requests.post("https://api.spacetraders.io/v2/my/ships", headers=headers, data=ship_data)
    # console.print_json(data=response.json())

    # response = requests.get("https://api.spacetraders.io/v2/my/ships", headers=headers)
    # console.print_json(data=response.json())

    mining_ship_symbol = "TWO_SIX_MITCH-3"

    # response = requests.post(f"https://api.spacetraders.io/v2/my/ships/{mining_ship_symbol}/orbit", headers=headers)
    # console.print_json(data=response.json())

    asteroid_waypoint = "X1-JF24-23225F"

    # nav_data = {"waypointSymbol": asteroid_waypoint}
    # response = requests.post(
    #     f"https://api.spacetraders.io/v2/my/ships/{mining_ship_symbol}/navigate", headers=headers, data=nav_data
    # )
    # console.print_json(data=response.json())

    # response = requests.post(f"https://api.spacetraders.io/v2/my/ships/{mining_ship_symbol}/dock", headers=headers)
    # console.print_json(data=response.json())

    # response = requests.post(f"https://api.spacetraders.io/v2/my/ships/{mining_ship_symbol}/refuel", headers=headers)
    # console.print_json(data=response.json())

    # response = requests.post(f"https://api.spacetraders.io/v2/my/ships/{mining_ship_symbol}/orbit", headers=headers)
    # console.print_json(data=response.json())

    # response = requests.post(f"https://api.spacetraders.io/v2/my/ships/{mining_ship_symbol}/extract", headers=headers)
    # console.print_json(data=response.json())

    # response = requests.get(f"https://api.spacetraders.io/v2/my/ships/{mining_ship_symbol}/cargo", headers=headers)
    # console.print_json(data=response.json())

    # response = requests.get(
    #     f"https://api.spacetraders.io/v2/systems/{system}/waypoints/{asteroid_waypoint}/market", headers=headers
    # )
    # console.print_json(data=response.json())

    # response = requests.get(
    #     f"https://api.spacetraders.io/v2/my/ships/{mining_ship_symbol}", headers=headers
    # )
    # console.print_json(data=response.json())

    # response = requests.post(
    #     f"https://api.spacetraders.io/v2/my/ships/{mining_ship_symbol}/dock", headers=headers
    # )
    # console.print_json(data=response.json())

    # sell_cargo = {
    #     "symbol": "ICE_WATER",
    #     "units": "3"
    # }
    # response = requests.post(
    #     f"https://api.spacetraders.io/v2/my/ships/{mining_ship_symbol}/sell", headers=headers, data=sell_cargo
    # )
    # console.print_json(data=response.json())
