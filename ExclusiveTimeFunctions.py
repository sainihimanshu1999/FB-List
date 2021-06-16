'''
This was pretty tricks but you just have to see intutively and then we have to use stack to easily implement this
'''

def cpu(logs,n):
    result = [0]*n
    stack = []

    for log in logs:
        ID,operation,time = log.split(':')
        ID = int(ID)
        time = int(time)

        if operation == 'start':
            if stack:
                result[stack[-1][0]] += time-stack[-1][1]
            stack.append([ID,time])
        
        else:
            prev = stack.pop()
            result[ID] += time-prev[1]+1
            if stack:
                stack[-1][1] = time+1
    return result


n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

print(cpu(logs,n))