"""
╔══════════════════════════════════════════════════════════════╗
║        APPLE INC. (AAPL) — STOCK DATA ANALYSIS              ║
╠══════════════════════════════════════════════════════════════╣
║  Student Name  : M. Umer Abdullah                           ║
║  SAP ID        : 80393                                       ║
║  Subject       : Design and Analysis of Algorithms           ║
║  Instructor    : Sir Krar Haider                             ║
║  Dataset       : Kaggle — Apple Stock Price 1980-2021        ║
╚══════════════════════════════════════════════════════════════╝
"""

# ─────────────────────────────────────────────────────────────
# SECTION 1: IMPORTS
# ─────────────────────────────────────────────────────────────
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['figure.figsize'] = (14, 5)
sns.set_theme(style='darkgrid')
print("=" * 60)
print("  APPLE STOCK ANALYSIS — M. Umer Abdullah | SAP: 80393")
print("  Subject: Design and Analysis of Algorithms")
print("  Sir: Krar Haider")
print("=" * 60)


# ─────────────────────────────────────────────────────────────
# SECTION 2: LOAD DATASET
# Note: Download 'AAPL.csv' from Kaggle first:
#   kaggle datasets download -d meetnagadia/apple-stock-price-from-19802021-ohlcv --unzip
# ─────────────────────────────────────────────────────────────
def load_data(filepath='AAPL.csv'):
    df = pd.read_csv(filepath, parse_dates=['Date'])
    df.sort_values('Date', inplace=True)
    df.reset_index(drop=True, inplace=True)
    print(f"\n[DATA LOADED]")
    print(f"  Shape      : {df.shape}")
    print(f"  Date Range : {df['Date'].min().date()} → {df['Date'].max().date()}")
    print(f"  Columns    : {list(df.columns)}")
    return df


# ─────────────────────────────────────────────────────────────
# SECTION 3: EXPLORATORY DATA ANALYSIS
# ─────────────────────────────────────────────────────────────
def run_eda(df):
    print("\n" + "=" * 48)
    print("  EXPLORATORY DATA ANALYSIS (EDA)")
    print("=" * 48)
    print("\n[INFO]")
    df.info()
    print("\n[MISSING VALUES]")
    print(df.isnull().sum())
    print("\n[STATISTICAL SUMMARY]")
    print(df.describe().round(2).to_string())


# ─────────────────────────────────────────────────────────────
# SECTION 4: COMPANY DATA SHEET
# ─────────────────────────────────────────────────────────────
def company_datasheet(df):
    df['Daily_Return'] = df['Close'].pct_change() * 100
    datasheet = pd.DataFrame({
        'Metric': [
            'All-Time High Price (Close)',
            'All-Time Low Price (Close)',
            'Average Closing Price',
            'Median Closing Price',
            'Std Deviation (Close)',
            'Maximum Daily Volume',
            'Minimum Daily Volume',
            'Average Daily Volume',
            'Max Single-Day Price Gain',
            'Max Single-Day Price Loss',
            'Average Daily Return (%)',
            'Volatility (Std Return %)',
            'Total Trading Days',
            'Most Recent Closing Price',
        ],
        'Value': [
            f"${df['Close'].max():.2f}",
            f"${df['Close'].min():.4f}",
            f"${df['Close'].mean():.2f}",
            f"${df['Close'].median():.2f}",
            f"${df['Close'].std():.2f}",
            f"{df['Volume'].max():,.0f}",
            f"{df['Volume'].min():,.0f}",
            f"{df['Volume'].mean():,.0f}",
            f"${df['Close'].diff().max():.2f}",
            f"${df['Close'].diff().min():.2f}",
            f"{df['Daily_Return'].mean():.4f}%",
            f"{df['Daily_Return'].std():.4f}%",
            f"{len(df):,}",
            f"${df['Close'].iloc[-1]:.2f}",
        ]
    })

    print("\n" + "=" * 48)
    print("  APPLE INC. (AAPL) — COMPANY DATA SHEET")
    print("=" * 48)
    print(datasheet.to_string(index=False))
    datasheet.to_csv('Apple_Company_DataSheet.csv', index=False)
    print("\n[SAVED] Apple_Company_DataSheet.csv")
    return df, datasheet


# ─────────────────────────────────────────────────────────────
# SECTION 5: VISUALIZATIONS
# ─────────────────────────────────────────────────────────────
def plot_all(df):
    # 1. Closing Price History
    plt.figure(figsize=(15, 5))
    plt.plot(df['Date'], df['Close'], color='#1f77b4', lw=0.8)
    plt.title('Apple Inc. (AAPL) — Historical Closing Price\nStudent: M. Umer Abdullah | SAP: 80393',
              fontsize=13, fontweight='bold')
    plt.xlabel('Year'); plt.ylabel('Price (USD)')
    plt.tight_layout(); plt.savefig('plot1_closing_price.png', dpi=150); plt.show()
    print("[SAVED] plot1_closing_price.png")

    # 2. Moving Averages
    df['MA50']  = df['Close'].rolling(50).mean()
    df['MA200'] = df['Close'].rolling(200).mean()
    plt.figure(figsize=(15, 5))
    plt.plot(df['Date'], df['Close'],  color='lightblue', lw=0.6, label='Close')
    plt.plot(df['Date'], df['MA50'],   color='orange',    lw=1.4, label='50-Day MA')
    plt.plot(df['Date'], df['MA200'],  color='red',       lw=1.4, label='200-Day MA')
    plt.title('Moving Averages — AAPL (50-Day & 200-Day)', fontsize=13, fontweight='bold')
    plt.xlabel('Year'); plt.ylabel('Price (USD)'); plt.legend()
    plt.tight_layout(); plt.savefig('plot2_moving_averages.png', dpi=150); plt.show()
    print("[SAVED] plot2_moving_averages.png")

    # 3. Trading Volume
    plt.figure(figsize=(15, 4))
    plt.bar(df['Date'], df['Volume'], color='steelblue', alpha=0.5, width=1)
    plt.title('Apple Inc. — Daily Trading Volume', fontsize=13, fontweight='bold')
    plt.xlabel('Year'); plt.ylabel('Volume')
    plt.tight_layout(); plt.savefig('plot3_volume.png', dpi=150); plt.show()
    print("[SAVED] plot3_volume.png")

    # 4. Daily Return Distribution
    plt.figure(figsize=(10, 5))
    sns.histplot(df['Daily_Return'].dropna(), bins=150, kde=True, color='mediumseagreen')
    plt.title('Distribution of Daily Returns — AAPL (%)', fontsize=13, fontweight='bold')
    plt.xlabel('Daily Return (%)'); plt.ylabel('Frequency')
    plt.tight_layout(); plt.savefig('plot4_daily_returns.png', dpi=150); plt.show()
    print("[SAVED] plot4_daily_returns.png")

    # 5. Correlation Heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(df[['Open','High','Low','Close','Volume']].corr(),
                annot=True, fmt='.2f', cmap='coolwarm', square=True)
    plt.title('Feature Correlation Heatmap — AAPL', fontsize=13, fontweight='bold')
    plt.tight_layout(); plt.savefig('plot5_heatmap.png', dpi=150); plt.show()
    print("[SAVED] plot5_heatmap.png")

    return df


# ─────────────────────────────────────────────────────────────
# SECTION 6: ALGORITHM ANALYSIS (DAA)
# ─────────────────────────────────────────────────────────────

# --- Bubble Sort --- O(n²)
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# --- Merge Sort --- O(n log n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])
    return _merge(L, R)

def _merge(L, R):
    res, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]: res.append(L[i]); i += 1
        else: res.append(R[j]); j += 1
    return res + L[i:] + R[j:]


# --- Binary Search --- O(log n)
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1


def run_algorithm_analysis(df):
    print("\n" + "=" * 48)
    print("  ALGORITHM ANALYSIS (DAA)")
    print("=" * 48)

    sample = df['Close'].tail(100).tolist()

    # Bubble Sort
    t0 = time.time(); bubble_sort(sample); t1 = time.time()
    print(f"\nBubble Sort  (n=100) → {(t1-t0)*1000:.4f} ms  | Complexity: O(n²)")
    print("  Best: O(n)  |  Worst: O(n²)  |  Space: O(1)")

    # Merge Sort
    t0 = time.time(); merge_sort(sample); t1 = time.time()
    print(f"\nMerge Sort   (n=100) → {(t1-t0)*1000:.4f} ms  | Complexity: O(n log n)")
    print("  Best: O(n log n)  |  Worst: O(n log n)  |  Space: O(n)")

    # Binary Search
    sp     = sorted(df['Close'].tolist())
    target = sp[len(sp) // 2]
    t0 = time.time(); idx = binary_search(sp, target); t1 = time.time()
    print(f"\nBinary Search (n={len(sp)}) → {(t1-t0)*1000:.6f} ms  | Complexity: O(log n)")
    print(f"  Target: ${target:.2f}  |  Found at index: {idx}")
    print("  Best: O(1)  |  Worst: O(log n)  |  Space: O(1)")

    # Complexity Chart
    n = np.arange(1, 101)
    plt.figure(figsize=(10, 5))
    plt.plot(n, np.log2(n),   label='O(log n)',   color='purple', lw=2.5)
    plt.plot(n, n,            label='O(n)',        color='green',  lw=2.5)
    plt.plot(n, n*np.log2(n), label='O(n log n)', color='blue',   lw=2.5)
    plt.plot(n, n**2,         label='O(n²)',       color='red',    lw=2.5)
    plt.ylim(0, 500)
    plt.title('Time Complexity Comparison — Applied to Apple Stock Data\nM. Umer Abdullah | SAP: 80393 | Sir Krar Haider',
              fontsize=12, fontweight='bold')
    plt.xlabel('Input Size (n)'); plt.ylabel('Operations')
    plt.legend(fontsize=11)
    plt.tight_layout()
    plt.savefig('plot6_complexity.png', dpi=150); plt.show()
    print("\n[SAVED] plot6_complexity.png")


# ─────────────────────────────────────────────────────────────
# SECTION 7: SAVE PROCESSED DATA
# ─────────────────────────────────────────────────────────────
def save_processed(df):
    df.to_csv('Apple_AAPL_Processed.csv', index=False)
    print("\n[SAVED] Apple_AAPL_Processed.csv")
    print(f"  Rows: {len(df):,}  |  Columns: {list(df.columns)}")


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────
if __name__ == '__main__':
    df = load_data('AAPL.csv')
    run_eda(df)
    df, datasheet = company_datasheet(df)
    df = plot_all(df)
    run_algorithm_analysis(df)
    save_processed(df)

    print("\n" + "=" * 60)
    print("  ANALYSIS COMPLETE")
    print("  Student : M. Umer Abdullah | SAP ID: 80393")
    print("  Subject : Design and Analysis of Algorithms")
    print("  Sir     : Krar Haider")
    print("=" * 60)
