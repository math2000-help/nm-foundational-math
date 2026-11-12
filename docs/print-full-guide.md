# Print the Full Guide

<div class="no-print" markdown>

!!! tip "How to save the whole guide as a PDF"

    1. Click **Print / Save as PDF** (top right), or press **Ctrl+P** (Windows) or **Cmd+P** (Mac).
    2. Choose **Save as PDF** as the destination.
    3. Turn on **Background graphics** so the colored boxes print.

    All answers open automatically in the printout. Scroll down to see the full guide.

</div>


# Start Here: The Setup-Line Method

!!! info "The idea"

    Most problems in this workshop are solved the same way. Write one setup line that shows what you start with, the fractions you multiply by, and the units canceling, so that only the unit you want is left. Then label your answer with that unit.

## The five-step routine

1. **WANT.** Find the question and <u>underline</u> what you are asked to find (including its unit).
2. **HAVE.** Find the given numbers and <span class="boxed">circle</span> each one with its unit.
3. **LABEL.** Write the unit next to every number. A number with no unit cannot be set up.
4. **SET UP.** Write a fraction setup so the units cancel and only the wanted unit is left. Use a fraction equal to 1 (such as \(\frac{37\ \text{MBq}}{1\ \text{mCi}}\)) for each conversion.
5. **CHECK.** Does the answer have the unit you wanted? Is the number the right size and the right direction (smaller unit means bigger number)?

In the worked examples that follow, the HAVE step is written as **Given** and the WANT step is written as **Find**.

## Model problem

!!! example "Model"

    **A patient weighs 154 lb. The protocol calls for 0.1 mCi per kg. How many MBq should be given?**

    **WANT:** <u>activity in MBq</u>

    **HAVE:** <span class="boxed">154 lb</span>, <span class="boxed">0.1 mCi per kg</span>. Memorized constants: 1 kg \(=\) 2.2 lb and 1 mCi \(=\) 37 MBq.

    **LABEL:** lb, mCi/kg, kg/lb, MBq/mCi

    **SET UP:**

    \[
    154\ \cancel{\text{lb}} \times \dfrac{1\ \bcancel{\text{kg}}}{2.2\ \cancel{\text{lb}}} \times \dfrac{0.1\ \xcancel{\text{mCi}}}{1\ \bcancel{\text{kg}}} \times \dfrac{37\ \text{MBq}}{1\ \xcancel{\text{mCi}}} = \dfrac{154 \times 0.1 \times 37}{2.2}\ \text{MBq} = 259\ \text{MBq}
    \]

    **CHECK:** The unit left over is MBq, which is what we wanted. 154 lb is 70 kg, 70 kg at 0.1 mCi/kg is 7 mCi, and 7 mCi × 37 is 259 MBq (more MBq than mCi, as expected).

    **Answer:** <span class="answer">259 MBq</span>

## Reading the setup line

- Each fraction is a conversion that equals 1, so multiplying by it changes the unit but not the amount.
- The unit you want to remove goes on the opposite side (top or bottom) from where it started. Cross out the matching pair.
- When only the wanted unit is left, you are done. If other units remain, a fraction is probably upside down.

# Constants, Formulas, and Rounding

!!! warning "Memorize these constants"

    1 mCi \(=\) 37 MBq &emsp; 1 kg \(=\) 2.2 lb &emsp; Tc-99m half-life \(=\) 6 h &emsp; 0.693 (\(\lambda = 0.693 \div T_{1/2}\))

    No constants are provided on quizzes and exams, so you need to recall these from memory.

## Formulas used in this guide

**On quizzes and exams you get a formula sheet with formulas only, and no constants.** Your instructor can tell you exactly which formulas are on it. This list shows the formulas used in the topics that follow.

| **Topic** | **Formula** |
| --- | --- |
| Concentration (6) | \(C = \dfrac{A}{V}\), &emsp; \(V = \dfrac{A}{C}\), &emsp; \(A = C \times V\) |
| Weight and BMI (7) | kg \(=\) lb \(\div\) 2.2, &emsp; BMI \(= \dfrac{703 \times \text{lb}}{\text{in}^2}\) |
| Dose rate and time (8) | total dose \(=\) dose rate \(\times\) time, &emsp; time \(=\) dose \(\div\) rate |
| Inverse square law (9) | \(I_1 d_1^2 = I_2 d_2^2\), &emsp; \(I_2 = \dfrac{I_1 d_1^2}{d_2^2}\), &emsp; \(d_2 = \sqrt{\dfrac{I_1 d_1^2}{I_2}}\) |
| Shielding (10) | \(n = \dfrac{\text{thickness}}{\text{HVL}}\), &emsp; rate \(= \dfrac{\text{start}}{2^n}\) |
| Decay by half-lives (11) | \(n = \dfrac{t}{T_{1/2}}\), &emsp; \(A = \dfrac{A_0}{2^n}\) |
| Decay constant and exponential decay (11) | \(\lambda = \dfrac{0.693}{T_{1/2}}\), &emsp; \(A = A_0 e^{-\lambda t}\), &emsp; \(A_0 = \dfrac{A}{e^{-\lambda t}}\) |

## Other relationships used in this guide

1 Ci \(=\) 3.7 × 10<sup>10</sup> Bq; &emsp; 1 Bq \(=\) 1 dps; &emsp; dpm \(=\) dps × 60; &emsp; 1 Gy \(=\) 100 rad; &emsp; 1 Sv \(=\) 100 rem.

## Rounding

- If a problem tells you how to round, do that.
- Do not round in the middle of a problem. Keep the full calculator value until the last step.

# Calculator Check

Calculators differ by brand and model, so the exact keys vary. Check your manual if you cannot find a key. Use these tests at the start of the workshop to confirm that your calculator is entering things correctly.

| **Task** | **What to enter** | **Test it** |
| --- | --- | --- |
| **Enter a power of ten** | Number, then the exponent key (EE, EXP, or ×10<sup>x</sup>), then the exponent. Do not type × 10 first. | 4.5 <kbd>EE</kbd> 5 ÷ 9 \(=\) 50,000 |
| **Enter a negative number or exponent** | Use the negative-sign key, usually (−). It is not the subtraction key. | 5 <kbd>EE</kbd> (−) 3 \(=\) 0.005 |
| **Square a number** | Use the x<sup>2</sup> key on the number itself, before you divide. | 6 <kbd>x<sup>2</sup></kbd> \(=\) 36 |
| **Square root** | Calculate the number under the root first, then press √. | \(\sqrt{16}\) \(=\) 4 |
| **Raise 2 to a power** | Use the y<sup>x</sup> or ^ key. | 2 ^ 5 \(=\) 32 |
| **e to a power** | Use the e<sup>x</sup> key (often the second function of LN). Put the whole exponent in parentheses with its sign. | e<sup>−0.693</sup> \(\approx\) 0.5 |
| **A fraction with a long bottom** | Put the denominator in parentheses, or calculate it first. | 24 ÷ (80 ÷ 5) \(=\) 1.5 |

!!! tip "Three calculator habits"

    1\. Put the whole exponent in parentheses. &emsp; 2. Use the negative-sign key, not subtraction. &emsp; 3. Do a sanity check: does the size and direction of the answer make sense?

!!! tip "Order of operations"

    A calculator follows this order, so type your problem in this order too:

    **1.** Parentheses first. &emsp; **2.** Exponents, squares, and roots next. &emsp; **3.** Multiply and divide, left to right. &emsp; **4.** Add and subtract, left to right.

    **Dividing by more than one number:** 7200 ÷ 60 × 60 gives 7,200, because the calculator divides first and then multiplies. To divide by both, write 7200 ÷ (60 × 60) \(=\) 2.

    **Squares come before multiplying:** 5 × 2<sup>2</sup> \(=\) 5 × 4 \(=\) 20, not \((5 \times 2)^2 = 100\). This is why the distance is squared before it is multiplied or divided by anything else.

# Reading Word Problems

## Words you will see

| **Word** | **What it means** |
| --- | --- |
| **Activity** | How much radioactive material is decaying each second. Units: Ci, mCi, Bq, MBq. |
| **Dose** | Radiation energy absorbed by the body. Units: Gy, rad, Sv, rem. |
| **Dose rate, exposure rate** | How fast radiation is delivered at a location. The unit has “per hour” in it (mrem/h, mR/h). |
| **Concentration** | Activity in each unit of volume, such as mCi/mL. |
| **Unshielded, shielded** | Without a barrier, with a barrier between you and the source. |
| **Half-life** | The time it takes for the activity to fall to half. |
| **Decay, remains** | Activity falls over time. “Remains” asks for the activity left after some time. |

## Turning words into math

| **If the problem says…** | **Think…** |
| --- | --- |
| “per” (mCi per kg, mrem per hour) | A fraction bar: mCi over kg, mrem over h. |
| “equivalent to”, “convert” | A conversion chain of fractions equal to 1. |
| “total”, “after \(t\) hours at that rate” | Rate × time (make the time units match). |
| “how long”, “how much time” | Solve for time. |
| “at what distance” | Inverse square law, solved for the distance (take the square root last). |
| “remains”, “is left after” | The final activity \(A\) (it must be smaller than the start \(A_0\)). |
| “volume to draw” | What you want \(\div\) what you have: \(V = A \div C\). |

## Two marked-up examples

!!! example "Example A"

    **A technologist stands near a source that reads 40 mrem/h for 30 minutes. What dose does the technologist receive?**

    **WANT:** <u>dose in mrem</u>&emsp; **HAVE:** <span class="boxed">40 mrem/h</span>, <span class="boxed">30 min</span>

    \[
    \dfrac{40\ \text{mrem}}{\cancel{\text{h}}} \times 30\ \cancel{\text{min}} \times \dfrac{1\ \cancel{\text{h}}}{60\ \cancel{\text{min}}} = 20\ \text{mrem}
    \]

    **Answer:** <span class="answer">20 mrem</span>

!!! example "Example B"

    **A syringe must contain 12 mCi. The vial concentration is 30 mCi/mL. What volume should be drawn?**

    **WANT:** <u>volume in mL</u>&emsp; **HAVE:** <span class="boxed">12 mCi</span>, <span class="boxed">30 mCi/mL</span>

    \[
    12\ \cancel{\text{mCi}} \times \dfrac{1\ \text{mL}}{30\ \cancel{\text{mCi}}} = 0.4\ \text{mL}
    \]

    **Answer:** <span class="answer">0.4 mL</span>

# Topic 1: Fractions, Unit Cancellation, and Dimensional Analysis

!!! info "Key idea"

    Every unit conversion is a multiplication by a fraction that equals 1. For example, \(\dfrac{\text{37 MBq}}{\text{1 mCi}}\) \(= 1\), because 37 MBq and 1 mCi are the same amount of activity.

    Write the fraction so the unit you want to get rid of sits on the opposite side (top or bottom) from where it started. It then cancels, and the unit you want is left.

## Worked examples

!!! example "Ex 1.1"

    **Convert 6 mCi to MBq.**

    **Given:** 6 mCi. &emsp; **Find:** activity in MBq, using 1 mCi \(=\) 37 MBq.

    \[
    6\ \cancel{\text{mCi}} \times \dfrac{37\ \text{MBq}}{1\ \cancel{\text{mCi}}} = 222\ \text{MBq}
    \]

    **Answer:** <span class="answer">222 MBq</span>

    *Why: mCi is on top in the starting amount, so it goes on the bottom of the fraction and cancels.*

!!! example "Ex 1.2"

    **Convert 7,200 seconds to hours.**

    **Given:** 7,200 s. &emsp; **Find:** time in h, using 1 min \(=\) 60 s and 1 h \(=\) 60 min.

    \[
    7{,}200\ \cancel{\text{s}} \times \dfrac{1\ \bcancel{\text{min}}}{60\ \cancel{\text{s}}} \times \dfrac{1\ \text{h}}{60\ \bcancel{\text{min}}} = \dfrac{7{,}200}{3{,}600}\ \text{h} = 2\ \text{h}
    \]

    **Answer:** <span class="answer">2 h</span>

    *Why: Chain the fractions. Seconds cancel with seconds (the / mark), then minutes cancel with minutes (the \\ mark).*

!!! example "Ex 1.3"

    **Convert 209 lb to kg.**

    **Given:** 209 lb. &emsp; **Find:** mass in kg, using 1 kg \(=\) 2.2 lb.

    \[
    209\ \cancel{\text{lb}} \times \dfrac{1\ \text{kg}}{2.2\ \cancel{\text{lb}}} = \dfrac{209}{2.2}\ \text{kg} = 95\ \text{kg}
    \]

    **Answer:** <span class="answer">95 kg</span>

    *Why: lb is on top in the starting value, so it goes on the bottom of the fraction and cancels.*

## Try these

*Work each problem on paper with the setup-line method, then click **Show answer** to check your work.*

!!! question "Try 1.1"

    **Convert 45 minutes to hours.**

    ??? success "Show answer"

        \[
        45\ \cancel{\text{min}} \times \dfrac{1\ \text{h}}{60\ \cancel{\text{min}}} = 0.75\ \text{h}
        \]

        **Answer:** <span class="answer">0.75 h</span>

!!! question "Try 1.2"

    **Convert 5,400 seconds to hours.**

    ??? success "Show answer"

        \[
        5{,}400\ \cancel{\text{s}} \times \dfrac{1\ \bcancel{\text{min}}}{60\ \cancel{\text{s}}} \times \dfrac{1\ \text{h}}{60\ \bcancel{\text{min}}} = 1.5\ \text{h}
        \]

        **Answer:** <span class="answer">1.5 h</span>

## Calculator tips

- For a chain, you can multiply each fraction in turn. In Ex 1.2, type 7200 × (1/60) × (1/60) to get 2.
- You can also treat the chain as one fraction: multiply all the top numbers, multiply all the bottom numbers, then divide the top by the bottom. Use parentheses around the bottom when it has more than one number. In Ex 1.2, type 7200 ÷ (60 × 60) to get 2.

## Common mistakes and pitfalls

- **Fraction upside down.** If the units do not cancel, flip the fraction.
- **Dropping the unit.** Always label your answer with its unit.
- **Skipping the direction check.** Smaller units mean a larger number (hours to seconds gets bigger).

# Topic 2: Scientific Notation and Powers of Ten

!!! info "Key idea"

    Scientific notation writes a number as one digit, a decimal, and a power of ten, such as 4.53 × 10<sup>5</sup>. When you write a number this way, moving the decimal left makes the exponent positive; moving it right makes it negative.

    To multiply, multiply the numbers and add the exponents. To divide, divide the numbers and subtract the exponents.

    **Fixing the number in front.** After calculating, check that the number in front is between 1 and 10. If it is not, move its decimal and adjust the exponent to match. Each place you move the decimal **left** makes the number in front 10 times smaller, so **add 1** to the exponent. Each place you move the decimal **right** makes the number in front 10 times larger, so **subtract 1** from the exponent.

    **Examples.** One place: 15 × 10<sup>4</sup> becomes 1.5 × 10<sup>5</sup>. The decimal moved 1 place left, so the exponent went up by 1.

    Two places: 251 × 10<sup>3</sup> becomes 2.51 × 10<sup>5</sup>. The decimal moved 2 places left, so the exponent went up by 2. In the other direction, 0.045 × 10<sup>\(-\)2</sup> becomes 4.5 × 10<sup>\(-\)4</sup>. The decimal moved 2 places right, so the exponent went down by 2.

## Worked examples

!!! example "Ex 2.1"

    **Write 3,400,000 in scientific notation.**

    **Given:** 3,400,000. &emsp; **Find:** the number in scientific notation.

    3,400,000 \(=\) \(3.4\times 10^{6}\)

    **Answer:** <span class="answer">\(3.4\times 10^{6}\)</span>

    *Why: The decimal moved 6 places to the left, so the exponent is +6.*

!!! example "Ex 2.2"

    **Write 0.00563 in scientific notation.**

    **Given:** 0.00563. &emsp; **Find:** the number in scientific notation.

    0\.00563 \(=\) \(5.63\times 10^{-3}\)

    **Answer:** <span class="answer">\(5.63\times 10^{-3}\)</span>

    *Why: The decimal moved 3 places to the right, so the exponent is \(-3\).*

!!! example "Ex 2.3"

    **A source gives \(2.5\times 10^{4}\) counts per minute. How many counts in 6 minutes?**

    **Given:** a rate of \(2.5\times 10^{4}\) counts per minute, and a time of 6 min. &emsp; **Find:** total counts.

    \[
    \dfrac{2.5\times 10^{4}\text{ counts}}{\text{1 }\cancel{\text{min}}}\ \times \text{ 6 }\cancel{\text{min}}\ =\ 15\times 10^{4}\text{ counts }=\ 1.5\times 10^{5}\text{ counts}
    \]

    **Answer:** <span class="answer">\(1.5\times 10^{5}\) counts</span>

    *Why: 15 is not between 1 and 10, so move the decimal one place left and add 1 to the exponent.*

!!! example "Ex 2.4"

    **Divide \(9.0\times 10^{8}\) counts by \(3.0\times 10^{3}\) minutes.**

    **Given:** \(9.0\times 10^{8}\) counts and \(3.0\times 10^{3}\) min. &emsp; **Find:** the rate in counts/min.

    \[
    \dfrac{9.0\times 10^{8}\text{ counts}}{3.0\times 10^{3}\text{ min}}\ =\ 3.0\times 10^{5}\text{ counts/min}
    \]

    **Answer:** <span class="answer">\(3.0\times 10^{5}\) counts/min</span>

    *Why: 9.0 ÷ 3.0 \(=\) 3.0, and 8 \(-\) 3 \(=\) 5.*

## Try these

*Work each problem on paper with the setup-line method, then click **Show answer** to check your work.*

!!! question "Try 2.1"

    **Write 0.0724 in scientific notation.**

    ??? success "Show answer"

        0\.0724 \(=\) \(7.24\times 10^{-2}\)

        **Answer:** <span class="answer">\(7.24\times 10^{-2}\)</span>

!!! question "Try 2.2"

    **Write \(6.2\times 10^{-3}\) as a decimal.**

    ??? success "Show answer"

        \(6.2\times 10^{-3}\) \(=\) 0.0062

        **Answer:** <span class="answer">0.0062</span>

!!! question "Try 2.3"

    **A well counter records \(1.2\times 10^{6}\) counts in 5 minutes. What is the counting rate?**

    ??? success "Show answer"

        \[
        \dfrac{1.2\times 10^{6}\text{ counts}}{\text{5 min}}\ =\ 0.24\times 10^{6}\ =\ 2.4\times 10^{5}\text{ counts/min}
        \]

        The decimal moved 1 place right, so the exponent went down by 1.

        **Answer:** <span class="answer">\(2.4\times 10^{5}\) counts/min</span>

## Calculator tips

- Use the exponent key (EE, EXP, or ×10<sup>x</sup>, depending on the brand) to enter powers of ten.
- Use the negative-sign key, usually (−), for negative exponents. It is not the subtraction key.
- Test it: 4.5 <kbd>EE</kbd> 5 ÷ 9 should give 50,000.

## Common mistakes and pitfalls

- **Wrong direction.** Large numbers have positive exponents; small decimals have negative exponents.
- **Forgetting to renormalize.** 15 × 10<sup>4</sup> should be written as 1.5 × 10<sup>5</sup>.
- **Adding exponents when dividing.** Dividing means subtracting the exponents.
- **Dropping the negative sign** on a negative exponent.

# Topic 3: Metric Prefixes

!!! info "Key idea"

    The prefixes you need most are giga (G, 10<sup>9</sup>), mega (M, 10<sup>6</sup>), kilo (k, 10<sup>3</sup>), milli (m, 10<sup>\(-\)3</sup>), and micro (\(\mu\), 10<sup>\(-\)6</sup>).

    Smaller units mean a larger number. Think of 1 yard = 3 feet = 36 inches: going to smaller units makes the number bigger.

    You can solve every prefix conversion three ways, and all three give the same answer:

    **Method 1: Conversion factor.** Multiply by a fraction that equals 1 and cancel the units.

    **Method 2: Move the decimal.** Each step on the prefix ladder below is 3 places. Use it to check your Method 1 answer.

    **Method 3: Adjust the exponent.** Each prefix is a power of ten, and a unit with no prefix (Ci, Bq, Gy) is 10<sup>0</sup>. Subtract the exponent of the unit you want from the exponent of the unit you start with, then multiply the number by 10 to that power: **old exponent \(-\) new exponent**. This is the same exponent rule from Topic 2. If you want scientific notation, fix the number in front as shown there.

## Prefix conversions (neighboring prefixes)

| **Conversion** | **Fraction form** |
| --- | --- |
| 1 G (giga) \(=\) 1,000 M (mega) | \(\dfrac{1{,}000\ \text{M}}{1\ \text{G}}\)  or  \(\dfrac{1\ \text{G}}{1{,}000\ \text{M}}\) |
| 1 M (mega) \(=\) 1,000 k (kilo) | \(\dfrac{1{,}000\ \text{k}}{1\ \text{M}}\)  or  \(\dfrac{1\ \text{M}}{1{,}000\ \text{k}}\) |
| 1 k (kilo) \(=\) 1,000 base units | \(\dfrac{1{,}000\ \text{base}}{1\ \text{k}}\)  or  \(\dfrac{1\ \text{k}}{1{,}000\ \text{base}}\) |
| 1 base unit \(=\) 1,000 m (milli) | \(\dfrac{1{,}000\ \text{m}}{1\ \text{base}}\)  or  \(\dfrac{1\ \text{base}}{1{,}000\ \text{m}}\) |
| 1 m (milli) \(=\) 1,000 \(\mu\) (micro) | \(\dfrac{1{,}000\ \mu}{1\ \text{m}}\)  or  \(\dfrac{1\ \text{m}}{1{,}000\ \mu}\) |

<small>Examples: 1 GBq \(=\) 1,000 MBq,  1 MBq \(=\) 1,000 kBq,  1 Ci \(=\) 1,000 mCi,  1 mCi \(=\) 1,000 µCi. To skip a prefix, chain two fractions (for example, G to k is \(1{,}000 \times 1{,}000 = 1{,}000{,}000\)).</small>

## The prefix ladder (3 decimal places per step)

| **G** | ↔ | **M** | ↔ | **k** | ↔ | **(base)** | ↔ | **m** | ↔ | **µ** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| giga | | mega | | kilo | | Ci, Bq, Gy | | milli | | micro |

- **Moving right** on the ladder (to a smaller unit): the number gets bigger, so move the decimal **right** 3 places per step.
- **Moving left** on the ladder (to a larger unit): the number gets smaller, so move the decimal **left** 3 places per step.
- Add zeros as placeholders when you run out of digits.

## Worked examples (all three methods)

!!! example "Ex 3.1"

    **Convert 750 µCi to mCi.**

    **Given:** 750 µCi. &emsp; **Find:** activity in mCi.

    **Method 1: Conversion factor**

    \[
    750\ \cancel{\text{µCi}} \times \dfrac{1\ \text{mCi}}{1{,}000\ \cancel{\text{µCi}}} = \dfrac{750}{1{,}000}\ \text{mCi} = 0.75\ \text{mCi}
    \]

    **Method 2: Move the decimal**

    µCi \(\rightarrow\) mCi is 1 step to the **left** (larger unit), so move the decimal 3 places left: 750. \(\rightarrow\) 0.750 \(=\) 0.75

    **Method 3: Adjust the exponent**

    µCi has exponent \(-6\) and mCi has exponent \(-3\). Old \(-\) new \(= -6 - (-3) = -3\), so \(750 \times 10^{-3} = 0.75\)

    **Answer:** <span class="answer">0.75 mCi</span>

    *Why: mCi is a larger unit than µCi, so the number gets smaller.*

!!! example "Ex 3.2"

    **Convert 0.4 Ci to mCi.**

    **Given:** 0.4 Ci. &emsp; **Find:** activity in mCi.

    **Method 1: Conversion factor**

    \[
    0.4\ \cancel{\text{Ci}} \times \dfrac{1{,}000\ \text{mCi}}{1\ \cancel{\text{Ci}}} = 400\ \text{mCi}
    \]

    **Method 2: Move the decimal**

    Ci \(\rightarrow\) mCi is 1 step to the **right** (smaller unit), so move the decimal 3 places right: 0.400 \(\rightarrow\) 400.

    **Method 3: Adjust the exponent**

    Ci has no prefix, so its exponent is 0, and mCi has exponent \(-3\). Old \(-\) new \(= 0 - (-3) = 3\), so \(0.4 \times 10^{3} = 400\)

    **Answer:** <span class="answer">400 mCi</span>

    *Why: mCi is a smaller unit than Ci, so the number gets larger.*

!!! example "Ex 3.3"

    **Convert 2,500 MBq to GBq.**

    **Given:** 2,500 MBq. &emsp; **Find:** activity in GBq.

    **Method 1: Conversion factor**

    \[
    2{,}500\ \cancel{\text{MBq}} \times \dfrac{1\ \text{GBq}}{1{,}000\ \cancel{\text{MBq}}} = \dfrac{2{,}500}{1{,}000}\ \text{GBq} = 2.5\ \text{GBq}
    \]

    **Method 2: Move the decimal**

    MBq \(\rightarrow\) GBq is 1 step to the **left**, so move the decimal 3 places left: 2,500. \(\rightarrow\) 2.500 \(=\) 2.5

    **Method 3: Adjust the exponent**

    MBq has exponent 6 and GBq has exponent 9. Old \(-\) new \(= 6 - 9 = -3\), so \(2{,}500 \times 10^{-3} = 2.5\)

    **Answer:** <span class="answer">2.5 GBq</span>

    *Why: GBq is a larger unit than MBq, so the number gets smaller.*

!!! example "Ex 3.4"

    **Convert 0.0005 Ci to µCi. (Two steps on the ladder.)**

    **Given:** 0.0005 Ci. &emsp; **Find:** activity in µCi.

    **Method 1: Conversion factor**

    \[
    0.0005\ \cancel{\text{Ci}} \times \dfrac{1{,}000\ \bcancel{\text{mCi}}}{1\ \cancel{\text{Ci}}} \times \dfrac{1{,}000\ \text{µCi}}{1\ \bcancel{\text{mCi}}} = 500\ \text{µCi}
    \]

    **Method 2: Move the decimal**

    Ci \(\rightarrow\) mCi \(\rightarrow\) µCi is 2 steps to the **right**, so move the decimal \(2 \times 3 = 6\) places right: 0.000500 \(\rightarrow\) 500.

    **Method 3: Adjust the exponent**

    Ci has exponent 0 and µCi has exponent \(-6\). Old \(-\) new \(= 0 - (-6) = 6\), so \(0.0005 \times 10^{6} = 500\)

    **Answer:** <span class="answer">500 µCi</span>

    *Why: Chain the fractions: Ci cancels with Ci, then mCi cancels with mCi. Two steps means 6 decimal places.*

## Try these

*Work each problem on paper with the setup-line method, then click **Show answer** to check your work.*

!!! question "Try 3.1"

    **Convert 0.06 mCi to µCi.**

    ??? success "Show answer"

        - Method 1: \(0.06\ \cancel{\text{mCi}} \times \dfrac{1{,}000\ \text{µCi}}{1\ \cancel{\text{mCi}}} = 60\ \text{µCi}\).
        - Method 2: 1 step right, move 3 places right: 0.060 \(\rightarrow\) 60.
        - Method 3: mCi is \(-3\) and µCi is \(-6\), so \(-3 - (-6) = 3\) and \(0.06 \times 10^{3} = 60\).

        **Answer:** <span class="answer">60 µCi</span>

!!! question "Try 3.2"

    **Convert 3,200 kBq to GBq.**

    ??? success "Show answer"

        - Method 1: \(3{,}200\ \cancel{\text{kBq}} \times \dfrac{1\ \bcancel{\text{MBq}}}{1{,}000\ \cancel{\text{kBq}}} \times \dfrac{1\ \text{GBq}}{1{,}000\ \bcancel{\text{MBq}}} = 0.0032\ \text{GBq}\).
        - Method 2: kBq \(\rightarrow\) MBq \(\rightarrow\) GBq is 2 steps left, so move the decimal \(2 \times 3 = 6\) places left: 3,200. \(\rightarrow\) 0.003200.
        - Method 3: kBq is 3 and GBq is 9, so \(3 - 9 = -6\) and \(3{,}200 \times 10^{-6} = 0.0032\).

        **Answer:** <span class="answer">0.0032 GBq</span>

!!! question "Try 3.3"

    **Convert 0.045 Ci to µCi.**

    ??? success "Show answer"

        - Method 1: \(0.045\ \cancel{\text{Ci}} \times \dfrac{1{,}000\ \bcancel{\text{mCi}}}{1\ \cancel{\text{Ci}}} \times \dfrac{1{,}000\ \text{µCi}}{1\ \bcancel{\text{mCi}}} = 45{,}000\ \text{µCi}\).
        - Method 2: Ci \(\rightarrow\) mCi \(\rightarrow\) µCi is 2 steps right, so move the decimal \(2 \times 3 = 6\) places right: 0.045000 \(\rightarrow\) 45,000.
        - Method 3: Ci is 0 and µCi is \(-6\), so \(0 - (-6) = 6\) and \(0.045 \times 10^{6} = 45{,}000\).

        **Answer:** <span class="answer">45,000 µCi</span>

## Common mistakes and pitfalls

- **Mixing up m and M.** Milli (m) and mega (M) differ by a factor of one billion.
- **Misreading \(\mu\) as m.** When writing by hand, write out “microcuries” instead of µCi, and use “mcg” for micrograms.
- **Moving the decimal the wrong way.** Do the direction check: smaller unit, bigger number.
- **Moving the wrong number of places.** One step on the ladder is 3 places, two steps is 6. Count the steps first.
- **Subtracting the exponents backward (Method 3).** Always do old exponent minus new exponent, then run the direction check: a smaller unit must give a bigger number.

# Topic 4: Activity Units (Ci, Bq, dpm)

!!! info "Key idea"

    Memorize 1 mCi = 37 MBq. Also: 1 Ci = 3.7 × 10<sup>10</sup> Bq, 1 Bq = 1 disintegration per second (dps), and dpm = dps × 60.

    Direction check: you always have more MBq than mCi, and more dpm than dps.

## Worked examples

!!! example "Ex 4.1"

    **Convert 150 dps to dpm.**

    **Given:** 150 dps. &emsp; **Find:** activity in dpm, using dpm \(=\) dps × 60.

    \[
    \dfrac{150\ \text{dis}}{1\ \cancel{\text{s}}} \times \dfrac{60\ \cancel{\text{s}}}{1\ \text{min}} = 9{,}000\ \text{dis/min}
    \]

    **Answer:** <span class="answer">9,000 dpm</span>

!!! example "Ex 4.2"

    **3.7 × 10<sup>10</sup> becquerels are equivalent to how many curies? Round your answer to 2 decimal places as needed.**

    **Given:** \(3.7\times 10^{10}\) Bq. &emsp; **Find:** activity in Ci, using 1 mCi \(=\) 37 MBq and the prefix steps.

    \[
    3.7 \times  10^{10}\ \cancel{\text{Bq}} \times \dfrac{1\ \bcancel{\text{kBq}}}{1{,}000\ \cancel{\text{Bq}}} \times \dfrac{1\ \bcancel{\text{MBq}}}{1{,}000\ \bcancel{\text{kBq}}} \times \dfrac{1\ \cancel{\text{mCi}}}{37\ \bcancel{\text{MBq}}} \times \dfrac{1\ \text{Ci}}{1{,}000\ \cancel{\text{mCi}}} = 1.00\ \text{Ci}
    \]

    **Answer:** <span class="answer">1.00 Ci</span>

    *Why: Go from Bq to kBq first, next from kBq to MBq, next from MBq to mCi, and then from mCi to Ci.*

## Try these

*Work each problem on paper with the setup-line method, then click **Show answer** to check your work.*

!!! question "Try 4.1"

    **Convert 127 mCi to GBq. Round your answer to 2 decimal places as needed.**

    ??? success "Show answer"

        \[
        127\ \cancel{\text{mCi}} \times \dfrac{37\ \bcancel{\text{MBq}}}{1\ \cancel{\text{mCi}}} \times \dfrac{1\ \text{GBq}}{1{,}000\ \bcancel{\text{MBq}}} = 4.699\ \text{GBq} = 4.70\ \text{GBq}
        \]

        **Answer:** <span class="answer">4.70 GBq</span>

!!! question "Try 4.2"

    **Convert 250 kBq to µCi. Round your answer to 2 decimal places as needed.**

    ??? success "Show answer"

        \[
        250\ \cancel{\text{kBq}} \times \dfrac{1\ \bcancel{\text{MBq}}}{1{,}000\ \cancel{\text{kBq}}} \times \dfrac{1\ \cancel{\text{mCi}}}{37\ \bcancel{\text{MBq}}} \times \dfrac{1{,}000\ \text{µCi}}{1\ \bcancel{\text{mCi}}} = 6.757\ \text{µCi} = 6.76\ \text{µCi}
        \]

        **Answer:** <span class="answer">6.76 µCi</span>

!!! question "Try 4.3"

    **Convert 75 dps to dpm.**

    ??? success "Show answer"

        \[
        \dfrac{75\ \text{dis}}{1\ \cancel{\text{s}}} \times \dfrac{60\ \cancel{\text{s}}}{1\ \text{min}} = 4{,}500\ \text{dis/min}
        \]

        **Answer:** <span class="answer">4,500 dpm</span>

## Calculator tips

- In Ex 4.2, type 3.7 <kbd>EE</kbd> 10 × (1/1000) × (1/1000) × (1/37) × (1/1000) to get 1.00.
- Enter 3.7 × 10<sup>10</sup> with the exponent key (3.7 <kbd>EE</kbd> 10). Do not type × 10 ^ 10 before or instead of the EE key.

## Common mistakes and pitfalls

- **Using 37 the wrong way.** If your MBq number is smaller than your mCi number, you divided when you should have multiplied.
- **Mixing m and M** (mCi vs MBq prefixes).
- **Forgetting ×60** when going from dps to dpm.

# Topic 5: Dose Units (Gy, rad, Sv, rem)

!!! info "Key idea"

    1 Gy = 100 rad and 1 Sv = 100 rem. The SI units (Gy, Sv) are the larger units, so you always have fewer Gy than rad and fewer Sv than rem.

    Prefixes carry over: 1 mGy = 100 mrad and 1 mSv = 100 mrem.

    Gy and Sv measure different things. The gray (Gy) measures absorbed dose, the energy deposited in tissue. The sievert (Sv) measures dose equivalent, which also accounts for the biological effect of the type of radiation. The rad and rem are the older units for the same two quantities.

## Worked examples

!!! example "Ex 5.1"

    **8 rad is equivalent to how many Gy?**

    **Given:** 8 rad. &emsp; **Find:** dose in Gy, using 1 Gy \(=\) 100 rad.

    \[
    8\ \cancel{\text{rad}} \times \dfrac{1\ \text{Gy}}{100\ \cancel{\text{rad}}} = \dfrac{8}{100}\ \text{Gy} = 0.08\ \text{Gy}
    \]

    **Answer:** <span class="answer">0.08 Gy</span>

!!! example "Ex 5.2"

    **Convert 0.25 Gy to rad.**

    **Given:** 0.25 Gy. &emsp; **Find:** dose in rad, using 1 Gy \(=\) 100 rad.

    \[
    0.25\ \cancel{\text{Gy}} \times \dfrac{100\ \text{rad}}{1\ \cancel{\text{Gy}}} = 25\ \text{rad}
    \]

    **Answer:** <span class="answer">25 rad</span>

!!! example "Ex 5.3"

    **12 mrem is equivalent to how many mSv?**

    **Given:** 12 mrem. &emsp; **Find:** dose in mSv, using 1 Sv \(=\) 100 rem.

    \[
    12\ \cancel{\text{mrem}} \times \dfrac{1\ \bcancel{\text{rem}}}{1{,}000\ \cancel{\text{mrem}}} \times \dfrac{1\ \cancel{\text{Sv}}}{100\ \bcancel{\text{rem}}} \times \dfrac{1{,}000\ \text{mSv}}{1\ \cancel{\text{Sv}}} = \dfrac{12{,}000}{100{,}000}\ \text{mSv} = 0.12\ \text{mSv}
    \]

    **Answer:** <span class="answer">0.12 mSv</span>

## Try these

*Work each problem on paper with the setup-line method, then click **Show answer** to check your work.*

!!! question "Try 5.1"

    **Convert 20 rad to Gy.**

    ??? success "Show answer"

        \[
        20\ \cancel{\text{rad}} \times \dfrac{1\ \text{Gy}}{100\ \cancel{\text{rad}}} = 0.2\ \text{Gy}
        \]

        **Answer:** <span class="answer">0.2 Gy</span>

!!! question "Try 5.2"

    **Convert 0.05 Sv to rem.**

    ??? success "Show answer"

        \[
        0.05\ \cancel{\text{Sv}} \times \dfrac{100\ \text{rem}}{1\ \cancel{\text{Sv}}} = 5\ \text{rem}
        \]

        **Answer:** <span class="answer">5 rem</span>

## Common mistakes and pitfalls

- **Wrong direction.** The Gy or Sv number must be smaller than the rad or rem number.
- **Mixing prefixes** (for example, converting mGy with a fraction that uses Gy).
- **Treating Gy and Sv as interchangeable.** They measure different things, so convert Gy to rad and Sv to rem separately.

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

# Topic 7: Weight and BMI

!!! info "Key idea"

    kg = lb ÷ 2.2 (memorize 1 kg = 2.2 lb). To go from kg to lb, multiply by 2.2.

    BMI = 703 × lb ÷ in<sup>2</sup>. Height must be in inches, and you square the inches. 5 ft 6 in = 66 in.

    The 703 is a built-in conversion factor from lb/in<sup>2</sup> to kg/m<sup>2</sup>, so the units in a BMI setup do not cancel the way they do in other problems. The BMI answer is labeled kg/m<sup>2</sup>.

    Direction check: the kg number should be about half the lb number.

## Worked examples

!!! example "Ex 7.1"

    **Convert 132 lb to kg.**

    **Given:** 132 lb. &emsp; **Find:** mass in kg, using kg \(=\) lb ÷ 2.2.

    \[
    132\ \cancel{\text{lb}} \times \dfrac{1\ \text{kg}}{2.2\ \cancel{\text{lb}}} = 60\ \text{kg}
    \]

    **Answer:** <span class="answer">60 kg</span>

!!! example "Ex 7.2"

    **A patient is 5 ft 6 in tall and weighs 150 lb. Find the BMI.**

    **Given:** height 5 ft 6 in, weight 150 lb. &emsp; **Find:** BMI (in kg/m<sup>2</sup>), using BMI \(=\) 703 × lb ÷ in<sup>2</sup>.

    Height: \(5\ \cancel{\text{ft}} \times \dfrac{12\ \text{in}}{1\ \cancel{\text{ft}}} + 6\ \text{in} = 66\ \text{in}\)

    \[
    \text{BMI} = \dfrac{703 \times 150\ \text{lb}}{(66\ \text{in})^2} = \dfrac{105{,}450}{4{,}356} = 24.2\ \text{kg/m}^2
    \]

    **Answer:** <span class="answer">24.2 kg/m<sup>2</sup></span>

    *Why: Convert feet to inches first, then square the inches.*

!!! example "Ex 7.3"

    **A patient weighs 132 lb. The dose is 0.1 mCi per kg. What dose should be given?**

    **Given:** weight 132 lb, dose 0.1 mCi per kg. &emsp; **Find:** dose in mCi.

    \[
    132\ \cancel{\text{lb}} \times \dfrac{1\ \text{kg}}{2.2\ \cancel{\text{lb}}} = 60\ \text{kg}
    \]

    \[
    60\ \cancel{\text{kg}} \times \dfrac{0.1\ \text{mCi}}{1\ \cancel{\text{kg}}} = 6.0\ \text{mCi}
    \]

    **Answer:** <span class="answer">6.0 mCi</span>

    *Why: Convert weight to kg first, because the dose is per kilogram.*

## Try these

*Work each problem on paper with the setup-line method, then click **Show answer** to check your work.*

!!! question "Try 7.1"

    **Convert 75 kg to lb.**

    ??? success "Show answer"

        \[
        75\ \cancel{\text{kg}} \times \dfrac{2.2\ \text{lb}}{1\ \cancel{\text{kg}}} = 165\ \text{lb}
        \]

        **Answer:** <span class="answer">165 lb</span>

!!! question "Try 7.2"

    **A patient is 70 inches tall and weighs 180 lb. Find the BMI. Round your answer to 1 decimal place as needed.**

    ??? success "Show answer"

        \[
        \text{BMI} = \dfrac{703 \times 180\ \text{lb}}{(70\ \text{in})^2} = \dfrac{126{,}540}{4{,}900} = 25.8\ \text{kg/m}^2
        \]

        **Answer:** <span class="answer">25.8 kg/m<sup>2</sup></span>

## Common mistakes and pitfalls

- **Using feet instead of inches** for height.
- **Dropping the 703.**
- **Squaring the wrong thing.** Only the height is squared, not the weight or the 703.
- **Skipping the direction check.** If your kg answer is bigger than your lb answer, you multiplied when you should have divided.

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

# Topic 10: Shielding (Half-Value Layers)

!!! info "Key idea"

    Each half-value layer (HVL) cuts the exposure rate in half. Number of HVLs = thickness ÷ HVL.

    Then halve the starting rate that many times: rate = start ÷ 2<sup>n</sup>, where \(n\) is the number of HVLs.

## Worked examples

!!! example "Ex 10.1"

    **An unshielded source reads 960 mR/h. What is the reading behind 2 HVLs?**

    **Given:** start \(= 960\) mR/h and \(n = 2\) HVL. &emsp; **Find:** the reading behind the shield.

    Each HVL cuts the exposure rate in half, so 2 HVLs means halving 2 times:

    \[
    \text{1 HVL: }\dfrac{\text{960 mR/h}}{\text{2}}\ =\text{ 480 mR/h}
    \]

    \[
    \text{2 HVL: }\dfrac{\text{480 mR/h}}{\text{2}}\ =\text{ 240 mR/h}
    \]

    **Answer:** <span class="answer">240 mR/h</span>

    *Why: Halving 2 times is the same as dividing the starting rate by \(2^n\), where \(n = 2\): \(2^2 = 2 \times 2 = 4\), and \(\dfrac{960\ \text{mR/h}}{4} = 240\) mR/h. The reading behind the shield is smaller than the starting rate, as it should be.*

!!! example "Ex 10.2"

    **A source reads 1,600 mR/h unshielded. A lead shield is 2.4 mm thick and the HVL of lead for this source is 0.6 mm. What is the reading behind the shield?**

    **Given:** start \(= 1{,}600\) mR/h, thickness \(= 2.4\) mm, and HVL \(= 0.6\) mm. &emsp; **Find:** the reading behind the shield.

    **Step 1: Find the number of HVLs.** Number of HVLs = thickness \(\div\) HVL:

    \[
    n = \dfrac{\text{thickness}}{\text{HVL}} = 2.4\ \cancel{\text{mm}} \times \dfrac{1\ \text{HVL}}{0.6\ \cancel{\text{mm}}} = 4\ \text{HVL}
    \]

    **Step 2: Halve the starting rate that many times.** Each HVL cuts the rate in half, so 4 HVLs means halving 4 times:

    \[
    \text{1 HVL: }\dfrac{\text{1,600 mR/h}}{\text{2}}\ =\text{ 800 mR/h}
    \]

    \[
    \text{2 HVL: }\dfrac{\text{800 mR/h}}{\text{2}}\ =\text{ 400 mR/h}
    \]

    \[
    \text{3 HVL: }\dfrac{\text{400 mR/h}}{\text{2}}\ =\text{ 200 mR/h}
    \]

    \[
    \text{4 HVL: }\dfrac{\text{200 mR/h}}{\text{2}}\ =\text{ 100 mR/h}
    \]

    **Answer:** <span class="answer">100 mR/h</span>

    *Why: The mm cancel in Step 1, leaving a plain number of HVLs. Halving 4 times is the same as dividing the starting rate by \(2^4\): \(2^4 = 2 \times 2 \times 2 \times 2 = 16\), and \(\dfrac{1{,}600\ \text{mR/h}}{16} = 100\) mR/h. The reading behind the shield is smaller than the starting rate, as it should be.*

!!! example "Ex 10.3"

    **If the HVL for some radionuclide in lead is 0.30 mm, what thickness of lead shielding is necessary to reduce the radiation exposure from 8 mR/h to 1 mR/h?**

    **Given:** HVL \(= 0.30\) mm, start \(= 8\) mR/h, and final \(= 1\) mR/h. &emsp; **Find:** thickness.

    This problem has two parts. The rates tell us how many HVLs are needed, and the HVL tells us how thick each one is.

    **Step 1: Find the number of HVLs.** Here the rates are given, not the thickness. Start with the shielding formula:

    \[
    \text{rate} = \dfrac{\text{start}}{2^n}
    \]

    To get \(2^n\) out of the denominator, multiply both sides by \(2^n\), then divide both sides by the rate. This gives \(2^n = \dfrac{\text{start}}{\text{rate}}\). Then ask how many 2s multiply to make that number:

    \[
    2^n = \dfrac{8\ \text{mR/h}}{1\ \text{mR/h}} = 8
    \]

    \(2 \times 2 \times 2 = 8\), so \(2^3 = 8\) and \(n = 3\) HVL

    **Step 2: Rearrange the HVL formula to solve for thickness.** The number of HVLs is:

    \[
    n = \dfrac{\text{thickness}}{\text{HVL}}
    \]

    Multiply both sides by the HVL to get thickness alone:

    \[
    \text{thickness} = n \times \text{HVL}
    \]

    **Step 3: Plug in and cancel units.** Each HVL is 0.30 mm of lead, so 3 HVLs is three of those layers:

    \[
    \text{thickness} = 3\ \cancel{\text{HVL}} \times \dfrac{0.30\ \text{mm}}{1\ \cancel{\text{HVL}}} = 0.90\ \text{mm}
    \]

    **Answer:** <span class="answer">0.90 mm</span>

    *Why: The HVL is given in mm, so the thickness comes out in mm. Check by halving: 8 \(\rightarrow\) 4 \(\rightarrow\) 2 \(\rightarrow\) 1 is 3 halvings, and each halving takes one 0.30 mm layer. The answer (0.90 mm) is thicker than one HVL, which makes sense because the rate must drop by more than half. When solving for thickness, multiply \(n \times\) HVL. Do not divide.*

## Try these

*Work each problem on paper with the setup-line method, then click **Show answer** to check your work.*

!!! question "Try 10.1"

    **A source reads 1,200 mR/h unshielded. What is the reading behind 4 HVLs?**

    ??? success "Show answer"

        \[
        \dfrac{1{,}200\ \text{mR/h}}{2^4} = \dfrac{1{,}200\ \text{mR/h}}{16} = 75\ \text{mR/h}
        \]

        **Answer:** <span class="answer">75 mR/h</span>

!!! question "Try 10.2"

    **A source reads 2,560 mR/h. The shield is 1.0 mm of lead and 1 HVL = 0.2 mm. What is the reading with the shield?**

    ??? success "Show answer"

        \[
        1.0\ \cancel{\text{mm}} \times \dfrac{1\ \text{HVL}}{0.2\ \cancel{\text{mm}}} = 5\ \text{HVL}
        \]

        \[
        \dfrac{2{,}560\ \text{mR/h}}{2^5} = \dfrac{2{,}560\ \text{mR/h}}{32} = 80\ \text{mR/h}
        \]

        **Answer:** <span class="answer">80 mR/h</span>

!!! question "Try 10.3"

    **A source reads 4,800 mR/h unshielded. A lead shield is 8 mm thick and the HVL of lead for this source is 2 mm. What is the reading behind the shield?**

    ??? success "Show answer"

        \[
        n = 8\ \cancel{\text{mm}} \times \dfrac{1\ \text{HVL}}{2\ \cancel{\text{mm}}} = 4\ \text{HVL}
        \]

        \[
        4{,}800 \rightarrow 2{,}400 \rightarrow 1{,}200 \rightarrow 600 \rightarrow 300\ \text{mR/h}
        \]

        **Answer:** <span class="answer">300 mR/h</span>

## Calculator tips

- Use the y<sup>x</sup> or ^ key for 2<sup>n</sup>: 2 ^ 5 \(=\) 32.
- Or halve repeatedly: enter the starting number and press ÷ 2 \(=\), then repeat \(n\) times (the Ans key helps).

## Common mistakes and pitfalls

- **Using thickness instead of the number of HVLs.** Convert thickness to HVLs first.
- **Dividing by n instead of 2<sup>n</sup>.** Three HVLs means dividing by 8, not by 3.
- **Unit mismatch** (mm vs. cm) between thickness and HVL.

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

# Common Checks Before Submitting Your Answer

- Does my setup line use fraction form with my units canceling?
- Did I check m (milli) against M (mega)?
- Do my time units match (hours vs. minutes)?
- Did I square the distance, and take the square root when solving for a distance?
- Is the decayed activity smaller than the starting activity?
- Did I use inches for BMI and include the 703?
- Direction check: smaller units give a larger number. Does my answer go the right way?
- Is my answer labeled with its unit?
