import graphviz

class GraphGenerator:
    @staticmethod
    def generate_graph(program):
        dot = graphviz.Digraph()

        # Modifier le style des nœuds
        dot.attr('node',  shape='box')

        def traverse(node, parent=None):
            nonlocal dot

            # Créer un nœud pour le type de nœud actuel
            node_id = str(id(node))
            node_label = type(node).__name__
            if(node_label == 'Lexem'):
                node_label = node.value
            
            dot.node(node_id, label=node_label)

            # Si le nœud a un parent, créer une arête vers lui
            if parent is not None:
                dot.edge(parent, node_id)

            # Si le nœud a des enfants, parcourir récursivement ses enfants
            if hasattr(node, '__dict__'):
                for attr_name, attr_value in node.__dict__.items():
                    if isinstance(attr_value, (list, tuple)):
                        for item in attr_value:
                            if hasattr(item, '__dict__'):
                                traverse(item, node_id)
                    elif hasattr(attr_value, '__dict__'):
                        traverse(attr_value, node_id)
            else:
                traverse(node)
        # Commencer la traversée à partir du nœud racine (Program)
        traverse(program)

        return dot


