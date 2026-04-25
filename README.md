# Blinkit Grocery Data Analysis using Hadoop MapReduce and Hive

## 📌 Overview

This project analyzes the Blinkit Grocery Dataset using the Hadoop ecosystem. It demonstrates how Big Data technologies like Hadoop MapReduce and Hive can be used to process large datasets, perform distributed computations, and generate meaningful business insights.

The dataset is stored in HDFS, processed using Python-based Hadoop Streaming, and analyzed using Hive queries.

---

## 🚀 Features

* Store Blinkit dataset in Hadoop Distributed File System (HDFS)
* Process data using Hadoop Streaming with Python
* Calculate average Item_MRP by Item_Type
* Perform outlet analysis using Hive
* Generate business insights from grocery retail data
* Understand real-world Big Data workflows

---

## 🛠️ Technologies Used

* Python
* Hadoop HDFS
* Hadoop MapReduce
* Hadoop Streaming
* Apache Hive
* Linux
* CSV

---

## 🏗️ Project Architecture

```text
Raw Dataset
    ↓
   HDFS
    ↓
MapReduce Processing
    ↓
Processed Data
    ↓
Hive Analysis
    ↓
Business Insights
```

---

## 📂 Dataset Information

The project uses the Blinkit Grocery Dataset containing grocery product and outlet information.

### Dataset Columns

* Item_Identifier
* Item_Weight
* Item_Fat_Content
* Item_Visibility
* Item_Type
* Item_MRP
* Outlet_Identifier
* Outlet_Establishment_Year
* Outlet_Size
* Outlet_Location_Type

---

## 🎯 Objectives

* Analyze grocery item pricing
* Calculate average price by item category
* Perform outlet-based analysis
* Identify pricing trends across locations
* Gain hands-on experience with Hadoop and Hive

---

## 📁 Project Structure

```text
Blinkit-Grocery-Data-Analysis/
│── blinkit_dataset.csv
│── mapper.py
│── reducer.py
│── hive_queries.sql
│── README.md
```

---

## ⚙️ MapReduce Workflow

### Mapper

* Reads input CSV data
* Extracts Item_Type and Item_MRP
* Emits key-value pairs

### Reducer

* Groups data by Item_Type
* Calculates average Item_MRP
* Produces final output

---

## 🐝 Hive Analysis

Hive is used to analyze the processed data and generate insights.

### Sample Query

```sql
SELECT Outlet_Location_Type,
       AVG(Item_MRP)
FROM blinkit_data
GROUP BY Outlet_Location_Type;
```

---

## ▶️ How to Run

### Step 1: Create HDFS Directory

```bash
hdfs dfs -mkdir /user/cloudera/Blinkit
```

### Step 2: Upload Dataset

```bash
hdfs dfs -put blinkit_dataset.csv /user/cloudera/Blinkit/
```

### Step 3: Run MapReduce Job

```bash
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files mapper.py,reducer.py \
-input /user/cloudera/Blinkit/blinkit_dataset.csv \
-output /user/cloudera/Blinkit/output \
-mapper "python mapper.py" \
-reducer "python reducer.py"
```

### Step 4: View Output

```bash
hdfs dfs -cat /user/cloudera/Blinkit/output/part-00000
```

---

## 📊 Results

* Average Item Price by Item Type
* Average Item Price by Outlet Location
* Outlet-wise Product Analysis
* Business Insights for Retail Decision Making

---

## 🤖 Role of Generative AI

Generative AI was used for:

* Writing MapReduce scripts
* Debugging code
* Generating Hive queries
* Understanding Hadoop concepts
* Improving development speed

---

## 🎓 Learning Outcomes

* Practical understanding of HDFS
* Experience with Hadoop Streaming
* Writing Python Mapper and Reducer
* Querying Big Data using Hive
* Building end-to-end Big Data pipelines

---

## 👨‍💻 Author

**Vishnu Tripathi**

---

## 📜 License

This project is for educational purposes only.

---

## ⭐ Acknowledgements

* IBM SkillsBuild
* Apache Hadoop
* Apache Hive
* Generative AI Tools
