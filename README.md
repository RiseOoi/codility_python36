# codility_python36

*I will clean up the formatting of README.md later for quick/easy linking to each problem*

* In short, this repository provides unofficial solutions to lessons provided by [codility](https://app.codility.com/programmers/lessons) in pure Python 3.6.

* All solutions score 100% and use only the standard library.


---

## Why this repo?

* There are not much of good repos of codility's solutions in Python 3.6.

* And I actually wrote all these to teach myself, I will be glad if it helps you. If it doesn't, well, please try other repos.

* Also, I try to provide extensive comments and additional Python information for study. If you don't like the additional comments, either ignore them or try other repos.

* I also try to provide constructive criticisms of the incomplete/incorrect codility solutions that didn't cover all the cases or are not flexible enough.

* In fact, you will sometimes find solutions that perform better than official/unofficial solutions.

* In some cases that have multiple very possibly good answers, time measurements and deeper explanations are also be provided.

* This repo aims to be a standalone technical interview preparation study package so every .py is self contained with questions and additional comments embedded in. You do not need to visit codility, though I highly recommend visiting it and trying on your own code before looking up the solutions.

* Personally, I think codility is not really that user-friendly compared to leetcode, hard to debug, and the website/notes themselves have a lot of bugs and outdated information. However, I think codility has a good structure of teaching coders to become better and is extremely useful in technical interview preparation.

* I recommend doing codility first and then leetcode. After completing this repo I will start working on leetcode.

---

## Some Advice

* The debugging process is mediocre when compared to leetcode. So to debug, try the following code:
```
def solution(A):
    test_cases = []
    for a in A:
        test_cases.append(a)

    print(test_cases)

    # or `print([a for a in A])` if you like golf
    # or just `print(A)` if it allows (sometimes it doesn't)
```
to check which test_cases you failed. But this is not foolproof because there exists a limit of test_cases you can print. (You will understand my pain sooner or later)

codility should upgrade this immediately and provides more useful information for failed test cases.

---

## How are the files structured?

Usually it's *(Lesson number numerically)*-*(Problem number alphabetically)*-*(Problem Title)*

But the *'r'* in `1r-Iterations.py` means reading section.

I recommend everyone reads the reading section before diving in.

---

## Notes:

Take note that I am using CPython 3.6 implementation for this particular repo
because... well... codility uses CPython 3.6.

That means, if I took advantage of some features of CPython 3.6 and
even if it ended up 100% score in codility it doesn't mean it will perform
perfectly in versions/implementations other than CPython 3.6.

That means, please for Guido's sake, don't use any of these in production.
