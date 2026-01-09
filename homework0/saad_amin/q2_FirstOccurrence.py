#Time Complexity O(N)
#Space Complexity O(N)

def FirstOccurrence(str):
    res = ""
    seen = set()

    for c in str:
        if c not in seen:
            res += c
            seen.add(c)

    return res

if __name__ == "__main__":
    print(FirstOccurrence("abracadabra")) #should be abrcd
    print(FirstOccurrence("Saad Amin")) #should be Sad Amin
    print(FirstOccurrence("Uber Engineer")) # should be Uber Engi

#Time taken 12 min
