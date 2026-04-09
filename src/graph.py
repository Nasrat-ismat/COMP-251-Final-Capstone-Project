from heap import MinHeap


class Graph:
    WHITE = 0
    GRAY = 1
    BLACK = 2

    def __init__(self):
        # adjacency list: node -> list of (neighbor, weight)
        self.adj = {}
        self.edge_count = 0

    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, src, dst, weight):
        self.add_node(src)
        self.add_node(dst)
        self.adj[src].append((dst, float(weight)))
        self.edge_count += 1

    def nodes(self):
        return list(self.adj.keys())

    def num_nodes(self):
        return len(self.adj)

    def num_edges(self):
        return self.edge_count

    def connected_components(self):
        # I counted weakly connected components, so I treat edges like undirected here
        visited = set()
        count = 0
        undirected = {node: [] for node in self.adj}

        for start in self.adj:
            for end, _ in self.adj[start]:
                undirected[start].append(end)
                undirected[end].append(start)

        for node in self.adj:
            if node not in visited:
                count += 1
                self._dfs_undirected(node, undirected, visited)
        return count

    def _dfs_undirected(self, start, undirected, visited):
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for neighbor in undirected[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    def dijkstra(self, source, destination):
        if source not in self.adj or destination not in self.adj:
            return None, float('inf')

        dist = {node: float('inf') for node in self.adj}
        prev = {node: None for node in self.adj}
        dist[source] = 0

        pq = MinHeap()
        pq.push((0, source))

        while not pq.is_empty():
            current_dist, node = pq.pop()

            if current_dist > dist[node]:
                continue

            if node == destination:
                break

            for neighbor, weight in self.adj[node]:
                new_dist = current_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    prev[neighbor] = node
                    pq.push((new_dist, neighbor))

        if dist[destination] == float('inf'):
            return None, float('inf')

        path = []
        cur = destination
        while cur is not None:
            path.append(cur)
            cur = prev[cur]
        path.reverse()
        return path, dist[destination]

    def bellman_ford(self, source):
        dist = {node: float('inf') for node in self.adj}
        prev = {node: None for node in self.adj}
        if source not in self.adj:
            return dist, prev, False

        dist[source] = 0
        all_nodes = self.nodes()

        for _ in range(len(all_nodes) - 1):
            changed = False
            for u in self.adj:
                for v, w in self.adj[u]:
                    if dist[u] != float('inf') and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        prev[v] = u
                        changed = True
            if not changed:
                break

        has_negative_cycle = False
        for u in self.adj:
            for v, w in self.adj[u]:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    has_negative_cycle = True
                    break

        return dist, prev, has_negative_cycle

    def detect_cycle(self):
        colors = {node: self.WHITE for node in self.adj}
        parent = {node: None for node in self.adj}

        for node in self.adj:
            if colors[node] == self.WHITE:
                cycle = self._dfs_cycle(node, colors, parent)
                if cycle:
                    return True, cycle
        return False, []

    def _dfs_cycle(self, node, colors, parent):
        colors[node] = self.GRAY

        for neighbor, _ in self.adj[node]:
            if colors[neighbor] == self.WHITE:
                parent[neighbor] = node
                cycle = self._dfs_cycle(neighbor, colors, parent)
                if cycle:
                    return cycle
            elif colors[neighbor] == self.GRAY:
                cycle = [neighbor]
                cur = node
                while cur != neighbor and cur is not None:
                    cycle.append(cur)
                    cur = parent[cur]
                cycle.append(neighbor)
                cycle.reverse()
                return cycle

        colors[node] = self.BLACK
        return None
