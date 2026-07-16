import heapq
from app.db.sqlite_client import get_sqlite_conn

def get_metro_route(source_name: str, destination_name: str):
    """
    Computes the shortest route (based on travel time) between the source and 
    destination metro stations using Dijkstra's algorithm.
    Reads station, connection, and interchange graphs dynamically from SQLite.
    """
    pass