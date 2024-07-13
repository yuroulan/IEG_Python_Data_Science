# Introduction and Read Operation

'''
files
-->> if you want some data, use purpose.file

open("filename", "mode and format") -->> should be strings

mode :
r - read
w - write -->> creates a new file
a - append -->> - to add more content in file, 
                - if file not exist, create a new file
                - else it appends the text
x - exclusive -->> - create a new file if the file does not exist
                    - it throughs error if file exist

format :
t - text (use text format)
b - byte

read 
'''
f = open("input.txt", "rt")

s = f.read()
print(s)
