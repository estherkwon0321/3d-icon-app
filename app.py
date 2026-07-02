import streamlit as st

st.set_page_config(
    page_title="3D Icon Prompt System",
    page_icon="✨",
    layout="centered"
)

# Sidebar
st.sidebar.title("3D Icon Prompt System")
st.sidebar.caption("운영 배너용 3D 아이콘 스타일 일관화 도구")
st.sidebar.markdown("---")
st.sidebar.write("**Version**: v1.0")
st.sidebar.write("**Owner**: 운영디자인")
st.sidebar.write("**Output**: Prompt / Negative Prompt / Style Guide")
st.sidebar.markdown("---")
st.sidebar.caption("3D 아이콘 생성 프롬프트를 유형별로 정리해주는 도구입니다.")

# Header
st.title("3D Icon Prompt System")
st.write("운영 배너용 3D 아이콘을 일관된 스타일로 생성하기 위한 프롬프트 도구입니다.")

st.markdown("---")

# Input
st.subheader("아이콘 정보 입력")

object_name = st.text_input("아이콘 오브젝트명", "N동전")

icon_type = st.selectbox(
    "아이콘 유형",
    [
        "01 젤리",
        "02 금속",
        "03 소프트 클레이",
        "04 무광 세라믹"
    ]
)

color_type = st.selectbox(
    "색상 톤",
    [
        "파스텔톤",
        "밝고 부드러운 파스텔톤",
        "따뜻한 파스텔톤",
        "저채도 뉴트럴 톤",
        "실버/메탈릭 톤",
        "직접 입력"
    ]
)

if color_type == "파스텔톤":
    color_tone = "파스텔톤"
elif color_type == "밝고 부드러운 파스텔톤":
    color_tone = "밝고 부드러운 파스텔톤"
elif color_type == "따뜻한 파스텔톤":
    color_tone = "따뜻한 파스텔톤"
elif color_type == "저채도 뉴트럴 톤":
    color_tone = "저채도의 차분한 뉴트럴 톤"
elif color_type == "실버/메탈릭 톤":
    color_tone = "실버, 크롬, 브러시드 메탈 계열의 메탈릭 톤"
else:
    color_tone = st.text_input("직접 입력", "부드럽고 저채도의 블루 계열")

st.caption(f"선택된 색상 톤: {color_tone}")

st.markdown("---")

# Prompt Templates
prompt_templates = {
    "01 젤리": """
[오브젝트명]을 중심으로 한 3D 아이콘을 생성한다.

스타일은 부드럽고 말랑한 젤리 느낌의 미니멀 3D 아이콘이며,
매우 둥글고 매끈한 형태로 표현한다.
재질은 반투명한 밀키 프로스티드 젤리 질감으로 표현하고,
표면은 부드럽고 깨끗하게 유지한다.

카메라는 정면 기준 약간 위에서 내려다보는 3/4 view로 고정한다.
조명은 전체적으로 부드럽고 확산된 느낌으로 적용하며,
강한 명암 대비 없이 은은하게 형태만 드러나도록 한다.

색상은 [색상톤]을 사용하고,
채도가 과하게 높거나 원색에 가까운 느낌은 피한다.

오브젝트는 중앙에 배치하고,
사방에 충분한 여백을 둔다.

배경은 흰색으로 처리한다.

텍스트, 로고, 복잡한 배경, 날카로운 하이라이트,
리얼한 표면 질감, 강한 그림자, 추가 오브젝트는 제외한다.
""",

    "02 금속": """
[오브젝트명]을 중심으로 한 3D 아이콘을 생성한다.

스타일은 단순하고 세련된 미니멀 3D 아이콘이며,
부드러운 라운드 형태를 유지하되 구조는 또렷하게 표현한다.
재질은 매끈하고 정돈된 금속 질감으로 표현하고,
너무 거칠거나 낡은 느낌 없이 깔끔하고 현대적인 인상을 준다.

카메라는 정면 기준 약간 위에서 내려다보는 3/4 view로 고정한다.
조명은 좌상단에서 부드럽게 들어오되,
금속 특유의 은은한 반사와 하이라이트가 자연스럽게 보이도록 한다.
과도하게 번쩍이거나 거울처럼 강한 반사는 피한다.

색상은 [색상톤]을 사용하고,
과하게 화려한 컬러 메탈 표현은 피한다.

오브젝트는 중앙에 배치하고,
사방에 충분한 여백을 둔다.

배경은 흰색으로 처리한다.

텍스트, 로고, 복잡한 배경, 과도한 광택, 지나치게 강한 반사,
스크래치가 심한 질감, 추가 오브젝트는 제외한다.
""",

    "03 소프트 클레이": """
[오브젝트명]을 중심으로 한 3D 아이콘을 생성한다.

스타일은 귀엽고 부드러운 소프트 클레이 느낌의 미니멀 3D 아이콘이며,
둥글고 도톰한 형태로 표현한다.
재질은 무광에 가까운 소프트 클레이 또는 부드러운 플라스틱 질감을 사용하고,
표면은 매끈하지만 손으로 빚은 듯한 포근한 인상을 준다.

카메라는 정면 기준 약간 위에서 내려다보는 3/4 view로 고정한다.
조명은 좌상단에서 부드럽게 들어오며,
바닥에는 짧고 은은한 그림자를 두어 형태를 자연스럽게 살린다.

색상은 [색상톤]을 사용하고,
부드럽고 친근한 분위기가 느껴지도록 구성한다.
강한 대비나 차가운 형광톤은 피한다.

오브젝트는 중앙에 배치하고,
사방에 충분한 여백을 둔다.

배경은 흰색으로 처리한다.

텍스트, 로고, 복잡한 배경, 금속성 광택, 사실적인 표면 질감,
과하게 날카로운 디테일, 추가 소품은 제외한다.
""",

    "04 무광 세라믹": """
[오브젝트명]을 중심으로 한 3D 아이콘을 생성한다.

스타일은 정갈하고 고급스러운 미니멀 3D 아이콘이며,
부드러운 라운드 형태와 안정감 있는 비율로 표현한다.
재질은 무광 세라믹 질감으로 표현하고,
표면은 매끈하고 단단하지만 지나치게 반짝이지 않도록 한다.

카메라는 정면 기준 약간 위에서 내려다보는 3/4 view로 고정한다.
조명은 전체적으로 부드럽고 정제된 스튜디오 조명으로 적용하며,
강한 반사보다는 은은한 명암으로 형태를 드러낸다.
바닥에는 매우 짧고 부드러운 그림자를 둔다.

색상은 [색상톤]을 사용하고,
고급스럽고 절제된 분위기가 느껴지도록 구성한다.

오브젝트는 중앙에 배치하고,
사방에 충분한 여백을 둔다.

배경은 흰색으로 처리한다.

텍스트, 로고, 복잡한 배경, 유광 느낌, 금속성 반사,
지나치게 장식적인 요소, 추가 오브젝트는 제외한다.
"""
}

style_guides = {
    "01 젤리": """
Style Guide

- Style Type: 젤리
- Material: 반투명 밀키 프로스티드 젤리
- Form: 매우 둥글고 매끈한 형태
- Lighting: 부드럽고 확산된 조명
- Contrast: 낮은 대비
- Shadow: 강한 그림자 없음
- Background: 흰색
- Composition: 중앙 배치, 충분한 여백
""",

    "02 금속": """
Style Guide

- Style Type: 금속
- Material: 매끈하고 정돈된 금속 질감
- Form: 라운드 형태 + 또렷한 구조
- Lighting: 좌상단에서 들어오는 부드러운 조명
- Highlight: 은은한 반사와 하이라이트
- Shadow: 과하지 않은 그림자
- Background: 흰색
- Composition: 중앙 배치, 충분한 여백
""",

    "03 소프트 클레이": """
Style Guide

- Style Type: 소프트 클레이
- Material: 무광 소프트 클레이 / 부드러운 플라스틱
- Form: 둥글고 도톰한 형태
- Lighting: 좌상단에서 들어오는 부드러운 조명
- Shadow: 짧고 은은한 그림자
- Mood: 포근하고 친근한 분위기
- Background: 흰색
- Composition: 중앙 배치, 충분한 여백
""",

    "04 무광 세라믹": """
Style Guide

- Style Type: 무광 세라믹
- Material: 무광 세라믹
- Form: 부드러운 라운드 형태와 안정감 있는 비율
- Lighting: 정제된 스튜디오 조명
- Shadow: 매우 짧고 부드러운 그림자
- Mood: 정갈하고 고급스러운 분위기
- Background: 흰색
- Composition: 중앙 배치, 충분한 여백
"""
}

if st.button("프롬프트 생성", type="primary"):

    prompt = prompt_templates[icon_type]
    prompt = prompt.replace("[오브젝트명]", object_name)
    prompt = prompt.replace("[색상톤]", color_tone)

    negative_prompt = """
제외 요소:
- 텍스트 포함 금지
- 로고 포함 금지
- 복잡한 배경 금지
- 추가 오브젝트 금지
- 과한 광택 금지
- 지나치게 강한 그림자 금지
- 사실적인 표면 질감 금지
- 지나치게 복잡한 장식 금지
- 저해상도 또는 흐릿한 렌더링 금지
"""

    style_guide = style_guides[icon_type] + f"""

Color Guide

- Color Type: {color_type}
- Color Tone: {color_tone}
"""

    safe_icon_type = icon_type.lower().replace(" ", "-")
    safe_object_name = object_name.replace(" ", "-")
    file_name = f"3d-icon_{safe_icon_type}_{safe_object_name}_v01.png"

    tab1, tab2, tab3 = st.tabs(
        ["Prompt", "Negative Prompt", "Style Guide"]
    )

    with tab1:
        st.subheader("생성 프롬프트")
        st.code(prompt, language=None)
        st.caption("우측 상단 복사 아이콘으로 프롬프트를 복사할 수 있습니다.")

    with tab2:
        st.subheader("네거티브 프롬프트")
        st.code(negative_prompt, language=None)
        st.caption("생성 결과에서 제외하고 싶은 요소를 함께 복사해 사용하세요.")

    with tab3:
        st.subheader("공통 스타일 가이드")
        st.code(style_guide, language=None)

    st.markdown("---")
    st.subheader("추천 파일명")
    st.code(file_name, language=None)
