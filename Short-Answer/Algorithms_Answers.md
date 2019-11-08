#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Although `a` is being compared against `n**3` in the `while` loop expression, it's being increased by `n**2` with every loop. Therefore, the loop will only run `n` times, **making this an `O(n)` function.**


b) So far as I can tell, `sum` isn't impacting runtime at all, so we're only concerned with `j` and `n`. The `for` loop iterating through `n` is the definition of an `O(n)` problem. The `while` loop inside *would* also be `O(n)`, except that `j` is doubling with every iteration, making it `O(log n)`. Since the `while` loop is inside of the `for` loop, we need to multiply the two together, **making this an `O(n log n)` problem.**


c)

## Exercise II


