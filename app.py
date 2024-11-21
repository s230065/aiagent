# 예측 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model=joblib.load('linear_regression_model.pkl')

# 2. 모델 설명
st.title('학생 스트레스 판독기')
st.subheader('당신의 스트레스는 어느 정도입니까?')
st.write(' - 기계학습 알고리즘: 선형 회귀')
st.write(' - 학습 데이터 출처: https://www.kaggle.com/datasets/rxnach/student-stress-factors-a-comprehensive-analysis')
st.write(' - 훈련 데이터 : 770건')
st.write(' - 테스트 데이터 : 330건')
st.write(' - 인공지능 모델 정확도 : 0.79')

# 3. 데이터시각화
col1,col2=st.columns(2)
with col1:
 st.subheader('데이터시각화1')
 st.image('시각화1.PNG')
with col2:
 st.subheader('데이터시각화2')
 st.image('시각화2.PNG')


# 4. 모델 활용
st.subheader('지능 에이전트 활용 방법')
st.subheader('****다음을 입력하세요. 인공지능이 당신의 스트레스 정도를 알려드립니다!')

a=st.number_input('불안함의 정도를 입력하세요', value=0)
b=st.number_input('자아 존중감의 정도를 입력하세요', value=0)
c=st.number_input('우울함의 정도를 입력하세요', value=0)
d=st.number_input('두통의 정도를 입력하세요', value=0)
e=st.number_input('수면의 질의 정도를 입력하세요', value=0)
f=st.number_input('기본적 욕구의 충족의 정도를 입력하세요', value=0)
g=st.number_input('미래 진로에 대한 고민의 정도를 입력하세요', value=0)
h=st.number_input('학업적 성공의 정도를 입력하세요', value=0)
i=st.number_input('괴롭힘의 정도를 입력하세요', value=0)

if st.button('인공지능의 예측 결과'):
 input_data = [[a,b,c,d,e,f,g,h,i]]
 p=model.predict(input_data)
 if p <1:
  p=0
 if 1<=p<2:
  p=1
 else:
  p=2

 st.write('인공지능의 예측 결과 당신의 스트레스 레벨은 0,1,2 중',p,'입니다 (0: 낮음, 1: 보통, 2: 높음)')
