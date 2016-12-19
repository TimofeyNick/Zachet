def bubble_sort(A):
    for prohod in range(1,len(A)):
        for i in range(0,len(A)-prohod):
            if A[i]>A[i+1]:
                A[i],A[i+1] = A[i+1],A[i]

#A = [6,8,9,6,5,4,1,2,3]
#bubble_sort(A)
#print(A)