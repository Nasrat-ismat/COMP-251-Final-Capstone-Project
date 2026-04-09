import os
from utils import load_network


def print_menu():
    print('\n===== Smart Network Logistics Engine =====')
    print('1. Display Network Summary')
    print('2. Find Shortest Path')
    print('3. Detect Cycles')
    print('4. Dispatch Highest-Priority Package')
    print('5. Search Depot by Name')
    print('6. Autocomplete Depot Name')
    print('7. Exit')
    print('==========================================')


def display_summary(graph):
    print('\n--- Network Summary ---')
    print(f'Number of nodes: {graph.num_nodes()}')
    print(f'Number of edges: {graph.num_edges()}')
    print(f'Connected components (weak): {graph.connected_components()}')


def shortest_path(graph):
    source = input('Enter source node: ').strip()
    destination = input('Enter destination node: ').strip()
    path, cost = graph.dijkstra(source, destination)

    if path is None:
        print('No path found, or maybe one of the nodes is not in the graph.')
    else:
        print('Shortest path: ' + ' -> '.join(path))
        print(f'Total cost: {cost}')


def detect_cycles(graph):
    has_cycle, cycle_nodes = graph.detect_cycle()
    if has_cycle:
        print('A cycle was found in the network.')
        print('Cycle nodes: ' + ' -> '.join(cycle_nodes))
    else:
        print('No cycles were found in the network.')


def dispatch_package(dispatch_queue):
    if dispatch_queue.is_empty():
        print('No packages left to dispatch.')
        return

    package = dispatch_queue.dequeue()
    print('Package dispatched:')
    print(f'  ID: {package.package_id}')
    print(f'  Priority: {package.priority}')
    print(f'  Destination: {package.destination}')
    print(f'  Weight (kg): {package.weight_kg}')


def search_depot(depot_map):
    name = input('Enter depot name: ').strip()
    depot_info = depot_map.search(name)
    if depot_info is None:
        print('Depot not found.')
    else:
        print(f'Depot: {name}')
        print(f"  Location: {depot_info['location']}")
        print(f"  Capacity: {depot_info['capacity']}")
        print(f"  Active: {depot_info['active']}")


def autocomplete_depot(trie):
    prefix = input('Enter prefix: ').strip()
    matches = trie.autocomplete(prefix)
    if matches:
        print('Matches:')
        for match in matches:
            print(f'  - {match}')
    else:
        print('No matching depot names found.')


def main():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', 'data', 'network.txt')
    graph, depot_map, trie, dispatch_queue = load_network(file_path)

    while True:
        print_menu()
        choice = input('Choose an option: ').strip()

        if choice == '1':
            display_summary(graph)
        elif choice == '2':
            shortest_path(graph)
        elif choice == '3':
            detect_cycles(graph)
        elif choice == '4':
            dispatch_package(dispatch_queue)
        elif choice == '5':
            search_depot(depot_map)
        elif choice == '6':
            autocomplete_depot(trie)
        elif choice == '7':
            print('Exiting program. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number from 1 to 7.')


if __name__ == '__main__':
    main()
