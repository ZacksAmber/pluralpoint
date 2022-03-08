# Northeastern University AI/ML Business Applications MPV Project
- Date: 10/29/2020
- Author: Zacks Shen

---

## Definition
**Data Source:**
- **Old data source**: Access DB & MDB: 
- **New data source**: MySQL, MSSQL, MariaDB, and PostgreSQL

**Report Source:**
- <mark>from our data source or the Internet?</mark>
  - **Our report source**: if the reports are our RDL files, we could check the visualization on code layer.
  - **Internet report source**: if the reports from the Internet, we have to classify them on **image classification** layer.

**Visualization engine**
- **Old visualization engine**: the videos you showed to me and Serigy, on the left window.
- **New visualization engine**: the videos you showed to me and Serigy, on the right window.

---

## Core Targets
**Data verification:**
- We could have a program checking the query results for each table from the old data source and new data source during the idle time, which means comparing the data between two data sources automatically.
- It is not necessary to validate the data source when we are generating the reports and showing them to the customers.

**Visualization verification:**
- visualization before chart (Zacks' suggestion): After the program did the **Data verification** without any error, there is one thing we can make sure -- our data is complete and correct. The next step we could check if the **New data engine** returns the chart correctly.There is no necessary to do any image ML/AI, since we could get the return code from the visualization engine. If the chart generation failed, it will return a error code. <mark>Then we could try to troubleshooting.</mark> e.g, missing value or wrong parameters. Then we need to check the original query statement to see if it works well in the **old visualization engine**? You know, the reason may be "" or \`\`, the quote symbol in different DBs. If you search `CharDataPoint` inside the rdl file. It will tell you which kind of visualization of the query statement is.
![](https://raw.githubusercontent.com/ZacksAmber/PicGo/master/img/20201029144631.png)
- Image Classification(Tim's plan): That is a very cool solution. Could we do it? Yes, but I think it is not necessary. Although the image ML/AI could classify the type of visualization or if it is a visualization, **it is not useful for us to troubleshooting**. We still need to check the query statement and parameters that passed to the visualization engine. In other words, if our **old visualization engine** returns a correct bar chart and our **new visualization engine** returns a bar chart but with wrong information. The ML/AI program will still make a conclusion that the two charts are the same type <mark>since it only can verify the visualization type.</mark> Unless your target is not to validate our report source, instead, you want to train a model to classify all of the reports from the Internet.

---

## Executive Summary
**Data verification:**
- I could write a Python program to compare the query data result between the **old data source** and the **new data source**
- I could write a Python program to check the `CharDataPoint` field is what parameter and convert it in our **new visualization engine**. For example, if our **old visualization engine** read `bar` to generate bar chart. But in our **new visualization engine**, it using `plot_chart` to generate bar chart. I can replace all of the fields in the RDL file. And validate the return code from the **new visualization engine**. Just like Sergiy said, if the results of the query statements are correct, it is impossible you get a incorrect data.

---

## My questions:
1. Is this project designed for our customers?
2. Your target is to verify **our report source** or the **Internet report source**?
