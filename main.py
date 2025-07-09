import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Definir tickers de activos
assets = {
    'S&P_500': '^GSPC',       # Índice bursátil de EE. UU.
    'Gold': 'GC=F',           # Futuros del oro
    'Crude_Oil': 'CL=F',      # Petróleo crudo (WTI)
    'US_Treasury_ETF': 'TLT'  # ETF de bonos del Tesoro de EE. UU.
}

# Rango de fechas para el estudio
start_date = '2025-02-01'
end_date = '2025-04-30'

# Definir carpeta de salida (en la misma carpeta del script)
output_dir = os.path.dirname(os.path.abspath(__file__))
prices_path = os.path.join(output_dir, 'traditional_assets_prices.csv')
returns_path = os.path.join(output_dir, 'traditional_assets_log_returns.csv')

try:
    # Descargar precios ajustados de cierre
    full_data = yf.download(list(assets.values()), start=start_date, end=end_date)
    data = full_data['Close']
    data.columns = list(assets.keys())
    data = data.dropna()
    returns = np.log(data / data.shift(1)).dropna()
except Exception as e:
    print(f"❌ Error al descargar o procesar los datos: {e}")
    exit(1)

# Mostrar primeras filas de los retornos logarítmicos
print("\n📈 Primeras filas de los retornos logarítmicos diarios:")
print(returns.head())

# Graficar precios
ax1 = data.plot(title='Precios de Activos (Feb–Abr 2025)', figsize=(10, 5))
ax1.set_xlabel('Fecha')
ax1.set_ylabel('Precio (USD)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Graficar retornos logarítmicos
ax2 = returns.plot(title='Retornos Logarítmicos Diarios (Feb–Abr 2025)', figsize=(10, 5))
ax2.set_xlabel('Fecha')
ax2.set_ylabel('Retorno Logarítmico')
plt.grid(True)
plt.tight_layout()
plt.show()

# Guardar archivos CSV
try:
    data.to_csv(prices_path)
    returns.to_csv(returns_path)
    print(f"✅ Precios guardados en: {prices_path}")
    print(f"✅ Retornos guardados en: {returns_path}")
except Exception as e:
    print(f"❌ Error al guardar los archivos CSV: {e}")
