Part 1 can be solved algebraically.

Let $y=f(t)$ be the distance travelled when pressing the button for $t$ milliseconds.
Then $f$ can be expressed as $f(t) = (t_f-t)t = -t^2 + t t_f$.
We want to know when $f(t) \gt d$, which is the same as

$$
\begin{align}
f(t) - d > 0 \\
-t^2 + t t_f -d > 0 \\
t^2 - t_f t +d < 0 \\
\end{align}
$$.
Solving for $t$ we get
$$

t = \frac{1}{2} (t_f \pm \sqrt{t_f^2-4d})

$$

Trying this out with example race 1:
$$

t = \frac{1}{2}(7 \pm \sqrt{49- 4 \times 7}) = \frac{1}{2}(7 \pm \sqrt{21}) = (3.5 \pm 2.29128785) \approx 5.8 \vee 1.2

$$

Take the floor of the smaller number and the ceil of the larger number, to get:

$$

t = 2 \vee
t = 5

$$
And thus the number of ways the boat can win is the whole integers in the closed interval $[2,5]$, i.e. $\set{2,3,4,5}$.
$$
