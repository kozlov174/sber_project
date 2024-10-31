from sqlalchemy import MetaData, Table, Column, Integer,  Numeric, TIMESTAMP, ForeignKey, func

metadata = MetaData()

trade_day = Table(
    "trade_day",
    metadata,
    Column("id", Integer, primary_key = True),
    Column("date", TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
)

future_prices = Table(
   "future_prices",
    metadata,
    Column("id", Integer, primary_key = True),
    Column("trade_day_id", Integer, ForeignKey(trade_day.c.id)),
    Column("open_price", Numeric, nullable=False),
    Column("high_price", Numeric, nullable=False),
    Column("low_price", Numeric, nullable=False),
    Column("close_price", Numeric, nullable=False),
)

market_data = Table(
    "market_data",
    metadata,
    Column("id", Integer, primary_key = True),
    Column("future_prices_id", Integer, ForeignKey(future_prices.c.id)),
    Column("amplitude", Numeric, nullable=False),
)


volume_data = Table(
    "volume_data",
    metadata,
    Column("id", Integer, primary_key = True),
    Column("future_prices_id", Integer, ForeignKey(future_prices.c.id)),
    Column("volume", Numeric, nullable=False),

)


amplitude_change = Table(
    "amplitude_change",
    metadata,
    Column("id", Integer, primary_key = True),
    Column("future_prices_id", Integer, ForeignKey(future_prices.c.id)),
    Column("previous_close_amplitude",Numeric, nullable=False),
    Column("amplitude_change",Numeric, nullable=False),
    Column("price_change_percent",Numeric, nullable=False),
)

