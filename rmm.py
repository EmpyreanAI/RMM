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