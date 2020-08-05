from b3data.trends import Trend
import numpy

class RMM:

    @staticmethod
    def trends(code='PETR3', start_month=1, period=6, mean=False, cap=50):
        t = Trend('PETR3')
        trends = t.trends(start_month=start_month, period=period)
        res = []
        if mean:
            cap = numpy.mean(trends)
        for pop in trends:
            if pop > cap:
                res.append(1)
            else:
                res.append(0)
    
        return res

    @staticmethod
    def trends_group(codes, prices, start_month=1, period=6, mean=False, cap=[50, 50, 50]):
        res = []
        for index, code in enumerate(codes):
            res.append(RMM.trends(code, start_month, period, mean, cap[index]))
        for i in range(len(res)):
            res[i] = res[i][len(res[i])-len(prices[0]):]

        return res

# from b3data.utils.stock_util import StockUtil
# stockutil = StockUtil(['PETR3', 'ABEV3', 'VALE3'], [6,9,6])
# prices, preds = stockutil.prices_preds(start_year=2014,
#                                         end_year=2014,
#                                         period=6)
# print(len(RMM.trends_group(['PETR3', 'ABEV3', 'VALE3'], prices)[1]))
# print(len(prices[1]))