username = "Mo\nty"
password = "Py\thon"
f = open("data.txt", "w")
f.write("username:" + username + "\n")
f.write("password:" + password)
f.close()