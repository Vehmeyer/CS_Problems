"""
There are N students in a baking class together. Some of them are friends, while some are not friends. 
The students' friendship can be considered transitive. This means that if Ami is a direct friend of Bill, 
and Bill is a direct friend of Casey, Ami is an indirect friend of Casey. A friend circle is a group of students 
who are either direct or indirect friends of some level. That is, the friend circle consists of a person, 
their friends, their friends-of-friends, their friends-of-friends-of-friends, and so on.

Given a N*N matrix M representing the friend relationships between students in the class. 
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.

You need to write a function that can output the total number of friend circles among all the students.
"""

def csFriendCircles(friendships):
    def dfs(node):
        visited[node] = True
        for i in range(n):
            if friendships[node][i] and not visited[i]:
                dfs(i)
    
    ret = 0
    n = len(friendships)
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            ret += 1
            dfs(i)
    return ret