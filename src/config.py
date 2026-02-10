from dataclasses import dataclass
from pathlib import Path
from datetime import datetime, timedelta

@dataclass(frozen=True)
class Settings:
    # Watchlist (edit anytime)
    tickers: tuple[str, ...] = (
        "VFV.TO",
        "SCHG",
        "CGL.TO",
        "MSFT",
        "AAPL",
        "NVDA",
        "XCH.TO",
        "TSLA",
        "AMD",
        "META",
    )

    # Last ~5 years rolling window
    start: str = (datetime.today() - timedelta(days=5 * 365)).strftime("%Y-%m-%d")
    end: str | None = None  # None = up to latest

    # Rolling windows (trading days)
    sma_windows: tuple[int, ...] = (21, 63, 126, 252)  # ~1m, 3m, 6m, 1y
    vol_window: int = 21  # ~1 month rolling volatility

    # Paths
    project_root: Path = Path(__file__).resolve().parents[1]
    data_dir: Path = project_root / "data"
    processed_dir: Path = data_dir / "processed"
    db_path: Path = data_dir / "finance.db"

    # Outputs for Power BI
    prices_csv: Path = processed_dir / "prices_clean.csv"
    features_csv: Path = processed_dir / "features_daily.csv"
    summary_csv: Path = processed_dir / "summary_by_ticker.csv"