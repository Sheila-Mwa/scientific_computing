# Task 02: NumPy Arrays and Numerical Computation

**Course:** BIT 2118 Scientific Computing  |  **Student GitHub:** Just-Iann

## 1. The idea in my own words
An array is just a list of numbers that NumPy treats as one object, so I can do maths on all of it in one line instead of writing a loop. If I write `1.8 * temps + 32`, every single temperature is converted at once. Summaries like the mean, minimum and maximum are one-liners too.

## 2. Handout program - inputs and operation
Program: [`code/Task_02_numpy_arrays.py`](../code/Task_02_numpy_arrays.py)

**Inputs:** 24 hourly temperature readings in degrees Celsius, stored in one NumPy array (`temperatures_c`).

**Mathematical operation:** Mean = (sum of all 24 values) / 24, then the minimum and maximum, then the element-wise conversion F = 1.8 C + 32 applied to the whole array.

<details><summary>Output of the handout program</summary>

```text
=== Part 1: original ===
Daily mean temperature: 23.12 C
Minimum temperature: 17.50 C
Maximum temperature: 29.40 C
First six Fahrenheit readings: [65.3  64.4  64.04 63.5  64.22 66.2 ]

=== Part 2: parameter change (reading at 12:00 replaced by a 45.0 C spike) ===
original    mean=23.12  median=22.75  max=29.40
with spike  mean=23.77  median=22.75  max=45.00
```
</details>

## 3. I changed a parameter
**What I changed:** I replaced the 12:00 reading (29.4 C) with a fake sensor spike of 45.0 C.

**What happened:** The mean went from 23.12 C to 23.77 C and the maximum jumped from 29.40 C to 45.00 C, but the median stayed at 22.75 C. So one bad reading changes the mean a little (it is shared among 24 values: (45 - 29.4)/24 = 0.65 C), changes the maximum completely, and does not move the median at all. That is a good reason to look at more than one summary statistic when a sensor might misbehave.

## 4. What the output means
The average temperature of the day was about 23.1 C, the coldest hour was 17.5 C (early morning) and the warmest was 29.4 C (around midday). The Fahrenheit values (65.3, 64.4, ...) are the same temperatures on a different scale, which also confirms that the conversion really ran on the whole array.


## 5. My own real-world case: Water level in a rooftop tank (rationed supply)
Program: [`modified/Task_02_modified_water_tank.py`](../modified/Task_02_modified_water_tank.py)

**Assumptions:** 5,000 L tank, one reading per hour for 24 hours, water supplied only at night. The numbers are made up for practice, they are not from a real sensor.

**Input data:** 24 hourly levels in litres (4200, 4050, 4600, ... 1250).

```text
Mean level: 2954 L | min: 700 L | max: 5000 L
Mean level in cubic metres: 2.95 m3
Hours at or below 20% full: [19, 20, 21, 22]
Biggest hourly drop: -400 L between hour 6 and 7
Total water used (sum of drops): 4450 L
Total water pumped in (sum of rises): 1500 L
```

**Interpretation:** On average the tank held about 2,954 L (2.95 m3, roughly 59% full), but it dropped to 700 L in the late evening. It was at or below 20% full during hours 19 to 22, so that is the window when residents are most at risk of running out. The biggest one-hour drop was 400 L (hour 6 to 7, the morning rush). Over the day 4,450 L were used but only 1,500 L were pumped in, which means supply covers only about a third of the demand and the tank ends the day far lower than it started. NumPy's `diff` and boolean masks made these checks one-liners.
