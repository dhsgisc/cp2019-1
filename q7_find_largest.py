
    
def find_largest(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        return max(alist[0],find_largest(alist[1:]))
