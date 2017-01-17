# -*- coding: utf-8 -*-
from flask import request

from . import Resource

from app.lib.stock_data import StockData
from app.lib.max_sub_array import MaxSubArray


class MaxGain(Resource):
  def get(self):
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    ticker_symbol = request.args.get("ticker_symbol")
    stock_date = StockData(ticker_symbol)
    data = stock_date.get_data(start_date, end_date)

    left, right, _ = MaxSubArray.find_max_sub_array(
      [i[3] for i in data])
    print data[left], data[right]
    buy_data = data[right]
    sell_data = data[left]
    buy_price = buy_data[1]
    sell_price = sell_data[2]
    profit = sell_price - buy_price
    profit_percent = (profit / buy_price) * 100
    result = dict(
      buy_date=data[right][0],
      buy_price=buy_price,
      sell_date=data[left][0],
      sell_price=sell_price,
      gain_absolute=round(profit, 2),
      gain_percent=profit_percent
    )
    return result, 200, None
