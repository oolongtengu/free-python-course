# Creating Lists

There are two possible ways of creating lists:

* Literally
* Programmatically

Let's explore them in detail

## Literally

This is the preferred (and most intuitive) way. With it, you create the list and specify elements "right in place". Everything seems like just one operation. It's what we've been doing up to this point:

```python
courses = ['Intro to Python', 'Advanced Python']
```

In this example we've created the list `courses` containing two elements. We're also using square brackets (`[]`) to denote the list.


## Programmatically

In this case the process of creating the list and populating it (inserting elements) will be split in several steps:

```python
courses = list()

courses.append('Intro to Python')
courses.append('Advanced Python')
```

This example looks a little bit less "intuitive". First, we're using the `list()` function to create an empty list (we're not using square brackets) and then we're adding elements one by one.
