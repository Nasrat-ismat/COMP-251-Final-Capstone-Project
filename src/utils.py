from graph import Graph
from hashmap import HashMap
from trie import Trie
from heap import MaxHeap


class Package:
    def __init__(self, package_id, priority, destination, weight_kg, order=0):
        self.package_id = package_id
        self.priority = int(priority)
        self.destination = destination
        self.weight_kg = float(weight_kg)
        self.order = order

    def __lt__(self, other):
        if self.priority != other.priority:
            return self.priority < other.priority
        return self.order > other.order

    def __gt__(self, other):
        if self.priority != other.priority:
            return self.priority > other.priority
        return self.order < other.order

    def __repr__(self):
        return (
            f"Package(id={self.package_id}, priority={self.priority}, "
            f"destination={self.destination}, weight_kg={self.weight_kg})"
        )


class DispatchQueue:
    def __init__(self):
        self.heap = MaxHeap()
        self.counter = 0

    def enqueue(self, package):
        self.heap.push(package)

    def dequeue(self):
        return self.heap.pop()

    def peek(self):
        return self.heap.peek()

    def is_empty(self):
        return self.heap.is_empty()

    def __len__(self):
        return len(self.heap)

    def make_package(self, package_id, priority, destination, weight_kg):
        # order is just there so same-priority packages still come out in a stable way
        package = Package(package_id, priority, destination, weight_kg, self.counter)
        self.counter += 1
        return package


def load_network(file_path):
    graph = Graph()
    trie = Trie()
    depot_map = HashMap()
    dispatch_queue = DispatchQueue()

    section = None
    with open(file_path, 'r', encoding='utf-8') as file:
        for raw_line in file:
            line = raw_line.strip()
            if not line:
                continue

            if line in {'NODES', 'EDGES', 'PACKAGES'}:
                section = line
                continue

            if section == 'NODES':
                names = line.split()
                for name in names:
                    graph.add_node(name)
                    trie.insert(name)
                    # I made some simple metadata here since the file only gives names
                    depot_map.insert(
                        name,
                        {
                            'location': f'Auto-generated location for {name}',
                            'capacity': 100,
                            'active': True,
                        },
                    )

            elif section == 'EDGES':
                start, end, weight = line.split()
                graph.add_edge(start, end, float(weight))

            elif section == 'PACKAGES':
                package_id, priority, destination, weight_kg = line.split()
                package = dispatch_queue.make_package(
                    package_id,
                    int(priority),
                    destination,
                    float(weight_kg),
                )
                dispatch_queue.enqueue(package)

    return graph, depot_map, trie, dispatch_queue
