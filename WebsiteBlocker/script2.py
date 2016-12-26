website_list = ["www.facebook.com","facebook.com"]

file = open('hosts','r+')
content  = file.readlines()
file.seek(0)
            # While reading the file the pointer goes to the EOF post which
            #all writes will append. So here we are ensuring the write to happen
            #from first location

            #We use readlines to get the list of all lines instead of chars
for line in content:
    if not any (website in line for website in website_list):
        file.write(line)
