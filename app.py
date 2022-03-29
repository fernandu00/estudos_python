from flask import  Flask, render_template, request
import pandas as pd
import pandas_datareader as pdr
import yfinance
from datetime import date
from jinja2 import Environment



def pega_primeiro(acao, inicio, final):
    '''retorna o primeiro preco do periodo'''
    df = pdr.data.get_data_yahoo(acao, start=inicio, end=final)
    primeiro = df.head(1)
    primeiro = primeiro.iloc[0]['Adj Close']
    primeiro = str(round(primeiro, 2))
    return primeiro


def pega_ultimo(acao, inicio, final):
    '''retorna o ultimo preco do periodo'''
    df = pdr.data.get_data_yahoo(acao, start=inicio, end=final)
    ultimo = df[-1:]
    ultimo = ultimo.iloc[0]['Adj Close']
    # ult = ultimo.iloc[0]
    ultimo = str(round(ultimo, 2))
    return ultimo

def variacao(acao, inicio, final):
    df = pdr.data.get_data_yahoo(acao, start=inicio, end=final)
    primeiro = df.head(1)
    ultimo = df[-1:]
    variacao = pd.concat([primeiro, ultimo])
    variacao.head()
    var = variacao.pct_change()
    var = var.iloc[1]['Adj Close']
    return "{:.2%}".format(var)


def pega_minimo(acao, inicio, final):
    '''retorna menor preco do periodo'''
    df = pdr.data.get_data_yahoo(acao, start=inicio, end=final)
    ordenaMin = df.sort_values(by=['Adj Close'])
    ordem = ordenaMin.iloc[0]['Adj Close']
    minimo = str(round(ordem, 2))
    return minimo


def pega_maximo(acao, inicio, final):
    '''retorna preco maximo do periodo'''
    df = pdr.data.get_data_yahoo(acao, start=inicio, end=final)
    ordenaMax = df.sort_values(by=['Adj Close'], ascending=False)
    ordem = ordenaMax.iloc[0]['Adj Close']
    maximo = str(round(ordem, 2))
    return maximo



app = Flask(__name__,template_folder='templates')




@app.route('/',methods=['POST','GET'])
def form():
    return render_template('index.html')




@app.route('/proc',methods=['POST','GET'] )
def processa():
    if request.method == 'POST':
        acao = request.form.get("acao")
        inicio = request.form.get("inicio")
        final = request.form.get("final")
        return f'''<h1>{acao}</h1>
                    <h2> Primeiro Preço do Período: {pega_primeiro(acao,inicio,final)}</h2>
                   <h2> Último Preço do Período: {pega_ultimo(acao,inicio,final)}</h2>
                   <h2> Preço Mínimo do Período: {pega_minimo(acao,inicio,final)}</h2>
                    <h2> Preço Máximo do Período: {pega_maximo(acao,inicio,final)}</h2>
                    <h2> Variação do Período: {variacao(acao,inicio,final)}</h2>
                     

'''







        # df = pdr.data.get_data_yahoo(acao, start=inicio, end=final)
        # primeiro = df.head(1)
        # primeiro = primeiro.iloc[0]['Adj Close']
        # primeiro = str(round(primeiro, 2))
        # return f'''<h1>PREÇO DA {acao} no período foi de {primeiro}</h1>'''









if __name__ == '__main__':
    app.run(debug=True, port=5000)