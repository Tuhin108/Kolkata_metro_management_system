import heapq
from app.db.sqlite_client import get_sqlite_conn


def get_metro_route(source_name: str, destination_name: str):

    with get_sqlite_conn() as conn:

        cursor = conn.cursor()

        # -------------------------
        # Load stations
        # -------------------------

        cursor.execute("""
            SELECT id, name, line
            FROM stations
        """)

        stations = cursor.fetchall()

        id_to_station = {}
        graph = {}

        source_ids = []
        destination_ids = []

        for s in stations:

            sid = s["id"]

            id_to_station[sid] = {
                "name": s["name"],
                "line": s["line"]
            }

            graph[sid] = []

            if s["name"].lower() == source_name.lower():
                source_ids.append(sid)

            if s["name"].lower() == destination_name.lower():
                destination_ids.append(sid)

        if not source_ids:
            raise ValueError(f"Unknown station: {source_name}")

        if not destination_ids:
            raise ValueError(f"Unknown station: {destination_name}")

        # -------------------------
        # Railway connections
        # -------------------------

        cursor.execute("""
            SELECT
                station_a_id,
                station_b_id,
                travel_time_minutes,
                fare_inr
            FROM connections
        """)

        for r in cursor.fetchall():

            graph[r["station_a_id"]].append(
                (
                    r["station_b_id"],
                    r["travel_time_minutes"],
                    r["fare_inr"]
                )
            )

        # -------------------------
        # Interchanges
        # -------------------------

        cursor.execute("""
            SELECT
                station_from_id,
                station_to_id,
                transfer_time_minutes
            FROM interchanges
        """)

        for r in cursor.fetchall():

            graph[r["station_from_id"]].append(
                (
                    r["station_to_id"],
                    r["transfer_time_minutes"],
                    0
                )
            )

        best_result = None

        for src in source_ids:

            pq = [(0, 0, src, [])]

            visited = {}

            while pq:

                time, fare, node, path = heapq.heappop(pq)

                if node in visited:
                    continue

                visited[node] = time

                path = path + [node]

                if node in destination_ids:

                    ordered_itinerary = []
                    interchanges = 0

                    for i, pid in enumerate(path):

                        current = id_to_station[pid]

                        item = {
                            "station_name": current["name"],
                            "line": current["line"],
                            "is_interchange": False,
                            "transfer_to": None
                        }

                        if i < len(path) - 1:

                            nxt = id_to_station[path[i + 1]]

                            if (
                                current["name"] == nxt["name"]
                                and current["line"] != nxt["line"]
                            ):
                                item["is_interchange"] = True
                                item["transfer_to"] = nxt["line"]
                                interchanges += 1

                        ordered_itinerary.append(item)

                    result = {
                        "route_summary": {
                            "source": source_name,
                            "destination": destination_name,
                            "total_fare_inr": fare,
                            "total_travel_time_minutes": time,
                            "interchanges_count": interchanges
                        },
                        "ordered_itinerary": ordered_itinerary
                    }

                    if (
                        best_result is None
                        or time < best_result["route_summary"]["total_travel_time_minutes"]
                    ):
                        best_result = result

                    break

                for nxt, edge_time, edge_fare in graph[node]:

                    if nxt not in visited:

                        heapq.heappush(
                            pq,
                            (
                                time + edge_time,
                                fare + edge_fare,
                                nxt,
                                path
                            )
                        )

        if best_result is None:
            raise ValueError(
                f"No route found between {source_name} and {destination_name}"
            )

        return best_result