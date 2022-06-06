# Analysis of Complexity
This section demonstrates some analysis of some classic algorithm,including the concept of the notation **O** such as **$O(n)$** and  **$O(n^2)$**


  ## Table of contents
 - [Concept](#concept)
 - [Comparison](#comparison)



### Concept
Let's say we have to functions: $f(n)$ and $g(n)$, where n is the positive integer. If we have a constant $c> 0$ and a integer constant $n_0\ge  1$, and it can satisfy the following conditions $$ f(n) \le cg(n), n \ge n_0$$ 

Then, we can say that $f(n)$ is $O(g(n))$. And when we are analying the time complexity of an algorithm, we only focus on the highest order. For example: $f(n)=n^2+2n+3$, then we can say that the time complexity if $n^2$.

Question: Prove that the time complexity of $5n^4+3n^3+2n^2+4n+1$ is $O(n^4)$

***Proof：*** $$5n^4+3n^3+2n^2+4n+1\le (5+3+2+4+1)n^4=cn^4$$


### Comparison

In this section, two classic sorting algortihms: Bubble Sorting and insert Sorting.
As we can see from the figure below, when n increases, the time taken to finish sorting increase sharply in the bubble sorting Algoritm, where the time complexity is $O(n^2)$, while that for the insert sorting algortihm is $O(n)$ and the worst case is also $O(n^2)$
<img src="/assets/img/MarineGEO_logo.png" alt="MarineGEO circle logo" style="height: 100px; width:100px;"/>