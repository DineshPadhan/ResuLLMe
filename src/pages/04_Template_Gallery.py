
import streamlit as st
import os
from PIL import Image

IFRAME = '<iframe src="https://ghbtns.com/github-btn.html?user=IvanIsCoding&repo=ResuLLMe&type=star&count=true&size=large" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>'

st.markdown(
    f"""
    # ResuLLMe's Template Gallery {IFRAME}
    """,
    unsafe_allow_html=True,
)

# Template dictionary: name -> {description, image_path}
current_dir = os.path.dirname(os.path.realpath(__file__))
img_dir = os.path.abspath(os.path.join(current_dir, '../../.github/images'))

TEMPLATES = {
    "Simple": {
        "description": "The most straightforward template, condensing the most information in a single page. Default for ResuLLMe due to its reliability.",
        "image": os.path.join(img_dir, "Simple_Template.png"),
    },
    "Awesome": {
        "description": "A popular template with nice fonts and design. Condenses a lot of information in a single page. Another strong candidate for default.",
        "image": os.path.join(img_dir, "Awesome_Template.png"),
    },
    "BGJC": {
        "description": "Another classic, single-column template. Presents less information with clear separations among sections.",
        "image": os.path.join(img_dir, "BGJC.png"),
    },
    "Deedy": {
        "description": "A sleek two-column template. More crowded, but excels at using all available space.",
        "image": os.path.join(img_dir, "Deedy.png"),
    },
    "Modern": {
        "description": "A take on the classic, single-column CV style. For a black-and-white template, it's an excellent choice.",
        "image": os.path.join(img_dir, "Modern.png"),
    },
    "Plush": {
        "description": "A variant of the Deedy template with a stylish look. Columns are swapped and the font is different, giving a distinct feeling.",
        "image": os.path.join(img_dir, "Plush.png"),
    },
    "Alta": {
        "description": "An eye-candy template and another popular option. It speaks for itself.",
        "image": os.path.join(img_dir, "Alta_Template.png"),
    },
}


# UI: Label in one column, dropdown and button stacked in another column, centered
st.markdown("---")
col1, col_input, col4 = st.columns([2, 2, 2])

with col_input:
    selected_template = st.selectbox(
        label="",
        options=list(TEMPLATES.keys()),
        key="template_select",
        index=0,
        label_visibility="collapsed"
    )
with col4:
    show = st.button("Show", key="show_button")


# Show template preview when button is clicked (or on first load)
if show or "shown_template" not in st.session_state:
    st.session_state["shown_template"] = selected_template

template = TEMPLATES[st.session_state["shown_template"]]

# Centered display of template name, description, and image
st.markdown("---")
st.markdown(f"<div style='text-align:center;'><b style='font-size:1.5em'>{st.session_state['shown_template']}</b></div>", unsafe_allow_html=True)
st.markdown(f"<div style='text-align:center; margin-bottom:1em;'>{template['description']}</div>", unsafe_allow_html=True)

try:
    image = Image.open(template["image"])
    st.image(image, use_container_width=True)
except Exception as e:
    st.warning(f"Image not found: {template['image']}")
