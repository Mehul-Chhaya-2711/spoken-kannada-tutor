import streamlit as st
import re

st.set_page_config(page_title="Spoken Kannada Tutor", page_icon="🗣️", layout="centered")

# -----------------------------
# LESSON DATA
# -----------------------------
LESSONS = [
    {
        "id": 1,
        "topic": "Greetings",
        "words": [
            ("namaskara", "hello"),
            ("hegiddira", "how are you?"),
            ("chennagiddini", "I am fine"),
        ],
        "examples": [
            ("namaskara", "Hello"),
            ("hegiddira", "How are you?"),
            ("nanu chennagiddini", "I am fine"),
        ],
        "homework_question": "How would you say: Hello, I am fine",
        "accepted_answers": [
            "namaskara nanu chennagiddini",
            "namaskara chennagiddini",
            "namaskara naanu chennagiddini",
            "namaskara chennagidini",
            "namaskara nanu chennagidini",
        ],
        "better_version": "Namaskara, nanu chennagiddini.",
        "english_meaning": "Hello, I am fine.",
    },
    {
        "id": 2,
        "topic": "Needs",
        "words": [
            ("nanage", "for me / I need"),
            ("neeru", "water"),
            ("beku", "want / need"),
        ],
        "examples": [
            ("nanage neeru beku", "I need water"),
            ("nanage coffee beku", "I need coffee"),
        ],
        "homework_question": "How would you say: I need water",
        "accepted_answers": [
            "nanage neeru beku",
            "nanage neer beku",
            "nanage neeru bekuu",
        ],
        "better_version": "Nanage neeru beku.",
        "english_meaning": "I need water.",
    },
    {
        "id": 3,
        "topic": "Home and place",
        "words": [
            ("nanna", "my"),
            ("mane", "house / home"),
            ("illi", "here"),
        ],
        "examples": [
            ("idu nanna mane", "This is my home"),
            ("nanu illi iddini", "I am here"),
        ],
        "homework_question": "How would you say: This is my home",
        "accepted_answers": [
            "idu nanna mane",
            "idu nanna maney",
            "idu nanna maneu",
        ],
        "better_version": "Idu nanna mane.",
        "english_meaning": "This is my home.",
    },
    {
        "id": 4,
        "topic": "Simple actions",
        "words": [
            ("nanu", "I"),
            ("barthini", "I come / will come"),
            ("hogthini", "I go / will go"),
        ],
        "examples": [
            ("nanu barthini", "I will come"),
            ("nanu hogthini", "I will go"),
        ],
        "homework_question": "How would you say: I will come",
        "accepted_answers": [
            "nanu barthini",
            "naanu barthini",
            "nanu bartini",
            "naanu bartini",
        ],
        "better_version": "Nanu barthini.",
        "english_meaning": "I will come.",
    },
    {
        "id": 5,
        "topic": "Polite everyday phrase",
        "words": [
            ("dayavittu", "please"),
            ("matte heli", "say again"),
            ("gothilla", "I don't know"),
        ],
        "examples": [
            ("dayavittu matte heli", "Please say it again"),
            ("nanage gothilla", "I don't know"),
        ],
        "homework_question": "How would you say: Please say it again",
        "accepted_answers": [
            "dayavittu matte heli",
            "dayavitu matte heli",
            "dayavittu mathe heli",
            "dayavitu mathe heli",
        ],
        "better_version": "Dayavittu matte heli.",
        "english_meaning": "Please say it again.",
    },
]

# -----------------------------
# SESSION STATE
# -----------------------------
if "current_lesson" not in st.session_state:
    st.session_state.current_lesson = 1

if "passed_lessons" not in st.session_state:
    st.session_state.passed_lessons = []

if "last_result" not in st.session_state:
    st.session_state.last_result = None

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def normalize_text(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text

def token_similarity(user_text, target_text):
    user_tokens = set(normalize_text(user_text).split())
    target_tokens = set(normalize_text(target_text).split())

    if not user_tokens or not target_tokens:
        return 0.0

    overlap = len(user_tokens.intersection(target_tokens))
    return overlap / len(target_tokens)

def evaluate_answer(user_answer, lesson):
    normalized_user = normalize_text(user_answer)

    # Exact or near-exact accepted answer
    for ans in lesson["accepted_answers"]:
        if normalized_user == normalize_text(ans):
            return {
                "pass": True,
                "message": "Good job! That is correct enough for a beginner.",
                "better_version": lesson["better_version"],
                "english_meaning": lesson["english_meaning"],
            }

    # Flexible meaning-based match
    best_score = 0
    best_target = ""
    for ans in lesson["accepted_answers"]:
        score = token_similarity(normalized_user, ans)
        if score > best_score:
            best_score = score
            best_target = ans

    if best_score >= 0.67:
        return {
            "pass": True,
            "message": "Nice try — that is understandable and correct enough to pass.",
            "better_version": lesson["better_version"],
            "english_meaning": lesson["english_meaning"],
        }

    return {
        "pass": False,
        "message": "Almost there. Please try once more.",
        "better_version": lesson["better_version"],
        "english_meaning": lesson["english_meaning"],
    }

def get_lesson(lesson_id):
    for lesson in LESSONS:
        if lesson["id"] == lesson_id:
            return lesson
    return None

# -----------------------------
# UI
# -----------------------------
st.title("🗣️ Spoken Kannada Tutor")
st.write("Learn beginner Kannada through English transliteration only.")

total_lessons = len(LESSONS)
passed_count = len(st.session_state.passed_lessons)
progress_percent = int((passed_count / total_lessons) * 100)

st.progress(progress_percent)
st.write(f"Progress: Lesson {st.session_state.current_lesson} of {total_lessons} ({progress_percent}% complete)")

lesson = get_lesson(st.session_state.current_lesson)

if lesson:
    st.subheader(f"Lesson {lesson['id']}: {lesson['topic']}")

    st.markdown("### Words")
    for word, meaning in lesson["words"]:
        st.write(f"- **{word}** = {meaning}")

    st.markdown("### Example sentences")
    for sentence, meaning in lesson["examples"]:
        st.write(f"- **{sentence}** = {meaning}")

    st.markdown("### Homework")
    st.write(lesson["homework_question"])

    user_answer = st.text_input("Type your answer in English letters:")

    if st.button("Submit homework"):
        if not user_answer.strip():
            st.warning("Please type an answer before submitting.")
        else:
            result = evaluate_answer(user_answer, lesson)
            st.session_state.last_result = {
                "user_answer": user_answer,
                "result": result
            }

            if result["pass"]:
                if lesson["id"] not in st.session_state.passed_lessons:
                    st.session_state.passed_lessons.append(lesson["id"])

                if st.session_state.current_lesson < total_lessons:
                    st.session_state.current_lesson += 1

    if st.session_state.last_result:
        last = st.session_state.last_result
        st.markdown("### Feedback")
        st.write(f"**What you wrote:** {last['user_answer']}")
        st.write(f"**Better version:** {last['result']['better_version']}")
        st.write(f"**English meaning:** {last['result']['english_meaning']}")

        if last["result"]["pass"]:
            st.success(last["result"]["message"])
        else:
            st.error(last["result"]["message"])

if passed_count == total_lessons:
    st.balloons()
    st.success("Excellent! You have completed all 5 lessons.")

st.markdown("---")
if st.button("Reset progress"):
    st.session_state.current_lesson = 1
    st.session_state.passed_lessons = []
    st.session_state.last_result = None
    st.rerun()
