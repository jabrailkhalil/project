import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Загрузка датасета
uploaded_file = st.file_uploader("Загрузите датасет в виде csv файла")
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except:
        st.error("Невозможно прочитать файл. Пожалуйста, убедитесь, что он имеет формат csv.")
else:
    st.error("Файл не загружен.")

# Выбор колонок
if uploaded_file is not None:
    col1 = st.selectbox("Выберите первую колонку для исследования", df.columns)
    col2 = st.selectbox("Выберите вторую колонку для исследования", df.columns)

    # Вывод названий колонок
    st.write(f"Вы выбрали колонки {col1} и {col2}")

    # Визуализация распределения
    if df[col1].dtype == "float64" or df[col1].dtype == "int64":
        # Гистограмма для числовых данных
        fig, ax = plt.subplots()
        ax.hist(df[col1], bins=20)
        ax.set_xlabel(col1)
        ax.set_ylabel("Частота")
        st.pyplot(fig)
    else:
        # Круговая диаграмма для категориальных данных
        pie_data = df[col1].value_counts().to_frame().rename(columns={col1: "Count"})
        st.pie_chart(pie_data)

    if df[col2].dtype == "float64" or df[col2].dtype == "int64":
        # Гистограмма для числовых данных
        fig, ax = plt.subplots()
        ax.hist(df[col2], bins=20)
        ax.set_xlabel(col2)
        ax.set_ylabel("Частота")
        st.pyplot(fig)
    else:
        # Круговая диаграмма для категориальных данных
        pie_data = df[col2].value_counts().to_frame().rename(columns={col2: "Count"})
        st.pie_chart(pie_data)

    # Выбор алгоритма теста гипотез
    test = st.selectbox("Выберите алгоритм теста гипотез", ["t-тест", "ANOVA"])

    # Проведение теста гипотез и вывод результатов
    if test == "t-тест":
        stat, pvalue = stats.ttest_ind(df[col1], df[col2])
        st.write(f"Результат t-теста: статистика = {stat:.3f}, p-значение = {pvalue:.3f}")
    elif test == "ANOVA":
        stat, pvalue = stats.f_oneway(df[col1], df[col2])
        st.write(f"Результат ANOVA: статистика = {stat:.3f}, p-значение = {pvalue:.3f}")
