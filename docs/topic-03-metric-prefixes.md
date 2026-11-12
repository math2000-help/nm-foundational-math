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
