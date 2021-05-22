
import logging,numpy as np
import azure.functions as func
from azure.storage.table import TableService 

allocation = [] 
maxallocations = []

table_service = TableService(account_name='storagebankersalgorithm', account_key='D36RqEMiAugfFpAegohTsURNMScBAM1LGqsiAdbPvhCBHEtlduAwmZorE7tTLg0wRme6OvpfnrrnOKovc6+SOg==')

rows=table_service.query_entities('allocationtable',"PartitionKey eq 'process'")

logging.info(f"Found process : {len(rows)}")

for row in rows:
    print(row.RowKey,row.allocations,row.maxallocations)

    allocation.append(list(map(int,row.allocations.split(','))))
    maxallocations.append(list(map(int,row.maxallocations.split(','))))

logging.info(f"Allocation row: {len(allocation)} \n  MaxAllocation rows : {len(maxallocations)}")

rownew = {'PartitionKey': 'process', 'RowKey': '6', 'allocations' : '2,6,1', 'maxallocations' : '5,8,3'}

# Insert the entity into the table
print('Inserting a new entity into table - ')
table_service.insert_entity('allocationtable', rownew)
print('Successfully inserted the new entity')

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
        print("Safe Sequence: ",Sequence)
        print("Available Resource:",work)
    return True

if __name__ == "__main__":
    allocation = [[0, 1, 0 ],[ 2, 0, 0 ],[3, 0, 2 ],[2, 1, 1] ,[ 0, 0, 2]] # consist of 2d list 
    # Each inner list consist of a process 

    maximum_allowance = [[7, 5, 3 ],[3, 2, 2 ],[ 9, 0, 2 ],[2, 2, 2],[4, 3, 3]] # a 2d matrix 
    # Each inner list consist of a process 

    result = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    
    # Define a function to calcualte the value from allcoation matrix
    # Assuming values of each process and subtracting it with our available.
    # return available as as list
    rowSum_allocation = [sum(i) for i in zip(*allocation)]  
    total = [10,5,7]
    work = [i-j for i,j in zip(total,rowSum_allocation)]
    P = len(allocation) # Defines number of process
    R = len(allocation[0]) # Defones number if resources

    # Calling our methods
    print('The need matrix is: ')
    print(needMatrix(allocation,maximum_allowance))
    print(isSafe(P,R))