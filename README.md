# Programming for Data Analytics – Assignments 2025
**Module:** Programming and Scripting  
**Author:** Finian Doonan
## Module Overview
This module introduces learners to programming and data analytics concepts using Python. The focus is on solving numerical problems, visualizing data, and working with data-intensive applications using appropriate programming techniques and libraries.

---

## Learning Outcomes
On successful completion of this module, learners will be able to:

1. **Programmatically create plots and other visual outputs from data**  
   - Generate clear, accurate, and aesthetically pleasing data visualizations.

2. **Design computer algorithms to solve numerical problems**  
   - Develop step-by-step solutions and implement efficient algorithms in code.

3. **Create software that incorporates and utilises standard numerical libraries**  
   - Employ libraries such as `numpy`, `pandas`, and `matplotlib` to enhance computational efficiency.

4. **Employ appropriate data structures when programming for data-intensive applications**  
   - Use lists, dictionaries, sets, and data frames effectively to store, process, and analyze data.

---

## Contents – Assignments

| Assignment | Filename | Description |
|------------|---------|-------------|
| 1 | `assignment02-bankholidays.py` | Northern Ireland bank holidays, including those unique to NI. |
| 2 | `assignment03-pie.ipynb` | Pie chart of email domains from a CSV file of 1000 people. |
| 3 | `assignment05-population.ipynb` | Population analysis in Ireland: sex differences, age groups, regional differences. |
| 4 | `assignment_6_Weather.ipynb` | Weather analysis for Knock Airport: temperature and windspeed plots. |

---

## Assignment Details

### Assignment 1 – Northern Ireland Bank Holidays
**Filename:** `assignment02-bankholidays.py`  
**Description:**  
- Print all Northern Ireland bank holiday dates.  
- Bonus: Print bank holidays unique to Northern Ireland (not occurring elsewhere in the UK).  

**Tips:**  
- Use lists or dictionaries to store holiday names and dates.  
- Compare NI holidays to other UK regions to find unique ones.  

---

### Assignment 2 – Email Domains Pie Chart
**Filename:** `assignment03-pie.ipynb`  
**Description:**  
- Create a pie chart showing the distribution of email domains in a CSV of 1000 people.  
- Source CSV: [Download Link](https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download)  
- Make the chart visually appealing with labels, colors, and percentages.  

**Tips:**  
- Use `pandas` for data manipulation and `matplotlib` for plotting.  
- Extract domains from email addresses using string operations.  

---

### Assignment 3 – Population Analysis in Ireland
**Filename:** `assignment05-population.ipynb`  

**Description:**  
- **Part 1 (70%)**: Analyze age differences between sexes, calculate weighted mean age.  
- **Part 2 (20%)**: Group people within ±5 years of a chosen age and calculate population difference between sexes.  
- **Part 3 (10%)**: Identify which region has the largest population difference in that age group.  

**Tips:**  
- Use `pandas` for filtering, grouping, and calculating weighted means.  
- Focus on sex differences; regions are only needed in Part 3.  

---

### Assignment 4 – Knock Airport Weather
**Filename:** `assignment_6_Weather.ipynb`  
**Data URL:** [Knock Airport CSV](https://cli.fusio.net/cli/climate_data/webdata/hly4935.csv)  

**Description:**  
- **Temperature plots (60%)**: raw temperatures, daily mean, monthly mean.  
- **Windspeed plots (40%)**: raw windspeed, 24-hour rolling mean, daily max, monthly mean of daily max.  

**Tips:**  
- Handle missing windspeed data using `.dropna()` or `.fillna()`.  
- Use `pandas` for rolling and aggregation calculations.  
- Use `matplotlib` for clear and visually appealing plots.  

---

## Notes
- Ensure your code is **well-structured, readable, and cleanly commented**.  
- Plot aesthetics contribute to marks, so label axes and provide titles.  
- Follow the exact filenames to match assignment submission requirements.  

---

## References & Resources

**Python Tutorials & Guides**  
- [W3Schools Python Tutorial](https://www.w3schools.com/python/default.asp)  
- [Real Python – Input & Output](https://realpython.com/python-input-output/)  
- [Stack Overflow – Mask Digits](https://stackoverflow.com/questions/59342854/how-to-mask-input-and-display-the-last-4-digit-using-python)  
- [GeeksForGeeks – Collatz Sequence](https://www.geeksforgeeks.org/program-to-print-collatz-sequence/?ref=ml_lbp)  
- [Python Datetime Module](https://docs.python.org/3/library/datetime.html)  
- [GeeksForGeeks – Newton's Method](https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/)  

**Data Visualization & Analysis**  
- [Real Python – Matplotlib Guide](https://realpython.com/python-matplotlib-guide/)  
- [DataCamp – Histograms in Python](https://www.datacamp.com/tutorial/histograms-matplotlib)  
- [GeeksForGeeks – Count Letters in File](https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/)  

**Datasets**  
- Email domains CSV: [Download Link](https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download)  
- Knock Airport Weather CSV: [Download Link](https://cli.fusio.net/cli/climate_data/webdata/hly4935.csv)  

