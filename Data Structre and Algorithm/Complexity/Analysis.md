# Analysis of Complexity
This section demonstrates some analysis of some classic algorithm,including the concept of the notation **O** such as **$O(n)$** and  **$O(n^2)$**

## Table of contents
- [Concept of O](#Concept)
- [Some comparison](#Comparison)



### Concept
Let's say we have to functions: $f(n)$ and $g(n)$, where n is the positive integer. If we have a constant $c> 0$ and a integer constant $n_0\ge  1$, and it can satisfy the following conditions $$ f(n) \le cg(n), n \ge n_0$$ 

Then, we can say that $f(n)$ is $O(g(n))$