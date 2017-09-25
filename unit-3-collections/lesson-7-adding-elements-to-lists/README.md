# Adding elements to lists

As we saw in the introduction, Lists are _mutable_ collections. That means we can modify lists, and one of the most common modifications is adding things to them. We can add elements in different positions, but the most common operation is adding elements "at the end". For that, we use the `append` method:

```python
my_list = ['a', 'b', 'c']

# Append an element (add at the end)
my_list.append('d')

print(my_list)  # ['a', 'b', 'c', 'd']
```

In this example we've just "mutated" (modified) `my_list` and added the element `'d'` at the end of it (we've _"appended"_ it).

We can also add elements at the beginning of the list with the `insert` method:

```python
my_list = ['a', 'b', 'c']

# Insert Z at the beginning of the list
my_list.insert(0, 'Z')

print(my_list)  # ['Z', 'a', 'b', 'c']
```

As you can see in our previous example, the `insert` method receives two parameters: the first one is the "position" to insert the element (`0` in our example) and the second one is the actual element to insert (`Z`). That means that insert can be used not only to insert elements at the beginning of a list, but in any position. Example:

```python
my_list = ['a', 'b', 'c']

# Insert X in position 1
my_list.insert(1, 'X')

print(my_list)  # ['a', 'X', 'b', 'c']

# Insert Y in position 3
my_list.insert(3, 'Y')

print(my_list)  # ['a', 'X', 'b', 'Y', 'c']
```

As you can see from these examples, we're using integers to specify the positions, which start counting from `0` (`0` is the **first** position). We'll learn more about this in the "String Indexing" section later.
