import heapq

def min_cost_cables(cables):
    if not cables:
        return 0
    
    heapq.heapify(cables)
    
    total_cost = 0
    
    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        cost = first + second
        total_cost += cost
        
        heapq.heappush(cables, cost)
    
    return total_cost


cables = [4, 3, 2, 6]
print("Minimum total cost:", min_cost_cables(cables))

cables = [4, 3, 2, 6, 9, 20, 10]
print("Minimum total cost:", min_cost_cables(cables))