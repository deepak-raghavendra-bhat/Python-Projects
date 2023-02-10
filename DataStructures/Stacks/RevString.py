import stack

s1 = "abc"
s2 = ""
s = stack.Stack()
for char in s1:
    s.push(char)
    
while not(s.isEmpty()):
    s2 += s.pop()
    
print(s2)
