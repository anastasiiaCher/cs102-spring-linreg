import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry
from pathlib import Path


def fetch_weather_for_year_range(
    latitude: float = 52.57,
    longitude: float = 30.19,
    start_year: int = 2022,
    end_year: int = 2026,
    timezone: str = "Europe/Moscow",
) -> pd.DataFrame:
    """Вдохновитесь материалами по этой ссылочке, чтобы создать функцию для сбора данных.
    Ссылочка-референс: https://open-meteo.com/en/docs/historical-weather-api?latitude=52.57&longitude=30.19&start_date=2022-04-30&timezone=Europe%2FMoscow&hourly=temperature_2m,apparent_temperature,wind_speed_10m,wind_direction_10m,relative_humidity_2m#api_response"""
    
    # PUT YOUR CODE HERE

    return hourly_dataframe


def save_dataset(df: pd.DataFrame, path: str | Path) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(target, index=False)
