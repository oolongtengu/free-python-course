# Collections

In this unit we'll start learning about "collections", also commonly known as "Data Structures". We'll approach collections from a "utility" (abstract) standpoint: _what are they used for?_, _When should we use one or the other?_, etc. We won't focus on how they're implemented internally, as that's a much more complicated topic.

The main objective of Collections is to let us store many elements in the same "container". As simple as that. Think how you've been "storing elements" up to this point: probably only using variables. If I ask you to keep track of 3 users' emails, you'd do something like:

```python
user1 = 'tom@example.com'
user2 = 'mary@example.com'
user3 = 'alice@example.com'
```

Now, how do you add a new user **dynamically** (at run time)? You can't think of a new variable, as variables must be defined before running your script. The obvious solution for this is to use a **collection**. Let me show you an example and we'll then go into more detail about what's going on here.

```python
users = ['tom@example.com', 'mary@example.com', 'alice@example.com']

# new user is bob@example.com
users.append('bob@example.com')

print(users)
# Prints: ['tom@example.com', 'mary@example.com', 'alice@example.com', 'bob@example.com']
```

`users` in our previous example is a **_list_**. A list is _one type_ of collection that lets you store elements sequentially. It's arguably the most popular type of collection used in Python and we're going to talk in detail about them in our next lesson.
