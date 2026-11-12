# Topic 11: Radioactive Decay (Tc-99m)

!!! info "Key idea"

    Memorize two values: the half-life of Tc-99m is \(T_{1/2} = 6\) hours, and \(\ln 2 \approx 0.693\). The decay constant is \(\lambda = 0.693 \div T_{1/2}\), which is about 0.1155 per hour for Tc-99m.

    Two methods give the same answer. Halving method: \(A = A_0 \div 2^n\), where \(n\) = elapsed time \(\div\) \(T_{1/2}\) (the number of half-lives). Exponential method: \(A = A_0 e^{-\lambda t}\).

    Check your work: elapsed time, \(T_{1/2}\), and \(\lambda\) must all use the same time units. The decayed activity \(A\) must always be smaller than the starting activity \(A_0\).

## Solving for the starting activity

Start with the exponential decay equation. To find the starting activity \(A_0\), divide both sides by \(e^{-\lambda t}\).

\[
A = A_0 \, e^{-\lambda t} \quad\Rightarrow\quad \frac{A}{e^{-\lambda t}} = \frac{A_0 \, \cancel{e^{-\lambda t}}}{\cancel{e^{-\lambda t}}} \quad\Rightarrow\quad A_0 = \frac{A}{e^{-\lambda t}}
\]

Use this when you know the activity wanted later (\(A\)) and need the activity to start with (\(A_0\)). The answer must be larger than \(A\), because the activity decays while it waits.

## Worked examples

!!! example "Ex 11.1"

    **A vial contains 48 mCi of Tc-99m. How much remains after 18 hours?**

    **Given:** \(A_0 = 48\) mCi (starting activity), \(t = 18\) h (elapsed time), \(T_{1/2} = 6\) h (half-life of Tc-99m). &emsp; **Find:** \(A\) (activity remaining), using \(A = A_0 \div 2^n\).

    \[
    n = 18\ \cancel{\text{h}} \times \dfrac{1\ \text{half-life}}{6\ \cancel{\text{h}}} = 3\ \text{half-lives}
    \]

    \[
    A = \dfrac{A_0}{2^n} = \dfrac{48\ \text{mCi}}{2^3} = \dfrac{48\ \text{mCi}}{8} = 6\ \text{mCi}
    \]

    **Answer:** <span class="answer">6 mCi</span>

    *Why: Three half-lives: 48 \(\rightarrow\) 24 \(\rightarrow\) 12 \(\rightarrow\) 6.*

!!! example "Ex 11.2"

    **Tc-99m has a half-life of 6 hours. Calculate the decay constant, \(\lambda\), for Tc-99m.**

    **Given:** \(T_{1/2} = 6\) h (half-life of Tc-99m). &emsp; **Find:** \(\lambda\) (decay constant), using \(\lambda = 0.693 \div T_{1/2}\).

    \[
    \lambda = \dfrac{0.693}{6\ \text{h}} = 0.1155\ \text{h}^{-1}
    \]

    **Answer:** <span class="answer">0.1155 h<sup>\(-\)1</sup></span>

!!! example "Ex 11.3"

    **A 50 mCi Tc-99m dose is prepared. How much activity remains after 240 minutes? Round your answer to 1 decimal place as needed. Use \(A = A_0 e^{-\lambda t}\).**

    **Given:** \(A_0 = 50\) mCi (starting activity), \(t = 240\) min (elapsed time), \(T_{1/2} = 6\) h (half-life of Tc-99m). &emsp; **Find:** \(A\) (activity remaining), using \(A = A_0 e^{-\lambda t}\). &emsp; \(t\) is in minutes but \(\lambda\) is per hour, so convert \(t\) first, and find \(\lambda\) from \(T_{1/2}\).

    \(240\ \cancel{\text{min}} \times \dfrac{1\ \text{h}}{60\ \cancel{\text{min}}} = 4\ \text{h}\), &emsp; \(\lambda = \dfrac{0.693}{6\ \text{h}} = 0.1155\ \text{h}^{-1}\)

    \[
    A = 50\ \text{mCi} \times e^{-(0.1155\ \cancel{\text{h}^{-1}})(4\ \cancel{\text{h}})} = 50\ \text{mCi} \times e^{-0.462} = 31.5\ \text{mCi}
    \]

    **Answer:** <span class="answer">31.5 mCi</span>

    *Why: Convert minutes to hours first, because \(\lambda\) and \(T_{1/2}\) are in hours. The h\(^{-1}\) and h cancel in the exponent. The result (31.5) is smaller than the start (50), so the negative sign is correct.*

!!! example "Ex 11.4"

    **A technologist needs 30 mCi of Tc-99m at the time of injection, which is 90 minutes from now. What activity should the dose have now?**

    **Given:** \(A = 30\) mCi (activity wanted at injection), \(t = 90\) min (time until injection), \(\lambda = 0.1155\) h\(^{-1}\) (from Ex 11.2). &emsp; **Find:** \(A_0\) (activity to have now), using \(A_0 = \dfrac{A}{e^{-\lambda t}}\).

    \[
    90\ \cancel{\text{min}} \times \dfrac{1\ \text{h}}{60\ \cancel{\text{min}}} = 1.5\ \text{h}
    \]

    \[
    A_0 = \dfrac{30\ \text{mCi}}{e^{-(0.1155\ \cancel{\text{h}^{-1}})(1.5\ \cancel{\text{h}})}} = \dfrac{30\ \text{mCi}}{e^{-0.17325}} = \dfrac{30\ \text{mCi}}{0.8409274} = 35.7\ \text{mCi}
    \]

    **Answer:** <span class="answer">35.7 mCi</span>

    *Why: The dose will decay while it waits, so it must start larger than 30 mCi. The answer (35.7) is larger than 30, which makes sense.*

## Try these

*Work each problem on paper with the setup-line method, then click **Show answer** to check your work.*

!!! question "Try 11.1"

    **A vial has 64 mCi of Tc-99m. How much remains after 24 hours?**

    ??? success "Show answer"

        \[
        n = 24\ \cancel{\text{h}} \times \dfrac{1\ \text{half-life}}{6\ \cancel{\text{h}}} = 4
        \]

        \[
        A = \dfrac{64\ \text{mCi}}{2^4} = \dfrac{64\ \text{mCi}}{16} = 4\ \text{mCi}
        \]

        **Answer:** <span class="answer">4 mCi</span>

!!! question "Try 11.2"

    **A 30 mCi Tc-99m dose is measured. How much remains after 2 hours? Use \(A = A_0 e^{-\lambda t}\).**

    ??? success "Show answer"

        \[
        \lambda = \dfrac{0.693}{6\ \text{h}} = 0.1155\ \text{h}^{-1}
        \]

        \[
        A = 30\ \text{mCi} \times e^{-(0.1155\ \cancel{\text{h}^{-1}})(2\ \cancel{\text{h}})} = 30\ \text{mCi} \times e^{-0.231} = 30\ \text{mCi} \times 0.793739 = 23.8\ \text{mCi}
        \]

        **Answer:** <span class="answer">23.8 mCi</span>

## Calculator tips

- Find the e<sup>x</sup> key. It is usually the second function of the LN key (press <kbd>2nd</kbd> or <kbd>SHIFT</kbd> first).
- Enter the whole exponent in parentheses, using the negative-sign key, so the calculator reads e<sup>\(-\)0.1155 × 4</sup>. If your calculator shows an in-line caret instead of a raised exponent, it will read e^(\(-\)0.1155 × 4).
- Test it: e<sup>\(-\)0.693</sup> (or e^(\(-\)0.693)) should give about 0.5. If it does not, check your negative sign and parentheses.
- Check the result: the decayed activity must be smaller than the starting activity.
- To find the starting activity (Ex 11.4), divide by the exponential term: 30 ÷ e<sup>\(-\)0.1155 × 1.5</sup> \(=\) 35.7 mCi. Keep the whole exponent in parentheses, e.g. 30 ÷ e^(\(-\)0.1155 × 1.5).

## Common mistakes and pitfalls

- **Time units not matching \(T_{1/2}\).** Convert minutes to hours before you start.
- **Dropping the negative sign** in the exponent. When you are finding the remaining activity, an answer bigger than the starting activity means the sign is wrong.
- **Forgetting to calculate \(\lambda\) first.** \(\lambda = 0.693 \div 6\) before you use \(A = A_0 e^{-\lambda t}\).
