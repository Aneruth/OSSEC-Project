def needMatrix(allocation,maximum_allowance): 
    need = []
    for i in range(len(allocation)):
        for j in range(len(allocation[0])):
            # find need matrix form allocation from maximum_allowance (max-allocation)
            result[i][j] = maximum_allowance[i][j] - allocation[i][j] # This calculates the need of our process
    for i in result:
        need.append(i)
    
    return need
    
def isSafe(P,R):
    # Considering all process are incomplete.
    # The allocation provides us the number of process present. This can be done by considering the list of our allocation matrix.
    done = [0] * P
    Sequence = [0] * P
    count = 0
    while( count < P ):
        temp=0
        for i in range( P ):
            if( needMatrix(allocation,maximum_allowance)[i] == 0 ):
                if(needMatrix(allocation,maximum_allowance)(i)):
                    Sequence[count]=i;
                    count+=1
                    done[i]=1
                    temp=1
                    for j in range(R):
                        work[j] += allocation[i][j] 
        if(temp == 0):
            break
    if(count < P):
        print('The system is Unsafe')
    else:
        print("Eureka!!!! We found the safe sequence for out given process and their sequece is: \n", end = " ")
        print("Safe Sequence: ",*Sequence)
        print("Available Resource:",work)
    return True

if __name__ == "__main__":
    allocation = [[4,0,0,1],[1,1,0,0],[1,2,5,4],[0,6,3,3],[0,2,1,2]] # consist of 2d list 
    # Each inner list consist of a process 

    maximum_allowance = [[6,0,1,2],[1,7,5,0],[2,3,5,6],[1,6,5,3],[1,6,5,6]] # a 2d matrix 
    # Each inner list consist of a process 

    result = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    # Define a function to calcualte the value from allcoation matrix
    # Assuming values of each process and subtracting it with our available.
    # return available as as list
    rowSum_allocation = [sum(i) for i in zip(*allocation)]  
    total = [10,5,7,3]
    work = [i-j for i,j in zip(total,rowSum_allocation)]
    P = len(allocation) # Defines number of process
    R = len(allocation[0]) # Defones number if resources

    # Calling our methods
    print('The need matrix is: ')
    print(needMatrix(allocation,maximum_allowance))
    print(isSafe(P,R))