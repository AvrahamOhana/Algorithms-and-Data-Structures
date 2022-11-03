def reverse(head):
    current = head
    previous = None
    next_node = None
    
    while current:
        
        # save the value to next node before override it
        next_node = current.next_node
    
        # replace the "direction" of the pointer
        current.next_node = previous
        
        # the current node became to be the previous for the next node
        previous = current
        
        # move the current to the next node
        current = next_node