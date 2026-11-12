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
