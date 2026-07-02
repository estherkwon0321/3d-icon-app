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

object_name = st.text_input("아이콘 오브젝트명", "shopping bag")

icon_type = st.selectbox(
    "아이콘 유형",
    [
        "01 Soft Commercial",
        "02 Warm Ceramic",
        "03 Floating Minimal",
        "04 Clean Isometric"
    ]
)

# Color Palette
palette_type = st.radio(
    "컬러 팔레트",
    [
        "Soft Blue",
        "Mint Fresh",
        "Warm Pastel",
        "Lavender Pink",
        "Neutral Gray",
        "Custom"
    ],
    horizontal=True
)

if palette_type == "Soft Blue":
    color_tone = "soft pastel blue, light sky blue, soft gray"
elif palette_type == "Mint Fresh":
    color_tone = "mint, light green, ivory"
elif palette_type == "Warm Pastel":
    color_tone = "cream, peach, light yellow"
elif palette_type == "Lavender Pink":
    color_tone = "lavender, light pink, soft purple"
elif palette_type == "Neutral Gray":
    color_tone = "light gray, white, low-saturation blue"
else:
    color_tone = st.text_input(
        "직접 입력",
        "warm, slightly desaturated colors"
    )

st.caption(f"선택된 팔레트: {color_tone}")

st.markdown("---")

# Prompt Templates
prompt_templates = {
    "01 Soft Commercial": """
Create a single 3D isometric icon of [object] in a clean soft commercial app icon style.
Use a simplified rounded silhouette, soft extruded geometry, smooth matte plastic with a subtle ceramic finish, and an ultra-clean textureless surface.
No gloss, no reflections, no metallic shine.
Use [color_tone].
Show a centered single object in a true 30-degree isometric view on a 1:1 canvas.
Apply soft ambient studio lighting with very subtle form shading only.
Present the object as a clean isolated icon, gently floating in space, with no floor shadow, no ground shadow, and no cast shadow.
Use a clean pure white background only.
No text, no extra elements, no floor line, no backdrop elements, high-resolution clean 3D render.
""",

    "02 Warm Ceramic": """
Create a single 3D isometric icon of [object] in a warm soft ceramic app icon style.
Use a simplified rounded silhouette, soft extruded geometry, smooth matte plastic with a subtle ceramic finish, and an ultra-clean textureless surface.
No gloss, no reflections, no metallic shine.
Use [color_tone] with a warm, slightly desaturated color mood.
Show a centered single object in a true 30-degree isometric view on a 1:1 canvas.
Apply soft ambient studio lighting with very subtle form shading only.
Present the object as a clean isolated icon, gently floating in space, with no floor shadow, no ground shadow, and no cast shadow.
Use a clean pure white background only.
No text, no extra elements, no floor line, no backdrop elements, high-resolution clean 3D render.
""",

    "03 Floating Minimal": """
Create a single 3D isometric icon of [object] in a clean floating minimal 3D icon style.
Use a simplified rounded silhouette, soft extruded geometry, smooth matte plastic with a subtle ceramic finish, and an ultra-clean textureless surface.
No gloss, no reflections, no metallic shine.
Use [color_tone].
Show a centered single object in a true 30-degree isometric view on a 1:1 canvas.
Apply soft ambient studio lighting with very subtle form shading only.
Present the object as a clean isolated icon, gently floating in space.
Use no floor shadow, no ground shadow, and no cast shadow.
Use a clean pure white background only.
No text, no extra elements, no floor line, no backdrop elements, high-resolution clean 3D render.
""",

    "04 Clean Isometric": """
Create a single 3D isometric icon of [object] in a clean soft commercial app icon style.
Use a simplified rounded silhouette, soft extruded geometry, smooth matte plastic with a subtle ceramic finish, and an ultra-clean textureless surface.
No gloss, no reflections, no metallic shine.
Use [color_tone].
Show a centered single object in a precise true 30-degree isometric view on a 1:1 canvas.
Apply soft ambient studio lighting with very subtle form shading only.
Present the object as a clean isolated icon, gently floating in space, with no floor shadow, no ground shadow, and no cast shadow.
Use a clean pure white background only.
No text, no extra elements, no floor line, no backdrop elements, high-resolution clean 3D render.
"""
}

if st.button("프롬프트 생성", type="primary"):

    prompt = prompt_templates[icon_type]
    prompt = prompt.replace("[object]", object_name)
    prompt = prompt.replace("[color_tone]", color_tone)

    negative_prompt = """
Negative Prompt:
text, logo, brand name, extra objects, complex background, floor line, ground shadow, cast shadow, backdrop elements, glossy material, reflections, metallic shine, realistic metal, noisy texture, low-resolution render, blurry render, over-detailed object
"""

    style_guide = f"""
Style Guide

- Style Type: {icon_type}
- View: True 30-degree Isometric View
- Object: Single Centered Object
- Geometry: Simplified Rounded Silhouette
- Material: Smooth Matte Plastic with Subtle Ceramic Finish
- Surface: Ultra-clean Textureless Surface
- Lighting: Soft Ambient Studio Lighting
- Shadow: No Floor Shadow / No Ground Shadow / No Cast Shadow
- Background: Pure White Background
- Color Palette: {palette_type}
- Color Tone: {color_tone}
- Canvas: 1:1
"""

    safe_icon_type = icon_type.lower().replace(" ", "-")
    safe_object_name = object_name.lower().replace(" ", "-")
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
