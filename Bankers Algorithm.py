
import logging,numpy as np

import azure.functions as func
from azure.storage.table import TableService

allocation = [] 
maxallocations = []

logging.info('Python HTTP trigger function processed a request.')
# Creating the table serive where we access our Azure Storage Services
table_service = TableService(account_name='storagebankersalgorithm', account_key='code')

# Adding entities to our table
# enity = {'PartitionKey': 'process', 'RowKey': '11', 'allocations' : '16,27,33', 'maxallocations' : '26,32,34'}
# print('Inserting a new entity into table - ' + 'allocationtable')
# table_service.insert_entity('allocationtable', enity)
# print('Successfully inserted the new entity')

# Fetching all the rows present inside our Azure Database Storage
rows=table_service.query_entities('allocationtable',"PartitionKey eq 'process'")
logging.info(f"Found process : {len(rows.items)}")
for row in rows:
    print(row.RowKey,row.allocations,row.maxallocations)
    allocation.append(list(map(int,row.allocations.split(','))))
    maxallocations.append(list(map(int,row.maxallocations.split(','))))
logging.info(f"Allocation row: {len(allocation)} \n  MaxAllocation rows : {len(maxallocations)}")


rowSum_allocation = [sum(i) for i in zip(*allocation)]  # Calculaing the row sum of each columns present
total = [10,5,7]
work = [i-j for i,j in zip(total,rowSum_allocation)] # Initaialsing the work list which will be compared and updated
P = len(allocation) # Defines number of process
R = len(allocation[0]) # Defones number if resources

def needMatrix(allocation,maxallocations): 
    result = [[0 for i in range(R)] for j in range(P)]
    need = []
    for i in range(len(allocation)):
        for j in range(len(allocation[0])):
            # find need matrix form allocation from maximum_allowance (max-allocation)
            result[i][j] = maxallocations[i][j] - allocation[i][j] # This calculates the need of our process
    for i in result:
        need.append(i)
    
    return need
    
def isSafe(P,R):
    # Considering all process are incomplete.
    # The allocation provides us the number of process present. This can be done by considering the list of our allocation matrix.
    running = [True] * P
    count = P
    while count != 0:
        safe = False
        for i in range(P):
            if running[i]:
                executing = True
                for j in range(R):
                    if maxallocations[i][j] - allocation[i][j] > work[j]:
                        executing = False
                        break
                if executing:
                    print(f"process {i + 1} running")
                    running[i] = False
                    count -= 1
                    safe = True
                    for j in range(R):
                        work[j] += allocation[i][j]
                    break
        if not safe:
            print("The process is in an insecure state.")
            break
 
        print(f"The process is in a safe state. \n Available resources: {work}\n")
    return True

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        
        # Calling our methods

        logging.info('The need matrix is: ')
        needmatrixresponse = needMatrix(allocation,maxallocations)
        logging.info(np.array(needmatrixresponse))
        response = isSafe(P,R)
        logging.info(response)

        if response:
            return func.HttpResponse(f"NeedMatrix : {needmatrixresponse} \n\n System : {response}")
        else:
            return func.HttpResponse(
                "Response status not available",
                status_code=204
            )
    except Exception as e:
        logging.info(e)
