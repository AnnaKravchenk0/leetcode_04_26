'''
Docstring for 01_Binary_Tree_Traversal.solution

data    # A number or a string
left    # A Node, which is None if there is no left child.
right   # A Node, which is None if there is no right child.


'''
# Pre-order traversal
def pre_order(node):
    '''
    Docstring for pre_order
    '''
    if node is None:
        return []

    result = []
    result.append(node.data)

    left = pre_order(node.left)
    result.extend(left)

    right = pre_order(node.right)
    result.extend(right)

    return result

# In-order traversal
def in_order(node):
    '''
    Docstring for in_order
    '''
    if node is None:
        return []

    result = []

    left = in_order(node.left)
    result.extend(left)

    result.append(node.data)

    right = in_order(node.right)
    result.extend(right)

    return result



# Post-order traversal
def post_order(node):
    '''
    Docstring for post_order
    '''
    if node is None:
        return []

    result = []

    left = post_order(node.left)
    result.extend(left)

    right = post_order(node.right)
    result.extend(right)

    result.append(node.data)

    return result
