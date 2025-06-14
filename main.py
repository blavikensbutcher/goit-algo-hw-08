import heapq

def min_cost_to_connect_cables(cables):
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

        print(f"З'єднуємо {first} + {second} = {cost} → Поточні витрати: {total_cost}")


    return total_cost

cables = [5, 6, 3, 8, 1, 2, 7, 30, 20, 11, 100]
result = min_cost_to_connect_cables(cables)
print("Мінімальні витрати на з'єднання кабелів:", result)