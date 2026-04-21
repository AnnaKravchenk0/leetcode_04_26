'''
Docstring for 02_Sort_binary_tree_by_levels.solution
'''
from collections import deque

def tree_by_levels(node):
    '''
    Docstring for tree_by_levels
    '''
    result = []
    if not node:
        return result


    queue = deque()
    queue.append(node)

    while queue:
        cur = queue.popleft()
        result.append(cur.value)



        if cur.left:
            queue.append(cur.left)

        if cur.right:
            queue.append(cur.right)

    return result
