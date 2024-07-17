def filtrar_votos_alvaro_locais_votacao(pd):
    df_votacao_alvaro_secoes = pd.read_csv('resultados_votacao_alvaro_secoes.csv', delimiter=";")
    locais_votacao = df_votacao_alvaro_secoes['Nº Local Vot.'].unique().tolist()
    locais_votacao.sort()
    df = df_votacao_alvaro_secoes.drop(
        'Seção', axis='columns'
    )
    linhas_final = []
    for local_votacao in locais_votacao:
        df_local_votacao = df[df["Nº Local Vot."] == local_votacao]
        anos_local_votacao = df_local_votacao['Ano'].unique().tolist()
        for ano in anos_local_votacao:
            df_local_ano = df_local_votacao[df_local_votacao["Ano"] == ano]
            nomes_locais_votacao = df_local_ano['Nome Local Vot.'].unique().tolist()
            if len(nomes_locais_votacao) == 1:
                nome_local_votacao = nomes_locais_votacao[0].replace(",", ".")
            else:
                nome_agrupado = [nomes_locais_votacao[0].replace(",", ".")]
                for i in range(1, len(nomes_locais_votacao)):
                    nome_agrupado.append(" / " + nomes_locais_votacao[i].replace(",", "."))
                nome_local_votacao = "".join([str(item) for item in nome_agrupado])
            bairro_local_votacao = df_local_ano['Bairro Locat Vot.'].unique().tolist()[0]
            quant_eleitores = df_local_ano['Quantidade Eleitores'].sum()
            quant_comparecimento = df_local_ano['Quantidade Comparecimento'].sum()
            quant_abstencoes = df_local_ano['Quantidade Abstenções'].sum()
            votos_nulos = df_local_ano['Votos Nulos'].sum()
            votos_brancos = df_local_ano['Votos Brancos'].sum()
            votos_alvaro = df_local_ano['Votos Alvaro'].sum()
            votos_validos = df_local_ano['Votos Validos'].sum()
            percentual_votos_validos = round(votos_alvaro / votos_validos * 100, 2)
            frame_linha = {'Ano': ano,
                           'Nº Local Vot.': local_votacao,
                           'Nome Local Vot.': nome_local_votacao,
                           'Bairro Locat Vot.': bairro_local_votacao,
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
