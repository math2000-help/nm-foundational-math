# Topic 8: Dose Rate and Time

!!! info "Key idea"

    Total dose = dose rate × time. The time unit in the rate (for example, per hour) must match the time you multiply by.

    If the exposure is in minutes and the rate is per hour, convert minutes to hours first. To find the time instead, rearrange: time = dose ÷ rate.

## Solving for different variables

Let \(R\) be the dose rate, \(d\) the dose, and \(t\) the time. The relationship is \(d = R \times t\).

**Solve for \(t\):** divide both sides by \(R\).

\[
d = R \times t \quad\Rightarrow\quad \frac{d}{R} = \frac{\cancel{R} \times t}{\cancel{R}} \quad\Rightarrow\quad t = \frac{d}{R}
\]

**Solve for \(R\):** divide both sides by \(t\).

\[
d = R \times t \quad\Rightarrow\quad \frac{d}{t} = \frac{R \times \cancel{t}}{\cancel{t}} \quad\Rightarrow\quad R = \frac{d}{t}
\]

The time unit in \(R\) (for example, per hour) must match the unit of \(t\).

## Worked examples

!!! example "Ex 8.1"

    **If the dose rate is 25 mrem/h and the person being exposed is present for 25 minutes, what is their total dose? (Express your answer in mrem and round your answer to 1 decimal place.)**

    **Given:** \(R = 25\) mrem/h (dose rate), \(t = 25\) min (time present). &emsp; **Find:** \(d\) (total dose, in mrem), using \(d = R \times t\). &emsp; \(R\) is per hour but \(t\) is in minutes, so a conversion is needed.

    \[
    \dfrac{25\ \text{mrem}}{\cancel{\text{h}}} \times 25\ \bcancel{\text{min}} \times \dfrac{1\ \cancel{\text{h}}}{60\ \bcancel{\text{min}}} = 10.4167\ \text{mrem} = 10.4\ \text{mrem}
    \]

    **Answer:** <span class="answer">10.4 mrem</span>

    *Why: \(d = R \times t\). The rate is per hour and the time is in minutes, so the fraction \(\frac{1\ \text{h}}{60\ \text{min}}\) makes the time units match.*

!!! example "Ex 8.2"

    **At 30 mrem/h, how long until the dose reaches 10 mrem? (Express your answer in minutes.)**

    **Given:** \(R = 30\) mrem/h (dose rate), \(d = 10\) mrem (dose to reach). &emsp; **Find:** \(t\) (time, in min), using \(t = \dfrac{d}{R}\).

    \[
    t = \dfrac{d}{R} = \dfrac{10\ \text{mrem}}{30\ \text{mrem/h}} = 10\ \cancel{\text{mrem}} \times \dfrac{1\ \text{h}}{30\ \cancel{\text{mrem}}} = \dfrac{1}{3}\ \text{h}
    \]

    Convert hours to minutes:

    \[
    \dfrac{1}{3}\ \cancel{\text{h}} \times \dfrac{60\ \text{min}}{1\ \cancel{\text{h}}} = 20\ \text{min}
    \]

    **Answer:** <span class="answer">20 min</span>

    *Why: \(t = d \div R\) gives the time in hours, because the rate is per hour. The mrem cancel first. Then the hours cancel in the conversion, leaving minutes.*

## Try these

*Work each problem on paper with the setup-line method, then click **Show answer** to check your work.*

!!! question "Try 8.1"

    **A dose rate is 8 mrem/h. What is the dose after 15 minutes?**

    ??? success "Show answer"

        \[
        \dfrac{8\ \text{mrem}}{\cancel{\text{h}}} \times 15\ \cancel{\text{min}} \times \dfrac{1\ \cancel{\text{h}}}{60\ \cancel{\text{min}}} = 2\ \text{mrem}
        \]

        **Answer:** <span class="answer">2 mrem</span>

!!! question "Try 8.2"

    **A technologist receives a dose of 30 µSv in 150 minutes. What was the dose rate in µSv/h?**

    ??? success "Show answer"

        \[
        R = \dfrac{d}{t} = \dfrac{30\ \text{µSv}}{150\ \cancel{\text{min}}} \times \dfrac{60\ \cancel{\text{min}}}{1\ \text{h}} = 12\ \text{µSv/h}
        \]

        **Answer:** <span class="answer">12 µSv/h</span>

## Calculator tips

- Convert minutes to hours by dividing by 60 first, and keep the decimal on screen. For 6 mrem/h for 20 minutes: 20 ÷ 60 \(=\) 0.3333333, then × 6 gives 2 mrem.
- Or type the whole thing with parentheses: 6 × (20 ÷ 60) \(=\) 2 mrem.

## Common mistakes and pitfalls

- **Minutes vs. hours.** This is the most common error. Make sure the time units match.
- **Confusing dose rate with dose.** Rate has “per hour” in the unit; dose does not.
- **Dropping the unit** on the final answer.
