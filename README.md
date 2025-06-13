# Elevate-labks-task-8

# 📊 Task 8 - Simple Sales Dashboard Design

## 🎯 Objective
Design a basic interactive dashboard to visualize sales performance by product category, region, and month using Power BI.

---

## 🛠 Tools Used
- Power BI
- Dataset: `Superstore_Sales.csv`
- Power Query Editor (for cleaning and column creation)

---

## 📁 Dataset Fields Used
- order_date
- region
- category
- sales
- profit

---

## 🔧 Steps Followed

1. **Loaded `Superstore_Sales.csv`** into Power BI.
2. **Transformed the `order_date`** column to ensure it's in Date format.
3. **Created a `MonthYear` column** using:
   ```powerquery
   = Date.ToText([order_date], "MMM-yyyy")
