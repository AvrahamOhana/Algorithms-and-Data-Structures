# two pointers with delta of n 
# moves together

def nth_to_last_node(n, head):
    left_pointer = head
    right_pointer = head
    
    
    for i in range(n-1):
        if not right_pointer.next_node:
            raise("error: n is greater then list len")  
        
        right_pointer = right_pointer.next_node
       
            
    
    # move the right pointer to the end of the list
    while right_pointer.next_node:
        left_pointer = left_pointer.next_node
        right_pointer = right_pointer.next_node
    
    return left_pointer
        