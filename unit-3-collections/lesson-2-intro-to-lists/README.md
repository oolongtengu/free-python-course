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

# List Operations

Having a list created is not enough. We'll need to "manipulate" these lists to achieve something useful. These are the most common operations with lists:

* Adding elements
* Removing elements
* Counting elements (_"How many elements does this list have?"_)
* Check if an element exists in a list (_"Is john@rmotr.com already part of this list?"_)
* "Concatenating" lists: Building a new list out of two or more lists.

We'll explore all these operations in detail in the following lessons.

## Creating Lists

There are two possible ways of creating lists:

##### Literally

This is the preferred (and most intuitive) way. With it, you create the list and specify elements "right in place". Everything seems like just one operation. It's what we've been doing up to this point:

```python
courses = ['Intro to Python', 'Advanced Python']
```

In this example we've created the list `courses` containing two elements. We're also using square brackets (`[]`) to denote the list.


##### Programmatically

In this case the process of creating the list and populating it (inserting elements) will be split in several steps:

```python
courses = list()

courses.append('Intro to Python')
courses.append('Advanced Python')
```

This example looks a little bit less "intuitive". First, we're using the `list()` function to create an empty list (we're not using square brackets) and then we're adding elements one by one.
