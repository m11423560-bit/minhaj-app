import streamlit as st

# صفحے کی بنیادی سیٹنگ
st.set_page_config(page_title="Minhaj School Assistant", page_icon="🏫")

# جمیل نوری نستعلیق کے لیے CSS
st.markdown("""
    <style>
    @font-face {
        font-family: 'Jameel Noori Nastaleeq';
        src: url('https://fonts.gstatic.com/s/jameelnoorinastaleeq/v1/font.woff2');
    }
    .urdu-text {
        font-family: 'Jameel Noori Nastaleeq', 'Arial';
        direction: rtl;
        text-align: right;
        font-size: 20px;
        line-height: 1.8;
    }
    .stButton>button {
        width: 100%;
        background-color: #28a745;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# ڈیٹا بینک
info = {
    "1": "1. اساتذہ کی عمومی ذمہ داریاں: اسمبلی میں ڈسپلن اور چھٹی کے وقت طلبہ کی باحفاظت روانگی اساتذہ کی بنیادی ذمہ داری ہے۔",
    "2": "2. ایونٹس انچارج: محترمہ لائبہ، محترمہ سحر، محترمہ عشرت، محترمہ عاصمہ، محترمہ پاکیزہ۔",
    "12": "12. مالی امور: تمام فیس وصولی اور ریکارڈ کی ذمہ داری ٹیچر زینت کے پاس ہے۔",
    "14": "14. فیس لسٹ: پلے 1100، نرسری 1200، پریپ 1300، اول 1400 روپے ہے۔"
}

st.title("منہاج ماڈل سکول ڈیجیٹل اسسٹنٹ")

# مینو دکھانا
st.markdown('<div class="urdu-text">--- نمبر لکھ کر معلومات حاصل کریں ---</div>', unsafe_allow_html=True)
st.write("1. ذمہ داریاں | 2. ایونٹس | 12. مالی امور | 14. فیس لسٹ")

# یوزر ان پٹ
user_input = st.text_input("یہاں نمبر لکھیں (مثلاً 1 یا 12):", key="input")

if user_input:
    ans = info.get(user_input, "معذرت، اس نمبر کی معلومات موجود نہیں ہیں۔ 1 سے 15 تک ٹرائی کریں۔")
    st.success(ans)

if st.button("ری سیٹ کریں"):
    st.rerun()