#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Although `a` is being compared against `n**3` in the `while` loop expression, it's being increased by `n**2` with every loop. Therefore, the loop will only run `n` times, **making this an `O(n)` function.**


b) So far as I can tell, `sum` isn't impacting runtime at all, so we're only concerned with `j` and `n`. The `for` loop iterating through `n` is the definition of an `O(n)` problem. The `while` loop inside *would* also be `O(n)`, except that `j` is doubling with every iteration, making it `O(log n)`. Since the `while` loop is inside of the `for` loop, we need to multiply the two together, **making this an `O(n log n)` problem.**


c) The recursive call decrements the input by one for each inner call, working towards the base case of zero. The base case itself is `O(1)`, so because the recursive calls are basically equivalent to `range(bunnies, 0, -1)` (iterating backwards over the length of zero to the number of bunnies), **this is an `O(n)` function.**

## Exercise II

<!--
- Building n stories tall, "plenty" of eggs
- Egg breaks from some floor f, upwards; doesn't break below
- Minimize the number of dropped & broken eggs
-->
```
is_broken_at_story = [false, false, true, ...] # 0-indexed array/list of boolean values for each floor from the bottom

function(is_broken_at_story):
    // Initialize high/low values at first/last indices
    h_unbroken = 0 // Bottom floor
    l_broken = is_broken_at_story.length - 1 // Top floor

    // Loop until the two indices are neighbors
    while (l_broken - h_unbroken) > 1:
        // Find the middle index between the references, rounded down to whole number
        mid = ((l_broken + h_unbroken) / 2).floor
        // If the egg breaks, that's a new low floor to break
        if is_broken_at_story[mid] is true:
            l_broken = mid
        // If the egg doesn't break, that's a new high floor to not break
        else if is_broken_at_story[mid] is false:
            h_unbroken = mid
    
    // Return the lowest floor at which the egg breaks
    return l_broken
```
