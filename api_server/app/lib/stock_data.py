from yahoo_finance import Share


class StockData(object):
  def __init__(self, ticker_symbol):
    self.share = Share(ticker_symbol)

  def convert(self, x):
    return round(float(x), 2)

  def _process_data(self, data):
    """
    Process date
    :param data:
    :return: list of (date, open_price, close_price, abs_gain)
    """
    return (data["Date"],
            self.convert(data["Open"]),
            self.convert(data["Close"]),
            self.convert(float(data["Close"]) - float(data["Open"])))

  def get_data(self, start_date, end_date):
    raw_data = self._fetch_data(start_date, end_date)
    return map(self._process_data, raw_data)

  def _fetch_data(self, start_date, end_date):
    return self.share.get_historical(start_date, end_date)
