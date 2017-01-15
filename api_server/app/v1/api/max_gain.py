# -*- coding: utf-8 -*-
from flask import request, g

from . import Resource
from .. import schemas

from lib.stock_data import StockData


class MaxGain(Resource):
  def get(self):
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    ticker_symbol = request.args.get("ticker_symbol")
    stock_date = StockData(ticker_symbol)
    data = stock_date.get_data(start_date, end_date)
    print data
    return {}, 200, None
