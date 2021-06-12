'''
We hve to convert from absolute path to canonical path, unix style
'''

def simplePath(paths):
    stack = []

    for path in paths.split('/'):
        if stack and path=='..':
            stack.pop()
        elif path not in ['.','','..']:
            stack.append(path)
    return '/'+'/'.join(stack)


paths = "/a/./b/../../c/"
print(simplePath(paths))