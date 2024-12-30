import networkx as nx


def is_symmetric_tree(tree):
    def is_mirror(left_node, right_node):
        if left_node is None and right_node is None:
            return True
        if left_node is None or right_node is None:
            return False

        left_children = list(tree.neighbors(left_node))
        right_children = list(tree.neighbors(right_node))

        if len(left_children) != len(right_children):
            return False

        return all(is_mirror(left_children[i], right_children[-(i + 1)]) for i in range(len(left_children)))

    root = list(tree.nodes())[0]
    return is_mirror(root, root)


G = nx.Graph()
edges_symmetric = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
G.add_edges_from(edges_symmetric)

print("Дерево симметрично:", is_symmetric_tree(G))

G_non_symmetric = nx.Graph()
edges_non_symmetric = [(1, 2), (1, 3), (2, 4), (3, 5)]
G_non_symmetric.add_edges_from(edges_non_symmetric)

print("Дерево симметрично:", is_symmetric_tree(G_non_symmetric))







