# Intro to Control Flow

As we've seen in class, our algorithms are just a set of rules that instruct the computer to do something. We're commanding the computer on what to do. But these algorithms won't be linear, there will be different "paths" to take. The most common example is the introduction of **_conditionals_**. Conditionals, also known as **_if statements_**, let us make decisions in our algorithms. Examples:

* If the user's age is less than 16, don't allow the registration.
* If the purchase is greater than $1000, check for fraud.

The general form of an **IF** statement in Python is as follows:

```python
if [CONDITION]:
    # do something
    # (Condition True path)
else:
    # do something else
    # (Condition False path)
```

In our previous example, the `[CONDITION]` is what will make you decide between one path or the other. If the condition evaluates to `True`, the "True" path is taken. If the condition is NOT True (it's `False`), the "False" path is taken. Note the square brackets around `[CONDITION]` are just placeholders for this example and are not actually used in code.

The condition for your if statements will be formed with a combination of data and boolean operators. For example, these are all valid conditions:

* `user_age > 16`
* `purchase_total > 1000`
* `user_is_active and date_registered < today`

There are many boolean operators, like:

* `>` : Greater than
* `<` : Less than
* `==` : Equals
* `>=` : Greater or equals than
* `<=` : Less or equals than

We also have operators **`and`** and **`or`** that "combine" other operations. Finally we have the **`not`** operator that just inverts the given value provided (like from `True` to `False`).

## Reading material

A good resource to find a comprehensive explanation of the if statement is [A Byte of Python's chapter about control flow](https://python.swaroopch.com/control_flow.html#the-if-statement).

[Chapter 2 from Automate the Boring Stuff with Python](https://automatetheboringstuff.com/chapter2/) has a longer explanation that covers **in detail** Python boolean operators and if statements.

**IMPORTANT:** We're not dealing with loops yet. You're not _supposed_ to read about them yet. If you still want to read about them, don't worry if you don't understand them completely. We'll explain them carefully in class.
