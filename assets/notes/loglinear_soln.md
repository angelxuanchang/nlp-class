Warning: the following solutions may contain error.

# Solutions to exercises

## Log linear models

### Question 1
Yes. Recall the definition:

$$
Pr(y∣\textbf{x};\textbf{v})=\frac{\textbf{v}⋅\textbf{f}(\textbf{x},y)}{\sum_{y'\in Y} \textbf{v}⋅\textbf{f}(\textbf{x},y')}
$$

The denominator here is exactly the same for all $y \in Y$, so when determining which label should be the output, $\textrm{argmax}_y Pr(y∣\textbf{x};\textbf{v}) = \textrm{argmax}_y \textbf{v}⋅\textbf{f}(\textbf{x},y)$ is enough.

### Question 2

$$k = |V| \times |Y|$$

$$|{\cal Y}| = \frac{k}{|{\cal V}|} $$

$$f_k(x, y) \in \R^{|V| \times |Y|}$$, each _y_ is associated with a one-hot vector of the input _x_.

### Question 3

It is incorrect. This algorithm exits upon seeing the first $y$, while it should return the $y$ which gives the smallest $−\log Pr(y∣\textbf{x};\textbf{v})$.

### Question 4

* $$f_1(u,v) = \log(0.9) \textrm{ if } u=v$$
* $$f_1(u,v) = \log(\frac{0.1}{|V|-1}) \textrm{ if } u \neq v$$
* $$v_1 = 1$$

or

* $$f_1(u,v) = 1 \textrm{ if } u=v$$
* $$f_1(u,v) = 0 \textrm{ if } u \neq v$$
* $$v_1 = \log(9|V|-9) $$

### Question 5

For input `ab` and label `+` the features that are non-zero are f1, f3.
For input `ab` and label `-` the features that are non-zero are f2, f4.
For input `ab` and labels either `+` or `-` the features that are non-zero are f1+, f3+, f2-, f4-.

For input `bb` and label `+` the feature that is non-zero is f3.
For input `bb` and label `-` the feature that is non-zero is f4.
For input `bb` and labels either `+` or `-` the features that are non-zero are f3+, f4-.

1. P(y=+ | x=ab) ; exp(v1 + v3) / exp(v1 + v3) + exp(v2 + v4)
1. P(y=- | x=ab) ; exp(v2 + v4) / exp(v1 + v3) + exp(v2 + v4)
1. P(y=+ | x=bb) ; exp(v3) / exp(v3) + exp(v4)
1. P(y=- | x=bb) ; exp(v4) / exp(v3) + exp(v4)

