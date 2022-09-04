import networkx as nx
import matplotlib.pyplot as plt

# Read resources dumped into a file by an RAML parser
def ReadResources():
    resources = []
    with open('api_resources.txt') as f:
        resources = f.read().splitlines()
    return resources

resource_list = ReadResources()


def CreateNodeSet(resource_list):
    new_resource_list = [resource.lstrip('/') for resource in resource_list]
    root_resource = new_resource_list[0]
    new_resource_list.pop(0)
    nested_node_list = [s.split('/') for s in new_resource_list]
    charsToMatch = ('{', ':')
    flattened_nested_node_list = [node for node_list in nested_node_list for node in node_list if not node.startswith(charsToMatch)]

    node_set = set(flattened_nested_node_list)

    return node_set, nested_node_list, root_resource

node_set, nested_node_list, root_resource = CreateNodeSet(resource_list)

def ClearIdsNestedNodes(nested_node_list):
    charsToMatch = ('{', ':')
    new_nested_node_list = []
    for node_list in nested_node_list:
        for node in node_list:
            if node.startswith(charsToMatch):
                get_index = node_list.index(node)
                node_list.pop(get_index)
        new_nested_node_list.append(node_list)
    return new_nested_node_list

new_nested_node_list = ClearIdsNestedNodes(nested_node_list)

def CreateNodeTuples(new_nested_node_list):
    tupled_node_list = []
    for node_list in new_nested_node_list:
        for i in range(0, len(node_list)):
            try:
                tuple_nodes = (node_list[i], node_list[i + 1])
                tupled_node_list.append(tuple_nodes)
            except IndexError:
                pass

    return tupled_node_list

graph_tupled_node_list = CreateNodeTuples(new_nested_node_list)

def PlotDomainModelGraph(graph_tupled_node_list):
    G = nx.Graph()
    G.add_edges_from(graph_tupled_node_list)
    nx.draw(G, with_labels=True)
    plt.show()

if __name__ == '__main__':
    PlotDomainModelGraph(graph_tupled_node_list)
