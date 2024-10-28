import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(df)

# 라인차트 그리기
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# 지도 그리기
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.514575, 127.0495556],
    columns=['lat', 'lon'])

# latitude: 위도 longitude: 경도
st.map(map_data)


x = st.slider('x')  #  this is a widget
st.write(x, 'squared is', x * x)


# 체크박스 ON/OFF 토글
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
    
# 셀렉트박스
option = st.selectbox(
    'Which number do you like best?',
     [1, 2, 3, 4, 5])

'You selected: ', option


# 사이드바 UI 
# Add a selectbox to the sidebar:

st.sidebar.write("연락 방법")
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

st.sidebar.write("범위")
# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

#TODO:
#(event: 버튼을 누르면): 유저한테 받은 인풋으로 예측하기!!!!
# user_input = [[a,b,c]]


import time
# import xgboost
# from xgboost import XGBRegressor

import pickle
with open("./xgboost_feature3.pkl", 'rb') as f:
    loaded_model = pickle.load(f)

def predict(input): # [[10, 20, 30]]
    result = loaded_model.predict(input) 
    return result

# LotFrontage : 부동산에 연결된 거리의 선형 피트
# LotArea : 평방 피트 단위의 부지 크기
# GrLivArea : 거실 면적 평방피트
with st.form(key="form1"):      
    value1 = st.number_input("input1", value=None, placeholder="부동산에 연결된 거리의 선형 피트")
    value2 = st.number_input("input2", value=None, placeholder="평방 피트 단위의 부지 크기")
    value3 = st.number_input("input3", value=None, placeholder="거실 면적 평방피트")
    
    # print(f"value type: {type(value1)}")    
    submit = st.form_submit_button(label="예측하기")
    
with st.form(key="form2"):
    pass
    
# 예측하기 버튼을 누르면 (form이 submit되면)
import time
if submit:
    user_input_data = [[value1, value2, value3]]    
    st.write(f"사용자가 입력한 데이터: {user_input_data}")   
    
    start = time.time()  
    result = predict(user_input_data)    
    end = time.time()  
    
    st.write(f"예측하는데: {end - start}초 걸림.")     
    st.write(f"예측 집값: {result[0]}")    
    
# st.write(result)
# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    st.write("해리포터")
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")