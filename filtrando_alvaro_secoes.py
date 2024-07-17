def filtrar_votos_alvaro_secoes(pd):
    df_votacao_geral = pd.read_csv('eleicoes_nova_lima.csv', delimiter=",")
    df_votacao_nominal_alvaro = df_votacao_geral[
        df_votacao_geral["nm_votavel"].str.contains("ALONSO PEREZ MORAIS DE AZEVEDO")]
    df_votacao_nominal_alvaro = df_votacao_nominal_alvaro.assign(nm_votavel='ALVARO')
    df_votacao_nulo = df_votacao_geral[df_votacao_geral["nm_votavel"].str.contains("VOTO NULO")]
    df_votacao_branco = df_votacao_geral[df_votacao_geral["nm_votavel"].str.contains("VOTO BRANCO")]
    df = pd.concat([df_votacao_nominal_alvaro, df_votacao_nulo, df_votacao_branco], axis=0)
    df = df.sort_values(by=['nr_secao', 'nr_local_votacao', 'aa_eleicao', 'nm_votavel'], ascending=True)
    df = df[['nr_secao',
             'aa_eleicao',
             'nr_local_votacao',
             'nm_local_votacao',
             'nr_votavel',
             'nm_votavel',
             'qt_aptos',
             'qt_comparecimento',
             'qt_abstencoes',
             'qt_votos']]

    df_bairros = pd.read_csv('bairros_nova_lima.csv', delimiter=";")

    linhas_final = []
    numeros_secoes = df['nr_secao'].unique().tolist()
    for secao in numeros_secoes:
        df_secao = df[df["nr_secao"] == secao]
        anos_da_secao = df_secao['aa_eleicao'].unique().tolist()
        for ano in anos_da_secao:
            df_secao_ano = df_secao[df_secao["aa_eleicao"] == ano]
            numero_local_votacao = df_secao_ano['nr_local_votacao'].unique().tolist()[0]
            nome_local_votacao = df_secao_ano['nm_local_votacao'].unique().tolist()[0].replace(",", ".")
            df_bairro_local_votacao = df_bairros[df_bairros['LocalVotacao'] == numero_local_votacao]
            bairro_local_votacao = df_bairro_local_votacao['Bairro'].unique().tolist()[0]
            qt_eleitores = df_secao_ano['qt_aptos'].unique().tolist()[0]
            qt_comparecimento = df_secao_ano['qt_comparecimento'].unique().tolist()[0]
            qt_abstencoes = df_secao_ano['qt_abstencoes'].unique().tolist()[0]
            frame_linha = {'Seção': secao,
                           'Ano': ano,
                           'Nº Local Vot.': numero_local_votacao,
                           'Nome Local Vot.': nome_local_votacao,
                           'Bairro Locat Vot.': bairro_local_votacao,
                           'Quantidade Eleitores': qt_eleitores,
                           'Quantidade Comparecimento': qt_comparecimento,
                           'Quantidade Abstenções': qt_abstencoes}
            df_alvaro = df_secao_ano[df_secao_ano["nm_votavel"].str.contains("ALVARO")]
            df_branco = df_secao_ano[df_secao_ano["nm_votavel"].str.contains("BRANCO")]
            df_nulo = df_secao_ano[df_secao_ano["nm_votavel"].str.contains("NULO")]
            if df_alvaro.empty:
                votos_alvaro = 0
            else:
                votos_alvaro = df_alvaro['qt_votos'].unique().tolist()[0]
            if df_branco.empty:
                votos_branco = 0
            else:
                votos_branco = df_branco['qt_votos'].unique().tolist()[0]
            if df_nulo.empty:
                votos_nulo = 0
            else:
                votos_nulo = df_nulo['qt_votos'].unique().tolist()[0]
            frame_linha['Votos Nulos'] = votos_nulo
            frame_linha['Votos Brancos'] = votos_branco
            frame_linha['Votos Alvaro'] = votos_alvaro
            votos_validos = qt_comparecimento - votos_nulo - votos_branco
            frame_linha['Votos Validos'] = votos_validos
            percentual_votos_validos = round(votos_alvaro/votos_validos * 100, 2)
            frame_linha['Perc. Votos Validos'] = percentual_votos_validos
            linhas_final.append(frame_linha)
    dataframe_final = pd.DataFrame(linhas_final)

    # for x in range(1, 298):
    #     if x in df['nr_secao'].values:
    #         numero_vezes_original = df['nr_secao'].value_counts()[x]
    #         numero_vezes_novo = dataframe_final['Seção'].value_counts()[x]
    #         if numero_vezes_novo != numero_vezes_original / 3:
    #             print(f"Ha um problema na secao {x}. Numero de vezes do original: {numero_vezes_original}. Numero de vezes do novo: {numero_vezes_novo}")

    return dataframe_final
