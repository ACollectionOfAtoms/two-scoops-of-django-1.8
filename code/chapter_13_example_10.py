"""
Using This Code Example
=========================

The code examples provided are provided by Daniel Greenfeld and Audrey Roy of
Two Scoops Press to help you reference Two Scoops of Django: Best Practices
for Django 1.8. Code samples follow PEP-0008, with exceptions made for the
purposes of improving book formatting. Example code is provided "as is", and
is not intended to be, and should not be considered or labeled as "tutorial code".

Permissions
============

In general, you may use the code we've provided with this book in your programs
and documentation. You do not need to contact us for permission unless you're
reproducing a significant portion of the code or using it in commercial
distributions. Examples:

* Writing a program that uses several chunks of code from this course does not require permission.
* Selling or distributing a digital package from material taken from this book does require permission.
* Answering a question by citing this book and quoting example code does not require permission.
* Incorporating a significant amount of example code from this book into your product's documentation does require permission.

Attributions usually include the title, author, publisher and an ISBN. For
example, "Two Scoops of Django: Best Practices for Django 1.8, by Daniel
Roy Greenfeld and Audrey Roy Greenfeld. Copyright 2015 Two Scoops Press."

If you feel your use of code examples falls outside fair use of the permission
given here, please contact us at info@twoscoopspress.org."""
# core/jinja2.py
from __future__ import absolute_import # Python 2 only
from jinja2 import Environment

import random

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        # Runs only on the first template load! The three displays below
        #   will all present the same number.
        #   {{ random }} {{ random }} {{ random }}
        'random_once': random.randint(1, 5)
        # Can be called repeated as a function in templates. Each call 
        #   returns a random number:
        #   {{ random() }} {{ random() }} {{ random() }}
        'random': lambda: random.randint(1, 5),
    })
    return env