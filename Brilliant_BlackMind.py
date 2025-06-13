'''
You are working on a web scraper. You have received the contents of many websites in the form of a collection of (website, string) pairs. In order to determine where to start investigating a topic, we would like to find the website with the most instances of a specific word.

Write a function that takes in a collection of strings, and a word, and returns the name of the website containing the most instances of the word. If multiple websites contain the same number, return the first one in the input.

Example:
scraping = [
  ["hockeyplayers.com", "Hockey Player magazine's exclusive interview with famous goalie"],
  ["sports.com", "Hockey player shot the hockey puck into the hockey net, scoring a goal"],
  ["football.com", "World record breaking touchdown made by a new football player"],
  ["rugby.com", "Unique point scored as ball bounces off foot of player"]
]
finder(scraping, "Hockey") -> "sports.com"
finder(scraping, "player") -> "hockeyplayers.com"
finder(scraping, "foot")   -> "rugby.com"

The word does not count if it is part of another word, and is not case sensitive. For example if the word is "foot", it would not count if "football" is present.

Complexity analysis variables:
P = Number of pairs
S = Length of website content strings 
(note: Web URLs and the searched for string have constant length)
'''
def finder(scraping:list, word:str):
    dic = {}
    ans = {}
    word = word.lower()
    for i in range(len(scraping)):
        key = scraping[i][0]
        value = scraping[i][1].lower()
        value = value.split()
        dic[key] = value
    
    for key, value in dic.items():
        for i in range(len(value)):
            if word in value[i]:
                ans[key] += 1
                
    max_value = max(ans.values())
    for key, value in ans.items():
        if value == max_value:
            return key
        

scraping = [
  ["hockeyplayers.com", "Hockey Player magazine's exclusive interview with famous goalie"],
  ["sports.com", "Hockey player shot the hockey puck into the hockey net, scoring a goal"],
  ["football.com", "World record breaking touchdown made by a new football player"],
  ["rugby.com", "Unique point scored as ball bounces off foot of player"]
]
finder(scraping, "Hockey") 
finder(scraping, "player") 
finder(scraping, "foot")   
