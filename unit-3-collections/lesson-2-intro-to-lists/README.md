# Intro to Lists

Lists are probably the most popular collections used in the Python programming language. They're similar to _"arrays"_ in other programming languages.

A list is an **_ordered_**, **_heterogeneous_**, **_mutable_** collection. This means:

##### Ordered

As you add new elements, the list "remembers" the order that you chose for your elements. Example:

```python
shopping_list = []  # An empty list

shopping_list.append('Eggs')
shopping_list.append('Milk')
shopping_list.append('Bread')

print(shopping_list)  # ['Eggs', 'Milk', 'Bread']
```

In the previous example you can see that the order of the elements in the resulting list (`['Eggs', 'Milk', 'Bread']`) is the same order we chose when building the list (_"Eggs"_ first, _"Milk"_ second and finally _"Bread"_).

##### Heterogeneous

This means that you can put any type of element in a list. This is a recurrent theme in all the other Python collections, they take any type of element. Example:


```python
my_list = ["Hello", 3, True, 2.5]
```

As you can see, we're storing a string object (`"Hello"`), an integer (`3`), a boolean (`True`) and a float (`2.5`). Python lists are perfectly capable of handling any type of elements. Even other lists (we'll talk more about this later).

##### Mutable

This means that we can change lists (we can _mutate_ them). It probably sounds a little bit dumb to mention, but you'll see later that there are other collections that are **not** mutable. But going back to lists, you can simply change them at will, for example:

```python
shopping_list = []  # An empty list

shopping_list.append('Eggs')  # Add an element (changed the list)
shopping_list.append('Milk')  # Add another element

print(shopping_list)  # ['Eggs', 'Milk']

shopping_list.remove('Milk')  # Remove an element (changed it again)

print(shopping_list)  # ['Eggs']
```

Don't _overthink_ this; it's the most intuitive way of thinking collections: being mutable.

## Creating Lists

There are two possible ways of creating lists:

##### Literally

This is the preferred (and most intuitive) way. With it, you create the list and specify elements "right in place". Everything seems like just one operation. It's what we've been doing up to this point:

```python
courses = ['Intro to Python', 'Advanced Python']
```

In this example we've created the list `courses` containing two elements. We're also using square brackets (`[]`) to denote the list.


##### Programatically

In this case the process of creating the list and populating it (inserting elements) will be split in several steps:

```python
courses = list()

courses.append('Intro to Python')
courses.append('Advanced Python')
```

This example looks a little bit less "intuitive". First, we're using the `list()` function to create an empty list (we're not using square brackets) and then we're adding elements one by one.

## Operations with Lists

Once you have a list, you'll want to perform different operations with it. For example, **counting elements, adding new elements, removing others,** etc.

Python makes it easy to operate with your list. There are **many** different operations you can perform, we just show you a few examples for you to see how useful they are, but we encourage you to check the [documentation](https://docs.python.org/3.5/tutorial/datastructures.html#more-on-lists) for more.

```python
my_list = ['a', 'b', 'c']

# Append an element (add at the end)
my_list.append('d')

# Add an element in a certain position
my_list.insert(0, 'z')  # Beginning
my_list.insert(3, 'z')  # 4th position (index == 3)

# Count how many items the list has
print(len(my_list))

# Remove all the elements from the list
my_list.clear()

# Reverse its items
my_list.reverse()

# ... many more ...
```

## Iterating a list

Iteration is key to understand how lists work. To properly understand lists you should be familiar with the **for loop** (control flow statement).

The good news is that it's simple to understand. Here are a few examples:
```python
names = ['Mary', 'Tom', 'Rose']
for name in names:
    print(name)
# This will print the names, each in a new line:
# Mary
# Tom
# Rose

numbers = [0, 1, 2, 3, 4]
for number in numbers:
    # I can define whatever I want inside the **for loop body**
    double = number * 2
    print(double)
# This will print the numbers, doubled (one number per line):
# 0
# 2
# 4
# 6
# 8
```
As you can see in the previous example, a `for loop` is composed of a few things:

![Python for loop explained](https://cloud.githubusercontent.com/assets/872296/20549004/261aac18-b107-11e6-8ff0-1e8ef783f737.png)

**Note 1:** `for` is a keyword, should always be used

**Note 2:** `name` in this case is a variable that **we choose**. We can choose whatever name we want for this variable (`name`, `n`, `a_name`). **It'll reference each one of the elements in the list**

**Note 3:** `in` is also a keyword. It precedes the list we'll iterate.

**Note 4:** `names` is the **list itself**. It's the list we want to iterate

**Note 5:** Finally, the **for loop body**. This is really important. We'll express here whatever we want to do with each one of the elements as we iterate through the list.

## List indexing

Finally, you can retrieve individual elements from a list by specifying the position they have in the list. Indexes start from the number 0\. So, the first element will have index 0, the second one will have index 1, the third one 3, etc... The last element of the list has index `len(list) - 1` (if the list has 8 elements, the last one is 7 (`8-1`))

There are also negative indexes, the last element of the list also has the index -1, the second to last -2, etc.

```python
names = ['Mary', 'Tom', 'Rose', 'Joe']
mary  = names[0]
tom   = names[1]
joe   = names[-1]
rose  = names[-2]
```

You can also get sublists from a given list. That'd be like a _fraction of a list_. A sublist specified by a range of indexes. For example, the **_elements between the second and the fifth position_**, the **_first three elements_**, etc.

To get a sublist you must specify two indexes separated by a colon sign. Example: `my_list[INDEX-1:INDEX-2]`.

**Important!** The resulting sublist will **NOT** include the element at the last position specified. See examples below

```python
names = ['Mary', 'Tom', 'Rose', 'Joe']
# First 3 names
print(names[0:3])
# ['Mary', 'Tom', 'Rose']

# Just the first name
print(names[0:1])
# ['Mary']

# Second and third
print(names[1:3])
# [Tom', 'Rose']

# From the second element up to the end of the list
print(names[1:4])
# ['Tom', 'Rose', 'Joe']

# The first index will be 0 by default, we can omit it:
print(names[:3])
# ['Mary', 'Tom', 'Rose']

# The last index will be the last element by default, we can also omit it
print(names[1:])
# ['Tom', 'Rose', 'Joe']
```
