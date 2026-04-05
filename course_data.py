COURSE_DATA = {
    "course_title": "Spoken Kannada for Real Life",
    "course_subtitle": "Level 1 - Foundation: Words to Useful Sentences",
    "version": "1.0",
    "language_mode": "English transliteration only",
    "target_audience": "Absolute beginners who want to speak basic Kannada in daily life",
    "teaching_style": {
        "approach": "conversation_first_pattern_based",
        "tone": "encouraging_clear_practical",
        "script_policy": "no_kannada_script_required_in_level_1",
        "evaluation_mode_for_app": "llm_generates_5_questions_only_from_current_subchapter_scope"
    },
    "level": {
        "level_id": "L1",
        "title": "Foundation",
        "goal": "Build comfort with pronunciation, identity, daily-use words, sentence patterns, questions, need/want expressions, place/location, and simple present tense",
        "outcomes": [
            "Introduce yourself",
            "Understand and use common daily words",
            "Ask and answer basic questions",
            "Say what you want, need, like, or do not want",
            "Talk about home, place, family, and objects",
            "Use simple daily actions in present tense",
            "Handle very short real-life spoken exchanges"
        ],
        "chapters": [
            {
                "chapter_id": "L1_C1",
                "title": "Sound, Flow, and Spoken Comfort",
                "chapter_goal": "Help the learner hear and type Kannada more naturally in English letters",
                "recommended_order": 1,
                "subchapters": [
                    {
                        "id": "L1_C1_S1",
                        "title": "How Kannada Sounds in Transliteration",
                        "learning_objective": "Understand that Kannada is largely phonetic and should be spoken in smooth sound groups, not broken English-style chunks",
                        "theory": "Kannada is easier when heard as flowing sound blocks. Transliteration is only an approximation, so small spelling variations can still be acceptable if the sound is understandable. Focus on saying words smoothly and consistently.",
                        "micro_tips": [
                            "Say words in sound chunks: na-ma-ska-ra",
                            "Do not over-stress English-style accents",
                            "Double letters often indicate slightly heavier sounds: chenna, gottilla",
                            "Long vowel variation is acceptable in Level 1 if the meaning is clear"
                        ],
                        "examples": [
                            {"kannada": "namaskara", "english": "hello", "pronunciation_hint": "na-ma-ska-ra"},
                            {"kannada": "chennagide", "english": "it is good / fine", "pronunciation_hint": "chen-na-gi-de"},
                            {"kannada": "nanage", "english": "to me / for me", "pronunciation_hint": "na-na-ge"},
                            {"kannada": "gottilla", "english": "I don't know", "pronunciation_hint": "got-ti-lla"}
                        ],
                        "patterns": [
                            "Focus on sound groups, not single English letters"
                        ],
                        "common_mistakes": [
                            "Breaking Kannada into hard English chunks",
                            "Thinking there is only one correct transliteration spelling",
                            "Ignoring flow and speaking letter-by-letter"
                        ],
                        "allowed_variations": [
                            "chennagide / chennagidey",
                            "namaskara / namaskaraa"
                        ],
                        "test_scope": "Only ask about pronunciation awareness, sound flow, and identifying the most natural transliteration among close variants"
                    },
                    {
                        "id": "L1_C1_S2",
                        "title": "Polite Spoken Flow",
                        "learning_objective": "Start with respectful, beginner-safe spoken Kannada",
                        "theory": "Beginners should first learn safe, polite spoken forms. Respectful forms like neevu are useful in most situations and avoid sounding too abrupt or too informal.",
                        "micro_tips": [
                            "Default to respectful forms first",
                            "Short polite lines are better than long broken ones"
                        ],
                        "examples": [
                            {"kannada": "neevu hegiddira?", "english": "How are you?"},
                            {"kannada": "naanu chennagiddini", "english": "I am fine"},
                            {"kannada": "dayavittu", "english": "please"}
                        ],
                        "patterns": [
                            "neevu ___",
                            "naanu ___",
                            "___ dayavittu"
                        ],
                        "common_mistakes": [
                            "Using very casual forms with strangers immediately",
                            "Memorizing words without practicing full mini-lines"
                        ],
                        "test_scope": "Generate simple beginner-safe spoken phrases using polite forms only"
                    }
                ]
            },
            {
                "chapter_id": "L1_C2",
                "title": "Identity, Pronouns, and Basic Self-Introduction",
                "chapter_goal": "Learn who is who, how to name people, and how to introduce yourself",
                "recommended_order": 2,
                "subchapters": [
                    {
                        "id": "L1_C2_S1",
                        "title": "Core Pronouns",
                        "learning_objective": "Recognize and use the most useful personal references in beginner speech",
                        "theory": "Pronouns are the backbone of early Kannada sentence building. Once these are understood, many real conversations become possible.",
                        "examples": [
                            {"kannada": "naanu", "english": "I"},
                            {"kannada": "neevu", "english": "you"},
                            {"kannada": "avanu", "english": "he"},
                            {"kannada": "avalu", "english": "she"},
                            {"kannada": "avaru", "english": "they / he / she (respectful)"}
                        ],
                        "patterns": [
                            "naanu ___",
                            "neevu ___",
                            "avanu ___",
                            "avalu ___",
                            "avaru ___"
                        ],
                        "common_mistakes": [
                            "Using avaru and avanu interchangeably without context",
                            "Forgetting that simple identity lines are often compact in Kannada"
                        ],
                        "test_scope": "Only generate questions on matching pronouns to meaning and building tiny identity lines"
                    },
                    {
                        "id": "L1_C2_S2",
                        "title": "Saying Your Name",
                        "learning_objective": "Introduce yourself and ask someone their name",
                        "theory": "A foundational pattern is naming: 'nanna hesaru ___' and asking 'nimma hesaru enu?'",
                        "examples": [
                            {"kannada": "nanna hesaru Mehul", "english": "My name is Mehul"},
                            {"kannada": "nimma hesaru enu?", "english": "What is your name?"},
                            {"kannada": "nanna hesaru Ananya", "english": "My name is Ananya"}
                        ],
                        "patterns": [
                            "nanna hesaru ___",
                            "nimma hesaru enu?"
                        ],
                        "common_mistakes": [
                            "Using English word order directly",
                            "Replacing nimma with ninna too early in formal contexts"
                        ],
                        "test_scope": "Generate only name-related speaking prompts and short intro exchanges"
                    },
                    {
                        "id": "L1_C2_S3",
                        "title": "Who Is This? Who Are You?",
                        "learning_objective": "Ask and answer simple identity questions",
                        "theory": "Basic who-questions are core to real conversation.",
                        "examples": [
                            {"kannada": "neevu yaaru?", "english": "Who are you?"},
                            {"kannada": "ivaru yaaru?", "english": "Who is this (respectful)?"},
                            {"kannada": "avaru nanna snehita", "english": "He / she is my friend"},
                            {"kannada": "naanu doctor", "english": "I am a doctor"}
                        ],
                        "patterns": [
                            "___ yaaru?",
                            "naanu ___",
                            "ivaru ___",
                            "avaru ___"
                        ],
                        "common_mistakes": [
                            "Trying to force English am/is/are everywhere",
                            "Not recognizing that short identity statements are normal"
                        ],
                        "test_scope": "Identity only: asking who someone is, answering with profession or relation"
                    }
                ]
            },
            {
                "chapter_id": "L1_C3",
                "title": "Greetings, Courtesy, and Social Basics",
                "chapter_goal": "Sound pleasant, polite, and socially functional in everyday Kannada",
                "recommended_order": 3,
                "subchapters": [
                    {
                        "id": "L1_C3_S1",
                        "title": "Greetings",
                        "learning_objective": "Use beginner-friendly greetings and responses",
                        "theory": "Short greeting exchanges are among the first things a learner should become comfortable with.",
                        "examples": [
                            {"kannada": "namaskara", "english": "hello"},
                            {"kannada": "neevu hegiddira?", "english": "How are you?"},
                            {"kannada": "naanu chennagiddini", "english": "I am fine"},
                            {"kannada": "chennagiddini, dhanyavaada", "english": "I am fine, thank you"}
                        ],
                        "patterns": [
                            "namaskara",
                            "neevu hegiddira?",
                            "naanu chennagiddini"
                        ],
                        "common_mistakes": [
                            "Trying to translate English greetings literally",
                            "Using too many words instead of short natural lines"
                        ],
                        "test_scope": "Only greetings, polite responses, and wellness phrases"
                    },
                    {
                        "id": "L1_C3_S2",
                        "title": "Please, Thank You, Sorry, Yes, No",
                        "learning_objective": "Handle the social glue words of daily interaction",
                        "theory": "Courtesy words are small but powerful in real conversations.",
                        "examples": [
                            {"kannada": "dayavittu", "english": "please"},
                            {"kannada": "dhanyavaada", "english": "thank you"},
                            {"kannada": "kshamisi", "english": "excuse me / sorry"},
                            {"kannada": "haudu", "english": "yes"},
                            {"kannada": "illa", "english": "no"}
                        ],
                        "patterns": [
                            "haudu / illa",
                            "dayavittu ___",
                            "kshamisi ___"
                        ],
                        "common_mistakes": [
                            "Using only yes/no without softening tone",
                            "Overusing English sorry instead of a Kannada courtesy line"
                        ],
                        "test_scope": "Only courtesy expressions and their everyday use"
                    }
                ]
            },
            {
                "chapter_id": "L1_C4",
                "title": "Daily Words: Food, Water, Home, Time",
                "chapter_goal": "Build a usable bank of high-frequency daily vocabulary",
                "recommended_order": 4,
                "subchapters": [
                    {
                        "id": "L1_C4_S1",
                        "title": "Food and Drink Basics",
                        "learning_objective": "Recognize and say the most useful daily food words",
                        "theory": "Food and drink vocabulary is highly reusable in early spoken Kannada.",
                        "examples": [
                            {"kannada": "thindi", "english": "snack / breakfast"},
                            {"kannada": "oota", "english": "meal / lunch / food"},
                            {"kannada": "kaapi", "english": "coffee"},
                            {"kannada": "neeru", "english": "water"},
                            {"kannada": "haalu", "english": "milk"},
                            {"kannada": "tea / chaha", "english": "tea"}
                        ],
                        "patterns": [
                            "___ beeku",
                            "___ beda",
                            "idu ___"
                        ],
                        "common_mistakes": [
                            "Learning words without using them in request sentences",
                            "Confusing oota and thindi everywhere"
                        ],
                        "test_scope": "Only basic food/drink identification and tiny request sentences"
                    },
                    {
                        "id": "L1_C4_S2",
                        "title": "Home and Everyday Objects",
                        "learning_objective": "Talk about a house, room, book, pen, and common objects",
                        "theory": "Early object vocabulary supports real conversation quickly.",
                        "examples": [
                            {"kannada": "mane", "english": "house"},
                            {"kannada": "roomu", "english": "room"},
                            {"kannada": "pustaka", "english": "book"},
                            {"kannada": "pennu", "english": "pen"},
                            {"kannada": "idu nanna pustaka", "english": "This is my book"},
                            {"kannada": "adu namma mane", "english": "That is our house"}
                        ],
                        "patterns": [
                            "idu ___",
                            "adu ___",
                            "idu nanna ___",
                            "adu namma ___"
                        ],
                        "common_mistakes": [
                            "Not distinguishing idu and adu",
                            "Trying to say long noun phrases too early"
                        ],
                        "test_scope": "Only objects, this/that, and simple ownership lines"
                    },
                    {
                        "id": "L1_C4_S3",
                        "title": "Time Words",
                        "learning_objective": "Understand common time references in simple speech",
                        "theory": "Short time words help learners build routine sentences quickly.",
                        "examples": [
                            {"kannada": "iga", "english": "now"},
                            {"kannada": "amele", "english": "later"},
                            {"kannada": "modalu", "english": "before"},
                            {"kannada": "beligge", "english": "morning"},
                            {"kannada": "madhyana", "english": "afternoon"},
                            {"kannada": "sanje", "english": "evening"},
                            {"kannada": "ratri", "english": "night"}
                        ],
                        "patterns": [
                            "iga ___",
                            "amele ___",
                            "beligge ___",
                            "ratri ___"
                        ],
                        "common_mistakes": [
                            "Using time words without a sentence pattern",
                            "Mixing now and later"
                        ],
                        "test_scope": "Only basic time words in beginner daily-life contexts"
                    }
                ]
            },
            {
                "chapter_id": "L1_C5",
                "title": "Possession and Belonging",
                "chapter_goal": "Say my, your, our, his, her, and mine/yours in natural early speech",
                "recommended_order": 5,
                "subchapters": [
                    {
                        "id": "L1_C5_S1",
                        "title": "My, Your, Our, His, Her",
                        "learning_objective": "Use possessive forms naturally in short speech",
                        "theory": "Possession patterns are essential to real daily conversation.",
                        "examples": [
                            {"kannada": "nanna mane", "english": "my house"},
                            {"kannada": "nimma pustaka", "english": "your book"},
                            {"kannada": "namma classu", "english": "our class"},
                            {"kannada": "avana pennu", "english": "his pen"},
                            {"kannada": "avala hesaru", "english": "her name"}
                        ],
                        "patterns": [
                            "nanna ___",
                            "nimma ___",
                            "namma ___",
                            "avana ___",
                            "avala ___"
                        ],
                        "common_mistakes": [
                            "Confusing nanna and nanage",
                            "Using English-style of-constructions"
                        ],
                        "test_scope": "Only possession phrases and tiny sentences"
                    },
                    {
                        "id": "L1_C5_S2",
                        "title": "Mine, Yours, Ours",
                        "learning_objective": "Express belonging with forms like mine and yours",
                        "theory": "These short belonging forms make beginner speech more flexible.",
                        "examples": [
                            {"kannada": "idu nandu", "english": "this is mine"},
                            {"kannada": "adu nimdu", "english": "that is yours"},
                            {"kannada": "idu namdu", "english": "this is ours"}
                        ],
                        "patterns": [
                            "idu nandu",
                            "adu nimdu",
                            "idu namdu"
                        ],
                        "common_mistakes": [
                            "Using nanna where nandu is needed",
                            "Over-translating from English"
                        ],
                        "test_scope": "Only mine/yours/ours patterns with this/that"
                    }
                ]
            },
            {
                "chapter_id": "L1_C6",
                "title": "Need, Want, Like, and Refusal",
                "chapter_goal": "Express practical everyday needs and simple preferences",
                "recommended_order": 6,
                "subchapters": [
                    {
                        "id": "L1_C6_S1",
                        "title": "Beeku - Need / Want",
                        "learning_objective": "Say what you want or need in daily life",
                        "theory": "One of the most useful early Kannada structures is expressing need or want with beeku.",
                        "examples": [
                            {"kannada": "nanage neeru beeku", "english": "I need water"},
                            {"kannada": "nanage coffee beeku", "english": "I want coffee"},
                            {"kannada": "nanage doctor beeku", "english": "I need a doctor"}
                        ],
                        "patterns": [
                            "nanage ___ beeku"
                        ],
                        "common_mistakes": [
                            "Dropping nanage",
                            "Using English order directly"
                        ],
                        "test_scope": "Only beginner request / need sentences using beeku"
                    },
                    {
                        "id": "L1_C6_S2",
                        "title": "Beda - Don't Want / No Need",
                        "learning_objective": "Refuse politely or say you do not want something",
                        "theory": "Beda is a very common everyday refusal word.",
                        "examples": [
                            {"kannada": "nanage coffee beda", "english": "I don't want coffee"},
                            {"kannada": "nanage idu beda", "english": "I don't want this"},
                            {"kannada": "nanage tumba beda", "english": "I really don't want it"}
                        ],
                        "patterns": [
                            "nanage ___ beda",
                            "idu beda"
                        ],
                        "common_mistakes": [
                            "Using beda too abruptly",
                            "Confusing illa with beda"
                        ],
                        "test_scope": "Only refusal / no-need expressions with everyday nouns"
                    },
                    {
                        "id": "L1_C6_S3",
                        "title": "Ishta / Gottu / Gottilla",
                        "learning_objective": "Express liking, knowing, and not knowing at a beginner level",
                        "theory": "These are very high-value expressions for natural conversation.",
                        "examples": [
                            {"kannada": "nanage kaapi ishta", "english": "I like coffee"},
                            {"kannada": "nanage gottu", "english": "I know"},
                            {"kannada": "nanage gottilla", "english": "I don't know"}
                        ],
                        "patterns": [
                            "nanage ___ ishta",
                            "nanage gottu",
                            "nanage gottilla"
                        ],
                        "common_mistakes": [
                            "Using English like-structure directly",
                            "Overcomplicating very short useful lines"
                        ],
                        "test_scope": "Only liking / knowing / not knowing in simple first-person lines"
                    }
                ]
            },
            {
                "chapter_id": "L1_C7",
                "title": "Question Words and Survival Questions",
                "chapter_goal": "Ask what, who, where, when, why, which, and simple help questions",
                "recommended_order": 7,
                "subchapters": [
                    {
                        "id": "L1_C7_S1",
                        "title": "Core Question Words",
                        "learning_objective": "Use beginner question words in short practical questions",
                        "theory": "Question words are best learned inside short usable sentence frames.",
                        "examples": [
                            {"kannada": "yaaru?", "english": "who?"},
                            {"kannada": "elli?", "english": "where?"},
                            {"kannada": "yaavaga?", "english": "when?"},
                            {"kannada": "yaake?", "english": "why?"},
                            {"kannada": "enu?", "english": "what?"},
                            {"kannada": "yaava?", "english": "which?"}
                        ],
                        "patterns": [
                            "___ yaaru?",
                            "___ elli?",
                            "___ enu?"
                        ],
                        "common_mistakes": [
                            "Learning question words separately but not in sentence frames",
                            "Adding too many English filler words"
                        ],
                        "test_scope": "Only question-word-based tiny questions and simple answers"
                    },
                    {
                        "id": "L1_C7_S2",
                        "title": "Useful Survival Questions",
                        "learning_objective": "Ask for help, location, and understanding",
                        "theory": "Short practical help questions are more useful than long perfect sentences at this stage.",
                        "examples": [
                            {"kannada": "nimage English gotha?", "english": "Do you know English?"},
                            {"kannada": "nanage artha aagalla", "english": "I don't understand"},
                            {"kannada": "toilet elli?", "english": "Where is the toilet?"},
                            {"kannada": "nimma sahaya beeku", "english": "I need your help"}
                        ],
                        "patterns": [
                            "___ elli?",
                            "nanage ___ beeku",
                            "nanage artha aagalla"
                        ],
                        "common_mistakes": [
                            "Trying long help requests before mastering short urgent ones",
                            "Using only English nouns when short Kannada questions work"
                        ],
                        "test_scope": "Only practical help / understanding / location questions"
                    }
                ]
            },
            {
                "chapter_id": "L1_C8",
                "title": "This, That, Here, There, Which One",
                "chapter_goal": "Talk about nearby and distant things naturally",
                "recommended_order": 8,
                "subchapters": [
                    {
                        "id": "L1_C8_S1",
                        "title": "Idu and Adu",
                        "learning_objective": "Distinguish this and that clearly",
                        "theory": "This and that patterns are basic building blocks for daily speech.",
                        "examples": [
                            {"kannada": "idu pustaka", "english": "This is a book"},
                            {"kannada": "adu mane", "english": "That is a house"},
                            {"kannada": "idu nanna pustaka", "english": "This is my book"}
                        ],
                        "patterns": [
                            "idu ___",
                            "adu ___"
                        ],
                        "common_mistakes": [
                            "Using one form for both this and that",
                            "Mixing object words with place words"
                        ],
                        "test_scope": "Only this/that object identification and ownership"
                    },
                    {
                        "id": "L1_C8_S2",
                        "title": "Illi, Alli, Elli",
                        "learning_objective": "Say here, there, and where",
                        "theory": "These location anchors make simple conversations much easier.",
                        "examples": [
                            {"kannada": "illi", "english": "here"},
                            {"kannada": "alli", "english": "there"},
                            {"kannada": "elli", "english": "where"},
                            {"kannada": "illi banni", "english": "Come here"},
                            {"kannada": "adu alli ide", "english": "That is there"}
                        ],
                        "patterns": [
                            "___ illi ide",
                            "___ alli ide",
                            "___ elli ide?"
                        ],
                        "common_mistakes": [
                            "Confusing object words with place words",
                            "Using only elli without practicing answers"
                        ],
                        "test_scope": "Only simple place-location questions and answers"
                    },
                    {
                        "id": "L1_C8_S3",
                        "title": "Which One?",
                        "learning_objective": "Ask and answer which one at a beginner level",
                        "theory": "Which-one questions are especially useful for houses, books, rooms, and objects.",
                        "examples": [
                            {"kannada": "nimma mane yaavdu?", "english": "Which is your house?"},
                            {"kannada": "yaava pustaka nimdu?", "english": "Which book is yours?"}
                        ],
                        "patterns": [
                            "___ yaavdu?",
                            "yaava ___ ?"
                        ],
                        "common_mistakes": [
                            "Mixing which and what too early",
                            "Making the sentence too long"
                        ],
                        "test_scope": "Only beginner which-one identification using known nouns"
                    }
                ]
            },
            {
                "chapter_id": "L1_C9",
                "title": "Family and People Around You",
                "chapter_goal": "Talk about family members and simple relationships",
                "recommended_order": 9,
                "subchapters": [
                    {
                        "id": "L1_C9_S1",
                        "title": "Family Words",
                        "learning_objective": "Use common family terms in simple speech",
                        "theory": "Family terms are among the most useful early conversation words.",
                        "examples": [
                            {"kannada": "amma", "english": "mother"},
                            {"kannada": "appa", "english": "father"},
                            {"kannada": "anna", "english": "elder brother"},
                            {"kannada": "akka", "english": "elder sister"},
                            {"kannada": "tamma", "english": "younger brother"},
                            {"kannada": "tangi", "english": "younger sister"}
                        ],
                        "patterns": [
                            "ivaru nanna ___",
                            "avaru namma ___"
                        ],
                        "common_mistakes": [
                            "Using only English family words while practicing",
                            "Not reusing pronoun + family patterns"
                        ],
                        "test_scope": "Only family relations and basic identity lines"
                    },
                    {
                        "id": "L1_C9_S2",
                        "title": "Talking About People Around You",
                        "learning_objective": "Describe who someone is in relation to you",
                        "theory": "Family language becomes much more useful when tied to simple identity sentences.",
                        "examples": [
                            {"kannada": "ivaru nanna appa", "english": "This is my father"},
                            {"kannada": "avalu nanna tangi", "english": "She is my younger sister"},
                            {"kannada": "avanu nanna snehita", "english": "He is my friend"}
                        ],
                        "patterns": [
                            "ivaru nanna ___",
                            "avalu nanna ___",
                            "avanu nanna ___"
                        ],
                        "common_mistakes": [
                            "Jumping to complicated relationship explanations too early"
                        ],
                        "test_scope": "Only identity + family/friend relations"
                    }
                ]
            },
            {
                "chapter_id": "L1_C10",
                "title": "Simple Actions in the Present",
                "chapter_goal": "Start speaking about what you do in simple daily life",
                "recommended_order": 10,
                "subchapters": [
                    {
                        "id": "L1_C10_S1",
                        "title": "Go, Come, Eat, Drink, Read, Write",
                        "learning_objective": "Use a small set of everyday verbs in present-style beginner sentences",
                        "theory": "A small controlled verb set is enough to start forming real-life daily sentences.",
                        "examples": [
                            {"kannada": "naanu barthini", "english": "I come / I will come"},
                            {"kannada": "naanu hogthini", "english": "I go / I will go"},
                            {"kannada": "naanu oodthini", "english": "I read / study"},
                            {"kannada": "naanu barithini", "english": "I write"},
                            {"kannada": "naanu neeru kudithini", "english": "I drink water"}
                        ],
                        "patterns": [
                            "naanu ___ thini",
                            "neevu ___ thira?"
                        ],
                        "common_mistakes": [
                            "Expecting perfect tense distinctions immediately",
                            "Mixing learned words with English verbs"
                        ],
                        "test_scope": "Only a small controlled verb set: go, come, eat, drink, read, write"
                    },
                    {
                        "id": "L1_C10_S2",
                        "title": "Mini Daily Routine Sentences",
                        "learning_objective": "Describe a tiny routine in two to four simple lines",
                        "theory": "This is where Level 1 starts feeling like real speech: combine time words, daily words, and common actions.",
                        "examples": [
                            {"kannada": "beligge naanu kaapi kudithini", "english": "In the morning I drink coffee"},
                            {"kannada": "naanu officege hogthini", "english": "I go to the office"},
                            {"kannada": "ratri naanu manege barthini", "english": "At night I come home"}
                        ],
                        "patterns": [
                            "beligge naanu ___",
                            "iga naanu ___",
                            "ratri naanu ___"
                        ],
                        "common_mistakes": [
                            "Trying to narrate too much too early",
                            "Using many English connectors instead of simple Kannada lines"
                        ],
                        "test_scope": "Only beginner daily-routine lines built from already taught words and verbs"
                    }
                ]
            }
        ]
    }
}
