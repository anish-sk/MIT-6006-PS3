class PriorityQueue:
        def __init__(self, A):
                self.n, self.A = 0, A

        def insert(self): # absorb element A[n] into the queue
                if not self.n < len(self.A):
                        raise IndexError("insert into full priority queue")
                self.n = self.n + 1

        def delete_max(self): # remove element A[n - 1] from the queue
                if self.n < 0: # this implementation is currently NOT correct
                        raise IndexError("pop from empty priority queue")
                self.n = self.n - 1
        def sort(self, A):
                pq = self.__init__(A) # make empty priority queue
                for _ in range(len(self.A)):
                        pq.insert() # n x T_i
                for _ in range(len(self.A)):
                        pq.delete_max() # n x T_e

class PQ_Heap(PriorityQueue):
        def insert(self): # O(log n)
                super().insert() # increases self.n by 1
                n, A = self.n, self.A
                max_heapify_up(A, n, n - 1)
        def delete_max(self): # O(log n)
                super().delete_max() # decreases self.n by 1
                n, A = self.n, self.A
                A[0], A[n] = A[n], A[0]
                max_heapify_down(A, n, 0)
                return A[n]
def parent(i):
        p=(i-1)//2
        if(i>0):
                return p
        else:
                return i
def left(i,n):
        l=2*i + 1
        if(l<n):
                return l
        else:
                return i
def right(i,n):
        l=2*i + 2
        if(l<n):
                return l
        else:
                return i
def max_heapify_up(A, n, c): # T(c) = O(log c)
        p = parent(c) # O(1) index of parent (or c)        
        if A[p] > A[c]: # O(1) compare
                A[c], A[p] = A[p], A[c] # O(1) swap parent
                max_heapify_up(A, n, p) # T(p) = T(c/2) recursive call on parent
def max_heapify_down(A, n, p): # T(p) = O(log n - log p)
        l, r = left(p, n), right(p, n) # O(1) indices of children (or p)
        if(r==p and l==p):
                return
        if(l==p):
                c=l
        else:
                if (A[r] > A[l]):
                        c=l
                else:
                        c=r # O(1) index of largest child
        if A[p] > A[c]: # O(1) compare
                A[c], A[p] = A[p], A[c] # O(1) swap child
                max_heapify_down(A, n, c)
def build_max_heap(A, n):
        for i in range(n // 2, -1, -1): # O(n) loop backward over array
                max_heapify_down(A, n, i)


def proximate_sort(A, k):
    ''' 
    Return an array containing the elements of 
    input tuple A appearing in sorted order.
    Input:  k | an integer < len(A)
            A | a k-proximate tuple
    '''
    ##################
    # YOUR CODE HERE #
    ##################
    n=len(A)
    L=list(A)
    L=L[0:k+1]
    build_max_heap(L,k)
    H=PQ_Heap(L)
    for i in range(k):
            H.insert()
    B=[]
    for i in range(0,n-k):
            L[k]=A[k+i]
            H.insert()            
            B.append(H.delete_max())            
    for i in range(0,k):
            B.append(H.delete_max())      
    print(B)
    return B
