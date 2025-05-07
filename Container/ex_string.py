str1 = 'Hello, how are you?'
str2 = "Hi, what's up"
str3 = '''Hello, 
          how are you?'''
str4 = """Hi,
            what's up?"""

def add_str(in_func_obj):
    print(f'In add [before]: in_func_obj = "{in_func_obj}"')
    in_func_obj += ' suffix'
    print(f'In add [after]: in_func_obj = "{in_func_obj}"')

orig_obj = 'foo'
print(f'Outside [before]: orig_obj = "{orig_obj}"')
add_str(orig_obj)
print(f'Outside [after]: orig_obj = "{orig_obj}"')