import random
import streamlit as st

st.set_page_config(page_title="중1 국어 서술형 마스터", page_icon="📚")

st.title("📚 중1 국어 2학기 1차고사 실전 서술형 마스터")
st.write(
    "비상교육 교과서('딩키스패너', '비스듬히', 단어의 짜임, 형태소, 새말 등) 기출"
    " 분석 기반 퀴즈입니다!"
)

# 다양한 기출 및 예상 문제 은행 (총 10문제)
question_bank = [
    {
        "category": "소설 '딩키스패너'",
        "question": (
            "주인공 '팔자'가 엄마가 없는 동안 집에서 마주친 두 가지 돌발"
            " 상황(문제 상황)을 각각 서술하시오."
        ),
        "answer": (
            "화장실 전등불이 나간 것과 세면대 배수구가 막힌 상황이다."
        ),
    },
    {
        "category": "소설 '딩키스패너'",
        "question": (
            "주인공이 '멍키 스패너'를 직접 쥐고 문제를 해결했을 때 느낀 점을"
            " 바탕으로, 이 도구가 가지는 문학적 상징성을 서술하시오."
        ),
        "answer": (
            "단순한 물건을 고치는 도구를 넘어 내 삶의 문제를 내 손으로 직접"
            " 해결하고 자립하게 만드는 '성장의 도구'를 상징한다."
        ),
    },
    {
        "category": "시 '비스듬히'",
        "question": (
            "시 <비스듬히>의 제목인 '비스듬히'가 뜻하는 삶의 태도와 타인과의"
            " 관계를 시의 핵심 은유와 연관 지어 서술하시오."
        ),
        "answer": (
            "꼿꼿하게 서서 혼자 버티는 것이 아니라, 나무와 공기처럼 서로에게"
            " 자연스럽게 기대어 의지하며 더불어 살아가는 아름다운 연대감과"
            " 공존의 자세를 뜻한다."
        ),
    },
    {
        "category": "문법 - 형태소",
        "question": (
            '문장 ["감나무가 크다."]를 형태소로 모두 쪼개고, 그 총개수를'
            " 쓰시오."
        ),
        "answer": "감, 나무, 가, 크-, -다 (총 5개)",
    },
    {
        "category": "문법 - 형태소",
        "question": (
            '문장 ["하늘이 매우 높고 푸르다."]에서 조사 "이"와 어미 "-고"의'
            " 형태소 종류(자립성 유무, 실질적 의미 유무)를 각각 쓰시오."
        ),
        "answer": (
            '"이" : 의존 형태소, 형식 형태소\n"-고" : 의존 형태소, 형식'
            " 형태소"
        ),
    },
    {
        "category": "문법 - 단어의 짜임",
        "question": (
            "다음 단어들의 짜임(단일어, 합성어, 파생어)을 바르게 분류하시오. [단어:"
            " 가을, 보름달, 슬픔, 바다]"
        ),
        "answer": (
            "단일어: 가을, 바다\n합성어: 보름달\n파생어: 슬픔"
        ),
    },
    {
        "category": "문법 - 단어의 짜임",
        "question": (
            "어근과 접사의 개념을 바탕으로 '날고기'와 '사냥꾼'의 단어 형성"
            " 방법(합성법/파생법)을 설명하시오."
        ),
        "answer": "두 단어 모두 어근에 접사(날-, -꾼)가 결합하여 만들어진 '파생어'이다.",
    },
    {
        "category": "문법 - 새말(신조어)",
        "question": (
            "새말 형성 방법 중 '웹툰(웹+카툰)'이나 '친추(친구+추가)'처럼"
            " 기존 단어의 짜임에 맞지 않게 만들어진 대표적인 두 가지 방식을"
            " 서술하시오."
        ),
        "answer": (
            "단어의 첫 글자를 결합하는 방법과 단어의 일부를 따서 결합하는"
            " 방법이다."
        ),
    },
    {
        "category": "문법 - 어휘",
        "question": (
            '다음 괄호에 들어갈 올바른 단어의 기본형을 각각 쓰시오.\n- "추석에 전을'
            ' ( )"\n- "병이 씻은 듯이 ( )"'
        ),
        "answer": "부치다, 낫다",
    },
    {
        "category": "작문 - 주장하는 글",
        "question": (
            "주장하는 글에서 MBTI 검사 결과에 과도하게 의존하면 안 되는 까닭으로"
            " 본문에 제시된 세 가지 근거를 요약하여 서술하시오."
        ),
        "answer": (
            "① '중간'의 성격을 반영하기 어렵고, ② 신뢰도가 떨어지는 자료나"
            " 검사가 뒤섞여 있으며, ③ 응답자의 상태나 상황에 따라 결과가"
            " 바뀔 수 있기 때문이다."
        ),
    },
]

# 세션 상태 관리
if "current_q" not in st.session_state:
  st.session_state.current_q = random.choice(question_bank)
  st.session_state.show_answer = False

q = st.session_state.current_q

st.info(f"📌 **출제 영역:** {q['category']}")
st.subheader(q["question"])

user_answer = st.text_area("✍️ 정답을 조건에 맞게 작성해 보세요:")

col1, col2 = st.columns(2)

with col1:
  if st.button("💡 모범 답안 확인하기"):
    st.session_state.show_answer = True

with col2:
  if st.button("🔄 다른 문제 뽑기 (무한 생성)"):
    st.session_state.current_q = random.choice(question_bank)
    st.session_state.show_answer = False
    st.rerun()

if st.session_state.show_answer:
  st.success(f"**[모범 답안]**\n\n{q['answer']}")