import pandas as pd
import streamlit as st

# 1. 앱 제목과 설명 설정
st.title("📚 공부 습관 대시보드")
st.write(
    "학생들의 공부 시간과 스마트폰 사용량이 점수에 미치는 영향을 확인해 보세요!"
)

# 2. CSV 파일 읽기 (실제 파일명이 study_4.csv인 경우 아래 이름을 수정하세요)
df = pd.read_csv("study.csv")

# 3. 데이터 요약 지표 계산 (학생 수, 평균 점수, 평균 공부시간)
total_students = len(df)  # 전체 학생 수
avg_score = df["점수"].mean()  # 평균 점수
avg_study = df["공부시간"].mean()  # 평균 공부시간

# 4. st.metric을 사용하여 요약 지표를 한 줄에 나란히 표시
col1, col2, col3 = st.columns(3)
col1.metric("전체 학생 수", f"{total_students}명")
col2.metric("평균 점수", f"{avg_score:.1f}점")
col3.metric("평균 공부시간", f"{avg_study:.1f}시간")

st.markdown("---")  # 시각적 구분을 위한 수평선

# 5. 슬라이더로 '최소 공부시간' 선택받기
st.subheader("🔍 조건별 학생 필터링 및 시각화")

min_val = float(df["공부시간"].min())
max_val = float(df["공부시간"].max())

min_study_time = st.slider(
    "최소 공부시간을 선택하세요 (시간)",
    min_value=min_val,
    max_value=max_val,
    value=min_val,
    step=0.5,
)

# 6. 선택한 최소 공부시간 이상인 학생들만 필터링
filtered_df = df[df["공부시간"] >= min_study_time]
st.write(f"현재 조건에 맞는 학생 수: **{len(filtered_df)}명**")

# 7. 스트림릿 기본 차트 함수를 이용해 산점도와 막대 그래프 그리기
if len(filtered_df) > 0:
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.markdown("##### 📈 공부시간 vs 점수 산점도")
        # 스트림릿 기본 산점도 함수 사용
        st.scatter_chart(filtered_df, x="공부시간", y="점수")

    with chart_col2:
        st.markdown("##### 📊 학생별 점수 막대 그래프")
        # 스트림릿 기본 막대 그래프 함수 사용
        st.bar_chart(filtered_df, x="학생ID", y="점수")
else:
    st.warning("선택한 조건에 해당하는 학생 데이터가 없습니다. 슬라이더를 조정해 주세요!")