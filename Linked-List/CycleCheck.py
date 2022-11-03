# check is there is a cycle in the kinked list
# 2 runners at the same course. one is faster then the other.
def cycle_check(node):
    marker1 = node
    marker2 = node
    
    while marker2 != None and marker2.next_node != None:
        marker1 = marker1.next_node
        marker2 = marker2.mext_node.next_node
        if marker2 == marker1:
            return True
        
    return False