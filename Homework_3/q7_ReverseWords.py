import heapq

def reverse_words(s):
    words=s.split()
    min_heap=[]
    result=[]
    for i,word in enumerate(words):
        heapq.heappush(min_heap,(-i,word))
    while min_heap:
        _, word = heapq.heappop(min_heap)
        result.append(word)

    return " ".join(result)

print(reverse_words("hello world"))                        
print(reverse_words("one"))                                
print(reverse_words("a b c d e"))                          
print(reverse_words("Go Bears"))                           
print(reverse_words("I love Uber Career Prep"))            
print("Uber Career Prep".split())

#Time Complexity: O(nlogn)
#Space Complexity: O(l) l=length of the word 

#Spent 15 mins