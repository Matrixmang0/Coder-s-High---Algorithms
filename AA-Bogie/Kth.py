def Kth(k,L) :

  """ This is a function to find the Kth element in an unsorted list, without even sorting it. Note that, the Kth element is counted form 0 and not from 1

  >>> Kth(3,[6,12,9,0,67,21,56])

     12                    """

  if len(L)==0 :

    return None   # Returns None if there is no element in L
    
  else :

    pivot = L[0]   # We are considering first element as pivot element
    right = []     # This is the right wing
    left = []      # This is the left wing

    for i in range(1,len(L)) :
      if pivot > L[i] : 
        left.append(L[i]) # Elements lesser than pivot appends at left wing
      else :
        right.append(L[i]) # Elements greatwer than or equal to pivot appends at right wing
   
    if len(left)==k :  # k equals the number of elements in left wing
      return pivot
    elif len(left)>k : # k lesser than the number of elements in left wing
      return Kth(k,left)
    elif len(left)<k : # k greater than the number of elements in left wing
      return Kth(k-(len(left)+1),right)


