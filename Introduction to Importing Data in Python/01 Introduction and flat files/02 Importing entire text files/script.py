# Open a file: file
file = open("moby_dick.txt", "r")

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)