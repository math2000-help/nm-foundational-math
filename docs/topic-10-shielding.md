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
