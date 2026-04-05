import streamlit as st
from course_data import COURSE_DATA

st.set_page_config(
    page_title="Spoken Kannada Tutor",
    page_icon="🗣️",
    layout="wide"
)

# -----------------------------
# HELPERS
# -----------------------------
def get_chapters():
    return COURSE_DATA["level"]["chapters"]

def flatten_subchapters():
    items = []
    for chapter in get_chapters():
        for sub in chapter["subchapters"]:
            items.append({
                "chapter_id": chapter["chapter_id"],
                "chapter_title": chapter["title"],
                "subchapter_id": sub["id"],
                "subchapter_title": sub["title"]
            })
    return items

def get_subchapter_by_id(subchapter_id):
    for chapter in get_chapters():
        for sub in chapter["subchapters"]:
            if sub["id"] == subchapter_id:
                return chapter, sub
    return None, None

def get_subchapter_index(subchapter_id):
    items = flatten_subchapters()
    for i, item in enumerate(items):
        if item["subchapter_id"] == subchapter_id:
            return i
    return 0

# -----------------------------
# SESSION STATE
# -----------------------------
all_subchapters = flatten_subchapters()

if "selected_subchapter_id" not in st.session_state:
    st.session_state.selected_subchapter_id = all_subchapters[0]["subchapter_id"]

if "visited_subchapters" not in st.session_state:
    st.session_state.visited_subchapters = set()

if "quiz_started_for" not in st.session_state:
    st.session_state.quiz_started_for = None

# mark current as visited
st.session_state.visited_subchapters.add(st.session_state.selected_subchapter_id)

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.title("📚 Course")
    st.caption(COURSE_DATA["course_title"])
    st.write(COURSE_DATA["course_subtitle"])

    for chapter in get_chapters():
        with st.expander(chapter["title"], expanded=False):
            for sub in chapter["subchapters"]:
                label = sub["title"]
                if sub["id"] == st.session_state.selected_subchapter_id:
                    label = f"👉 {label}"

                if st.button(label, key=f"nav_{sub['id']}", use_container_width=True):
                    st.session_state.selected_subchapter_id = sub["id"]
                    st.session_state.visited_subchapters.add(sub["id"])
                    st.session_state.quiz_started_for = None
                    st.rerun()

# -----------------------------
# LOAD CURRENT SUBCHAPTER
# -----------------------------
current_chapter, current_subchapter = get_subchapter_by_id(
    st.session_state.selected_subchapter_id
)

current_index = get_subchapter_index(st.session_state.selected_subchapter_id)
total_subchapters = len(all_subchapters)
visited_count = len(st.session_state.visited_subchapters)
progress_percent = int((visited_count / total_subchapters) * 100)

# recommended next
next_subchapter = None
if current_index + 1 < total_subchapters:
    next_subchapter = all_subchapters[current_index + 1]

# -----------------------------
# HEADER
# -----------------------------
st.title("🗣️ Spoken Kannada Tutor")
st.write("A structured spoken Kannada learning app using English transliteration only.")

# -----------------------------
# LAYOUT
# -----------------------------
main_col, side_col = st.columns([3, 1])

with main_col:
    st.subheader(current_chapter["title"])
    st.markdown(f"### {current_subchapter['title']}")

    if current_subchapter.get("learning_objective"):
        st.info(f"**Learning objective:** {current_subchapter['learning_objective']}")

    st.markdown("### Theory")
    st.write(current_subchapter.get("theory", "No theory available."))

    micro_tips = current_subchapter.get("micro_tips", [])
    if micro_tips:
        st.markdown("### Quick Tips")
        for tip in micro_tips:
            st.write(f"- {tip}")

    examples = current_subchapter.get("examples", [])
    if examples:
        st.markdown("### Examples")
        for ex in examples:
            line = f"**{ex.get('kannada', '')}** = {ex.get('english', '')}"
            if ex.get("pronunciation_hint"):
                line += f"  \nPronunciation hint: `{ex['pronunciation_hint']}`"
            st.markdown(line)

    patterns = current_subchapter.get("patterns", [])
    if patterns:
        st.markdown("### Patterns")
        for p in patterns:
            st.code(p)

    common_mistakes = current_subchapter.get("common_mistakes", [])
    if common_mistakes:
        st.markdown("### Common Mistakes")
        for mistake in common_mistakes:
            st.write(f"- {mistake}")

    allowed_variations = current_subchapter.get("allowed_variations", [])
    if allowed_variations:
        st.markdown("### Acceptable Variations")
        for variation in allowed_variations:
            st.write(f"- {variation}")

    st.markdown("---")
    st.markdown("### Practice")

    if st.button("Test Myself", type="primary"):
        st.session_state.quiz_started_for = current_subchapter["id"]
        st.rerun()

    if st.session_state.quiz_started_for == current_subchapter["id"]:
        st.success("Quiz mode placeholder is ready. In the next step, this button will generate 5 LLM-based questions for this subchapter.")

    # navigation buttons
    nav_left, nav_right = st.columns(2)

    with nav_left:
        if current_index > 0:
            if st.button("⬅ Previous Subchapter", use_container_width=True):
                prev_item = all_subchapters[current_index - 1]
                st.session_state.selected_subchapter_id = prev_item["subchapter_id"]
                st.session_state.quiz_started_for = None
                st.rerun()

    with nav_right:
        if current_index + 1 < total_subchapters:
            if st.button("Next Subchapter ➡", use_container_width=True):
                next_item = all_subchapters[current_index + 1]
                st.session_state.selected_subchapter_id = next_item["subchapter_id"]
                st.session_state.visited_subchapters.add(next_item["subchapter_id"])
                st.session_state.quiz_started_for = None
                st.rerun()

with side_col:
    st.markdown("### Progress")
    st.progress(progress_percent)
    st.write(f"**Visited:** {visited_count} / {total_subchapters}")
    st.write(f"**Progress:** {progress_percent}%")

    st.markdown("---")
    st.markdown("### You Are Here")
    st.write(f"**Chapter:** {current_chapter['title']}")
    st.write(f"**Section:** {current_subchapter['title']}")

    st.markdown("---")
    st.markdown("### Recommended Path")
    st.write("Move chapter by chapter from the top. Read the theory, review examples, then click **Test Myself**.")

    if next_subchapter:
        st.write(f"**Next suggested section:** {next_subchapter['subchapter_title']}")
    else:
        st.write("You are at the final section of Level 1.")

    st.markdown("---")
    st.markdown("### Test Scope")
    st.write(current_subchapter.get("test_scope", "No scope defined."))

    st.markdown("---")
    if st.button("Reset Session Progress", use_container_width=True):
        st.session_state.selected_subchapter_id = all_subchapters[0]["subchapter_id"]
        st.session_state.visited_subchapters = set()
        st.session_state.quiz_started_for = None
        st.rerun()
