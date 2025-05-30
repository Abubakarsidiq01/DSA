"""
You are working for a large retailer. We would like to determine what was the product which sold the most, and how many times it was sold.

Write a function that takes in a collection of product name strings representing purchases and returns the name of the product with the most purchases, and the total number of sales for that product. If multiple products sold the same amount, return the first to appear in the purchases list. Product names are case insensitive.

Example:
purchases1 = ["Television", "Laptop", "MacBook", "MacBook", "Nintendo Switch"]
findMostSold(inventory1) -> MacBook, 2

purchases2 = ["Blue Shirt", "Red Shirt", "blue pants", "blue shirt", "Red Shirt", "Red Shirt", "blue shirt", "Blue Shirt"]
purchases3 = ["Plushy", "Teddy Bear", "Doll", "Plushy", "Teddy Bear"]
purchases4 = ["Plushy", "Teddy Bear", "Doll", "Doll", "Plushy", "Teddy Bear"]
purchases5 = ["Teddy BeAr", "Plushy", "Doll", "Plushy", "Teddy Bear"]

All Test Cases:
findMostSold(purchases1) -> MacBook, 2
findMostSold(purchases2) -> Blue Shirt, 4
findMostSold(purchases3) -> Plushy, 2
findMostSold(purchases4) -> Plushy, 2
findMostSold(purchases5) -> Teddy Bear, 2

Complexity analysis variables:
P = Number of purchases
(Note: Individual purchase strings have constant length)

"""
# Create a dictionary (hashmap)
# Go through the list and add them to a dictionary
# Go through dictionary and return the key, value with the highest frequency

from collections import defaultdict
class Solution:
    def Maximum_purchase(self, purchase:list):
        dic = defaultdict(int)
        for item in purchase:
            dic[item.lower()] += 1
            
        lst = []
        for key in dic:
            lst.append(dic[key])
        a = max(lst)
        
        for key, value in dic.items():
            if value == a:
                return key, value
        
        # maxKey = ""
        # maxVal = -1
        # for each element in the dictionary:
        #     if value > maxVal:
        #         maxKey = key
        #         maxVal = val
        
        # Look at Python's Counter
        # Counter(purchases) -> counter.maxKey()
        
sol = Solution()
purchases1 = ["Television", "Laptop", "MacBook", "MacBook", "Nintendo Switch"]
purchases2 = ["Blue Shirt", "Red Shirt", "blue pants", "blue shirt", "Red Shirt", "Red Shirt", "blue shirt", "Blue Shirt"]
purchases3 = ["Plushy", "Teddy Bear", "Doll", "Plushy", "Teddy Bear"]
purchases4 = ["Plushy", "Teddy Bear", "Doll", "Doll", "Plushy", "Teddy Bear"]
purchases5 = ["Teddy BeAr", "Plushy", "Doll", "Plushy", "Teddy Bear"]

print(sol.Maximum_purchase(purchases1))
print(sol.Maximum_purchase(purchases2))
print(sol.Maximum_purchase(purchases3))
print(sol.Maximum_purchase(purchases4))
print(sol.Maximum_purchase(purchases5))