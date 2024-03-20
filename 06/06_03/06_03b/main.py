from collections import deque

history_stack = deque()
history_stack.append("http://google.com")
history_stack.append("http://linkedin.com")
history_stack.append("http://stackoverflow.com")

print(history_stack[-1])
print(history_stack.pop())
