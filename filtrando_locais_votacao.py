
def filtrar_locais_votacao(pd):
    df = pd.read_csv(f'eleicoes_nova_lima.csv', delimiter=",")
    df = df.drop(
        [
            'aa_eleicao',
            'nr_secao',
            'nr_votavel',
            'nm_votavel',
            'qt_votos',
            'qt_aptos',
            'qt_comparecimento',
            'qt_abstencoes'
        ], axis='columns')
    df = df.drop_duplicates(['nr_local_votacao', 'nm_local_votacao', 'ds_local_votacao_endereco'], keep='last')
    df = df.sort_values(by=['nr_local_votacao'], ascending=True)
    df = df[['nr_local_votacao', 'nm_local_votacao', 'ds_local_votacao_endereco']]

    linhas_finais = []
    locais_votacao = df['nm_local_votacao'].unique().tolist()
    for local in locais_votacao:
        df_local_votacao = df[df["nm_local_votacao"] == local]
        numero_local_votacao = df_local_votacao['nr_local_votacao'].unique().tolist()[0]
        nome_local_votacao = df_local_votacao['nm_local_votacao'].unique().tolist()[0].replace(",", ".")
        descricao_local_votacao = df_local_votacao['ds_local_votacao_endereco'].unique().tolist()[0].replace(",", ".")
        frame_linha = {'Nº Local de Votação': numero_local_votacao,
                       'Nome Local de Votação': nome_local_votacao,
                       'End. Local de Votação': descricao_local_votacao}
        linhas_finais.append(frame_linha)
    dataframe_enderecos = pd.DataFrame(linhas_finais)
    return dataframe_enderecos