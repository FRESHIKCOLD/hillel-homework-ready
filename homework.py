from pathlib import Path
import matplotlib
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    folder = Path(__file__).resolve().parent
    df = pd.read_csv(folder / "sales_clean.csv")
    by_seller = df.groupby("seller")["total"].sum().sort_values(ascending=False)
    by_seller.to_csv(folder / "sellers.csv")
    by_seller.plot(kind="bar", title="Дохід за продавцями", rot=0, figsize=(9, 5))
    plt.xlabel("Продавець")
    plt.ylabel("грн")
    plt.tight_layout()
    plt.savefig(folder / "sellers.png", dpi=150)
    plt.close()
    print(by_seller)


if __name__ == "__main__":
    main()
