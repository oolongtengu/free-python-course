# Creating Lists

There are two possible ways of creating lists:

* Literally
* Programmatically

Let's explore them in detail.

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

## Literally vs Programmatically

The difference between these two methods lies in the "expressiveness" of our solution. With the **Literal** method we're explicitly and declaratively and **specifying** how our list will look like:

```python
shopping_list = ['Milk', 'Eggs', 'Bread']
```

With the programmatic method we're specifying the steps that the computer needs to follow to achieve the same result:

```python
shopping_list = list()
shopping_list.append('Milk')
shopping_list.append('Eggs')
shopping_list.append('Bread')
```

If it sounds confusing, think about that time that you asked someone to do something for you. If that person had enough "domain knowledge" you can just tell them directly what to do, in other case, you'd need to tell them specifically the steps required to achieve that result.

Consider the example of "baking cookies". If you're sharing your special cookies recipe with someone that knows about cooking, you'll just tell them: "bake the cookies for about 10 minutes". If you're talking with someone less experienced with cooking (or maybe a robot), you'll need to be a lot more explicit: "Open the oven door, turn on the oven, set it in 350º, wait 10 minutes, take the cookies out". You're giving a specific set of steps that will achieve the same result as the previous "more declarative" way ("just bake the cookies").

**Let's do some practice related to creating lists...**
