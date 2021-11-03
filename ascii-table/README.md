# CMPT 1105 | ASCII Table

ASCII Table

ASCII table is a reference table of a character value. 
http://www.asciitable.com/

For example, letter `a` has a binary value of 97. Using this value, we can convert binary value `0`s and/or `1`s into a string.

Also to compare string, you cannot use `==` to compare the string because the value of a character is converted directly back to ASCII value. 

`a > b` is not true, because if we look at the ASCII table, we can see that `97 > 98` is false.

Another Example

```python
if 'Hello' > 'hello':
  print('HELLLOW')
else
  print('Nope') # this is the output
```
If you add each character of the string, you are basically comparing this:
```python
if 500 > 532:
  print('HELLLOW')
else
  print('Nope') # this is the output
```
