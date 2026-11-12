# Topic 9: Distance (Inverse Square Law)

!!! info "Key idea"

    \(I_1 d_1^2 = I_2 d_2^2\). Radiation drops quickly as you move away: double the distance, and the rate drops to one quarter.

    Use the same distance unit on both sides. Direction check: farther away must give a smaller reading.

## Solving for different variables

Start with \(I_1 d_1^2 = I_2 d_2^2\).

**Solve for \(I_2\):** divide both sides by \(d_2^2\).

\[
I_1 d_1^2 = I_2 d_2^2 \quad\Rightarrow\quad \frac{I_1 d_1^2}{d_2^2} = \frac{I_2 \cancel{d_2^2}}{\cancel{d_2^2}} \quad\Rightarrow\quad I_2 = \frac{I_1 d_1^2}{d_2^2}
\]

**Solve for \(d_2\):** divide both sides by \(I_2\), then take the square root of both sides.

\[
I_1 d_1^2 = I_2 d_2^2 \quad\Rightarrow\quad \frac{I_1 d_1^2}{I_2} = \frac{\cancel{I_2} d_2^2}{\cancel{I_2}} \quad\Rightarrow\quad d_2^2 = \frac{I_1 d_1^2}{I_2} \quad\Rightarrow\quad d_2 = \sqrt{\frac{I_1 d_1^2}{I_2}}
\]

## Worked examples

!!! example "Ex 9.1"

    **A point source produces an exposure rate of 100 mR/h at a distance of 1 ft. What is the exposure rate at a distance of 2 ft?**

    **Given:** \(I_1 = 100\) mR/h (rate at the first distance), \(d_1 = 1\) ft (first distance), \(d_2 = 2\) ft (second distance). &emsp; **Find:** \(I_2\) (rate at the second distance), using \(I_2 = \dfrac{I_1 d_1^2}{d_2^2}\).

    \[
    I_2 = 100\ \text{mR/h} \times \dfrac{(1\ \cancel{\text{ft}})^2}{(2\ \cancel{\text{ft}})^2} = \dfrac{100\ \text{mR/h}}{4} = 25\ \text{mR/h}
    \]

    **Answer:** <span class="answer">25 mR/h</span>

    *Why: Doubling the distance cuts the rate to one quarter. The feet cancel, so the answer keeps the mR/h unit.*

!!! example "Ex 9.2"

    **A source reads 160 mR/h at 1 m. At what distance is the reading 10 mR/h?**

    **Given:** \(I_1 = 160\) mR/h (rate at the first distance), \(d_1 = 1\) m (first distance), \(I_2 = 10\) mR/h (the reading we want). &emsp; **Find:** \(d_2\) (distance where that reading occurs), using \(d_2 = \sqrt{\dfrac{I_1 d_1^2}{I_2}}\).

    \[
    d_2 = \sqrt{160\ \cancel{\text{mR/h}} \times \dfrac{(1\ \text{m})^2}{10\ \cancel{\text{mR/h}}}} = \sqrt{16\ \text{m}^2} = 4\ \text{m}
    \]

    **Answer:** <span class="answer">4 m</span>

    *Why: The mR/h cancel inside the square root, leaving m\(^2\). When solving for distance, take the square root as the last step.*

## Try these

*Work each problem on paper with the setup-line method, then click **Show answer** to check your work.*

!!! question "Try 9.1"

    **A source reads 45 mR/h at 2 ft. What is the reading at 6 ft?**

    ??? success "Show answer"

        \[
        I_2 = \dfrac{(45\ \text{mR/h})(2\ \cancel{\text{ft}})^2}{(6\ \cancel{\text{ft}})^2} = \dfrac{45 \times 4}{36}\ \text{mR/h} = 5\ \text{mR/h}
        \]

        **Answer:** <span class="answer">5 mR/h</span>

!!! question "Try 9.2"

    **A source reads 90 mR/h at 1 m. At what distance is the reading 10 mR/h?**

    ??? success "Show answer"

        \[
        d_2^2 = \dfrac{(90\ \bcancel{\text{mR/h}})(1\ \text{m})^2}{10\ \bcancel{\text{mR/h}}} = 9\ \text{m}^2
        \]

        \[
        d_2 = \sqrt{9\ \text{m}^2} = 3\ \text{m}
        \]

        **Answer:** <span class="answer">3 m</span>

## Calculator tips

- Use the x<sup>2</sup> key to square distances and the √ key for square roots.
- Square first, then divide. Use parentheses: (100 × 1<sup>2</sup>) ÷ 2<sup>2</sup>.
- When solving for distance, compute the number under the root first, then press √.

## Common mistakes and pitfalls

- **Forgetting to square the distance.** This is the most common error.
- **Forgetting the square root** at the end when solving for distance.
- **Mixed units** (feet on one side, inches on the other).
- **Wrong direction.** If your reading gets bigger as you move away, you flipped the equation.
