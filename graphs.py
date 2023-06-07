import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd

gabarito = ["D", "D", "B", "A", "C", "C", "D", "C", "B", "D", "C", "D", "D", "A", "D", "B", "D", "B", "A", "C", "C", "B", "A", "D", "C", "A", "B", "B", "C", "A", "D", "A",
            "A", "B", "C", "B", "B", "A", "C", "B", "B", "D", "B", "A", "C", "B", "D", "B", "B", "B", "D", "C", "C", "D", "C", "A", "D", "C", "B", "D", "C", "D", "B", "C", "D", "D"]

numero_questoes = {
    "Total": 66,
    "Matematica": 12,
    "Fisica": 7,
    "Quimica": 7,
    "Biologia": 7,
    "Historia": 7,
    "Geografia": 7,
    "Sociologia": 3,
    "Filosofia": 3,
    "Gramatica": 6,
    "Literatura": 7,
}

def show_disiciplina(df, periodo):

    totais = ["NotaTotal", "NotaMatematica", "NotaFisica", "NotaQuimica", "NotaBiologia", "NotaHistoria", "NotaGeografia", "NotaSociologia", "NotaFilosofia", "NotaGramatica", "NotaLiteratura"]
    medias = []

    totaisMax = [66, 12, 7, 7, 7, 7, 7, 3, 3, 6, 7]

    if periodo == "Geral":
        df = df
    elif periodo == "Manhã":
        df = df.query("Período == 'Manhã'")
    elif periodo == "Tarde":
        df = df.query("Período == 'Tarde'")
    elif periodo == "Noite":
        df = df.query("Período == 'Noite'")

    for i in range(0, len(totais)):
        total = totais[i]
        media = df[total].mean()
        medias.append(round(media))
        
    fig = px.bar(x=totais, y=medias, color=totais, text=medias, labels={"y": "Média", "x": "Disciplinas"})
    fig.update_traces(texttemplate='%{text:.2s}')
        
    fig.add_trace(go.Bar(
        x=totais,
        y=totaisMax,
        name='Quantidade Máxima de Questões',
        marker_color="red",
        opacity=0.6,
        text=totaisMax,
    ))

    fig.update_layout(
        title=f'Médias dos Estudantes de {periodo}',
        xaxis=dict(title='Matéria'),
        yaxis=dict(title='Média/Quantidade Máxima'),
    )

    fig.update_layout(xaxis={'categoryorder':'total descending'})
    fig.update_traces(texttemplate='%{text:.2s}')

    st.plotly_chart(fig)

def scatter_view(df, disciplina, view_students):
    if view_students:
        fig = px.box(df, 
                    x="Período", y=f"Nota{disciplina}", hover_data=["Nome", "Período"], 
                    color="Período",
                    title="Distribuição de Notas nos Períodos",
                    points="all"
                    )
    else:
        fig = px.box(df, 
                    x="Período", y=f"Nota{disciplina}",  
                    color="Período",
                    title="Distribuição de Notas nos Períodos",
                    points="all"
                    )
    st.plotly_chart(fig)

def compare_disciplinas(df, disciplina1, disciplina2):
    fig = px.scatter(df,
                    x=f"Nota{disciplina1}",
                    y=f"Nota{disciplina2}",
                    color=f"Nota{disciplina1}",
                    title=f"{disciplina1} vs {disciplina2}",
                    hover_data=["Nome", "Período"],
                    trendline_scope="overall")
    
    fig.update_traces(texttemplate='%{text:.2s}')

    st.plotly_chart(fig)

def histogramDist(df, disciplina, periodo):
    if periodo == "Geral":
        df = df
    else:
        df = df.query(f"Período == '{periodo}'")

    fig = px.histogram(df,
                       x=f"Nota{disciplina}",
                       title=f"Distribuição das pontuações em {disciplina} | {periodo}")
    
    st.plotly_chart(fig)

def deficts(df, disciplina):
    maximo = numero_questoes[disciplina]

    deficts_manha = []
    deficts_tarde = []
    deficts_noite = []

    notas_manha = list(df.query("Período == 'Manhã'")[f"Nota{disciplina}"])
    notas_tarde = list(df.query("Período == 'Tarde'")[f"Nota{disciplina}"])
    notas_noite = list(df.query("Período == 'Noite'")[f"Nota{disciplina}"])

    for i in notas_manha:
        proporcao = i/maximo
        deficts_manha.append(proporcao)    

    for i in notas_tarde:
        proporcao = i/maximo
        deficts_tarde.append(proporcao)    

    for i in notas_noite:
        proporcao = i/maximo
        deficts_noite.append(proporcao)    

    media_manha = round(1 - pd.Series(deficts_manha).mean(), 5)
    media_tarde = round(1 - pd.Series(deficts_tarde).mean(), 5)
    media_noite = round(1 - pd.Series(deficts_noite).mean(), 5)

    fig = px.bar(y=[media_manha, media_tarde, media_noite], x=["Manhã", "Tarde", "Noite"], color=["Manhã", "Tarde", "Noite"],
                 title="Déficts na prova por disciplina em cada período", labels={"y": "Défict", "x": "Períodos"})
    
    st.plotly_chart(fig)

def view_questions(df, question):
    questoes = df.columns[2:68]
    coluna = questoes[question-1]
    correta = gabarito[question - 1]

    respostas = list(df[coluna])
    disciplina = coluna.split(".")[0]
    st.text(f"Disciplina: {disciplina}")
    st.text(f"Resposta correta: {correta}")

    fig = px.bar(df, x=respostas, title=f"Correta: {correta}", color="Período", barmode="group",
                 labels={"x": "Alternativas", "count": "Quantidade"})
    st.plotly_chart(fig)

def get_cursos(data, df, curso):
    pontuacoes = data.query(f"Curso == '{curso}'")
    valores = list(pontuacoes.iloc[0].values
                   )
    st.text(list(pontuacoes.iloc[0].values))
    
    notas = list(df["NotaTotal"])

    naoCotistasPaais0 = 0
    naoCotistasPaais20 = 0
    naoCotistasPaais40 = 0
    naoCotistasPaais60 = 0
    cotistasPaais0 = 0
    cotistasPaais20 = 0
    cotistasPaais40 = 0
    cotistasPaais60 = 0

    for i in notas:
            if i + 4 >= valores[2]:
                naoCotistasPaais0 += 1
            if i + 4 >= valores[3]:
                naoCotistasPaais20 += 1
            if i + 4 >= valores[4]:
                naoCotistasPaais40 += 1
            if i + 4 >= valores[5]:
                naoCotistasPaais60 += 1
            if i + 4 >= valores[6]:
                cotistasPaais0 += 1
            if i + 4 >= valores[7]:
                cotistasPaais20 += 1
            if i + 4 >= valores[8]:
                cotistasPaais40 += 1
            if i + 4 >= valores[9]:
                cotistasPaais60 += 1


    x = ["Não Cotista PAAIS (0)", "Não Cotista (20)", "Não Cotista (40)", "Não Cotista (60)",
         "Cotistas (0)", "Cotistas (20)", "Cotistas (40)", "Cotistas (60)"]
    y = [naoCotistasPaais0, naoCotistasPaais20, naoCotistasPaais40, naoCotistasPaais60, cotistasPaais0, cotistasPaais20, cotistasPaais40, cotistasPaais60]
    
    fig = px.bar(x=x, y=y, title=f"Quantidade de alunos aprovados na primeira fase para {curso}",
                 labels={"x": "Categoria", "y": "Quantidade"})
    st.plotly_chart(fig)

    st.write(f"""
             Curso: {valores[1]}\n
             Não Cotistas (PAAIS 0): {naoCotistasPaais0}\n
             Não Cotistas (PAAIS 20): {naoCotistasPaais20}\n
             Não Cotistas (PAAIS 40): {naoCotistasPaais40}\n
             Não Cotistas (PAAIS 60): {naoCotistasPaais60}\n
             Cotistas (PAAIS 0): {cotistasPaais0}\n
             Cotistas (PAAIS 20): {cotistasPaais20}\n
             Cotistas (PAAIS 40): {cotistasPaais40}\n
             Cotistas (PAAIS 60): {cotistasPaais60}\n
             """)

def plot_student(df, name):
    row = df.query(f"Nome == '{name}'")
    totais = ["NotaTotal", "NotaMatematica", "NotaFisica", "NotaQuimica", "NotaBiologia", "NotaHistoria", "NotaGeografia", "NotaSociologia", "NotaFilosofia", "NotaGramatica", "NotaLiteratura"]
    totaisMax = [66, 12, 7, 7, 7, 7, 7, 3, 3, 6, 7]

    values = list(row[totais].iloc[0])

    fig = px.bar(x=totais, y=values, color=totais, text=values)

    fig.add_trace(go.Bar(
        x=totais,
        y=totaisMax,
        name='Quantidade Máxima de Questões',
        marker_color="red",
        opacity=0.6,
        text=totaisMax,
    ))

    st.plotly_chart(fig)    


def identifyProblems(periodo):

    df = pd.read_csv("simulado.csv", sep=",")
    banco = pd.read_csv("bancoQuestoes.csv", sep=",")
    df.drop(index=df.index[0], axis=0, inplace=True)

    deficts = {}

    gabarito = ["D", "D", "B", "A", "C", "C", "D", "C", "B", "D", "C", "D", "D", "A", "D", "B", "D", "B", "A", "C", "C", "B", "A", "D", "C", "A", "B", "B", "C", "A", "D", "A",
                "A", "B", "C", "B", "B", "A", "C", "B", "B", "D", "B", "A", "C", "B", "D", "B", "B", "B", "D", "C", "C", "D", "C", "A", "D", "C", "B", "D", "C", "D", "B", "C", "D", "D"]

    if periodo != "Geral":
        df = df.query(f"Período == '{periodo}'")
    
    

    for i in range(0, len(df)):
        aluno = df.iloc[i]
        nome = aluno["Nome"]
        deficts[nome] = {}

        for j in range(2, len(df.columns) - 1):
            if aluno[j] == gabarito[j-2]:
                continue
            else:
                tags = banco.iloc[j-1]["Tags"].split(",")
            for tag in tags:
                if tag not in deficts[nome].keys():
                    deficts[nome][tag.strip()] = 1
                else:
                    deficts[nome][tag] += 1  

    return deficts

def viewDefictsTags(periodo):
    deficts = identifyProblems(periodo)
    alunos = deficts.keys()
    
    tags_dict = {}

    for aluno in alunos:
        tags = deficts[aluno].keys()
        for tag in tags:
            if tag not in tags_dict.keys():
                tags_dict[tag] = 1
            else:
                tags_dict[tag] += 1
    
    names = tags_dict.keys()
    values = tags_dict.values()

    fig = px.bar(x=names, y=values, color=names, title="Erros por Assuntos")
    st.plotly_chart(fig)    

def identifyByStudent(aluno):
    deficts = identifyProblems("Geral")
    names = list(deficts[aluno].keys())
    values = list(deficts[aluno].values())

    fig = px.bar(x=names, y=values, color=names, title="Erros por Assuntos")
    st.plotly_chart(fig)    