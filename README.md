# String-Challenge
A few challenges borrowed from [/r/dailyprogrammer](www.reddit.com/r/dailyprogrammer) for exercising string methods and concepts.

## Using This Repo
Edit the `.py` files in `src/` to pass the tests.  To run the tests, `cd` into the root of this repo and run
```bash
$ python3 test.py
```
When editing the files in `src/`, you can add any functions you like, or even add more modules (`.py` files),
but if you change any of the original names of files or functions, *you're gonna have a bad time.*  Take a
look at `test.py` to understand why.

## Exercises

### Pangrams
A [pangram](http://en.wikipedia.org/wiki/Pangram) is a sentence that uses all of the letters of the alphabet.
You will need to edit the function `ispangram()` in pangram.py to accept a single string (the sentence) and
return `True` or `False` if the sentence is or isn't a pangram, respectively.
```Python
>>> x = "The quick brown fox jumps over the lazy dog."
>>> ispangram(x)
>>> True
>>>
>>> y = "A not-so-interesting string."
>>> ispangram(y)
>>> False
```

### Vowels
There are very few English words without vowels, and a few more that contain all the vowels, but less of those
that contain a-e-i-o-u-y *in order*.  Write a function called `ordered_vowels()` that accepts a list of strings
(single words) and returns a list of strings, comprised of only those words that have all the vowels in order.
Words with repeated vowels should not be returned.  `autoeciously` is a string with all the vowels in order, but
it also has a `u` before the `e`, so it shall not pass!
```Python
>>> x = ['facetiously', 'egregiously']
>>> ordered_vowels(x)
>>> ['facetiously']
>>>
>>> x = ['nth', 'word', 'autoeciously']
>>> ordered_vowels(x)
>>> []
```

