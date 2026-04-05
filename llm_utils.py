import json
from typing import Any, Dict, List, Tuple

import streamlit as st
from google import genai
from google.genai import types


MODEL_NAME = "gemini-2.0-flash"


def get_gemini_client() -> genai.Client:
    api_key = st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in Streamlit secrets.")
    return genai.Client(api_key=api_key)


def build_subchapter_context(subchapter: Dict[str, Any]) -> str:
    lines = []
    lines.append(f"Title: {subchapter.get('title', '')}")
    lines.append(f"Learning objective: {subchapter.get('learning_objective', '')}")
    lines.append(f"Theory: {subchapter.get('theory', '')}")

    micro_tips = subchapter.get("micro_tips", [])
    if micro_tips:
        lines.append("Quick tips:")
        for tip in micro_tips:
            lines.append(f"- {tip}")

    examples = subchapter.get("examples", [])
    if examples:
        lines.append("Examples:")
        for ex in examples:
            parts = [f"{ex.get('kannada', '')} = {ex.get('english', '')}"]
            if ex.get("pronunciation_hint"):
                parts.append(f"Pronunciation hint: {ex['pronunciation_hint']}")
            lines.append("- " + " | ".join(parts))

    patterns = subchapter.get("patterns", [])
    if patterns:
        lines.append("Patterns:")
        for p in patterns:
            lines.append(f"- {p}")

    common_mistakes = subchapter.get("common_mistakes", [])
    if common_mistakes:
        lines.append("Common mistakes:")
        for m in common_mistakes:
            lines.append(f"- {m}")

    allowed_variations = subchapter.get("allowed_variations", [])
    if allowed_variations:
        lines.append("Allowed transliteration variations:")
        for v in allowed_variations:
            lines.append(f"- {v}")

    lines.append(f"Test scope: {subchapter.get('test_scope', '')}")
    return "\n".join(lines)


def quiz_schema() -> Dict[str, Any]:
    return {
        "type": "object",
        "properties": {
            "quiz_title": {"type": "string"},
            "instructions": {"type": "string"},
            "questions": {
                "type": "array",
                "minItems": 5,
                "maxItems": 5,
                "items": {
                    "type": "object",
                    "properties": {
                        "question_no": {"type": "integer"},
                        "question_type": {
                            "type": "string",
                            "enum": [
                                "translation_en_to_kn",
                                "translation_kn_to_en",
                                "fill_blank",
                                "pattern_building",
                                "meaning_check"
                            ]
                        },
                        "question_text": {"type": "string"},
                        "expected_skill": {"type": "string"},
                        "hint": {"type": "string"}
                    },
                    "required": [
                        "question_no",
                        "question_type",
                        "question_text",
                        "expected_skill",
                        "hint"
                    ]
                }
            }
        },
        "required": ["quiz_title", "instructions", "questions"]
    }


def evaluation_schema() -> Dict[str, Any]:
    return {
        "type": "object",
        "properties": {
            "overall_score": {"type": "integer"},
            "max_score": {"type": "integer"},
            "pass": {"type": "boolean"},
            "summary_feedback": {"type": "string"},
            "encouragement": {"type": "string"},
            "results": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "question_no": {"type": "integer"},
                        "question_text": {"type": "string"},
                        "user_answer": {"type": "string"},
                        "result": {"type": "string", "enum": ["pass", "retry"]},
                        "score": {"type": "integer"},
                        "better_answer": {"type": "string"},
                        "english_meaning": {"type": "string"},
                        "explanation": {"type": "string"}
                    },
                    "required": [
                        "question_no",
                        "question_text",
                        "user_answer",
                        "result",
                        "score",
                        "better_answer",
                        "english_meaning",
                        "explanation"
                    ]
                }
            }
        },
        "required": [
            "overall_score",
            "max_score",
            "pass",
            "summary_feedback",
            "encouragement",
            "results"
        ]
    }


def generate_quiz(subchapter: Dict[str, Any]) -> Dict[str, Any]:
    client = get_gemini_client()
    context = build_subchapter_context(subchapter)

    prompt = f"""
You are creating a quiz for a beginner spoken Kannada lesson.

Important rules:
1. Use ONLY the lesson content provided below.
2. Do NOT introduce concepts, grammar, words, or sentence patterns not present in the lesson.
3. The learner uses Kannada written in English letters only.
4. Keep all questions beginner-friendly.
5. Generate EXACTLY 5 questions.
6. Keep wording simple and clear.
7. Use a mix of question types, but stay within the lesson scope.
8. Return valid JSON only.

Lesson content:
{context}
""".strip()

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.5,
            response_mime_type="application/json",
            response_schema=quiz_schema(),
        ),
    )

    return json.loads(response.text)


def evaluate_quiz(
    subchapter: Dict[str, Any],
    quiz_data: Dict[str, Any],
    user_answers: List[str]
) -> Dict[str, Any]:
    client = get_gemini_client()
    context = build_subchapter_context(subchapter)

    questions = quiz_data.get("questions", [])
    packaged_questions = []
    for i, q in enumerate(questions):
        packaged_questions.append(
            {
                "question_no": q.get("question_no", i + 1),
                "question_text": q.get("question_text", ""),
                "question_type": q.get("question_type", ""),
                "expected_skill": q.get("expected_skill", ""),
                "hint": q.get("hint", ""),
                "user_answer": user_answers[i] if i < len(user_answers) else ""
            }
        )

    prompt = f"""
You are evaluating answers for a beginner spoken Kannada lesson.

Important rules:
1. Use ONLY the lesson content provided below.
2. Do NOT require Kannada script. The learner writes Kannada only in English transliteration.
3. Be tolerant of minor spelling variation in transliteration.
4. Judge primarily by meaning, understandable transliteration, and beginner-level correctness.
5. Be encouraging and gentle.
6. Score each answer from 0 to 2.
7. Mark an answer as "pass" if it is correct enough for a beginner.
8. Mark an answer as "retry" if meaning is wrong, too incomplete, or clearly outside the lesson.
9. Set overall pass=true if the learner scores at least 6 out of 10.
10. Return valid JSON only.

Lesson content:
{context}

Questions and learner answers:
{json.dumps(packaged_questions, ensure_ascii=False, indent=2)}
""".strip()

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.3,
            response_mime_type="application/json",
            response_schema=evaluation_schema(),
        ),
    )

    return json.loads(response.text)
