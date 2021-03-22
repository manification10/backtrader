from datetime import timedelta
import backtrader as bt
import backtrader.indicators as btind

class HarshadV0(bt.Strategy):
    alias = 'HarshadV0'

    def __init__(self, portfolio, symbol):
        self.mom = []
        self.portfolio = portfolio

        # initialize indicators here.
        self.mom.append(
            {"symbol": symbol,
             "indicator90": btind.MomentumOscillator(period = 90),
             "indicator60":btind.MomentumOscillator(period = 60),
             "indicator30": btind.MomentumOscillator(period=30),
             "indicator45": btind.MomentumOscillator(period=45),
             "indicator25": btind.MomentumOscillator(period=25),
             "EMA12": btind.EMA(period=12),
             "EMA30": btind.EMA(period=30),
             "Max15": btind.Max(period=15),
             "Max20": btind.Max(period=20),
             "Max25": btind.Max(period=25),
             "Max30": btind.Max(period=30),
             "Max45": btind.Max(period=45),
             "Min20": btind.Min(period=20),
             "Min25": btind.Min(period=25),
             "Min30": btind.Min(period=30),
             "Min45": btind.Min(period=45)});
