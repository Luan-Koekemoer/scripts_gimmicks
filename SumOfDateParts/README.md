## The problem 

The problem in the proposed .jpg image is that the happening of certain events might be very coincidental.
Though, those events are tragic. The argument is just that the real occurance rate of such an 'event date summation' is not really that infrequent i.e. correlation != causation. 

### Caclulations and Results
**Calculating the year summations** <br/>
The program adds the day, month and the year's parts first two and last two dates. <br />
Example: 1/11/2022 would be. <br />
[1] + [11] + [20] + [22...] <br />
1 + 11 + 20 + 22 = 54 

**Evaluation** <br/>
The program does this calculation from a given starting year until an ending year and compares it to the target value.

**Results** <br/>
For this problem the occurance count of dates that add up to 68 from 1900 to 2022 is: <br />
count: 514 times <br />
average: 1.41 times per year (514/365.25)

### Usage
```python3
python3 /path/to/dates.py 
```

or

```python3
python3 /path/to/dates.py {startYear} {endYear} {targetValue}
```
