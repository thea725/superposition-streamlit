import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.header("Gelombang")
wa, wb = st.sidebar.tabs(["Gelombang A", "Gelombang B"])
st.sidebar.code('''Anggota:
- Muhammad Rifki Muchtar''')
# Gelombang A
f_a = wa.slider("Frequency", 0, 10, key="f_a")
a_a = wa.slider("Amplitudo", 0, 10, key="a_a")
p_a = (wa.slider("Phase", 0, 180, key="p_a"))*(np.pi/180)
# Gelombang B
f_b = wb.slider("Frequency", 0, 10, key="f_b")
a_b = wb.slider("Amplitudo", 0, 10, key="a_b")
p_b = (wb.slider("Phase", 0, 180, key="p_b"))*(np.pi/180)

w_a = 2*np.pi*f_a
w_b = 2*np.pi*f_b

x =np.arange(0,3.01,0.01)

amplitudo_a = [round(a_a*np.sin((w_a*t)+p_a), 3) for t in np.arange(0,np.pi,0.01)]
amplitudo_b = [round(a_b*np.sin((w_b*t)+p_b), 3) for t in np.arange(0,np.pi,0.01)]
resultant = [sum(i) for i in zip(amplitudo_a, amplitudo_b)]
df = pd.DataFrame(list(zip(x, amplitudo_a, amplitudo_b, resultant)), columns =['t', 'amplitudo_a', 'amplitudo_b', 'resultant'])
col1, col2 = st.columns(2)
col1.line_chart(data=df, x="t", y="amplitudo_a", height=250, use_container_width=True)
col2.line_chart(data=df, x="t", y="amplitudo_b", height=250, use_container_width=True)
st.line_chart(data=df, x="t", y="resultant")
