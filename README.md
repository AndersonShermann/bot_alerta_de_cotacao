## 🪙 Cripto Bot
Um projeto simples em Python para monitorar os preços de criptomoedas em tempo real e enviar notificações baseadas em limites de compra e venda.

## 📋 Descrição
O Cripto Bot acompanha os preços das criptomoedas Bitcoin (BTC) e Ethereum (ETH) e dispara alertas no sistema operacional quando os valores atingem os limites configurados para compra ou venda.

## ⚡ Funcionalidades principais:

Busca de preços em tempo real usando Yahoo Finance.
Envio de notificações personalizadas com winotify.
Configuração simples de limites para cada criptomoeda.

## 🛠️ Como Funciona
Bibliotecas Utilizadas
Certifique-se de instalar as dependências abaixo antes de executar o código:

bash
Copiar código
pip install yfinance winotify
Configuração
No código, configure as seguintes variáveis:

symbols: Criptomoedas a serem monitoradas (padrão: BTC e ETH).
upper_limits: Limites superiores para alerta de venda.
lower_limits: Limites inferiores para alerta de compra.
Exemplo:

python
Copiar código
symbols = ['btc-usd', 'eth-usd']
upper_limits = [91100, 3000]  # Limite de venda para BTC e ETH
lower_limits = [90200, 3050]  # Limite de compra para BTC e ETH
Execução
Execute o script para iniciar o monitoramento contínuo:

bash
Copiar código
python cripto_bot.py
## 🔔 Notificações
O Cripto Bot usa a biblioteca winotify para exibir notificações no Windows.

Compra:
Enviado quando o preço cai abaixo do limite configurado.
Venda:
Enviado quando o preço supera o limite configurado.
Os ícones para notificações podem ser personalizados substituindo os arquivos comprar.png e vender.png.

## 📂 Organização do Projeto
cripto_bot.py: Arquivo principal do script.
comprar.png: Ícone para notificações de compra.
vender.png: Ícone para notificações de venda.

## 📈 Melhorias Futuras
Adicionar suporte para mais criptomoedas.
Implementar interface gráfica para facilitar o uso.
Exportar logs de preços monitorados.

## 📜 Licença
Este projeto é de uso livre sob a licença MIT. Sinta-se à vontade para modificá-lo e utilizá-lo como desejar.

💬 Dúvidas ou sugestões? Entre em contato ou abra uma issue no repositório! 
