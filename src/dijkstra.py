from pysnit import snippet
import heapq as hp

@snippet(prefix="dik",
         description="Dijkstra method.")
class Dijkstra:
    def dijkstra(self, graph, start, goal=None):
        """dijkstraにより最短経路を求める
        :param graph
            隣接リスト表現による経路
            graph[v]:  頂点vから辿れる頂点のリスト
                       各頂点は(経路コスト,頂点ID)で表される
        :param start: start地点のID
        :param goal(optional): goal地点のID
        :return
            goal指定なし: startから各頂点への最短経路コスト
            goal指定あり: startからgoalまでの最短経路
        """
        num = len(graph)
        dist = [float('inf')]*num # 始点から各頂点までの最短距離
        prev = [float('inf')]*num # 最短経路における、ある頂点の前のID

        q = [] # priority_queue (startから頂点vまでのコスト, 頂点v)
        dist[start] = 0
        hp.heappush(q, (0, start))

        while q:
            prev_cost, src = hp.heappop(q)
            if dist[src] < prev_cost:
                continue
            for cost,dst in graph[src]:
                if dist[src] + cost < dist[dst]:
                    dist[dst] = dist[src] + cost
                    hp.heappush(q, (dist[dst], dst))
                    prev[dst] = src

        return dist if goal is None else self._get_shortest_path(start, goal, prev)

    def _get_shortest_path(self, start, goal, prev):
        """startからgoalまでの最短経路をprevから復元する
        """
        path = [goal]
        dst = goal
        while prev[dst] != float('inf'):
            path.append(prev[dst])
            dst = prev[dst]
        return path[::-1]
