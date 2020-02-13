Warning: the following solutions may contain errors.

# Solutions to exercises

## n-gram Language models

### Question 1

    1. Pr(s) = Pr(<bs>|<bs>) *   
            Pr('I'|<bs>) *   
            Pr('would'|'I') *   
            Pr('like'|'would') *   
            Pr('to'|'like') *   
            Pr('go'|'to') *   
            Pr('West'|'go') *   
            Pr('.'|'West') *   
            Pr(<es>|'.') 
    2. Pr(s) = Pr('I'|<bs>,<bs>) *   
            Pr('would'|<bs>,'I') *   
            Pr('like'|'I', 'would') *   
            Pr('to'|'would', 'like') *   
            Pr('go'|'like', 'to') *   
            Pr('West'|'to', 'go') *   
            Pr('.' |'go', 'West') *   
            Pr(<es>|'West', '.')

### Question 2
$$
1/(3^{n-1})
$$

Because there are these many different $x_1 ... x_n$ strings (as $x_n$ is STOP always), so sum over all $x_1 ... x_n$ strings to be equal to $1$ means each string gets probability $\frac{0.5^n}{3^{n-1}}$.

### Question 3
1. Max value of perplexity is $\infty$ if any sentence gets zero probability.

2. Min value is 1 as it predicts each sentence perfectly.

3. The test corpus should have a bigram unobserved in training which gets zero.

4. The test corpus should have exactly the same bigram as in training and each bigram should be unique.

### Question 4

$\lambda_1 = \alpha$, $\lambda_2 = \beta(1 - \alpha)$, $\lambda_3 = (1-\alpha)(1-\beta)$, take in $\alpha=\beta=0.5$ then we have the answer.

### Question 5

$$
P('I' | <bs>) = 2/3\\
P('Sam' | <bs>) = 1/3\\
P(<es> | 'Sam') = 1/2\\
P('Sam' | 'am') = 1/2\\
P('am' | 'I') = 2/3\\
P('do' | 'I') = 1/3\\
$$

