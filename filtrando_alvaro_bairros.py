def filtrar_votos_alvaro_bairros(pd):
    df_votacao_alvaro_locais = pd.read_csv('resultados_votacao_alvaro_locais.csv', delimiter=";")
    bairros = df_votacao_alvaro_locais['Bairro Locat Vot.'].unique().tolist()
    bairros.sort()
    df = df_votacao_alvaro_locais.drop([
        'Nº Local Vot.',
        'Nome Local Vot.'], axis='columns'
    )
    linhas_final = []
    for bairro in bairros:
        df_bairro = df[df["Bairro Locat Vot."] == bairro]
        anos_bairros = df_bairro['Ano'].unique().tolist()
        for ano in anos_bairros:
            df_bairro_ano = df_bairro[df_bairro["Ano"] == ano]
            quant_eleitores = df_bairro_ano['Quantidade Eleitores'].sum()
            quant_comparecimento = df_bairro_ano['Quantidade Comparecimento'].sum()
            quant_abstencoes = df_bairro_ano['Quantidade Abstenções'].sum()
            votos_nulos = df_bairro_ano['Votos Nulos'].sum()
            votos_brancos = df_bairro_ano['Votos Brancos'].sum()
            votos_alvaro = df_bairro_ano['Votos Alvaro'].sum()
            votos_validos = df_bairro_ano['Votos Validos'].sum()
            percentual_votos_validos = round(votos_alvaro / votos_validos * 100, 2)
            frame_linha = {'Ano': ano,
                           'Bairro': bairro,
                           'Quantidade Eleitores': quant_eleitores,
                           'Quantidade Comparecimento': quant_comparecimento,
                           'Quantidade Abstenções': quant_abstencoes,
                           'Votos Nulos': votos_nulos,
                           'Votos Brancos': votos_brancos,
                           'Votos Alvaro': votos_alvaro,
                           'Votos Validos': votos_validos,
                           'Perc. Votos Validos': percentual_votos_validos}
            linhas_final.append(frame_linha)
    dataframe_final = pd.DataFrame(linhas_final)
    return dataframe_final
