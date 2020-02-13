Warning: the following solutions may contain error.

# Solutions to exercises
https://github.com/anoopsarkar/nlp-class/blob/gh-pages/assets/notes/linearb_solution.pdf
## Word2Vec Practice

### Question 1

2. $-\log(0.01)$

$Pr(y)$ for all $y$ equals 0.01, and cross-entropy is just negative log.

### Question 2
No. Suppose the algorithm is Skip-gram with negative sample, the classifier here is trained to maximise $u_w \cdot v_w$ for all positive samples, and penalise $u_w \cdot v_w'$ for all negative samples, then it is possible that while $u^A_w⋅v^A_w=u^B_w⋅v^B_w$ since such values are all maximised, but the actual trained values of $v_w^A$ and $v_w^B$ are different. For instance, you can divide $u^A$ by $k$ and multiply $v^A$ by $k$ to still obtain the equality but the vectors $v^A$ and $v^B$ are different. 

### Question 3
1. |V|
2. 1
3. $u_w \in \mathbb{R}^k$ are weights for scoring how likely the is $w$ the target word under the current context $\hat{v}$ 
4. $$U \in \mathbb{R}^{|V| \times k}$$
5. Negative sampling uses a separate classifier to distinguish between positive samples and negative samples and makes an independence assumption over the context vectors. Without modification to the cross-entropy loss function, such classifier cannot be trained due to the average over the context vectors.

SideNote: one could use negative sampling in a modified cross-entropy based loss function for CBOW, but empirical results suggest that this might not work very well as cross-entropy tends to be fairly powerful on its own.

### Question 4

Very simple proof.

$P(Y=1∣x)=\sigma(\beta x)  = \frac{1}{1+\exp(-\beta x)} = \frac{1}{1+\exp(\beta_2 x-\beta_1 x)} = \frac{\exp(\beta_1 x)}{\exp(\beta_1 x)+\exp(\beta_2 x)}$
$P(Y=2∣x)=1-\sigma(\beta x)  = 1-\frac{1}{1+\exp(-\beta x)} = \frac{\exp(-\beta x)}{1+\exp(-\beta x)} = \frac{1}{1+\exp(\beta x)} = \frac{\exp(\beta_2 x)}{\exp(\beta_1 x)+\exp(\beta_2 x)}$

### Question 5

1. Example answer:
$L_E(Q_E) = \sum_{w_i\in V_E} \left[ \alpha( ||v_i^E-\hat{v_i^E}||^2 + ||u_i^E-\hat{u_i^E}||^2) + \sum_{(w_i, w_j)\in \textit{Trans}, w_j\in V_F} \beta(||v_i^E-v_j^F||^2  +||u_i^E-u_j^F||^2) \right]$

2. Example answer:
$Q_E = \hat{Q}_E$

3. Same as subq1 and subq2, except that E and F are swapped.
