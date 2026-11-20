# Task 16: Numerical Integration

**Course:** BIT 2118 Scientific Computing  |  **Student GitHub:** Just-Iann

## 1. The idea in my own words
An integral adds up many tiny pieces, such as power over time to get energy. The trapezoidal rule joins neighbouring points with straight lines and adds the trapezoid areas. Simpson's rule fits small parabolas and is usually more accurate for smooth data, but it needs enough points.

## 2. Handout program - inputs and operation
Program: [`code/Task_16_numerical_integration.py`](../code/Task_16_numerical_integration.py)

**Inputs:** Smart-meter power readings every 2 hours (0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9 kW) from 0 to 12 hours.

**Mathematical operation:** Energy = integral of power over time, calculated with the trapezoidal rule and with Simpson's rule (`scipy.integrate.simpson`).

<details><summary>Output of the handout program</summary>

```text
Readings every 2 h
  Trapezoidal: 15.700 kWh | Simpson: 15.800 kWh | difference 0.100 kWh
Readings every 6 h (parameter change)
  Trapezoidal: 15.900 kWh | Simpson: 17.800 kWh
```
</details>

## 3. I changed a parameter
**What I changed:** I kept only every third reading (times 0, 6 and 12 hours).

**What happened:** With the full data the trapezoidal rule gave 15.700 kWh and Simpson 15.800 kWh. With only three readings they gave 15.900 and 17.800 kWh. Simpson's answer moved by 2 kWh because three points cannot describe the peak at 6 hours. So the answer depends heavily on how often I measure, and neither rule can recover detail that the data never captured.

## 4. What the output means
The house used about 15.7 to 15.8 kWh in 12 hours, i.e. an average of about 1.3 kW. The two methods differ by only 0.1 kWh, which tells me the estimate is fairly stable with 2-hour data.


## 5. My own real-world case: Daily energy from a rooftop solar array
Program: [`modified/Task_16_modified_solar_energy.py`](../modified/Task_16_modified_solar_energy.py)

**Assumptions:** A clear-day power curve P(t) = 4.2 sin(pi (t - 6)/12) kW from 06:00 to 18:00, so the exact energy is known to be 4.2 x 24/pi. A cloudy day reduces four of the hourly readings by factors 0.35, 0.3, 0.45 and 0.6. Electricity is valued at an assumed KES 28 per kWh.

**Input data:** 13 hourly power readings (clear and cloudy).

```text
Clear day exact: 32.0856 kWh (= 4.2*24/pi = 32.0856)
  trapezoid 31.9022 (error 0.1835) | Simpson 32.0865 (error 0.00084)
  only 5 readings (every 3 h): trapezoid 30.419 | Simpson 32.159

Cloudy day (measured hourly): 23.693 kWh (74% of a clear day)
Value of clear day: KES 898 | cloudy day: KES 663 | loss KES 235
```

**Interpretation:** The exact clear-day energy is 32.0856 kWh. The trapezoidal rule gave 31.9022 (error 0.18) and Simpson 32.0865 (error 0.0008), so Simpson is about 200 times closer for this smooth curve. With only 5 readings (every 3 hours) the trapezoidal rule fell to 30.42 kWh while Simpson stayed at 32.16. On the cloudy day the array produced 23.69 kWh, only 74% of a clear day. At KES 28 per kWh that is about KES 663 instead of KES 898, a loss of around KES 235 for that day.
