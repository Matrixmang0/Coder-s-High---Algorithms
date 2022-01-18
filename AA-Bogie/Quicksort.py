def Quicksort(L) :

  """ The sorting technique used here is the quickest sorting technique ever known to man kind. This sorting technique uses recursion to sort the elements in the list.
  
  >>> Quicksort([6,8,45,90,263,3,1234]) 
    
      [3,6,8,45,90,263,1234]                            """

  if len(L) <= 1 :

    return L         # Returns the same if the list contains one or no elements

  else :

    right = []    # Right wing
    left = []     # Left wing
    pivot = L[0]  # Element fo importance. Here we taken the first element in the list. But any element can be taken

    for i in range(1,len(L)) :

      if pivot > L[i] :
        left.append(L[i])  # the elements lesser than the pivot element are appended to the left wing
      elif pivot <= L[i] :
        right.append(L[i]) # the elements greater than or equal to the pivot element are appended to the right wing

    return ( Quicksort(left) + [pivot] + Quicksort(right) )

    # The above return statement calls the recursion twice on both left wing and right wing
