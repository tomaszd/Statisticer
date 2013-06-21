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


def get_data_from_cvs(sp_500_directory='/home/tomaszd/workspace/StatisticsAndTrends/Data/SP500.ods'):
    '''
    Opening the cvs file and create the historical_data dictionary with keys equal to
    
    daily_data[date]= {'Open':value,'High':value,'Low':value,'Close':value,'Volume':value,'Adj_Close':value}
    
    **Paramters** 
    
    *sp_500_directory* dir to file with data containing for company   Date,Open,High,Low,Close,Volume,Adj_Close
    
    *returns* : *dict* - the **historical_data** dict with keys to date in *YYYY-MM-DD* format and value is dict with : keys :
                            *'Date','Open','High','Low','Close','Volume','Adj_Close'*
    
     
    '''
    SP500 = csv.reader(open(sp_500_directory, 'rb'), delimiter=',')
    print type(SP500)
    print 'reverting'
    reversed=[]
    for x in SP500:
        reversed.insert(0,x)
    historical_data={}
    for x in reversed:
        daily_data={}
        Date,Open,High,Low,Close,Volume,Adj_Close=x
        #print 'Date,Open,High,Low,Close,Volume,Adj_Close',Date,Open,High,Low,Close,Volume,Adj_Close
        #print "Date=%s, Open = %s , High= %s, Low=%s , Close=%s, Volume=%s,Adj_Close= %s " %(str(Date),Open,High,Low,Close,Volume,Adj_Close)
        daily_data['Open']=Open
        daily_data['High']=High
        daily_data['Low']=Low
        daily_data['Close']=Close
        daily_data['Volume']=Volume
        daily_data['Adj_Close']=Adj_Close
        historical_data[Date]=daily_data
    for date,values in sorted(historical_data.items()):
        print 'For date : %s values are :%s'%(date,values)     
    return historical_data   
        
        
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
    get_data_from_cvs(data_file)


if __name__ == '__main__':
    main()
    print 'Finished script'