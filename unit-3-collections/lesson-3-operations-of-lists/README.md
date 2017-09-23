# Operations of Lists

Having a list created is not enough. We'll need to "manipulate" these lists to achieve something useful. These are the most common operations with lists:

* Adding elements
* Removing elements
* Counting elements (_"How many elements does this list have?"_)
* Check if an element exists in a list (_"Is john@rmotr.com already part of this list?"_)
* "Concatenating" lists: Building a new list out of two or more lists.

We'll explore all these operations in detail in this lesson.

## Adding elements

As we saw in our previous lesson, Lists are _mutable_ collections. That means we can add elements to them. We can add elements in different positions, but the most common operation is adding elements "at the end". For that, we use the `append` method:

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

As you can see in our previous example, the `insert` method receives two parameters: the "position" to insert the element (`0` in our example) and the element to insert (`Z`). That means that insert can be used not only to insert elements at the beginning of a list, but in any position. Example:

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

## Removing elements

There will be two main ways to remove elements from a list:

* By **element**: "Remove the element `'Z'`", "Remove the element `3`".
* By **position**: "Remove first element", "Remove second to last element".

Let's explore them in detail.

##### Remove by element

To remove an element from a list we can use the `remove` method:

```python
shopping_list = ['Milk', 'Eggs', 'Bread']

shopping_list.remove('Eggs')

print(shopping_list)  # ['Milk', 'Bread']  ("Eggs" is gone)
```

In our previous example we're matching "by element". We specify explicitly which element we want to remove. It might sound obvious, but to use the `remove` method you need to know upfront the element you want to remove. It's **important:** to note that the `remove` method will remove the **first** element that matches the value. Example:

```python
my_list = ['a', 'b', 'c', 'b', 'b']

my_list.remove('b')

print(my_list)  # ['a', 'c', 'b', 'b']
```

In this example you can see how we've removed the first occurrence of the element `'b'`, but the last two ones are still in the list.

##### Remove by element

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

To remove the **last** element, we need to know how many elements the list has (which we'll explore further in the following sections). But for now, we can just count. If the original list is `['a', 'b', 'c', 'd']` and we start counting from `0`, the **last** element (`'d'`) is in the position `3`:

```python
my_list = ['a', 'b', 'c', 'd']
# Pos:      0    1    2    3
```

Complete example:

```python
my_list = ['a', 'b', 'c', 'd']

# Remove the *last* element ('d' in position 3)
my_list.pop(3)

print(my_list)  # ['a', 'b', 'c']  ('d' is gone)
```

## Counting elements in a list

Given a list `my_list`, how can you know how many elements does it have? The answer is simple: the `len` function:

```python
my_list = ['a', 'b', 'c']

print(len(my_list))  # 3

my_list.append('d')

new_length = len(my_list)
print(new_length)  # 4
```

We usually refer to "counting elements" as "getting the **length** of a list". You can associate the `len` function with the **_length_** word.

Remember our previous example in which we were trying to `pop` the **last** element of a list? We could have used the `len` function for that instead of manually counting. Let's do the counting once again just to review the positions:

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

## Check if an element exists in a list

This is a simple operation that will involve the `in` operator. Let's see an example first:

```python
shopping_list = ['Milk', 'Eggs', 'Bread']

print('Bread' in shopping_list)  # True
print('Cookies' in shopping_list)  # False

do_i_need_to_buy_milk = 'Milk' in shopping_list

print(do_i_need_to_buy_milk)  # True
```

Something to note is that `in` is an **_operator_**, not a function (as `len`, for example) or a list method (like `my_list.remove()` or `my_list.append()`). We use `in` as we'd use other operators (`+`, `-`, etc).

## Concatenating lists

Suppose that you have two lists (`starks` and `lannisters`). How can we build a final list containing **ALL** the elements from both lists? This operation is usually called "concatenating" lists and it's simply performed with the `+` operator. Example:

```python
starks = ['Ned', 'Arya', 'Sansa']
lannisters = ['Jamie', 'Tyrion', 'Cersei']

got_main_characters = starks + lannisters

print(got_main_characters)  # (see below)
# ['Ned', 'Arya', 'Sansa', 'Jamie', 'Tyrion', 'Cersei']

# Both lists remain unchanged

print(starks)  # ['Ned', 'Arya', 'Sansa']
print(lannisters)  # ['Jamie', 'Tyrion', 'Cersei']
```

As you can see in our previous example, we **_concatenate_** both lists (`starks` and `lannisters`) with the `+` operator. Let's explore a few other examples just for you to see how simple it is:

```python
# Example 1 - Two lists in place
chars_and_numbers = ['a', 'b', 'c'] + [1, 2, 3]
print(chars_and_numbers)  # ['a', 'b', 'c', 1, 2, 3]

# Example 2
chars = ['a', 'b', 'c']
numbers = [1, 2, 3]
print(chars + numbers)    # ['a', 'b', 'c', 1, 2, 3]

# Example 3
print([1, 2] + [3, 4])  # [1, 2, 3, 4]
```
