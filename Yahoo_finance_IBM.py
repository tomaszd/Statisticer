from urllib import urlopen
import csv


class StockQuote:
    """gets stock data from Yahoo Finance"""

    def __init__(self, quote):
        self.quote = quote

    def lastPrice(self):
        url = 'http://finance.yahoo.com/d/quotes.csv?s={ticker}&f=l1'.format(ticker=self.quote)
        return bytes.decode((urlopen(url).read().strip()))

    def volume(self):
        url = 'http://finance.yahoo.com/d/quotes.csv?s={ticker}&f=v0'.format(ticker=self.quote)
        return bytes.decode((urlopen(url).read().strip()))

    def yearrange(self):
        url = 'http://finance.yahoo.com/d/quotes.csv?s={ticker}&f=w0'.format(ticker=self.quote)
        return bytes.decode((urlopen(url).read().strip()))

    def PEratio(self):
        url = 'http://finance.yahoo.com/d/quotes.csv?s={ticker}&f=r0'.format(ticker=self.quote)
        return bytes.decode((urlopen(url).read().strip()))

    def bookValue(self):
        url = 'http://finance.yahoo.com/d/quotes.csv?s={ticker}&f=b4'.format(ticker=self.quote)
        return bytes.decode((urlopen(url).read().strip()))

    def EBITDA(self):
        url = 'http://finance.yahoo.com/d/quotes.csv?s={ticker}&f=j4'.format(ticker=self.quote)
        return bytes.decode((urlopen(url).read().strip()))

    def PEGRatio(self):
        url = 'http://finance.yahoo.com/d/quotes.csv?s={ticker}&f=r5'.format(ticker=self.quote)
        return bytes.decode((urlopen(url).read().strip()))

    def ticker(self):
        url = 'http://finance.yahoo.com/d/quotes.csv?s={ticker}&f=s0'.format(ticker=self.quote)
        return bytes.decode((urlopen(url).read().strip()))


def openCSVFile(sp_500_directory='/home/tomaszd/workspace/StatisticsAndTrends/Data/SP500.ods'):
    SP500 = csv.reader(open(sp_500_directory, 'rb'), delimiter=',')
    print type(SP500)
    print 'reverting'
    reversed=[]
    for x in SP500:
        reversed.insert(0,x)
    BIG_DICT={}
    for x in reversed:
        #print x
        dict={}
        #---------------------------------------------------------------- Date=x
        #----------------------------------------------------------------- Open=
        #----------------------------------------------------------------- High=
        #------------------------------------------------------------------ Low=
        #---------------------------------------------------------------- Close=
        #--------------------------------------------------------------- Volume=
        #------------------------------------------------------------ Adj_Close=
        Date,Open,High,Low,Close,Volume,Adj_Close=x
        #print 'Date,Open,High,Low,Close,Volume,Adj_Close',Date,Open,High,Low,Close,Volume,Adj_Close
        #print "Date=%s, Open = %s , High= %s, Low=%s , Close=%s, Volume=%s,Adj_Close= %s " %(str(Date),Open,High,Low,Close,Volume,Adj_Close)
        dict['Open']=Open
        dict['High']=High
        dict['Low']=Low
        dict['Close']=Close
        dict['Volume']=Volume
        dict['Adj_Close']=Adj_Close
        BIG_DICT['Date']=dict
        
        
        
        
def printdata(stk):
    print 'stk = ',stk
    stkObj = StockQuote(stk)
    stkdata= {}
    stkdata['Ticker'] = stkObj.ticker()
    stkdata['Price'] = stkObj.lastPrice()
    stkdata['PE Ratio'] = stkObj.PEratio()
    stkdata['Volume'] = stkObj.volume()
    stkdata['Year Range'] = stkObj.yearrange()
    stkdata['Book Value per Share'] = stkObj.bookValue()
    stkdata['EBITDA'] = stkObj.EBITDA()
    stkdata['PEG Ratio'] = stkObj.PEGRatio()
    print(stkdata)  

def main():
    IBM_historical='IBM_historical.csv'
    SP_500='SP500.csv'
    data_file='/home/tomaszd/workspace/StatisticsAndTrends/Data/'+IBM_historical
    openCSVFile(data_file)


if __name__ == '__main__':
    main()
    print 'Finished script'