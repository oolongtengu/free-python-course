# Removing Elements

There are two main methods to remove elements from a list:

* By **element**: "Remove the element `'Z'`", "Remove the element `3`".
* By **position**: "Remove first element", "Remove second to last element".

Let's explore them in detail.

## Remove by element

To remove an element from a list we can use the `remove` method:

```python
shopping_list = ['Milk', 'Eggs', 'Bread']

shopping_list.remove('Eggs')

print(shopping_list)  # ['Milk', 'Bread']  ("Eggs" is gone)
```

In our previous example we're matching "by element". We specify explicitly which element we want to remove. It might sound obvious, but to use the `remove` method you need to know upfront the element you want to remove. It's **important** to note that the `remove` method will remove the **first** element that matches the value. Example:

```python
my_list = ['a', 'b', 'c', 'b', 'b']

my_list.remove('b')  # There are three 'b's in this list.

print(my_list)  # ['a', 'c', 'b', 'b']
# (Only first one was removed)
```

In this example you can see how we've removed the first occurrence of the element `'b'`, but the last two ones are still in the list. 

One more example just to make sure you get it!

```python
matthew_mcconaughey = ["alright", "alright", "alright"]
matthew_mcconaughey.remove("alright")
print(matthew_mcconaughey) # ["alright", "alright"] 
# Not quite the same, huh.
```

## Remove by position

To remove an element from a list we can use the `pop` method:

```python
my_list = ['a', 'b', 'c', 'd']

# Remove from the beginning
my_list.pop(0)

print(my_list)  # ['b', 'c', 'd']

# Remove from the middle
# (remember my_list is now: ['b', c', 'd'])
my_list.pop(1)
print(my_list)  # ['b', 'd']
```

To remove the **last** element, we need to know how many elements the list has we saw we can use the `len` function for that. Let's start first by "manually" enumerating the elements of the list. If the original list is `['a', 'b', 'c', 'd']` and we start counting from `0`, the **last** element (`'d'`) is in the position `3`:

```python
my_list = ['a', 'b', 'c', 'd']
# Pos:      0    1    2    3
```

The _length_ of `my_list` is `4` (it has 4 elements). As lists start counting from `0`, the **last** element is always `length - 1`, in this case, `3`. Full example:

```python
my_list = ['a', 'b', 'c', 'd']
length_of_my_list = len(my_list)

print(length_of_my_list)  # 4

my_list.pop(length_of_my_list - 1)  # 'd'

print(my_list)  # ['a', 'b', 'c']
```

But we have **good news!** What we've just shown you seems overly complicated, and it is. But it's also a really common pattern ("Remove the last element of a list"). That's why the creators of Python have made this the **default** value of `pop`. That means that the position of `pop` is **_optional_** and if you don't specify one, the last element will be removed. Example:


```python
my_list = ['a', 'b', 'c', 'd']

my_list.pop()  # No parameter passed! Using default!
print(my_list)  # ['a', 'b', 'c']

# One more time
my_list.pop()

print(my_list)  # ['a', 'b']
```

So now you know, you can use `pop` to remove from the beginning (`my_list.pop(0)`), the end (`my_list.pop()`) or any position in the middle.
