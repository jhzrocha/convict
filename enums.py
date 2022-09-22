
from distutils.log import debug


class connectionData():
    local = 'localhost'
    user = 'root'
    password = ''
    dataBaseName = 'convict'

class sectors():
    sectorTypes = [{'Petróleo, Gás e Biocombustíveis':['Exploração, Refino e Distribuição', 'Equipamentos e Serviços']} ,
                   {'Mineração' : ['Minerais Metálicos']},
                   {'Siderurgia e Metalurgia': ['Siderurgia', 'Artefatos de Ferro e Aço', 'Artefatos de Cobre']},
                   {'Químicos' : ['Petroquímicos', 'Fertilizantes e Defensivos', 'Químicos Diversos']},
                   {'Madeira e Papel' : ['Madeira', 'Papel e Celulose']},
                   {'Embalagens': ['Embalagens']},
                   {'Materiais Diversos': ['Materiais Diversos']},
                   {'Construção e Engenharia' :['Produtos para Construção', 'Construção Pesada', 'Engenharia Consultiva']},
                   {'Material de Transporte': ['Material Aeronáutico e de Defesa','Material Rodoviário']},
                   {'Máquinas e Equipamentos': ['Motores, Compressores e Outros','Máq. e Equip. Industriais', 'Máq. e Equip. Construção e Agrícolas','Armas e Munições']},
                   {'Transporte' : ['Transporte Aéreo','Transporte Ferroviário','Transporte Hidroviário','Transporte Rodoviário','Exploração de Rodovias', 'Serviços de Apoio e Armazenagem']},
                    {'Serviços Diversos' : ['Serviços Diversos']},
                    {'Comércio':['Material de Transporte']},
                    {'Agropecuária':['Agricultura']},
                    {'Alimentos Processados':['Açucar e Alcool','Carnes e Derivados','Alimentos Diversos']},
                    {'Bebidas':['Cervejas e Refrigerantes']},
                    {'Produtos de Uso Pessoal e de Limpeza':['Produtos de Uso Pessoal','Produtos de Limpeza']},
                    {'Comércio e Distribuição':['Mercados']},
                    { 'Construção Civil':['Incorporações']},
                    {'Tecidos, Vestuário e Calçados':['Fios e Tecidos','Vestuário', 'Calçados', 'Acessórios']},
                    {'Utilidades Domésticas':['Eletrodomésticos','Móveis','Utensílios Domésticos']},
                    {'Automóveis e Motocicletas':['Automóveis e Motocicletas']},
                    {'Hoteis e Restaurantes': ['Hotelaria','Restaurante e Similares']},
                    {'Viagens e Lazer':['Bicicletas','Brinquedos e Jogos','Produção de Eventos e Shows','Viagens e Turismo','Atividades Esportivas']},
                    {'Comércio Diversos':['Serviços Educacionais','Aluguel de carros','Programas de Fidelização']},
                    {'Comércio':['Tecidos, Vestuário e Calçados','Eletrodomésticos','Produtos Diversos']},
                    {'Medicamentos e Outros Produtos':['Medicamentos e Outros Produtos']},
                    {'Serviços Médico - Hospitalares, Análises e Diagnósticos':['Serviços Médico - Hospitalares, Análises e Diagnósticos']},
                    {'Equipamentos de saúde':['Equipamentos']},
                    {'Comércio e Distribuição de saúde':['Medicamentos e Outros Produtos']},
                    {'Computadores e Equipamentos':['Computadores e Equipamentos']},
                    {'Programas e Serviços':['Programas e Serviços']},
                    {'Telecomunicações':['Telecomunicações']},
                    {'Mídia':['Produção e Difusão de Filmes e Programas','Publicidade e Propaganda']},
                    {'Energia Elétrica':['Energia Elétrica']},
                    {'Água e Saneamento':['Água e Saneamento']},
                    {'Gás':['Gás']},
                    {'Intermediários Financeiros':['Bancos','Soc. Crédito e Financiamento', 'Soc. Arrendamento Mercantil']},
                    {'Securitizadoras de Recebíveis':['Securitizadoras de Recebíveis']},
                    {'Serviços Financeiros Diversos':['Gestão de Recursos e Investimentos','Serviços Financeiros Diversos']},
                    {'Previdência e Seguros':['Seguradoras','Resseguradoras','Corretoras de Seguros e Resseguros']},
                    {'Exploração de Imóveis' : ['Exploração de Imóveis','Intermediação Imobiliária']},
                    {'Holdings Diversificadas' : ['Holdings Diversificadas']},
                    {'Outros Títulos':['Outros Títulos']},
                    {'Outros':['Outros']}]





class shareSectors():
    sector = { 'Petróleo': 
                    {'Exploração, Refino e distribuição de petróleo' : ['RRRP', 'CSAN', 'DMMO', 'ENAT', 'RPMG', 'PETR', 'RECV' , 'PRIO', 'UGPA', 'VBBR'],                    
                     'Equipamentos e serviços de petróleo' : ['LUPA', 'OPCT', 'OSXB'] },
                'Mineração': 
                    {'Mineração de minerais metálicos': ['AURA', 'BRAP', 'CBAV', 'CMIN', 'LTEL', 'LTLA', 'MMXM', 'VALE']},
                'Siderurgia e Metalurgia':
                    {'Siderurgia' : ['FESA','GGBR','GOAU','CSNA','USIM'],
                     'Artefatos de Ferro e Aço': ['MGEL','PATI','TKNO'],
                     'Artefatos de Cobre': ['PMAM']},
                'Químicos':
                    {'Petroquímicos' : ['BRKM','DEXP'],
                    'Fertilizantes e Defensivos' : ['FHER','NUTR','VITT'],
                    'Químicos Diversos' : ['CRPG','UNIP']},
                'Madeira e Papel:':
                    {'Madeira': ['DXCO','EUCA'],
                    'Papel e Celulose': ['KLBN','MSPA','NEMO','SUZB']},
                'Embalagens':
                    {'Embalagens': ['RANI','MTIG']},
                'Materiais Diversos':
                    {'Materiais Diversos': ['SNSY']},
                'Construção e Engenharia':
                    {'Produtos para Construção':['ETER','HAGA','PTBL'],
                     'Construção Pesada' : ['AZEV'],
                     'Engenharia Consultiva' : ['SOND','TCNO']},
                'Material de Transporte':
                    {'Material Aeronáutico': ['EMBR'],
                     'Material Rodoviário' : ['FRAS','POMO','RAPT','RCSL','RSUL','TUPY','MWET']}
            }