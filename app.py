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
        "01 Pastel Jelly",
        "02 Semi Glossy",
        "03 Soft Clay",
        "04 Basic"
    ]
)

color_type = st.selectbox(
    "색상 톤",
    [
        "Bright Soft Pastel",
        "Warm Pastel",
        "Soft Blue",
        "Mint Fresh",
        "Lavender Pink",
        "Neutral Gray",
        "Custom"
    ]
)

if color_type == "Bright Soft Pastel":
    color_tone = "bright soft pastel colors"
elif color_type == "Warm Pastel":
    color_tone = "warm pastel colors"
elif color_type == "Soft Blue":
    color_tone = "soft pastel blue, light sky blue, soft gray"
elif color_type == "Mint Fresh":
    color_tone = "mint, light green, ivory"
elif color_type == "Lavender Pink":
    color_tone = "lavender, light pink, soft purple"
elif color_type == "Neutral Gray":
    color_tone = "light gray, white, low-saturation blue"
else:
    color_tone = st.text_input(
        "직접 입력",
        "warm, slightly desaturated colors"
    )

st.caption(f"선택된 색상 톤: {color_tone}")

st.markdown("---")

# Prompt Templates
prompt_templates = {
    "01 Pastel Jelly": """
Create a single 3D isometric icon of [object], in a soft pastel jelly-like style, with a very smooth rounded silhouette, simplified details, semi-translucent milky frosted material, soft diffused lighting, low contrast, and blurred gentle highlights.
Center the object in a clean 1:1 composition on a pure white background.
No sharp highlights, no realistic texture, no harsh shadows, no text, no extra objects.
""",

    "02 Semi Glossy": """
Create a single 3D isometric icon of [object], in a soft semi-glossy 3D app icon style, with a very smooth rounded silhouette, simplified details, softly polished plastic material, subtle semi-gloss finish, soft diffused lighting, low contrast, and gentle highlights.
Center the object in a clean 1:1 composition on a pure white background.
No sharp highlights, no realistic texture, no harsh shadows, no text, no extra objects.
""",

    "03 Soft Clay": """
A single [object] icon, in a consistent soft rounded 3D icon style, cute and minimal, chunky toy-like form, smooth matte plastic / soft clay material, simplified details, soft studio lighting, subtle ambient occlusion, gentle shadow underneath, clean white background, centered composition, 3/4 isometric view, high-quality 3D render, no text, no logo, no extra props, no photorealism, no harsh shadows, no glossy metal, no realistic texture.
""",

    "04 Basic": """
Create a single 3D isometric icon of [object] in a clean soft commercial app icon style.
Use a simplified rounded silhouette, soft extruded geometry, smooth matte plastic with a subtle ceramic finish, and an ultra-clean textureless surface.
No gloss, no reflections, no metallic shine.
Show a centered single object in a true 30-degree isometric view on a 1:1 canvas.
Apply soft ambient studio lighting with very subtle form shading only.
Present the object as a clean isolated icon, gently floating in space, with no floor shadow, no ground shadow, and no cast shadow.
Use a clean pure white background only.
No text, no extra elements, no floor line, no backdrop elements, high-resolution clean 3D render.
"""
}

style_guides = {
    "01 Pastel Jelly": """
Style Guide

- Style Type: Pastel Jelly
- Material: Semi-translucent milky frosted material
- Form: Very smooth rounded silhouette
- Detail Level: Simplified
- Lighting: Soft diffused lighting
- Contrast: Low contrast
- Highlight: Blurred gentle highlights
- Background: Pure white background
- Composition: Clean 1:1 centered composition
""",

    "02 Semi Glossy": """
Style Guide

- Style Type: Semi Glossy
- Material: Softly polished plastic
- Finish: Subtle semi-gloss finish
- Form: Very smooth rounded silhouette
- Detail Level: Simplified
- Lighting: Soft diffused lighting
- Contrast: Low contrast
- Highlight: Gentle highlights
- Background: Pure white background
- Composition: Clean 1:1 centered composition
""",

    "03 Soft Clay": """
Style Guide

- Style Type: Soft Clay
- Material: Smooth matte plastic / soft clay
- Form: Cute, minimal, chunky toy-like form
- Detail Level: Simplified
- Lighting: Soft studio lighting
- Shadow: Gentle shadow underneath
- View: 3/4 isometric view
- Background: Clean white background
- Composition: Centered composition
""",

    "04 Basic": """
Style Guide

- Style Type: Basic
- Material: Smooth matte plastic with subtle ceramic finish
- Form: Simplified rounded silhouette / soft extruded geometry
- Surface: Ultra-clean textureless surface
- Lighting: Soft ambient studio lighting
- Shadow: No floor shadow / no ground shadow / no cast shadow
- View: True 30-degree isometric view
- Background: Pure white background
- Composition: Clean 1:1 centered composition
"""
}

if st.button("프롬프트 생성", type="primary"):

    base_prompt = prompt_templates[icon_type].replace("[object]", object_name)

    color_prompt = f"""
Use {color_tone} as the color direction.
Keep the colors clean, harmonious, and suitable for a modern commercial digital product.
"""

    prompt = base_prompt.strip() + "\n\n" + color_prompt.strip()

    negative_prompt = """
Negative Prompt:
text, logo, brand name, extra objects, complex background, realistic texture, harsh shadows, sharp highlights, metallic shine, glossy metal, floor line, backdrop elements, photorealism, low-resolution render, blurry render
"""

    style_guide = style_guides[icon_type] + f"""

Color Guide

- Color Type: {color_type}
- Color Tone: {color_tone}
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
