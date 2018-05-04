# codility_python36

*I will clean up the formatting of README.md later for quick/easy linking to each problem*

* In short, this repository provides unofficial solutions to lessons provided by [codility](https://app.codility.com/programmers/lessons) in pure Python 3.6.

* All solutions score 100% and use only the standard library.


---

## Why this repo?

* There are not much of good repos of codility's solutions in Python 3.6. They are usually copy-pastas of the popular Python 2 solutions from other sites and not only they are outdated, hard to read, a lot of them never take advantage of Python 3.6+'s language features.

* And so, I try to provide extensive comments and additional Python information for study. If you don't like the additional comments, either ignore them or try other repos.

* Acutally, I wrote all these to teach myself Python 3.6 better, I will be delighted if it helps anyone. If it doesn't, well, please try other repos.

* I also try to provide constructive criticisms of the incomplete/incorrect codility solutions that didn't cover all the cases or are not flexible enough.

* In fact, you will often find solutions that perform better than official codility solutions (if there is one) and unofficial solutions from other sites.

* In some cases that have multiple very possibly good answers, time measurements and deeper explanations are also be provided.

* This repo aims to be a standalone technical interview preparation study package so every .py is self contained with questions and additional comments embedded in. You do not need to visit codility, though I highly recommend visiting it and trying on your own code before looking up the solutions.

* Personally, I think codility is not really that user-friendly compared to leetcode, hard to debug, and the website/notes themselves have a lot of bugs and outdated information. However, I think codility has a good structure of teaching coders to become better and is extremely useful in technical interview preparation.

* I recommend doing codility first and then leetcode. After completing this repo I will start working on leetcode.

---

## Some Advice

* The debugging process is mediocre when compared to leetcode.

* So to debug, try `print(A)` or `print([do something with a for a in A])` to check which test_cases you failed. But this is not foolproof because there exists a limit of test_cases you can print. (You will understand my pain sooner or later)

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

That means, I took advantage of a lot of features of CPython 3.6 and
even if it ended up 100% score in codility it doesn't mean it will perform
perfectly in versions/implementations other than CPython 3.6.

Moreover, it is very possible that you cannot convert many of my code (that depended on Python's prowness) to other programming languages.

Finally, since this is a pure CPython 3.6 implementation, there exists far better solutions using other implementations (PyPy) and non-standard libraries (SciPy/NumPy). Just take that in mind.

---

## Contributions:

Although I think I may have the best (most up-to-date, modern, Pythonic, best in terms of time complexity and space complexity) solutions so far, I may miss a few. So if you find any bugs or errors, or better, if you find even better solutions (within the constraints of CPython 3.6), please feel free to make an issue or pull request.
