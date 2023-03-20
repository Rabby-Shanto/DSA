#  Tree Data Structure

# Creating a Simple Tree
class Tree:
    def __init__(self,node,children=[]) -> None:

        self.node = node
        self.children = children

    def __str__(self,level=0) -> str:
        ret = "  " * level + str(self.node) + "\n"

        for child in self.children:
            ret += child.__str__(level + 1)
        
        return ret
    

    def addChild(self,childNode):
        self.children.append(childNode)




tree = Tree('Drinks',[])
Hot = Tree('Hot',[])
Cold = Tree('Cold',[])

tree.addChild(Hot)
tree.addChild(Cold)


print(tree)
