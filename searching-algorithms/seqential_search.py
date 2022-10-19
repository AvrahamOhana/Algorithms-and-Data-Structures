# seqential search in unordered array 
def seq_search(arr, element):
    for pos, x in enumerate(arr):
        if x == element:
            return True
    return False

# seqential search in ordered array 
def seq_search_orderd(arr, element):
    for pos, x in enumerate(arr):
        if x > element :
            return False
        if x == element:
            return True