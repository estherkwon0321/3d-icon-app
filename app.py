import streamlit as st

st.set_page_config(
    page_title="3D Icon Prompt Generator",
    page_icon="✨",
    layout="centered"
)

st.title("3D Icon Prompt Generator")
st.write("운영 배너용 3D 아이콘 생성 프롬프트를 만들어주는 툴입니다.")

object_name = st.text_input("아이콘 오브젝트명을 입력하세요", "쇼핑백")

icon_type = st.selectbox(
    "아이콘 유형을 선택하세요",
    [
        "기본 단일 오브젝트형",
        "커머스 아이콘형",
        "커뮤니케이션 아이콘형",
        "혜택/이벤트 아이콘형",
        "AI/자동화 아이콘형"
    ]
)

if st.button("프롬프트 생성"):
    prompt = f"""
{object_name}을 중심으로 한 {icon_type} 3D 아이콘을 생성한다.

스타일은 부드러운 라운드 형태의 미니멀 3D 아이콘이며,
무광에 가까운 소프트 클레이/플라스틱 질감을 사용한다.

카메라는 정면 기준 약간 위에서 내려다보는 3/4 view로 고정한다.
조명은 좌상단에서 부드럽게 들어오며,
바닥에는 짧고 연한 그림자를 둔다.

색상은 파스텔톤을 사용하고,
과하게 채도가 높거나 강한 대비는 피한다.

오브젝트는 중앙에 배치하고,
사방에 충분한 여백을 둔다.

배경은 흰색으로 처리한다.

텍스트, 로고, 복잡한 배경, 과한 광택,
리얼한 금속 재질, 지나치게 세밀한 장식은 제외한다.
"""

    st.subheader("생성된 프롬프트")
    st.code(prompt, language=None)
