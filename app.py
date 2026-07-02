import streamlit as st

st.set_page_config(
    page_title="3D Icon Prompt System",
    page_icon="✨",
    layout="centered"
)

# Sidebar
st.sidebar.title("3D Icon Prompt System")
st.sidebar.caption("3D 아이콘 스타일 프롬프트 도구")
st.sidebar.markdown("---")
st.sidebar.write("**Version**: v1.2")
st.sidebar.write("**Owner**: 운영디자인")
st.sidebar.write("**Output**: Prompt / Negative Prompt / Style Guide")
st.sidebar.markdown("---")
st.sidebar.caption("선택한 스타일과 색상 톤에 맞춰 3D 아이콘 생성 프롬프트를 정리해주는 도구입니다.")

# Header
st.title("3D Icon Prompt System")
st.write("선택한 스타일과 색상 톤에 맞춰 3D 아이콘 생성 프롬프트를 만들 수 있습니다.")

st.markdown("---")

# Input
st.subheader("아이콘 정보 입력")

object_name = st.text_input("아이콘 오브젝트명", "N동전")

icon_type = st.selectbox(
    "아이콘 유형",
    [
        "01 Clean Soft Commercial",
        "02 Soft Clay Commercial",
        "03 Semi Glossy Vivid",
        "04 Pastel Jelly",
        "05 Brushed Metal Coin",
        "06 Layered Paper Craft",
        "07 Frosted Acrylic Blue"
    ]
)

color_type = st.selectbox(
    "색상 톤",
    [
        "Warm Desaturated",
        "Warm Pastel",
        "Bright Vivid",
        "Bright Soft Pastel",
        "Soft Blue",
        "Mint Fresh",
        "Lavender Pink",
        "Neutral Gray",
        "Silver Metallic",
        "Soft Paper Pastel",
        "Pastel Blue Acrylic",
        "Custom"
    ]
)

if color_type == "Warm Desaturated":
    color_tone = "warm, slightly desaturated colors"
elif color_type == "Warm Pastel":
    color_tone = "warm pastel colors"
elif color_type == "Bright Vivid":
    color_tone = "a vibrant and bright color palette with high saturation"
elif color_type == "Bright Soft Pastel":
    color_tone = "bright soft pastel colors"
elif color_type == "Soft Blue":
    color_tone = "soft pastel blue, light sky blue, and soft gray"
elif color_type == "Mint Fresh":
    color_tone = "mint, light green, and ivory"
elif color_type == "Lavender Pink":
    color_tone = "lavender, light pink, and soft purple"
elif color_type == "Neutral Gray":
    color_tone = "light gray, white, and low-saturation blue"
elif color_type == "Silver Metallic":
    color_tone = "silver, cool gray, soft chrome, and subtle blue-gray highlights"
elif color_type == "Soft Paper Pastel":
    color_tone = "soft pastel colors with gentle contrast"
elif color_type == "Pastel Blue Acrylic":
    color_tone = "a soft pastel blue palette using light sky blue, milky blue, and slightly deeper vivid blue on edges and thicker parts"
else:
    color_tone = st.text_input(
        "직접 입력",
        "warm pastel orange, cream white, and soft yellow"
    )

st.caption(f"선택된 색상 톤: {color_tone}")

st.markdown("---")

# Prompt Templates
prompt_templates = {
    "01 Clean Soft Commercial": """
Subject: A single [object] icon.

Style: Clean soft commercial app icon style, minimal, polished, modern, and visually simple.

Shape / Form: Simplified rounded silhouette, soft extruded geometry, balanced proportions, clean isolated single object.

Material: Smooth matte plastic with a subtle ceramic finish, ultra-clean textureless surface, no gloss, no reflections, no metallic shine.

Color: [color_tone].

View / Composition: True 30-degree isometric view, centered single object, 1:1 square canvas.

Lighting: Soft ambient studio lighting with very subtle form shading only.

Shadow: No floor shadow, no ground shadow, no cast shadow.

Background: Clean pure white background only, no floor line, no backdrop elements.

Quality: High-resolution clean 3D render, polished commercial icon quality.
""",

    "02 Soft Clay Commercial": """
Subject: A single [object] icon.

Style: Consistent soft rounded 3D icon style, cute and minimal, friendly, clean, and commercial.

Shape / Form: Chunky toy-like form, rounded edges, simplified details, centered single object.

Material: Smooth matte plastic / soft clay material.

Color: [color_tone].

View / Composition: 3/4 isometric view, centered composition, clean 1:1 square canvas.

Lighting: Soft studio lighting with subtle ambient occlusion.

Shadow: Gentle shadow underneath.

Background: Clean white background only.

Quality: High-quality 3D render, soft and polished icon finish.
""",

    "03 Semi Glossy Vivid": """
Subject: A single [object] icon.

Style: Soft rounded 3D icon style, bright, cheerful, vivid, and eye-catching.

Shape / Form: Rounded silhouette, simplified details, slightly puffy and playful form, centered single object.

Material: Semi-glossy clay material with subsurface scattering.

Color: [color_tone].

View / Composition: 3/4 isometric view, centered single object, clean 1:1 square canvas.

Lighting: Bright studio lighting.

Shadow: Very soft subtle shadow only, no harsh shadows.

Background: Clean white background only.

Quality: High-quality 3D render, vibrant polished icon finish.
""",

    "04 Pastel Jelly": """
Subject: A single [object] icon.

Style: Soft pastel jelly-like 3D icon style, dreamy, soft, playful, and clean.

Shape / Form: Very smooth rounded silhouette, simplified details, soft and minimal single object.

Material: Semi-translucent milky frosted material, jelly-like appearance.

Color: [color_tone].

View / Composition: Isometric view, centered single object, clean 1:1 square canvas.

Lighting: Soft diffused lighting, low contrast, blurred gentle highlights.

Shadow: Very soft subtle shadow only, no harsh shadows.

Background: Pure white background only.

Quality: High-resolution clean 3D render, soft polished finish.
""",

    "05 Brushed Metal Coin": """
Subject: A single [object] icon.

Style: Premium brushed metal 3D icon style, clean, polished, modern, and slightly futuristic.

Shape / Form: Simplified rounded silhouette, solid coin-like volume, beveled edges, clean embossed details, centered single object.

Material: Smooth metal with a subtle brushed finish, soft metallic reflection, refined beveled surface, no rough scratches, no damaged texture.

Color: [color_tone].

View / Composition: Front-facing 3/4 view, centered single object, clean 1:1 square canvas.

Lighting: Soft studio lighting from the upper left, with controlled highlights along the beveled edges.

Shadow: Very soft subtle shadow only, no harsh cast shadow.

Background: Clean pure white background only.

Quality: High-resolution clean 3D render, premium polished icon quality, refined commercial product icon finish.
""",

    "06 Layered Paper Craft": """
Subject: A single [object] icon.

Style: Layered paper craft 3D icon style, clean, soft, friendly, and minimal.

Shape / Form: Simplified rounded silhouette, flat layered cutout shapes, soft stacked paper depth, centered single object.

Material: Smooth matte paper material, subtle paper thickness, clean cut edges, soft tactile surface, no plastic, no metal, no glossy finish.

Color: [color_tone].

View / Composition: Slight 3/4 isometric view, centered single object, clean 1:1 square canvas.

Lighting: Soft diffused studio lighting, gentle depth between paper layers.

Shadow: Very soft small shadows between layers, subtle shadow underneath.

Background: Clean pure white background only.

Quality: High-resolution clean 3D render, polished editorial icon quality, simple and easy to recognize.
""",

    "07 Frosted Acrylic Blue": """
Subject: A single [object] icon.

Style: Soft translucent pastel 3D icon style, clean commercial app icon, minimal, dreamy, polished, and visually simple.

Shape / Form: A simplified [object] with a rounded silhouette, soft rounded corners, smooth edges, and slightly puffy proportions. The form should feel like a small cute object made of soft acrylic or jelly plastic. Avoid sharp edges and complex details.

Material: Semi-translucent milky frosted acrylic material, soft jelly-like plastic, smooth surface, subtle transparency, gentle depth, soft diffused highlights, no strong gloss, no metallic texture.

Color: [color_tone].

View / Composition: True isometric view, slightly from above, centered single object, clean 1:1 square canvas. The object should be placed large in the center with enough white space around it.

Lighting: Soft diffused studio lighting, low contrast, gentle colored glow, blurred soft highlights, subtle form shading only.

Shadow: Very soft and faint tinted shadow only, no harsh cast shadow.

Background: Pure white background only, no floor line, no backdrop elements.

Quality: High-resolution clean 3D render, soft polished commercial icon quality.
"""
}

negative_prompts = {
    "01 Clean Soft Commercial": """
Text, logo, extra elements, extra objects, photorealism, realistic texture, glossy surface, metallic material, harsh shadows, busy composition.
""",

    "02 Soft Clay Commercial": """
Text, logo, extra props, photorealism, realistic texture, glossy metal, harsh shadows, overly detailed surfaces, busy scene.
""",

    "03 Semi Glossy Vivid": """
Text, logo, extra props, photorealism, realistic texture, rough surface, metallic finish, harsh shadows, dull colors, noisy details.
""",

    "04 Pastel Jelly": """
Text, logo, extra objects, photorealism, realistic texture, sharp highlights, harsh shadows, metallic material, overly detailed surfaces.
""",

    "05 Brushed Metal Coin": """
Text, logo, extra objects, busy background, rusty metal, scratched texture, overly realistic coin, harsh reflections, dark mood, noisy surface, low-resolution render.
""",

    "06 Layered Paper Craft": """
Text, logo, extra objects, realistic paper fiber, dirty texture, glossy surface, metallic material, harsh shadows, complex background, overly detailed decoration, low-resolution render.
""",

    "07 Frosted Acrylic Blue": """
Text, logo, brand mark, extra objects, complex background, harsh shadows, realistic paper texture, leather texture, metallic material, strong reflections, photorealism, excessive detail.
"""
}

style_guides = {
    "01 Clean Soft Commercial": """
Style Guide

- Style Type: Clean Soft Commercial
- Mood: Minimal, polished, modern, visually simple
- Shape / Form: Simplified rounded silhouette, soft extruded geometry, balanced proportions
- Material: Smooth matte plastic with subtle ceramic finish
- Surface: Ultra-clean textureless surface
- View / Composition: True 30-degree isometric view, centered single object, 1:1 square canvas
- Lighting: Soft ambient studio lighting with very subtle form shading only
- Shadow: No floor shadow / no ground shadow / no cast shadow
- Background: Clean pure white background, no floor line, no backdrop elements
- Quality: High-resolution clean 3D render
""",

    "02 Soft Clay Commercial": """
Style Guide

- Style Type: Soft Clay Commercial
- Mood: Cute, minimal, friendly, clean, commercial
- Shape / Form: Chunky toy-like form, rounded edges, simplified details
- Material: Smooth matte plastic / soft clay
- View / Composition: 3/4 isometric view, centered composition, clean 1:1 square canvas
- Lighting: Soft studio lighting with subtle ambient occlusion
- Shadow: Gentle shadow underneath
- Background: Clean white background only
- Quality: High-quality 3D render, soft polished icon finish
""",

    "03 Semi Glossy Vivid": """
Style Guide

- Style Type: Semi Glossy Vivid
- Mood: Bright, cheerful, vivid, eye-catching
- Shape / Form: Rounded silhouette, simplified details, slightly puffy and playful form
- Material: Semi-glossy clay material with subsurface scattering
- View / Composition: 3/4 isometric view, centered single object, clean 1:1 square canvas
- Lighting: Bright studio lighting
- Shadow: Very soft subtle shadow only
- Background: Clean white background only
- Quality: High-quality 3D render, vibrant polished icon finish
""",

    "04 Pastel Jelly": """
Style Guide

- Style Type: Pastel Jelly
- Mood: Dreamy, soft, playful, clean
- Shape / Form: Very smooth rounded silhouette, simplified details, soft minimal single object
- Material: Semi-translucent milky frosted material, jelly-like appearance
- View / Composition: Isometric view, centered single object, clean 1:1 square canvas
- Lighting: Soft diffused lighting, low contrast, blurred gentle highlights
- Shadow: Very soft subtle shadow only
- Background: Pure white background only
- Quality: High-resolution clean 3D render, soft polished finish
""",

    "05 Brushed Metal Coin": """
Style Guide

- Style Type: Brushed Metal Coin
- Mood: Premium, polished, modern, slightly futuristic
- Shape / Form: Rounded silhouette, solid coin-like volume, beveled edges, embossed details
- Material: Smooth metal with subtle brushed finish
- Reflection: Soft metallic reflection
- View / Composition: Front-facing 3/4 view, centered single object, clean 1:1 square canvas
- Lighting: Soft studio lighting from the upper left
- Shadow: Very soft subtle shadow only
- Background: Clean pure white background only
- Quality: High-resolution clean 3D render, premium polished icon finish
""",

    "06 Layered Paper Craft": """
Style Guide

- Style Type: Layered Paper Craft
- Mood: Soft, friendly, minimal, editorial
- Shape / Form: Flat layered cutout shapes, soft stacked paper depth
- Material: Smooth matte paper, subtle paper thickness, clean cut edges
- View / Composition: Slight 3/4 isometric view, centered single object, clean 1:1 square canvas
- Lighting: Soft diffused studio lighting
- Shadow: Very soft small shadows between layers, subtle shadow underneath
- Background: Clean pure white background only
- Quality: High-resolution clean 3D render, polished paper-craft icon quality
""",

    "07 Frosted Acrylic Blue": """
Style Guide

- Style Type: Frosted Acrylic Blue
- Mood: Dreamy, polished, clean, commercial, visually simple
- Shape / Form: Rounded silhouette, soft rounded corners, smooth edges, slightly puffy proportions
- Material: Semi-translucent milky frosted acrylic, soft jelly-like plastic
- Surface: Smooth surface, subtle transparency, gentle depth
- View / Composition: True isometric view, slightly from above, centered single object, clean 1:1 square canvas
- Lighting: Soft diffused studio lighting, low contrast, blurred soft highlights
- Shadow: Very soft faint tinted shadow only
- Background: Pure white background only, no floor line, no backdrop elements
- Quality: High-resolution clean 3D render, soft polished commercial icon quality
"""
}

if st.button("프롬프트 생성", type="primary"):
    prompt = prompt_templates[icon_type]
    prompt = prompt.replace("[object]", object_name)
    prompt = prompt.replace("[color_tone]", color_tone)

    negative_prompt = negative_prompts[icon_type]

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
        st.caption("생성 결과에서 제외할 요소를 함께 복사해 사용하세요.")

    with tab3:
        st.subheader("공통 스타일 가이드")
        st.code(style_guide, language=None)

    st.markdown("---")
    st.subheader("추천 파일명")
    st.code(file_name, language=None)
