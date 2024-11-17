import time
from datetime import datetime
import os
import yfinance as yf
from winotify import Notification, audio

symbols = ['btc-usd', 'eth-usd']
tickers = yf.Tickers(','.join(symbols))

for symbol in symbols:
    print(tickers.tickers[symbol.upper()].history(period='1d')['Close'][0])

upper_limits = [91000, 3150]
lower_limits = [90200, 3050]

while True:
    last_price = [tickers.tickers[symbol.upper()].history(period='1d')['Close'][0] for symbol in symbols]
    print(datetime.now())
    print(last_price)
    time.sleep(4)
    for i in range (len(symbols)):
        if last_price[i] > upper_limits[i]:
            #alerta de venda
            toast = Notification(app_id='Cripto Bot',
                                 title='Alerta de preço para ' + symbols[i].upper(),
                                 msg=f'{symbols[i].upper()} atingiu o preço de {last_price[i]:.2f}. Boa hora pra vender',
                                 icon=os.path.join(os.getcwd(), 'vender.png'),
                                 duration='long'
                                 )
            toast.add_actions(label='Ir para Exchange', launch='#')
            toast.set_audio(audio.LoopingAlarm, loop=False)
            toast.show()
        elif last_price[i] < lower_limits[i]:
            #alerta de compra
            toast = Notification(app_id='Cripto Bot',
                                 title='Alerta de preço para ' + symbols[i].upper(),
                                 msg=f'{symbols[i].upper()} atingiu o preço de {last_price[i]:.2f}. Boa hora pra comprar',
                                 icon=os.path.join(os.getcwd(), 'comprar.png'),
                                 duration='long'
                                 )
            toast.add_actions(label='Ir para Exchange', launch='#')
            toast.set_audio(audio.LoopingAlarm, loop=False)
            toast.show()
            time.sleep(1) #evitar notificações silmultaneas