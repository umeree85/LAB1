# 🍎 Apple Inc. (AAPL) Stock Data Analysis

> **Design and Analysis of Algorithms — Assignment**

---

## 👤 Student Details

| Field | Info |
|---|---|
| **Name** | M. Umer Abdullah |
| **SAP ID** | 80393 |
| **Subject** | Design and Analysis of Algorithms |
| **Instructor** | Sir Krar Haider |

---

## 📁 Repository Files

| # | File | Description |
|---|---|---|
| 1 | `Apple_Stock_Analysis_M_Umer_Abdullah.ipynb` | Google Colab Notebook — run step by step |
| 2 | `apple_analysis.py` | Python script — run locally after downloading dataset |
| 3 | `README.md` | This documentation file |

---

## 📊 Dataset Source

- **Platform:** [Kaggle](https://www.kaggle.com/datasets/meetnagadia/apple-stock-price-from-19802021-ohlcv)
- **Dataset:** Apple Stock Price from 1980–2021 (OHLCV)
- **Columns:** `Date`, `Open`, `High`, `Low`, `Close`, `Volume`
- **Records:** ~10,000+ trading days

---

## 🚀 How to Run — Google Colab (Recommended)

1. Open [colab.research.google.com](https://colab.research.google.com)
2. Click **File → Upload Notebook**
3. Upload `Apple_Stock_Analysis_M_Umer_Abdullah.ipynb`
4. Get your Kaggle API key:
   - Go to [kaggle.com](https://kaggle.com) → Account → **Create New API Token**
   - It downloads `kaggle.json`
5. When prompted in the notebook, upload `kaggle.json`
6. Click **Runtime → Run All**

---

## 💻 How to Run — Locally (Python Script)

```bash
# 1. Install dependencies
pip install pandas numpy matplotlib seaborn kaggle

# 2. Download dataset
kaggle datasets download -d meetnagadia/apple-stock-price-from-19802021-ohlcv --unzip

# 3. Run the script
python apple_analysis.py
```

---

## 📈 What the Analysis Covers

### Exploratory Data Analysis
- Dataset shape, data types, null value check
- Full statistical summary (mean, std, min, max, quartiles)

### Apple Company Data Sheet

| Metric | Description |
|---|---|
| All-Time High / Low | Extreme closing prices |
| Average & Median Close | Central tendency |
| Std Deviation | Price volatility |
| Max/Min/Avg Volume | Trading activity |
| Max Single-Day Gain/Loss | Extreme daily moves |
| Average Daily Return % | Expected return per day |
| Total Trading Days | Dataset coverage |
| Most Recent Close | Latest price |

### Visualizations (5 Charts)

| # | Chart | Purpose |
|---|---|---|
| 1 | Historical Closing Price | Full price trend 1980–2021 |
| 2 | 50-Day & 200-Day Moving Averages | Trend smoothing |
| 3 | Daily Trading Volume | Market activity |
| 4 | Daily Return Distribution | Return histogram + KDE |
| 5 | Feature Correlation Heatmap | OHLCV relationships |

---

## 🧮 Algorithm Analysis (DAA Core)

| Algorithm | Time Complexity | Space | Applied To |
|---|---|---|---|
| Bubble Sort | O(n²) | O(1) | Sort closing prices |
| Merge Sort | O(n log n) | O(n) | Sort closing prices (efficient) |
| Binary Search | O(log n) | O(1) | Search a specific price |

A **complexity growth comparison chart** is generated to visualize:
`O(log n)` vs `O(n)` vs `O(n log n)` vs `O(n²)`

---

## 🛠 Libraries Used

```python
pandas      # Data loading and manipulation
numpy       # Numerical operations
matplotlib  # Charts and plots
seaborn     # Statistical visualizations
kaggle      # Dataset download API
time        # Algorithm benchmarking
```

---

## 📤 Output Files Generated

| File | Description |
|---|---|
| `Apple_AAPL_Processed.csv` | Full dataset with computed columns (MA50, MA200, Daily Return) |
| `Apple_Company_DataSheet.csv` | Summary metrics table |
| `plot1_closing_price.png` | Historical price chart |
| `plot2_moving_averages.png` | MA50 & MA200 chart |
| `plot3_volume.png` | Volume bar chart |
| `plot4_daily_returns.png` | Return distribution |
| `plot5_heatmap.png` | Correlation heatmap |
| `plot6_complexity.png` | Algorithm complexity comparison |

---

## 📝 Assignment Summary

This project applies **Design and Analysis of Algorithms** concepts to real financial data:

- **Sorting algorithms** (Bubble & Merge Sort) were implemented and benchmarked on Apple stock closing prices
- **Binary Search** was used to locate specific price values efficiently
- **Time complexity** was analyzed theoretically and visualized graphically
- The dataset provides a practical, real-world context for understanding why algorithm efficiency matters at scale

---

*Submitted by: **M. Umer Abdullah** | SAP ID: **80393***  
*Subject: **Design and Analysis of Algorithms** | Instructor: **Sir Krar Haider***
