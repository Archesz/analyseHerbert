import streamlit as st
import pandas as pd

import graphs as pg
import clear as cl

regras = {
    "Unicamp": [66, '5h00']
}

cursos = ['Selecione', 'Administração (Noturno)', 'Administração Publica (Noturno)', 'Arquitetura e Urbanismo (Noturno)', 'Artes Cênicas (Integral)', 'Artes Visuais (Integral)', 'Ciência da Computação (Noturno)', 'Ciências Biológicas – Licenciatura (Noturno)', 'Ciências Biológicas (Integral)', 'Ciências do Esporte (Integral)', 'Ciências Econômicas (Integral)', 'Ciências Econômicas (Noturno)', 'Ciências Sociais (Integral)', 'Ciências Sociais (Noturno)', 'Comunicação Social-Midialogia (Integral)', 'Dança (Integral)', 'Educação Física (Integral)', 'Educação Física (Noturno)', 'Enfermagem (Integral)', 'Curso 51 – Ingresso para: Engenharia Física (Integral) Física (Integral) Física: Física Médica e Biomédica (Integral) Matemática (integral) Matemática Aplicada e Computacional (Integral)', 'Engenharia Agrícola (Integral)', 'Engenharia Ambiental (Noturno)', 'Engenharia Civil (Integral)', 'Engenharia de Alimentos (Integral)', 'Engenharia de Alimentos (Noturno)', 'Engenharia de Computação (Integral)', 'Engenharia de Controle e Automação (Noturno)', 'Engenharia de Manufatura (Integral)', 'Engenharia de Produção (Integral)', 'Engenharia de Telecomunicações (Integral)', 'Engenharia de Transportes (Noturno)', 'Engenharia Elétrica (Integral)', 'Engenharia Elétrica (Noturno)', 'Engenharia Mecânica (Integral)', 'Engenharia Química (Integral)', 'Engenharia Química (Noturno)', 'Estatística (Integral)', 'Estudos Literários (I)', 'Farmácia (Integral)', 'Filosofia (Integral)', 'Física – Licenciatura (Noturno)', 'Fonoaudiologia (Integral)', 'Geografia (Integral)', 'Geografia (Noturno)', 'Geologia (Integral)', 'Historia (Integral)', 'Letras – Licenciatura (Integral)', 'Letras – Licenciatura (Noturno)', 'Licenciatura Integrada Química/Física (Noturno)', 'Linguística (Integral)', 'Matemática – Licenciatura (Noturno)', 'Medicina (Integral)', 'Nutrição (Integral)', 'Odontologia (Integral)', 'Pedagogia – Licenciatura (Integral)', 'Pedagogia – Licenciatura (Noturno)', 'Química (Integral)', 'Química Tecnológica (Noturno)', 'Sistemas de Informação (Integral)', 'Tecnologia em Analise e Des. de Sist. (Noturno)', 'Tecnologia em Saneamento Ambiental (Noturno)']

view_students = True

vestibular = "Unicamp"

simulados = {
    "Simulado Unicamp 01": "simulado.csv",
    "Colmeias": "SimuladoComeia.csv",
}

simulado_select = st.selectbox("Escolha o Simulado", ["Simulado Unicamp 01", "Colmeias"])

#df_base = pd.read_csv("simulado.csv")
#data = pd.read_csv("cursos.csv", sep=";")
df_base = pd.read_csv(simulados[simulado_select])
# Passar os dados para limpeza
df = cl.clear(df_base, simulado_select)
#banco = pd.read_csv("bancoQuestoes.csv", sep=",")

#data = cl.clear_cursos(data)

st.warning("Esse projeto é parte do Projeto L.U.N.A.H | Desenvolvedor: Jovi | Em fase de desenvolvimento")

with st.container():
    st.header("Modo ADM")
    st.markdown("Caso seja necessário visualizar nomes e dados específicos sobre os estudantes (Com intuíto de auxiliar), insira abaixo o código: ")

    password = st.text_input("Enter a password", type="password")
    btnPass = st.button("Ativar")

    if btnPass:
        if password == "projetoHerbert2023":
            view_students = True
            st.success('Credencial Válida :)')

        else:
            st.error('Credencial Inválida :(')
        

st.title("Análise de Dados | Simulado Herbert")
st.text("Essa análise foi feita utilizando os dados do simulado de 28/05/2023.")
st.markdown("A análise foi feita por **Jovi**, utilizando auxilio de L.U.N.A | Versão 0.2.7")

st.divider()

# Análises Gerais

with st.container():
    st.header("Análises Gerais: ")

    st.text(f"Número de Alunos: {df.shape[0]}")
    st.text(f"Número de Questões: {regras[vestibular][0]}")
    st.text(f"Tempo de Prova: {regras[vestibular][1]}")

    st.dataframe(df.describe())

    st.text("Resumo do Simulado: ")
    st.text(f"Menor Número de Acertos: {min(df['NotaTotal'])}/25")
    st.text(f"Média Geral de Acertos: {round(df['NotaTotal'].mean())}/25")
    st.text(f"Maior Número de Acertos: {max(df['NotaTotal'])}/25")

    #st.text(" ")
    #st.markdown("**Resumo gerado por L.U.N.A**")
    #st.markdown("**Tamanho da Amostra**:")
    #st.markdown("Pelas informações que tenho acesso, a quantidade de alunos que realizaram o simulado é abaixo do esperado para a quantidade dos estudantes presentes no Herbert. Nossa amostra conta com 38 estudantes, o cálculo sugere que necessitariamos de 62 estudantes para garantir melhores precisões nos resultados futuros.")
#
    #st.markdown("**Nota Total**:")
    #st.markdown("A nota total é a quantidade de acertos realizado pelos estudantes. A informação que possuo indica que não foram colocadas questões de Inglês. Dessa forma, a média dos estudantes foi 29 questões. Com desvio padrão de 7 questões.")
    #st.markdown("Considerando a média de acertos em inglês com 4 questões, caso atribuimos esse valor aos estudantes e analisando os últimos vestibulares da COMVEST, a média geral de pontuação não é suficientemente boa, no entanto, levando em consideração o fato de ser o primeiro simulado, a taxa de evolução média sugere que os resultados podem ser satisfatório para uma parcela considerável dos estudantes.")     

st.divider()

# Análises por Disciplina
with st.container():
    st.header("Análise Por Períodos: ")
    st.markdown(f"**Objetivo**: Compreender o desempenho dos estudantes dos diferentes períodos no simulado.")

    periodo = st.selectbox("Período: ", ["Geral", "Manhã", "Tarde", "Noite"])

    # Gráfico barras
    pg.show_disiciplina(df, periodo)    

    with st.expander("Sugestões de Perguntas e Observações"):
        st.write("""
                - Quais períodos estão com a média abaixo dos outros?\n
                - Qual conteúdo os professores de determinado período já passaram?
                - Matérias correlatas (Ex: Física e Química) estão com médias muito diferentes? Por que?
                """)

# Scatter Periodo X Assunto
with st.container():
    st.header("Análise Box Por Períodos: ")
    disciplina = st.selectbox("Disciplina: ", ["Total", "Matematica", "Fisica", "Quimica", "Biologia",
                                               "Historia", "Sociologia", "Filosofia", "Gramatica", "Literatura", "Geografia"])
    pg.scatter_view(df, disciplina, view_students)

    with st.expander("Sugestões de Perguntas e Observações"):
        st.write("""
                - A distribuição na minha disciplina está com alta descrepância?\n
                - A frequência de alunos na aula parece coerente com as notas?
                - Estudantes com pontuações muito abaixo da média em disciplinas específicas necessitam de um auxilio extra? 
                """)

with st.container():
    st.header("Comparação de Pontuação entre Disciplinas")
    st.markdown(f"**Objetivo**: Verificar a relação nos estudantes entre diferentes disciplinas.")

    disciplina1 = st.selectbox("Disciplina 1: ", ["Total", "Matematica", "Fisica", "Quimica", "Biologia",
                                               "Historia", "Sociologia", "Filosofia", "Gramatica", "Literatura", "Geografia"])
    
    disciplina2 = st.selectbox("Disciplina 2: ", ["Total", "Matematica", "Fisica", "Quimica", "Biologia",
                                               "Historia", "Sociologia", "Gramatica", "Literatura", "Geografia"])

    pg.compare_disciplinas(df, disciplina1, disciplina2)

    with st.expander("Sugestões de Perguntas e Observações"):
        st.write("""
                - Disciplinas da mesma área (Ex: História e Geografia) estão alinhadas com as pontuações?\n
                - Disciplinas de áreas diferentes (Ex: Matemática e Biologia) que possuam grande diferença na pontuação, poderiam fazer alguma aula conjunta?
                """)

with st.container():
    st.header("Distribuição por disciplina")
    st.markdown(f"**Objetivo**: Verificar a distribuição de acertos por Disciplina e Período.")

    disciplinaHist = st.selectbox("Escolha a Disciplina: ", ["Total", "Matematica", "Fisica", "Quimica", "Biologia",
                                               "Historia", "Sociologia", "Filosofia", "Gramatica", "Literatura", "Geografia"])
    periodo = st.selectbox("Escolha o Período: ", ["Geral", "Manhã", "Tarde", "Noite"])

    pg.histogramDist(df, disciplinaHist, periodo)

    with st.expander("Sugestões de Perguntas e Observações"):
        st.write("""
                - Em seu período, houve mais notas "preocupantes" do que em outros? Quais possíveis motivos?\n
                """)


with st.container():
    st.header("Identificar Déficit")
    st.markdown(f"**Objetivo**: Compreender em qual período está o maior défict entre os estudantes.")

    disciplinaDefict = st.selectbox("Qual disciplina: ", ["Total", "Matematica", "Fisica", "Quimica", "Biologia", "Geografia",
                                               "Historia", "Sociologia", "Filosofia", "Gramatica", "Literatura"])
    
    pg.deficts(df, disciplinaDefict)

    st.text("Obs: O défict é a média dos déficts de todos os alunos do periodo. O défict de cada aluno é calculado com: ")
    st.latex("f(x, z) = \\frac{x}{z} = y")
    st.text("x: Quantidade de questões corretas disciplina.")
    st.text("z: Quantidade total de questões da disciplina.")
    st.text("Dessa forma, quanto maior o valor, maior o défict.")

with st.container():
    st.header("Análise de Questões")
    st.markdown(f"**Objetivo**: Analisar questões específicas e verificar quais foram as alternativas selecionadas, buscando entender o pensamento dos estudantes.")

    st.markdown("Caso precise verificar o simulado, basta clicar aqui: [Simulado 202301](https://drive.google.com/file/d/1zrNFtx6iYo5VwHAUMBv6J8JH__58X1ka/view?usp=sharing)")

    questao = st.number_input("Selecione o Número da questão: ", min_value=1, max_value=66, step=1)

    pg.view_questions(df, questao)

    with st.expander("Sugestões de Perguntas e Observações"):
        st.write("""
                - Por que os estudantes optaram por alternativas erradas especificas?\n
                """)

with st.container():
    st.header("Analise Individual do Estudante: ")

    aluno = st.selectbox("Selecione o Estudante: ", list(df["Nome"]))
    pg.plot_student(df, aluno)
    
with st.container():
    periodo = st.selectbox("Período Para Identificar: ", ["Geral", "Manhã", "Tarde", "Noite"])
    pg.viewDefictsTags(periodo)

with st.container():
    aluno = st.selectbox("Aluno: ", list(df["Nome"]))
    pg.identifyByStudent(aluno)

with st.container():
    st.header("Verificar Nota de Corte")
    st.markdown("**Objetivo**: Verificar quantos estudantes passariam na nota de corte de determinado curso.")
    st.markdown("O simulado foi feito co 6 questões a menos (Inglês), considerando que a média de acertos em inglês é 4, a analise será feita com uma soma de 4 questões aos estudantes.")

    curso = st.selectbox("Curso: ", cursos) 

    if curso != "Selecione":
        pg.get_cursos(data, df, curso)
