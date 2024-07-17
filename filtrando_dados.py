
def filtrar_dados(ano, pd):
    df = pd.read_csv(f'./dados_brutos/{ano}.csv', delimiter=";", encoding='latin-1')
    df = df.drop(['cd_tipo_eleicao',
                  'nm_tipo_eleicao',
                  'ds_local_votacao_endereco',
                  'cd_eleicao',
                  'ds_eleicao',
                  'dt_eleicao',
                  'sq_candidato',
                  'sg_uf',
                  'cd_municipio',
                  'nm_municipio',
                  'nr_zona',
                  'cd_modelo_urna',
                  'ds_modelo_urna',
                  'nr_turno',
                  'ds_cargo',
                  'dt_carga',
                  'qt_registros'], axis='columns')
    df = df[['aa_eleicao', 'nr_local_votacao', 'nm_local_votacao', 'nr_secao', 'nr_votavel', 'nm_votavel', 'qt_aptos',
             'qt_comparecimento', 'qt_abstencoes', 'qt_votos']]
    return df