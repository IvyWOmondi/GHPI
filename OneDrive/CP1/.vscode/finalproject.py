# Writing to a file
with open('settings.json', 'w') as f:
    f.write('this is a file I/O')
#Reading from the file
with open("settings.json", "r") as file:
    content = file.read()
    print("File content:")
    print(content)