# Spoken Kannada Tutor Agent

A detailed build guide, architecture walkthrough, and code explanation for a beginner-friendly AI tutor built with **Streamlit + GitHub + Streamlit Community Cloud + Gemini API**.

---

## What this project is

This project is a **Spoken Kannada Tutor Agent** that teaches Kannada through **English transliteration only**.

That means the learner does **not** need to type Kannada script.  
They can type things like:

- `namaskara`
- `nanage neeru beeku`
- `nanna hesaru Rahul`
- `idu nanna mane`

The app teaches theory, examples, patterns, and then generates a small AI quiz for the currently selected topic. The learner answers in transliterated Kannada, and the app evaluates those answers with an LLM.

This is not a full production LMS. It is a strong **advanced MVP** that demonstrates:

- structured course design
- static curriculum
- dynamic quiz generation
- dynamic answer evaluation
- session-based progress
- public sharing through Streamlit

---

# Table of Contents

1. [Project Goal](#project-goal)
2. [What Makes This an AI Agent](#what-makes-this-an-ai-agent)
3. [High-Level Architecture](#high-level-architecture)
4. [Project Files and Their Roles](#project-files-and-their-roles)
5. [How the App Flow Works](#how-the-app-flow-works)
6. [Detailed File-by-File Explanation](#detailed-file-by-file-explanation)
7. [How `app.py` Works](#how-apppy-works)
8. [How `course_data.py` Works](#how-course_datapy-works)
9. [How `llm_utils.py` Works](#how-llm_utilspy-works)
10. [How `requirements.txt` Helps Streamlit](#how-requirementstxt-helps-streamlit)
11. [How Streamlit Session State Is Used](#how-streamlit-session-state-is-used)
12. [How Gemini Integration Works](#how-gemini-integration-works)
13. [How the Quiz Generation Prompt Works](#how-the-quiz-generation-prompt-works)
14. [How the Evaluation Prompt Works](#how-the-evaluation-prompt-works)
15. [How the Files Are Interconnected](#how-the-files-are-interconnected)
16. [Why the Curriculum Was Kept Static](#why-the-curriculum-was-kept-static)
17. [Why the Quiz Was Kept Dynamic](#why-the-quiz-was-kept-dynamic)
18. [Deployment Flow](#deployment-flow)
19. [Rate Limits and Costs](#rate-limits-and-costs)
20. [How Someone Else Can Build Their First Agent from This](#how-someone-else-can-build-their-first-agent-from-this)
21. [Recommended Future Improvements](#recommended-future-improvements)

---

# Project Goal

The goal was to build a first real AI tutoring app that is:

- beginner-friendly
- public-link shareable
- not overengineered
- teachable in a structured way
- dynamic enough to feel intelligent
- deployable in one afternoon

The app was designed around one key principle:

> Keep the **course content fixed**, but make the **practice and evaluation dynamic**.

This is a very good beginner architecture because it avoids two extremes:

### Too rigid
A purely rule-based system only works for pre-coded answers.

### Too loose
A fully LLM-generated curriculum can become inconsistent, repetitive, or hard to control.

So the final design became:

- **Static textbook**
- **Dynamic AI quiz**
- **Dynamic AI evaluator**

That balance is the sweet spot for a first real tutoring agent.

---

# What Makes This an AI Agent

This is an AI agent because it is not just a static webpage or a rule checker.

It does four agent-like things:

1. **Understands current context**
   - Which subchapter is open?
   - What theory and examples are relevant?

2. **Takes a goal**
   - Generate questions only from this lesson
   - Evaluate learner answers against this lesson

3. **Uses a model as reasoning engine**
   - Gemini generates questions
   - Gemini evaluates responses

4. **Produces structured action/results**
   - quiz JSON
   - evaluation JSON
   - pass/retry
   - score
   - corrections
   - explanations

It is still a lightweight agent, not a multi-step autonomous system. But it is a real, useful, purpose-specific AI application.

---

# High-Level Architecture

The project has four main layers:

## 1. Curriculum Layer
Static structured course content.

Stored in:

- `course_data.py`

Contains:

- chapters
- subchapters
- theory
- examples
- patterns
- common mistakes
- test scope

This layer gives the product stability.

---

## 2. UI Layer
Built using Streamlit.

Stored in:

- `app.py`

This layer does:

- sidebar chapter navigation
- main lesson display
- right-side progress/status panel
- quiz button
- answer form
- feedback rendering

---

## 3. Intelligence Layer
Built using Gemini API.

Stored in:

- `llm_utils.py`

This layer does:

- convert lesson content into prompt-ready context
- generate structured quiz JSON
- evaluate answers into structured result JSON

---

## 4. Deployment Layer
Built using:

- `requirements.txt`
- GitHub
- Streamlit Community Cloud

This layer ensures Streamlit knows which Python packages to install and how to run the app.

---

# Project Files and Their Roles

## `app.py`
The main application file.

It is the entrypoint for Streamlit and controls:

- page layout
- sidebar navigation
- content rendering
- quiz form
- state management
- calling the LLM functions

Think of this as the **orchestrator**.

---

## `course_data.py`
The static course knowledge base.

It contains the full structured course as a Python dictionary.

Think of this as the **textbook**.

---

## `llm_utils.py`
The AI helper layer.

It contains functions that:

- connect to Gemini
- build prompts
- define JSON schema
- parse model responses

Think of this as the **AI brain adapter**.

---

## `requirements.txt`
The dependency declaration file.

It tells Streamlit Cloud which Python packages it must install before running the app.

Think of this as the **installation manifest**.

---

# How the App Flow Works

Here is the full flow from open to result:

## Step 1: User opens the app
Streamlit runs `app.py`.

## Step 2: App loads course content
`app.py` imports `COURSE_DATA` from `course_data.py`.

## Step 3: App builds sidebar
The sidebar shows chapters and subchapters from the course file.

## Step 4: User clicks a subchapter
`st.session_state.selected_subchapter_id` changes.

## Step 5: App finds the matching lesson content
`app.py` uses helper functions to fetch the selected chapter and subchapter.

## Step 6: Theory and examples are rendered
The learner sees:
- learning objective
- theory
- examples
- patterns
- mistakes

## Step 7: User clicks **Test Myself**
`app.py` calls:

- `generate_quiz(current_subchapter)`

from `llm_utils.py`

## Step 8: Gemini receives lesson context
The model is told:
- only use this subchapter
- generate exactly 5 questions
- stay within scope
- return valid JSON

## Step 9: Quiz appears
The questions are shown in a form.

## Step 10: User submits answers
`app.py` calls:

- `evaluate_quiz(current_subchapter, quiz_data, answers)`

## Step 11: Gemini evaluates answers
The model is told:
- allow transliteration variation
- focus on meaning and beginner correctness
- score each answer
- return pass/retry and explanation

## Step 12: Feedback appears
The app shows:
- total score
- pass/retry
- summary feedback
- per-question corrections
- encouragement

That is the complete agent loop.

---

# Detailed File-by-File Explanation

# How `app.py` Works

`app.py` is the most visible file because it controls the actual user experience.

It does several jobs.

## 1. Imports

It imports:

- `streamlit as st`
- `COURSE_DATA` from `course_data.py`
- `generate_quiz`, `evaluate_quiz` from `llm_utils.py`

This is the first sign of interconnection.

### Why it matters
`app.py` itself does not contain:
- the curriculum
- the LLM prompt logic

It simply coordinates them.

That separation is very healthy.

---

## 2. Page Configuration

```python
st.set_page_config(page_title="Spoken Kannada Tutor", page_icon="🗣️", layout="wide")
```

This controls:

- browser tab title
- icon
- wide layout

Why wide layout?
Because the app uses:
- main content
- right-side status panel
- left sidebar

A wider layout supports that textbook-like UI better.

---

## 3. Helper Functions

### `get_chapters()`
Returns the list of chapters from the course.

### `flatten_subchapters()`
Converts nested chapter → subchapter structure into a flat ordered list.

This makes it easier to:
- calculate current position
- navigate previous/next
- calculate progress

### `get_subchapter_by_id(subchapter_id)`
Finds the currently selected subchapter.

### `get_subchapter_index(subchapter_id)`
Finds where the selected subchapter sits in the total sequence.

### `reset_quiz_state()`
Clears quiz-related session state whenever:
- the learner changes section
- a new quiz starts
- session progress is reset

This prevents stale quizzes from one subchapter appearing in another.

---

## 4. Session State Initialization

Streamlit reruns the script frequently, so persistent UI values must be stored in `st.session_state`.

This app stores:

- `selected_subchapter_id`
- `visited_subchapters`
- `quiz_started_for`
- `quiz_data`
- `quiz_answers`
- `quiz_result`
- `quiz_error`

### Why session state matters
Without it:
- every click would reset navigation
- quiz questions would vanish
- user answers would disappear
- progress would be lost instantly

Session state gives the app temporary memory during the current browser session.

---

## 5. Sidebar Navigation

The sidebar loops through chapters and subchapters from `COURSE_DATA`.

Each subchapter becomes a button.

When clicked:
- the selected subchapter changes
- it gets marked visited
- quiz state resets
- the app reruns

This creates the textbook-style chapter browser.

---

## 6. Current Lesson Loading

After a subchapter is selected, `app.py` resolves:

- `current_chapter`
- `current_subchapter`

These drive all rendering in the main area.

---

## 7. Progress Calculation

The app calculates:

- total number of subchapters
- number of visited subchapters
- percentage progress

This is not a strict learning lock.
It is a session-only orientation tool.

That matches the product goal:
> advanced MVP, not a full learner account system.

---

## 8. Main Content Rendering

The main content area displays:

- chapter title
- section title
- learning objective
- theory
- micro tips
- examples
- patterns
- common mistakes
- allowed variations

This content comes entirely from `course_data.py`.

`app.py` simply formats it.

---

## 9. Quiz Trigger

When the user clicks **Test Myself**, the app calls:

```python
quiz_data = generate_quiz(current_subchapter)
```

This is the bridge from static curriculum to dynamic AI behavior.

The returned quiz JSON is stored in session state.

---

## 10. Quiz Form Rendering

Once a quiz exists, `app.py` shows the 5 questions inside a Streamlit form.

Why a form?
Because forms let the learner fill all answers first, then submit once.

That is much cleaner than one text box causing multiple reruns.

---

## 11. Evaluation Trigger

When the form is submitted, the app calls:

```python
result = evaluate_quiz(current_subchapter, quiz_data, answers)
```

Again, the actual intelligence is outsourced to `llm_utils.py`.

---

## 12. Feedback Rendering

The app then renders:

- overall score
- pass/retry
- summary feedback
- encouragement
- per-question breakdown

This makes the app feel like a tutor, not just a checker.

---

## 13. Previous / Next Navigation

The learner can move manually across the curriculum.

This is why the app feels like a dynamic textbook rather than a locked lesson queue.

---

# How `course_data.py` Works

This file is the static curriculum database.

It contains one big dictionary called:

```python
COURSE_DATA = {...}
```

---

## Why use a Python file instead of raw JSON?

Two reasons:

### 1. Easier import into Streamlit
Python can directly do:

```python
from course_data import COURSE_DATA
```

### 2. Easier editing for this project
The curriculum was handcrafted and iteratively expanded, so a Python dictionary was more convenient than a separate JSON parsing step.

---

## Structure of the file

The course contains:

- metadata
- level info
- chapters
- subchapters

Each subchapter includes:

- `id`
- `title`
- `learning_objective`
- `theory`
- `micro_tips`
- `examples`
- `patterns`
- `common_mistakes`
- `allowed_variations`
- `test_scope`

---

## Why this design is strong

It gives each lesson both:
- **display content**
- **LLM boundary**

That is important.

The app does not just show a lesson.
It also knows:
> what the AI is allowed to ask from this lesson

That is why `test_scope` exists.

---

## Why examples are rich
The expanded version includes many examples per subchapter so the learner can:
- see repeated patterns
- understand structure
- generalize better
- give the LLM enough material for controlled question generation

---

# How `llm_utils.py` Works

This file is where the AI integration happens.

It acts like an adapter between:
- your structured course
- the Gemini API
- your Streamlit app

---

## 1. Imports

It imports:
- `json`
- typing helpers
- `streamlit`
- Gemini SDK

This lets it:
- read secrets
- call Gemini
- enforce JSON behavior
- return Python dictionaries back to the app

---

## 2. `MODEL_NAME`

This stores the Gemini model name.

This makes model switching easy later.

---

## 3. `get_gemini_client()`

This function reads:

```python
st.secrets["GEMINI_API_KEY"]
```

and creates the Gemini client.

### Why this is good
The API key is not stored:
- in GitHub
- in the code
- in the README

It is securely stored in Streamlit Secrets.

---

## 4. `build_subchapter_context(subchapter)`

This is one of the most important functions.

It takes the selected subchapter and converts it into a clean lesson summary string for the model.

It includes:
- title
- learning objective
- theory
- quick tips
- examples
- patterns
- mistakes
- allowed variations
- test scope

### Why this function matters
This is what keeps the model grounded.

Instead of sending the entire course every time, it sends only:
> the current subchapter context

That keeps:
- cost lower
- latency lower
- behavior more focused
- question generation more relevant

---

## 5. `quiz_schema()`

This defines the required structure for quiz JSON.

Fields include:
- quiz title
- instructions
- exactly 5 questions
- question type
- question text
- expected skill
- hint

### Why schema matters
Without schema, LLM output becomes unpredictable.

Schema helps force the model into:
- valid JSON
- fixed shape
- easier rendering in the UI

---

## 6. `evaluation_schema()`

This defines the required shape for answer evaluation JSON.

Fields include:
- overall score
- max score
- pass
- summary feedback
- encouragement
- per-question result objects

### Why this matters
This lets the UI reliably display the result without brittle text parsing.

---

## 7. `generate_quiz(subchapter)`

This function:
- gets the Gemini client
- builds subchapter context
- constructs a tightly constrained prompt
- requests structured JSON output
- parses the response with `json.loads()`

### The prompt tells Gemini:
- use only the lesson content
- do not invent outside concepts
- generate exactly 5 questions
- keep it beginner friendly
- return JSON only

This is the controlled generation layer.

---

## 8. `evaluate_quiz(subchapter, quiz_data, user_answers)`

This function:
- packages the questions with user answers
- sends them with subchapter context
- asks Gemini to score and explain
- requires structured evaluation JSON

### The evaluator prompt tells Gemini:
- use only this lesson
- allow English transliteration only
- tolerate minor spelling variation
- focus on beginner-acceptable correctness
- score 0 to 2 per answer
- pass if score is 6/10 or higher
- return JSON only

This is the controlled grading layer.

---

# How `requirements.txt` Helps Streamlit

This file looks tiny, but it is essential.

Example:

```txt
streamlit
google-genai
```

## Why it exists

When Streamlit Community Cloud deploys your app, it does not magically know which packages are needed.

It checks the repo for dependency files like `requirements.txt`.

It then installs those packages before running `app.py`.

---

## In this project

### `streamlit`
Needed because the entire UI is built in Streamlit.

Without it:
- the app cannot run
- `import streamlit as st` fails

### `google-genai`
Needed because Gemini integration uses Google’s GenAI SDK.

Without it:
- `from google import genai` fails
- no quiz generation
- no evaluation

---

## Why this matters for beginners
A beginner often thinks:
> “I wrote the Python code, so the app should run.”

But deployment environments are blank machines.
They need instructions about which packages to install.

That is what `requirements.txt` does.

---

# How Streamlit Session State Is Used

Session state is temporary memory inside Streamlit.

In this app it is used for:

- selected lesson
- visited lessons
- current quiz
- current answers
- current result
- error message

## Why this is perfect for MVP
You specifically did **not** want:
- user accounts
- permanent storage
- saved scores across days

So session state is the right choice.

It lasts during:
- current browser session
- current app interaction

and disappears later.

That is exactly the scope you wanted.

---

# How Gemini Integration Works

The integration works like this:

## 1. Secret stored in Streamlit Cloud
```toml
GEMINI_API_KEY="..."
```

## 2. `llm_utils.py` reads the key
via `st.secrets`

## 3. Gemini client is created
inside `get_gemini_client()`

## 4. Current subchapter context is built
using `build_subchapter_context()`

## 5. Model is asked to:
- generate quiz
or
- evaluate answers

## 6. Response is returned as JSON
and converted into Python dictionary

## 7. `app.py` renders it

This is a clean separation of concerns.

---

# How the Quiz Generation Prompt Works

The quiz generation prompt contains strict rules like:

- Use only the lesson content below
- Do not introduce outside grammar or vocabulary
- Generate exactly 5 questions
- Keep wording simple
- Return valid JSON only

This is important because otherwise the model may:
- wander outside the lesson
- ask too difficult questions
- return natural language instead of JSON

The prompt is intentionally narrow.

That is how you make an LLM reliable in product settings.

---

# How the Evaluation Prompt Works

The evaluation prompt does similar guardrailing, but for grading.

It says:
- use only the lesson content
- allow English transliteration only
- tolerate minor spelling variation
- judge mainly by meaning and beginner correctness
- be encouraging
- score 0 to 2 per answer
- pass at 6/10 or higher
- return JSON only

This is what turns the model from “chatbot” into “tutor evaluator.”

---

# How the Files Are Interconnected

This is the simplest way to visualize it:

```text
course_data.py  --->  app.py  --->  llm_utils.py  --->  Gemini API
        ^               |
        |               v
        +------ content display + quiz rendering + evaluation rendering
```

Or in function terms:

## `course_data.py`
Supplies structured lesson content

## `app.py`
Uses that content to:
- show lessons
- capture user interaction
- trigger AI functions

## `llm_utils.py`
Uses the selected lesson content to:
- create prompt context
- call Gemini
- return structured quiz/evaluation data

## `requirements.txt`
Ensures deployment environment can install everything needed to run all of the above

This modular design is one of the strongest parts of the project.

---

# Why the Curriculum Was Kept Static

This was deliberate.

If the LLM generated the entire course dynamically every time:
- lesson quality would vary
- structure would drift
- chapters would become inconsistent
- the app would be harder to trust

A language tutor should feel stable.

So:
- curriculum = static
- testing and grading = dynamic

That is the right beginner architecture.

---

# Why the Quiz Was Kept Dynamic

This was also deliberate.

If quiz questions were hardcoded:
- repetition would become boring
- answers would be easy to memorize
- the app would feel less intelligent

By generating 5 questions from the current subchapter:
- the experience feels fresh
- the app feels smarter
- content remains controlled because the prompt is bounded

This gives you both novelty and safety.

---

# Deployment Flow

Here is the full deployment journey:

## 1. Create GitHub repo
Store:
- `app.py`
- `course_data.py`
- `llm_utils.py`
- `requirements.txt`
- `README.md`

## 2. Deploy to Streamlit Community Cloud
Choose:
- repo
- branch
- `app.py` as entrypoint

## 3. Streamlit reads `requirements.txt`
Installs dependencies

## 4. Add secrets in Streamlit dashboard
Not in GitHub.

## 5. App starts
and becomes publicly available via a shareable `streamlit.app` URL

This is why Streamlit is so good for first AI app projects.

---

# Rate Limits and Costs

A few practical points matter:

## 1. LLM calls are the expensive part
Static course display is basically free.

Cost happens when the app:
- generates quiz
- evaluates answers

## 2. One quiz session can use multiple requests
Usually:
- 1 request to generate
- 1 request to evaluate

But reruns or retries may add more.

## 3. Streamlit reruns scripts often
So app design should avoid wasteful repeated API calls.

That is why future optimization should include:
- caching generated quiz during session
- limiting repeated accidental calls
- graceful error handling

---

# How Someone Else Can Build Their First Agent from This

This project is actually a strong template for first-time builders.

## Core lesson:
Do not start with:
- autonomous workflows
- multiple tools
- databases
- complex memory
- huge system design

Start with this formula:

## Step 1: Choose one specific use case
Example:
- Kannada tutor
- interview coach
- policy explainer
- Excel formula trainer

## Step 2: Separate static and dynamic parts
Ask:
- what should remain fixed?
- what should the AI generate?

## Step 3: Build structured content first
If the content is chaotic, the AI experience becomes chaotic too.

## Step 4: Add one model call at a time
First:
- question generation

Then:
- answer evaluation

## Step 5: Deploy early
A public URL changes the way you think. It makes the project real.

This app follows exactly that pattern.

---

# Recommended Future Improvements

Here are sensible next upgrades.

## 1. Add request caching
Reduce unnecessary API calls.

## 2. Add friendly quota error handling
Instead of showing raw 429 error text.

## 3. Add “Generate easier / harder quiz”
This could be done by adding difficulty in prompt.

## 4. Add spoken audio examples
Only after text experience feels stable.

## 5. Add optional Kannada script toggle
Not required for Level 1, but useful later.

## 6. Add pronunciation audio
Could be done through TTS later.

## 7. Add teacher/admin content editing
Useful only after the MVP is stable.

## 8. Add progress persistence
Only if you later want accounts or repeat learners.

---

# Final Summary

This app works because it combines:

- **structured curriculum**
- **simple but effective Streamlit UI**
- **dynamic AI quiz generation**
- **dynamic AI evaluation**
- **clean separation across files**

## The files play these roles:

- `course_data.py` = the textbook
- `llm_utils.py` = the AI adapter
- `app.py` = the orchestrator and UI
- `requirements.txt` = the deployment dependency manifest

## The main design principle is:
> Keep learning content fixed. Let AI handle bounded generation and evaluation.

That is why this project is a strong example of a first real AI agent app.

---

# Suggested Repo Note

If you want, you can rename this file to the main `README.md` or keep it as:

- `README.md`
- `DETAILED_GUIDE.md`
- `BUILD_NOTES.md`

For public GitHub sharing, a nice pattern is:

- short `README.md`
- detailed `DETAILED_GUIDE.md`

That keeps the repo approachable while still preserving the full textbook-like explanation.
