"""Find Minsheng Bank's highest and lowest prices over the past two years.

Run from the repository root after installing akshare:

    python examples/minsheng_bank_extreme.py
"""
from __future__ import annotations

from datetime import date, timedelta

import akshare as ak


SYMBOL = "600016"
NAME = "Minsheng Bank"
LOOKBACK_DAYS = 365 * 2


def main() -> None:
    end = date.today()
    start = end - timedelta(days=LOOKBACK_DAYS)

    data = ak.stock_zh_a_hist(
        symbol=SYMBOL,
        period="daily",
        start_date=start.strftime("%Y%m%d"),
        end_date=end.strftime("%Y%m%d"),
        adjust="",
    )

    if data.empty:
        raise SystemExit(f"No data returned for {SYMBOL} between {start} and {end}.")

    data["日期"] = data["日期"].astype(str)
    highest = data.loc[data["最高"].idxmax()]
    lowest = data.loc[data["最低"].idxmin()]

    print(f"Stock: {NAME} ({SYMBOL})")
    print(f"Range: {start} to {end}")
    print(f"Rows: {len(data)}")
    print()
    print(f"Highest price: {highest['最高']}")
    print(f"Highest date: {highest['日期']}")
    print()
    print(f"Lowest price: {lowest['最低']}")
    print(f"Lowest date: {lowest['日期']}")


if __name__ == "__main__":
    main()
