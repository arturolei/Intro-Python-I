"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

with open('foo.txt') as foo:
    print(foo.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open ('bar.txt', 'w') as bar:
    bar.write("There's an east wind coming all the same, such a wind as never blew on England yet. \n")
    bar.write("It will be cold and bitter, Watson, and a good many of us may wither before its blast. \n")
    bar.write("But it's God's own wind none the less and a cleaner, better stronger land will lie in the sunshine when the storm has cleared.")

with open('bar.txt') as bar:
    print(bar.read())