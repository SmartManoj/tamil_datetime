[draft]
# tamil_datetime
 Python module for tamil_datetime

The `tamil_datetime` refers to a date in the traditional Tamil calendar, which follows a cyclical system of **60 years**, with each year having a unique name. The Tamil calendar also includes **12 months**, each with varying days, similar to the Gregorian calendar.

#### Key Components:
1. **Tamil Year**: Each Tamil year has a specific name from a fixed sequence of 60 years (such as 'சார்வரி', 'வைகாசி', etc.). After 60 years, the cycle repeats.
2. **Tamil Month**: The year is divided into 12 months, with names like 'சித்திரை', 'வைகாசி', 'ஆனி', and so on. The number of days in each month can vary between 29 and 32 days, depending on the year in the cycle.
3. **Days**: The Tamil day count is based on a specific cycle of days for each month. The variation in the number of days per month comes from the way the lunar cycle is calculated.

#### Subtracting One Day
When calculating dates, subtracting one day from a Tamil date involves:
- **Month Transition**: If you are at the 1st day of the month, subtracting one day will move you to the last day of the previous month.
- **Year Transition**: If you are at the first month of the year (சித்திரை) and the first day, subtracting one day moves to the last day of the last month of the previous year.

#### Example:
If today is **1 வைகாசி, சார்வரி** and we subtract one day, the result would be **31 சித்திரை, சார்வரி**, as it moves to the last day of the previous month in the same year.

This system is useful for calculating dates in traditional Tamil festivals, astrology, and other cultural events that follow the Tamil calendar.

This description will provide the necessary understanding of the concept of `tamil_datetime` and how it functions in terms of year, month, and day calculations.