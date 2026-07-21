# Netflix Data Analysis

## 📌 Project Overview

This project explores the **Netflix Movies and TV Shows** dataset using **Python**, **Pandas**, and **Matplotlib**. The goal is to perform data cleaning, exploratory data analysis (EDA), create meaningful visualizations, and uncover insights about Netflix's content library.

The project demonstrates practical data analysis skills, including data preprocessing, feature engineering, aggregation, visualization, and interpretation of results.

---

## 📂 Dataset

**Dataset:** `netflix_titles.csv`

The dataset contains information about Netflix titles, including:

* Show ID
* Content Type (Movie / TV Show)
* Title
* Director
* Cast
* Country
* Date Added
* Release Year
* Rating
* Duration
* Genre
* Description

---

## 🛠 Technologies Used

* Python
* Pandas
* Matplotlib
* Pathlib

---

## 📊 Data Cleaning

The following preprocessing steps were performed before analysis:

* Loaded the dataset from a CSV file
* Explored dataset structure and dimensions
* Checked data types
* Identified missing values
* Removed rows with missing values in essential columns (`date_added`, `rating`, and `duration`)
* Checked for duplicate records
* Converted the `date_added` column to datetime format
* Converted movie durations from text format (e.g., `"90 min"`) into numeric values for analysis

---

## 📈 Exploratory Data Analysis (EDA)

The project includes the following analyses:

### General Statistics

* Number of rows and columns
* Number of Movies
* Number of TV Shows

### Content Type Analysis

* Movie vs TV Show distribution
* Bar Chart
* Pie Chart

### Country Analysis

* Top 10 countries producing Netflix content
* Horizontal Bar Chart

### Release Year Analysis

* Number of Movies released each year
* Number of TV Shows released each year
* Multi-Line Plot

### Netflix Added Content Analysis

* Number of titles added by Netflix each year
* Line Chart

### Genre Analysis

* Most popular genre
* Top 10 genres
* Horizontal Bar Chart

### Movie Duration Analysis

* Minimum duration
* Maximum duration
* Average duration
* Median duration
* Histogram

### Rating Analysis

* Most common audience ratings
* Bar Chart

### Director Analysis

* Top 10 directors with the most Netflix titles
* Horizontal Bar Chart

### Actor Analysis

* Top 10 actors appearing in Netflix titles
* Horizontal Bar Chart

### Monthly Trend Analysis

* Number of titles added in each month
* Bar Chart

### Yearly Growth

* Netflix catalog growth by year
* Line Chart

---

## 🔍 Advanced Analysis

Additional analyses include:

* Longest Movie
* Shortest Movie
* Oldest Movie
* Newest Movie
* Content growth during the last 10 years

---

## 📷 Visualizations

The project automatically generates and saves charts inside the **images/** directory.

Generated visualizations include:

* Content Type Distribution
* Country Analysis
* Release Year Analysis
* Genre Analysis
* Rating Distribution
* Movie Duration Distribution
* Director Analysis
* Actor Analysis
* Monthly Trend
* Yearly Growth
* Last 10 Years Analysis

---

## 📁 Project Structure

```text
Netflix-Data-Analysis/
│
├── data/
│   └── netflix_titles.csv
│
├── images/
│   ├── content_type_bar.png
│   ├── content_type_pie.png
│   ├── top_countries.png
│   ├── release_year.png
│   ├── genres.png
│   ├── dateadded_analysis.png
│   ├── duration.png
│   ├── rating.png
│   ├── directors.png
│   ├── actors.png
│   ├── monthlytrend.png
│   ├── yearly.png
│   └── last10.png
│
├── netflix_analysis.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Netflix-Data-Analysis.git
```

Move into the project directory:

```bash
cd Netflix-Data-Analysis
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python data_analysis.py
```

---

## 📌 Key Findings

Some insights obtained from the analysis include:

* Movies significantly outnumber TV Shows on Netflix.
* A small number of countries contribute the majority of Netflix content.
* Drama-related genres are among the most common categories.
* Netflix experienced rapid catalog growth during the last decade.
* Certain directors and actors appear much more frequently than others across Netflix productions.

---

## 💡 Future Improvements

Possible extensions for this project include:

* Interactive dashboard using Streamlit
* Visualizations with Plotly or Seaborn
* Genre comparison between countries
* Content recommendation system
* Machine Learning-based analysis
* Interactive filtering and search

---

## 👩‍💻 Author

**Zahide Bayramova**

Computer Engineering Student | Aspiring Data Scientist

GitHub: https://github.com/ZahidaBayramova
