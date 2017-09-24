# Get Position of Element

On occasion you need to figure out the position on an element in a list. 
Remember how lists keep order and start at element position 0 instead of 1?

We can use the index method on a list to find out the position of things.

Example:
```python
best_python_course = ['r', 'm', 'o', 't', 'r']

print(best_python_course.index('o')) # Prints 2

# Note that 'r' is in two places in the list
# In those situations index prints the index of the first one

print(best_python_course.index('r')) # Prints 0

# If the thing you are searching for is not present, Python will give you an error
```

Use index in the function get_bookmark_index to return the index of the word "bookmark".