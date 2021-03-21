# find need matrix form allocation from maximum_allowance (max-allocation)
# Define a function called need matrix this returns all in matrix format
    # Check if need <= previousFunction()
    # update available += allocation
def needMatrix(allocation,maximum_allowance): 
    need = []
    for i in range(len(allocation)):
        for j in range(len(allocation[0])):
            result[i][j] = maximum_allowance[i][j] - allocation[i][j] # This calculates the need of our process
    for i in result:
        need.append(i)
    
    # Considering all process are incomplete.
    # The allocation provides us the number of process present. This can be done by considering the list of our allocation matrix.
    done = [0] * len(allocation) 
    
    # To print safe sequence for our problem
    # This safety sequence provides us which all process are safe
    # Initially we are assigning our safe sequence as 0 with the length of our allocation. 
    safe_sequence = [0] * len(allocation)

    pointer = 0

    while (pointer < len(allocation)):
        find = False

        for i in range(len(allocation)):

            for j in range(len(work)):

                if need[i][j] > work[j]:
                    pointer = 1
                    break
            
            if (j == len(work)-1):

                for k in range(len(work)):
                    work[k] += allocation[i][k]
                
                safe_sequence[0] = i
                pointer += 1
                done[i] = 1
                find = True

        if find == False:
            return f"Is system in safe state: {False}"
    
    print("Eureka!!!! We found the safe sequence for out given process and their sequece is: \n", end = " ")
    print(*safe_sequence) 
    return True

if __name__ == "__main__":
    allocation = [[0,1,1],[2,0,0],[3,0,2],[2,1,1]] # consist of 2d list 
    # Each inner list consist of a process 

    maximum_allowance = [[7,5,3],[3,2,2],[9,0,2],[4,3,3]] # a 2d matrix 
    # Each inner list consist of a process 

    result = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    
    # Define a function to calcualte the value from allcoation matrix
    # Assuming values of each process and subtracting it with our available.
    # return available as as list
    work = [sum(i) for i in zip(*allocation)]  

    # Calling our methods
    print(needMatrix(allocation,maximum_allowance))