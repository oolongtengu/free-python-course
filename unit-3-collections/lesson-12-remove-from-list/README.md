# Remove From List

There are moments in life when we must do chores and clean things up. Like lists.
Sometimes they need to be sanitized!

There are a couple of ways to get rid of stuff we don't want from lists.

**Remove:**
Remove allows you to search for a piece of data in a list and gets rid of it for you


Example:
```python

birthday_list = ["happy", "birthday", "Santiago"]
birthday_list.remove("Santiago")
print(birthday_list) # Prints ["happy", "birthday"]... no more birthday for you Santiago! :(

# Note that this only removes the first time it matches
matthew_mcconaughey = ["alright", "alright", "alright"]
matthew_mcconaughey.remove("alright")
print(matthew_mcconaughey) # Prints ["alright", "alright"]. Not quite the same, huh.
```

**Pop:**
Pop destroys a element at an index instead of searching by data and returns that number for you to use

Example:
```python
some_numbers = [1, 2, 3]
a_number = some_numbers.pop(1)

print(some_numbers) # Prints [1, 3]
print(a_number) # Prints 2
```