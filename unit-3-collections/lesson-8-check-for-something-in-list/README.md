# Check for Something in List

Sometimes you need to see if there is specific data inside a list.
There's a way to do that in python! Just use the `in` keyword.

Example:

```python
grocery_list = ["apple", "banana", "carrot"]

if "banana" in grocery_list:
    print("I AM A BANANA!") # This would print since there is "banana" in the grocery list 
```

On to your assignment.

When Christmas rolls around, everybody knows Santiago, AKA Santa, 
has to check his list twice.

Lets help him do that!

Create a function that uses the keyword `in` to verify if there are any good 
students in his list. Check for the string `good_student` and return True or False
depending if it is present.

