# Customer Behavior Dashboard

> **Data Cleaning, Feature Engineering, Database Integration, and Business Intelligence using Python, MySQL, and Power BI**

---

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![MySQL](https://img.shields.io/badge/MySQL-8.x-orange?style=for-the-badge&logo=mysql)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?style=for-the-badge&logo=powerbi)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green?style=for-the-badge&logo=pandas)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

---

## 👤 Author

| Field | Details |
|-------|---------|
| **Name** | Devansh Singh Raghuvanshi |
| **Department** | Computer Science Engineering |
| **University** | Chandigarh University |
| **Academic Year** | 2026 |
| **Domain** | Business Intelligence & Data Analytics |

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Project Architecture](#-project-architecture)
- [Technology Stack](#-technology-stack)
- [Dataset Description](#-dataset-description)
- [Project Workflow](#-project-workflow)
- [Data Cleaning](#-data-cleaning)
- [Feature Engineering](#-feature-engineering)
- [Database Integration](#-database-integration)
- [Power BI Dashboard](#-power-bi-dashboard)
- [Key Performance Indicators](#-key-performance-indicators)
- [Business Insights](#-business-insights)
- [Business Recommendations](#-business-recommendations)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [Hardware Requirements](#-hardware-requirements)
- [Software Requirements](#-software-requirements)
- [Results Summary](#-results-summary)
- [Future Scope](#-future-scope)
- [References](#-references)
- [License](#-license)

---

## 📌 Project Overview

The **Customer Behavior Dashboard** is a complete end-to-end **Business Intelligence solution** that transforms raw customer shopping data into meaningful, actionable business insights using **Python**, **MySQL**, **SQLAlchemy**, and **Microsoft Power BI**.

The project demonstrates a full **ETL (Extract–Transform–Load)** pipeline covering:

- ✅ Raw dataset import and exploration
- ✅ Data cleaning and missing value treatment
- ✅ Feature engineering for customer segmentation
- ✅ MySQL database integration
- ✅ Interactive Power BI dashboard development
- ✅ Business insight generation and strategic recommendations

> The dataset contains approximately **3,900 customer records** with demographic, transactional, and behavioral attributes collected from a retail shopping environment.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🧹 **Automated Data Cleaning** | Category-wise median imputation for missing review ratings |
| 🔧 **Feature Engineering** | Age Group segmentation and Purchase Frequency conversion |
| 🗄️ **Database Integration** | Processed data stored in MySQL via SQLAlchemy |
| 📊 **Interactive Dashboard** | Power BI dashboard with KPIs, charts, and slicers |
| 🎯 **Customer Segmentation** | Age-based demographic grouping |
| 📈 **Revenue Analysis** | Category-wise and demographic revenue breakdowns |
| 🔍 **Subscription Analysis** | Subscriber vs non-subscriber behavior study |
| 💡 **Business Recommendations** | Data-driven strategic insights for decision-makers |

---

## 🏗️ Project Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  Customer Shopping Data                     │
│                     (CSV Dataset)                           │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  Python (Pandas)                            │
│               Data Exploration & EDA                        │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    Data Cleaning                            │
│         Missing Values │ Standardization │ Validation       │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  Feature Engineering                        │
│              Age Group │ Purchase Frequency                 │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                 SQLAlchemy + PyMySQL                        │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                     MySQL Database                          │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  Microsoft Power BI                         │
│                 Interactive Dashboard                       │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              Business Insights & Decision Support           │
└─────────────────────────────────────────────────────────────┘
```

**Architecture Layers:**

| Layer | Component | Purpose |
|-------|-----------|---------|
| 1️⃣ Data Source | CSV Dataset | Raw customer shopping data |
| 2️⃣ Processing | Python / Pandas | Data exploration and EDA |
| 3️⃣ Transformation | Cleaning & Engineering | Data quality improvement |
| 4️⃣ Storage | MySQL Database | Structured data storage |
| 5️⃣ Visualization | Power BI Dashboard | Interactive reporting |
| 6️⃣ Decision Support | Business Insights | Strategic recommendations |

---

## 🛠️ Technology Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.x | Data preprocessing and ETL |
| **Pandas** | Latest Stable | Data manipulation and analysis |
| **SQLAlchemy** | Latest Stable | ORM and database connectivity |
| **PyMySQL** | Latest Stable | MySQL Python driver |
| **MySQL Community Server** | 8.x | Relational database storage |
| **Microsoft Power BI Desktop** | Latest | Dashboard development |
| **VS Code / Jupyter Notebook** | Latest | Development environment |

---

## 📂 Dataset Description

### Overview

| Attribute | Details |
|-----------|---------|
| **Dataset Name** | Customer Shopping Behavior Dataset |
| **Total Records** | ~3,900 customers |
| **Total Attributes** | 15+ |
| **Data Format** | CSV |
| **Data Type** | Mixed (Numerical + Categorical) |

### Attribute Details

| Column | Type | Description |
|--------|------|-------------|
| `customer_id` | INT | Unique customer identifier |
| `age` | INT | Customer age |
| `gender` | VARCHAR | Customer gender |
| `category` | VARCHAR | Product category |
| `purchase_amount` | FLOAT | Purchase amount in USD |
| `review_rating` | FLOAT | Product review rating |
| `subscription_status` | VARCHAR | Subscription information |
| `discount_applied` | VARCHAR | Discount status |
| `shipping_type` | VARCHAR | Shipping method |
| `payment_method` | VARCHAR | Payment method |
| `season` | VARCHAR | Purchase season |
| `previous_purchases` | INT | Number of previous purchases |
| `frequency_of_purchases` | VARCHAR | Original purchase frequency |
| `purchase_frequency_days` | INT | Engineered numeric frequency |
| `age_group` | VARCHAR | Engineered customer segment |

### Numerical Columns

- Age
- Purchase Amount
- Review Rating
- Previous Purchases

### Categorical Columns

- Gender
- Category
- Subscription Status
- Shipping Type
- Payment Method
- Season
- Frequency of Purchases

---

## 🔄 Project Workflow

```
Customer Shopping Dataset
            │
            ▼
   Data Import & Loading
            │
            ▼
  Exploratory Data Analysis
            │
            ▼
   Missing Value Detection
            │
            ▼
       Data Cleaning
            │
            ▼
   Feature Engineering
            │
            ▼
     Data Validation
            │
            ▼
  MySQL Database Storage
            │
            ▼
    Power BI Connection
            │
            ▼
   Dashboard Development
            │
            ▼
    Business Analysis
            │
            ▼
 Strategic Recommendations
```

---

## 🧹 Data Cleaning

### Missing Value Treatment

The **Review Rating** column contains missing values that are handled using **category-wise median imputation**.

```
Missing Review Rating Detected
            │
            ▼
  Group by Product Category
            │
            ▼
  Calculate Category Median
            │
            ▼
  Fill Missing Values with
     Category Median
            │
            ▼
   Zero Missing Values ✅
```

**Why Category-Wise Median?**

| Reason | Explanation |
|--------|-------------|
| ✅ Outlier Resistant | Median is not affected by extreme values |
| ✅ Category Specific | Preserves rating behavior per category |
| ✅ No Data Loss | Customer records are retained |
| ✅ Statistical Accuracy | Maintains distribution integrity |

### Column Standardization

| Original Column Name | Standardized Name |
|---------------------|-------------------|
| `Purchase Amount (USD)` | `purchase_amount` |
| `Customer ID` | `customer_id` |
| `Review Rating` | `review_rating` |
| `Subscription Status` | `subscription_status` |

**Benefits:**

- ✅ SQL-friendly naming conventions
- ✅ Improved code readability
- ✅ Consistent formatting
- ✅ Better database compatibility

---

## 🔧 Feature Engineering

Two new analytical features are engineered from existing data:

### 1️⃣ Age Group

Customer ages are segmented into quartile-based groups for demographic analysis.

| Age Group | Description |
|-----------|-------------|
| **Young Adult** | Youngest quartile |
| **Adult** | Second quartile |
| **Middle-Aged** | Third quartile |
| **Senior** | Oldest quartile |

**Purpose:**

- Improve demographic analysis
- Enable customer segmentation
- Compare purchasing behavior across age groups
- Enhance dashboard readability

---

### 2️⃣ Purchase Frequency (Days)

Textual purchase frequency values are converted into numerical representations.

| Original Text | Converted Days |
|---------------|---------------:|
| Weekly | 7 |
| Fortnightly | 14 |
| Monthly | 30 |
| Quarterly | 90 |
| Annually | 365 |

**Benefits:**

- ✅ Enables numerical analysis
- ✅ Supports statistical calculations
- ✅ Improves visualization quality
- ✅ Prepares data for machine learning

---

## 🗄️ Database Integration

### MySQL Schema

```sql
CREATE TABLE customer (
    customer_id           INT,
    age                   INT,
    gender                VARCHAR(50),
    category              VARCHAR(100),
    purchase_amount       FLOAT,
    review_rating         FLOAT,
    subscription_status   VARCHAR(50),
    discount_applied      VARCHAR(10),
    shipping_type         VARCHAR(100),
    payment_method        VARCHAR(100),
    season                VARCHAR(50),
    previous_purchases    INT,
    frequency_of_purchases VARCHAR(50),
    purchase_frequency_days INT,
    age_group             VARCHAR(50)
);
```

### Connection Method

The project uses **SQLAlchemy** with **PyMySQL** driver to establish database connectivity.

```
Python (Pandas DataFrame)
            │
            ▼
       SQLAlchemy
            │
            ▼
         PyMySQL
            │
            ▼
     MySQL Database
            │
            ▼
     customer table
```

### Benefits of Database Integration

| Benefit | Description |
|---------|-------------|
| 🗃️ Centralized Storage | All processed data in one place |
| ⚡ Efficient Querying | Fast SQL-based data retrieval |
| 🔒 Data Integrity | Structured and validated storage |
| 📊 BI Ready | Direct Power BI connection |
| 📈 Scalable | Supports larger datasets |

---

## 📊 Power BI Dashboard

### Dashboard Layout

```
╔══════════════════════════════════════════════════════════════╗
║                       KPI CARDS                              ║
║   [Total Customers]  [Avg Purchase]  [Avg Review Rating]     ║
╠══════════════════════════════════════════════════════════════╣
║              ║                                               ║
║   SLICERS    ║           REVENUE BY CATEGORY                 ║
║              ║                                               ║
║ Subscription ║           SALES BY CATEGORY                   ║
║   Gender     ║                                               ║
║  Category    ╠═══════════════════════════════════════════════╣
║  Shipping    ║   REVENUE BY AGE GROUP  │  SUBSCRIPTION PIE   ║
║              ║                         │                     ║
╚══════════════╩═════════════════════════╧═════════════════════╝
```

### Dashboard Components

| Component | Type | Description |
|-----------|------|-------------|
| Total Customers | KPI Card | Customer base count |
| Average Purchase Amount | KPI Card | Mean spending per customer |
| Average Review Rating | KPI Card | Customer satisfaction score |
| Revenue by Category | Bar Chart | Category revenue comparison |
| Sales by Category | Bar Chart | Category sales comparison |
| Revenue by Age Group | Column Chart | Demographic revenue analysis |
| Sales by Age Group | Column Chart | Demographic sales analysis |
| Subscription Status | Donut Chart | Subscriber breakdown |
| Interactive Slicers | Filter Panel | Dynamic report filtering |

### Interactive Slicers

- 🔘 Subscription Status
- 🔘 Gender
- 🔘 Product Category
- 🔘 Shipping Type

---

## 📈 Key Performance Indicators

| KPI | Value | Business Significance |
|-----|-------|-----------------------|
| 👥 **Total Customers** | **3.9K** | Overall customer base size |
| 💰 **Average Purchase Amount** | **$59.76** | Customer spending behavior |
| ⭐ **Average Review Rating** | **3.75** | Customer satisfaction level |

### KPI Interpretations

#### 👥 Total Customers — 3.9K

> The dataset contains approximately **3,900 customers**, providing a sufficiently large sample for reliable business analysis and trend identification.

#### 💰 Average Purchase Amount — $59.76

> Customers spend approximately **$60 per transaction**, indicating moderate purchasing power with potential for upselling and cross-selling strategies.

#### ⭐ Average Review Rating — 3.75

> A rating of **3.75 out of 5** indicates generally positive customer satisfaction with identifiable opportunities for service and product improvement.

---

## 💡 Business Insights

### 📦 Product Category Performance

| Category | Revenue Rank | Sales Rank |
|----------|:------------:|:----------:|
| **Clothing** | 🥇 1st | 🥇 1st |
| **Accessories** | 🥈 2nd | 🥈 2nd |
| **Footwear** | 🥉 3rd | 🥉 3rd |
| **Outerwear** | 4th | 4th |

### 👥 Customer Demographics

| Age Group | Revenue Contribution | Sales Activity |
|-----------|---------------------|----------------|
| **Young Adult** | High | Highest |
| **Middle-Aged** | High | Second Highest |
| **Adult** | Moderate | Lower |
| **Senior** | Low | Lowest |

### 🔔 Subscription Status

| Status | Percentage |
|--------|:----------:|
| ❌ Not Subscribed | **73%** |
| ✅ Subscribed | **27%** |

### 🔑 Key Findings Summary

- 🏆 **Clothing** is the highest revenue and sales generating product category.
- 📉 Approximately **73%** of customers are **not enrolled** in subscription programs.
- 👨‍💼 **Young Adults** contribute the highest number of purchases.
- 💵 Average customer spending is approximately **$60 per transaction**.
- ⭐ Customer satisfaction is **generally positive** with a rating of **3.75**.

---

## 📋 Business Recommendations

### 1️⃣ Increase Customer Subscription Rate

**Problem:** 73% of customers are not subscribed.

**Actions:**

- Introduce loyalty reward points
- Offer exclusive member-only discounts
- Provide early access to new products
- Add birthday and anniversary rewards
- Offer free shipping for subscribers

**Expected Outcome:** Higher customer retention and improved lifetime value.

---

### 2️⃣ Focus on High-Revenue Categories

**Problem:** Clothing dominates while other categories underperform.

**Actions:**

- Expand Clothing product variety
- Launch seasonal collections
- Increase Clothing inventory
- Run targeted Clothing advertising

**Expected Outcome:** Increased revenue from the top-performing category.

---

### 3️⃣ Improve Low-Performing Categories

**Problem:** Outerwear generates lowest revenue.

**Actions:**

- Conduct customer preference surveys
- Offer promotional discounts
- Introduce new product designs
- Review and optimize pricing strategies

**Expected Outcome:** Balanced category sales distribution.

---

### 4️⃣ Target High-Value Customer Segments

**Problem:** Young Adults and Middle-Aged customers are underutilized.

**Actions:**

- Invest in social media advertising
- Use mobile app push notifications
- Partner with influencers
- Develop premium product offerings
- Launch personalized email campaigns

**Expected Outcome:** Better marketing ROI and higher engagement.

---

### 5️⃣ Increase Average Purchase Value

**Problem:** Average spend of $59.76 has room for growth.

**Actions:**

- Introduce product bundles
- Offer combo deals
- Implement cross-selling strategies
- Apply upselling techniques
- Provide free shipping above a purchase threshold

**Expected Outcome:** Higher revenue per transaction.

---

### 6️⃣ Improve Customer Satisfaction

**Problem:** Average rating of 3.75 indicates improvement potential.

**Actions:**

- Enhance product quality
- Ensure faster deliveries
- Improve packaging standards
- Strengthen customer support
- Simplify return and refund policies

**Expected Outcome:** Higher ratings and improved brand loyalty.

---

### 7️⃣ Optimize Inventory Management

**Actions:**

- Increase stock for high-demand categories
- Reduce inventory for slow-moving products
- Monitor seasonal demand patterns
- Forecast future inventory requirements

**Expected Outcome:** Reduced operational costs and improved availability.

---

### 📊 Recommendations Summary Table

| # | Recommendation | Expected Benefit |
|---|----------------|------------------|
| 1 | Increase subscription enrollment | Higher customer retention |
| 2 | Focus on Clothing category | Increased revenue |
| 3 | Improve low-performing categories | Balanced sales portfolio |
| 4 | Target Young Adults & Middle-Aged | Better marketing ROI |
| 5 | Increase average purchase value | Higher profitability |
| 6 | Improve customer satisfaction | Better brand loyalty |
| 7 | Optimize inventory management | Reduced operational cost |
| 8 | Implement personalized marketing | Higher conversion rates |

---

## 📁 Project Structure

```
customer-behavior-dashboard/
│
├── 📂 data/
│   ├── customer_shopping_data.csv        # Raw dataset
│   └── customer_shopping_cleaned.csv     # Processed dataset
│
├── 📂 scripts/
│   ├── 01_data_import.py                 # Dataset loading
│   ├── 02_data_exploration.py            # EDA and profiling
│   ├── 03_data_cleaning.py               # Missing value treatment
│   ├── 04_feature_engineering.py         # Age Group & Frequency
│   ├── 05_data_validation.py             # Validation checks
│   └── 06_database_integration.py        # MySQL export
│
├── 📂 database/
│   └── schema.sql                        # MySQL table schema
│
├── 📂 dashboard/
│   └── customer_behavior_dashboard.pbix  # Power BI dashboard file
│
├── 📂 reports/
│   └── project_report.md                 # Full project report
│
├── 📄 requirements.txt                   # Python dependencies
├── 📄 README.md                          # Project documentation
└── 📄 LICENSE                            # License file
```

---

## ⚙️ Installation & Setup

### Step 1 — Clone the Repository

```bash
git clone https://github.com/yourusername/customer-behavior-dashboard.git
cd customer-behavior-dashboard
```

---

### Step 2 — Create a Virtual Environment

```bash
python -m venv venv
```

**Activate on Windows:**

```bash
venv\Scripts\activate
```

**Activate on macOS/Linux:**

```bash
source venv/bin/activate
```

---

### Step 3 — Install Required Libraries

```bash
pip install -r requirements.txt
```

**Contents of `requirements.txt`:**

```
pandas
sqlalchemy
pymysql
```

---

### Step 4 — Configure MySQL Database

Open your MySQL client and run:

```sql
CREATE DATABASE customer_db;
USE customer_db;
```

---

### Step 5 — Update Database Credentials

In `06_database_integration.py`, update:

```python
username   = "your_mysql_username"
password   = "your_mysql_password"
host       = "localhost"
database   = "customer_db"
```

---

### Step 6 — Run Python Scripts in Order

```bash
python scripts/01_data_import.py
python scripts/02_data_exploration.py
python scripts/03_data_cleaning.py
python scripts/04_feature_engineering.py
python scripts/05_data_validation.py
python scripts/06_database_integration.py
```

---

### Step 7 — Connect Power BI to MySQL

1. Open **Power BI Desktop**
2. Click **Get Data** → Select **MySQL Database**
3. Enter `localhost` as server and `customer_db` as database
4. Select the **customer** table
5. Click **Load**
6. Open `dashboard/customer_behavior_dashboard.pbix`

---

## 💻 Hardware Requirements

| Component | Minimum Specification |
|-----------|----------------------|
| **Processor** | Intel Core i5 or higher |
| **RAM** | 8 GB minimum |
| **Storage** | 20 GB free disk space |
| **Operating System** | Windows 10 / 11 |
| **Internet** | Required for software installation |

---

## 🖥️ Software Requirements

| Software | Version | Download |
|----------|---------|----------|
| **Python** | 3.x | [python.org](https://www.python.org/) |
| **MySQL Community Server** | 8.x | [mysql.com](https://dev.mysql.com/downloads/) |
| **Power BI Desktop** | Latest | [Microsoft](https://powerbi.microsoft.com/) |
| **VS Code / Jupyter Notebook** | Latest | [code.visualstudio.com](https://code.visualstudio.com/) |

---

## 📊 Results Summary

### Dashboard KPIs

| Metric | Value |
|--------|-------|
| Total Customers | **3,900** |
| Average Purchase Amount | **$59.76** |
| Average Review Rating | **3.75 / 5** |
| Subscription Rate | **27%** |
| Non-Subscription Rate | **73%** |

### Revenue Rankings

| Rank | Category | Performance |
|------|----------|-------------|
| 🥇 1st | Clothing | Highest Revenue |
| 🥈 2nd | Accessories | Second Highest |
| 🥉 3rd | Footwear | Third |
| 4th | Outerwear | Lowest |

### Customer Segment Rankings

| Rank | Age Group | Contribution |
|------|-----------|--------------|
| 🥇 1st | Young Adult | Highest Sales & Revenue |
| 🥈 2nd | Middle-Aged | High Sales & Revenue |
| 🥉 3rd | Adult | Moderate |
| 4th | Senior | Lowest |

---

## 🚀 Future Scope

| Enhancement | Description |
|-------------|-------------|
| 🔴 **Real-Time Data** | Integrate live transactional data streams |
| 🤖 **Machine Learning** | Sales forecasting and demand prediction models |
| 📉 **Churn Prediction** | Identify customers likely to stop purchasing |
| 🎯 **Recommendation Engine** | Collaborative filtering-based product suggestions |
| 💎 **CLV Analysis** | Customer Lifetime Value measurement |
| 💬 **Sentiment Analysis** | NLP-based analysis of customer reviews |
| ☁️ **Cloud Deployment** | Deploy on Microsoft Azure or AWS |
| 🌐 **Web Dashboard** | Browser-accessible interactive reporting |
| 🧠 **AI Insights** | Automated anomaly detection and AI-driven analysis |
| 🏪 **Multi-Store Analysis** | Expand schema to support multiple retail locations |

---

## 📚 References

### Books

- Han, J., Kamber, M., & Pei, J. — *Data Mining: Concepts and Techniques* — Morgan Kaufmann
- Kimball, R., & Ross, M. — *The Data Warehouse Toolkit* — Wiley
- McKinney, W. — *Python for Data Analysis* — O'Reilly Media
- Provost, F., & Fawcett, T. — *Data Science for Business* — O'Reilly Media
- Silberschatz, A., Korth, H., & Sudarshan, S. — *Database System Concepts* — McGraw-Hill

### Official Documentation

| Resource | URL |
|----------|-----|
| Python | https://docs.python.org/ |
| Pandas | https://pandas.pydata.org/docs/ |
| SQLAlchemy | https://docs.sqlalchemy.org/ |
| MySQL | https://dev.mysql.com/doc/ |
| Power BI | https://learn.microsoft.com/power-bi/ |
| PyMySQL | https://pymysql.readthedocs.io/ |

### Online Resources

- Microsoft Learn — Power BI Learning Resources
- Kaggle Dataset Repository
- Stack Overflow
- W3Schools SQL Tutorials
- Real Python
- Analytics Vidhya
- Towards Data Science

---

## 🏷️ Project Highlights

| Category | Details |
|----------|---------|
| **Project Domain** | Business Intelligence |
| **Industry** | Retail Analytics |
| **Programming Language** | Python |
| **Database** | MySQL |
| **Visualization Tool** | Microsoft Power BI |
| **Dataset Size** | ~3,900 Customer Records |
| **Dashboard Type** | Interactive |
| **Analytics Type** | Descriptive Analytics |
| **Methodology** | ETL Pipeline |
| **DB Connectivity** | SQLAlchemy + PyMySQL |

---

## 📄 License

```
MIT License

Copyright (c) 2026 Devansh Singh Raghuvanshi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 🙏 Acknowledgements

- **Chandigarh University** — for providing an environment that supports practical learning
- **Python Community** — for developing and maintaining Pandas and SQLAlchemy
- **Microsoft** — for Power BI Desktop
- **MySQL** — for reliable open-source database management
- **Kaggle** — for publicly available datasets
- **Open Source Community** — for continuous development of analytics tools

---

<div align="center">

**⭐ If you found this project useful, please consider giving it a star ⭐**

---

**Developed by Devansh Singh Raghuvanshi**

*Department of Computer Science Engineering — Chandigarh University — 2026*

</div>
