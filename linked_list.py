# We start by initializing a class and define where the list begins
class LinkedList:
    def __init__(self, nodes = None):
        self.head = None
        # the section below "automates" the setup of nodes
        if nodes is not None:
            node = Node(data = nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data = elem)
                node = node.next
    # add_first inserts a node as the new head by setting it's next as the old head
    # and then assigning itself as the head
    def add_first(self, node):
        node.next = self.head
        self.head = node
    # add_last first checks if there are any nodes already in the list, and adds as head if one isn't assigned
    # otherwise, it runs through the linked list, setting the last node as current_node
    # and assign it's next as the new node
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        # add_after runs through the list looking for the node containing the specified data
        # then it sets the targets next as the new nodes next, before updating the targets next with itself 
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        # after checking that the list isnt empty
        # add_before checks if the target is the head
        # if so, it runs add_first
        if self.head.data == target_node_data:
            return self.add_first(new_node)
    
        prev_node = self.head
        # using a prev_node variable to keep track of the previous node
        # when target is found, update previous nodes next to the new node
        # then set the added nodes next to the target
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")
        # if targeting the head to remove, set the next node as head
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        # otherwise, set previous_node to head and run through list
        # when the target is found, set the next for previous node to the 
        # targets next
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    # the iter method is used to run through the nodes one by one
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next#iterates the next node until node = None

# We also create a node class and define the data to be stored as well as the default pointer to None
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data


llist = LinkedList()
print(llist)
llist.add_first(Node('b'))
print(llist)
llist.add_first(Node('a'))
print(llist)
llist.add_last(Node('c'))
print(llist)
llist.add_after('b',(Node('b+')))
print(llist)
llist.add_before('c',(Node('b-')))
print(llist)
llist.remove_node('b+')

print(llist)

for node in llist:
    print(node)