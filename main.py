# -*- coding: utf-8 -*-
from time import sleep
import pandas as pd
import openpyxl
from filtrando_dados import filtrar_dados
from filtrando_alvaro_secoes import filtrar_votos_alvaro_secoes
from filtrando_alvaro_locais_votacao import filtrar_votos_alvaro_locais_votacao
from filtrando_alvaro_bairros import filtrar_votos_alvaro_bairros

anos = ['2012', '2016', '2020']
dataframes = []
for ano in anos:
    df = filtrar_dados(ano, pd)
    dataframes.append(df)
final_df = pd.concat(dataframes, axis=0)
final_df.to_csv('eleicoes_nova_lima.csv', index=False)
df_votacao_alvaro_secoes = filtrar_votos_alvaro_secoes(pd)
df_votacao_alvaro_secoes.to_csv('resultados_votacao_alvaro_secoes.csv', sep=';', index=False)
df_votacao_alvaro_locais = filtrar_votos_alvaro_locais_votacao(pd)
df_votacao_alvaro_locais.to_csv('resultados_votacao_alvaro_locais.csv', sep=';', index=False)
df_votacao_alvaro_bairros = filtrar_votos_alvaro_bairros(pd)
df_votacao_alvaro_bairros.to_csv('resultados_votacao_alvaro_bairros.csv', sep=';', index=False)

