import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 점심 추천", page_icon="🍱")

# 제목 및 설명
st.title("🍱 오늘 뭐 먹지?")
st.write("버튼을 누르면 오늘의 점심 메뉴를 랜덤으로 골라드립니다!")

# 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정하세요)
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "비빔밥",
    "짜장면",
    "짬뽕",
    "초밥",
    "쌀국수",
    "햄버거",
    "파스타",
    "국밥",
    "마라탕",
    "떡볶이",
    "샌드위치",
    "카레라이스",
]

st.divider()

# 버튼 생성 및 클릭 이벤트 처리
if st.button("🎲 오늘의 점심 메뉴 뽑기!", use_container_width=True):
  selected_menu = random.choice(lunch_menus)

  # 풍선 애니메이션 효과
  st.balloons()

  # 결과 출력
  st.success(f"오늘의 추천 메뉴는 **{selected_menu}** 입니다! 맛있게 드세요 😋")
