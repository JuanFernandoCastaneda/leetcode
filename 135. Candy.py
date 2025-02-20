def candy(ratings: list[int]) -> int:
    candies = [1]
    tiempo_desc = 0
    for i in range(1, len(ratings)):
        if ratings[i-1] < ratings[i]:
            if tiempo_desc > 0:
                candies[-1] = max(candies[-1], tiempo_desc+1)
                for d in range(1, tiempo_desc+1):
                    candies.append(tiempo_desc+1-d)
                tiempo_desc = 0
            candies.append(candies[i-1]+1)
        elif ratings[i-1] == ratings[i]:
            if tiempo_desc > 0:
                candies[-1] = max(candies[-1], tiempo_desc+1)
                for d in range(1, tiempo_desc+1):
                    candies.append(tiempo_desc+1-d)
                tiempo_desc = 0
            candies.append(1)
        else:
            tiempo_desc += 1
    if tiempo_desc > 0:
        candies[-1] = max(candies[-1], tiempo_desc+1)
        for d in range(1, tiempo_desc+1):
            candies.append(tiempo_desc+1-d)
    print(candies)
    return sum(candies)

'''
Old solution

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]
    tiempo_desc = 0
    for i in range(1, len(ratings)):
        if ratings[i-1] < ratings[i]:
            if tiempo_desc > 0:
                candies[-1] = max(candies[-1], tiempo_desc+1)
                for d in range(1, tiempo_desc+1):
                    candies.append(tiempo_desc+1-d)
                tiempo_desc = 0
            candies.append(candies[i-1]+1)
        elif ratings[i-1] == ratings[i]:
            if tiempo_desc > 0:
                candies[-1] = max(candies[-1], tiempo_desc+1)
                for d in range(1, tiempo_desc+1):
                    candies.append(tiempo_desc+1-d)
                tiempo_desc = 0
            candies.append(1)
        else:
            tiempo_desc += 1
    if tiempo_desc > 0:
        candies[-1] = max(candies[-1], tiempo_desc+1)
        for d in range(1, tiempo_desc+1):
            candies.append(tiempo_desc+1-d)
    print(candies)
    return sum(candies)
'''


print(candy([1,0,2]))
print(candy([1,2,2]))
print(candy(list(reversed(range(50)))))
print(candy(list(reversed(range(200000)))))