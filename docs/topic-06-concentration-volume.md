# Topic 6: Concentration and Volume

!!! info "Key idea"

    \(C = A \div V\), \(V = A \div C\), and \(A = C \times V\), where \(C\) is concentration (mCi/mL), \(A\) is activity (mCi), and \(V\) is volume (mL).

    The algebra for solving for \(A\) or \(V\) is shown in the next section. In the worked examples, use a setup line with the units canceling.

    Easy memory trick: volume needed \(=\) what you want \(\div\) what you have. Round syringe volumes to the nearest tenth of a mL.

## Solving for different variables

Start with the definition of concentration. To solve for another variable, do the same thing to both sides of the equation.

**Solve for \(A\):** multiply both sides by \(V\).

\[
C = \frac{A}{V} \quad\Rightarrow\quad C \times V = \frac{A}{\cancel{V}} \times \cancel{V} \quad\Rightarrow\quad A = C \times V
\]

**Solve for \(V\):** start again with \(C = \dfrac{A}{V}\). Multiply both sides by \(V\) to get \(V\) out of the denominator, then divide both sides by \(C\).

\[
\begin{aligned}
C &= \frac{A}{V}\\[4pt]
C \times V &= \frac{A}{\cancel{V}} \times \cancel{V}\\[4pt]
C \times V &= A\\[4pt]
\frac{\cancel{C} \times V}{\cancel{C}} &= \frac{A}{C}\\[4pt]
V &= \frac{A}{C}
\end{aligned}
\]

## Worked examples

!!! example "Ex 6.1"

    **A vial contains 60 mCi in 4 mL. What is the concentration?**

    **Given:** \(A = 60\) mCi (activity), \(V = 4\) mL (volume). &emsp; **Find:** \(C\) (concentration, in mCi/mL).

    \[
    C = \dfrac{A}{V} = \dfrac{60\ \text{mCi}}{4\ \text{mL}} = 15\ \text{mCi/mL}
    \]

    **Answer:** <span class="answer">15 mCi/mL</span>

!!! example "Ex 6.2"

    **A 30 mCi dose is needed from a vial at 15 mCi/mL. What is the volume? (Express your answer in mL.)**

    **Given:** \(A = 30\) mCi (the dose we want), \(C = 15\) mCi/mL (the vial concentration we have). &emsp; **Find:** \(V\) (volume, in mL).

    \[
    V = \dfrac{A}{C} = \dfrac{30\ \text{mCi}}{15\ \text{mCi/mL}}
    \]

    Dividing by a fraction is the same as multiplying by its reciprocal:

    \[
    V = 30\ \cancel{\text{mCi}} \times \dfrac{1\ \text{mL}}{15\ \cancel{\text{mCi}}} = 2.0\ \text{mL}
    \]

    **Answer:** <span class="answer">2.0 mL</span>

    *Why: \(V = A \div C\) (what you want \(\div\) what you have). Flipping 15 mCi/mL to its reciprocal, 1 mL/15 mCi, makes the mCi cancel, leaving mL.*

!!! example "Ex 6.3"

    **How much activity is in 1.5 mL of a solution at 0.02 mCi/µL? (Express your answer in mCi.)**

    **Given:** \(V = 1.5\) mL (volume), \(C = 0.02\) mCi/µL (concentration). &emsp; **Find:** \(A\) (activity, in mCi). &emsp; \(V\) is in mL but \(C\) is per µL, so convert first.

    **Step 1: Convert \(C\) to mCi/mL.**

    \[
    C = \dfrac{0.02\ \text{mCi}}{1\ \bcancel{\text{µL}}} \times \dfrac{1{,}000\ \bcancel{\text{µL}}}{1\ \text{mL}} = 20\ \text{mCi/mL}
    \]

    **Step 2: Plug into \(A = C \times V\).**

    \[
    A = 20\ \dfrac{\text{mCi}}{\cancel{\text{mL}}} \times 1.5\ \cancel{\text{mL}} = 30\ \text{mCi}
    \]

    **Answer:** <span class="answer">30 mCi</span>

    *Why: The µL cancel in Step 1, leaving mCi/mL. Then the mL cancel in Step 2, leaving mCi.*

## Try these

*Work each problem on paper with the setup-line method, then click **Show answer** to check your work.*

!!! question "Try 6.1"

    **A vial contains 80 mCi in 5 mL. What is the concentration in mCi/mL?**

    ??? success "Show answer"

        \[
        C = \dfrac{80\ \text{mCi}}{5\ \text{mL}} = 16\ \text{mCi/mL}
        \]

        **Answer:** <span class="answer">16 mCi/mL</span>

!!! question "Try 6.2"

    **A 24 mCi dose is needed from a vial at 40 mCi/mL. What volume in mL should be drawn?**

    ??? success "Show answer"

        \[
        V = 24\ \cancel{\text{mCi}} \times \dfrac{1\ \text{mL}}{40\ \cancel{\text{mCi}}} = 0.6\ \text{mL}
        \]

        **Answer:** <span class="answer">0.6 mL</span>

## Calculator tips

- If the concentration comes from a division, calculate it first and keep the answer on screen (or use the Ans key) before dividing the dose by it.
- If you chain it in one line, use parentheses. For a different example, a 24 mCi dose from a vial with 80 mCi in 5 mL: 24 ÷ (80 ÷ 5) \(=\) 1.5 mL.

## Common mistakes and pitfalls

- **Flipping A and V.** Concentration is activity over volume, never volume over activity.
- **Unit mismatch.** If the dose is in mCi and the vial is in µCi/mL, convert first.
- **Not rounding** the volume to the nearest tenth of a mL.
- **Mixing up “want” and “have.”** The dose is what you want; the concentration is what you have.
