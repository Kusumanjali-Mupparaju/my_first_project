import streamlit as st
import requests
from datetime import datetime

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Kusuma Currency Hub",
    page_icon="💱",
    layout="centered"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* ---------- MAIN BACKGROUND ---------- */

.stApp {
    background:
        radial-gradient(circle at 10% 20%, rgba(255,255,255,0.8), transparent 25%),
        radial-gradient(circle at 90% 10%, rgba(255,220,240,0.8), transparent 25%),
        radial-gradient(circle at 80% 90%, rgba(200,240,255,0.8), transparent 30%),
        linear-gradient(135deg, #f6f8ff, #eef7ff, #fff5fb);

    background-attachment: fixed;
}

/* ---------- TITLE ---------- */

.main-title {
    text-align: center;
    font-size: 45px;
    font-weight: 800;
    background: linear-gradient(
        90deg,
        #6a11cb,
        #2575fc,
        #ff4ecd
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 0px;
}

/* ---------- SUBTITLE ---------- */

.subtitle {
    text-align: center;
    color: #666;
    font-size: 18px;
    margin-bottom: 30px;
}

/* ---------- GLASS CARD ---------- */

.glass-card {
    background: rgba(255,255,255,0.55);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);

    border: 1px solid rgba(255,255,255,0.8);

    padding: 25px;
    border-radius: 25px;

    box-shadow:
        0px 10px 30px rgba(80,80,150,0.12);

    margin-bottom: 20px;
}

/* ---------- RESULT ---------- */

.result-card {
    background: linear-gradient(
        135deg,
        rgba(106,17,203,0.95),
        rgba(37,117,252,0.95)
    );

    color: white;

    padding: 30px;

    border-radius: 28px;

    text-align: center;

    box-shadow:
        0px 12px 35px rgba(37,117,252,0.30);

    margin-top: 25px;
}

/* ---------- AMOUNT ---------- */

.amount {
    font-size: 30px;
    font-weight: 700;
}

/* ---------- ARROW ---------- */

.arrow {
    font-size: 35px;
    margin: 10px;
}

/* ---------- CONVERTED AMOUNT ---------- */

.converted {
    font-size: 38px;
    font-weight: 800;
}

/* ---------- RATE CARD ---------- */

.rate-card {
    background: rgba(255,255,255,0.75);

    padding: 18px;

    border-radius: 18px;

    text-align: center;

    margin-top: 15px;

    box-shadow:
        0px 5px 20px rgba(0,0,0,0.08);
}

/* ---------- FOOTER ---------- */

.footer {
    text-align: center;
    color: #777;
    margin-top: 40px;
    font-size: 14px;
}

/* ---------- SECTION TITLE ---------- */

.section-title {
    font-size: 22px;
    font-weight: 700;
    color: #4a148c;
}

/* ---------- BUTTON ---------- */

.stButton > button {
    border-radius: 15px;
    border: none;

    font-weight: 700;

    padding: 10px;

    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="main-title">💱 Kusuma Currency Hub</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    '🌍 Your Smart Currency Journey • Fast • Simple • Live'
    '</div>',
    unsafe_allow_html=True
)

# =========================================================
# CURRENCY DATA
# =========================================================

currencies = {

    "USD": ("🇺🇸", "US Dollar", "$"),
    "EUR": ("🇪🇺", "Euro", "€"),
    "GBP": ("🇬🇧", "British Pound", "£"),
    "INR": ("🇮🇳", "Indian Rupee", "₹"),
    "JPY": ("🇯🇵", "Japanese Yen", "¥"),
    "AUD": ("🇦🇺", "Australian Dollar", "A$"),
    "CAD": ("🇨🇦", "Canadian Dollar", "C$"),
    "SGD": ("🇸🇬", "Singapore Dollar", "S$"),
    "AED": ("🇦🇪", "UAE Dirham", "د.إ"),
    "CHF": ("🇨🇭", "Swiss Franc", "CHF"),
    "CNY": ("🇨🇳", "Chinese Yuan", "¥"),
    "KRW": ("🇰🇷", "South Korean Won", "₩"),
    "NZD": ("🇳🇿", "New Zealand Dollar", "NZ$"),
    "ZAR": ("🇿🇦", "South African Rand", "R"),
    "BRL": ("🇧🇷", "Brazilian Real", "R$")

}

# =========================================================
# LIVE RATE FUNCTION
# =========================================================

@st.cache_data(ttl=3600)
def get_rates(base):

    try:

        url = f"https://open.er-api.com/v6/latest/{base}"

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if data.get("result") == "success":

            return data["rates"]

        return None

    except Exception:

        return None


# =========================================================
# SESSION STATE
# =========================================================

if "history" not in st.session_state:

    st.session_state.history = []


# =========================================================
# INPUT CARD
# =========================================================

st.markdown(
    '<div class="glass-card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">💰 Start Your Currency Journey</div>',
    unsafe_allow_html=True
)

st.write("")

amount = st.number_input(
    "Enter Amount",
    min_value=0.0,
    value=100.0,
    step=1.0
)

currency_list = list(currencies.keys())

col1, col2 = st.columns(2)

with col1:

    from_currency = st.selectbox(
        "🌎 From",
        currency_list,
        index=3
    )

with col2:

    to_currency = st.selectbox(
        "🌍 To",
        currency_list,
        index=0
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

# =========================================================
# SWAP
# =========================================================

if st.button(
    "🔄 Swap Currency",
    use_container_width=True
):

    st.session_state.swap_from = to_currency
    st.session_state.swap_to = from_currency

    st.rerun()

# =========================================================
# CONVERT
# =========================================================

if st.button(
    "✨ Convert My Money",
    use_container_width=True
):

    if amount <= 0:

        st.error(
            "⚠️ Please enter an amount greater than 0."
        )

    else:

        with st.spinner(
            "🌐 Connecting to the currency world..."
        ):

            rates = get_rates(from_currency)

        if rates is None:

            st.error(
                "❌ Could not load live exchange rates."
            )

        elif to_currency not in rates:

            st.error(
                "❌ Selected currency is unavailable."
            )

        else:

            rate = rates[to_currency]

            converted = amount * rate

            # =================================================
            # UNIQUE CURRENCY JOURNEY
            # =================================================

            st.markdown(
                f"""
                <div class="result-card">

                    <div style="font-size:18px;">
                        🌎 YOUR CURRENCY JOURNEY
                    </div>

                    <br>

                    <div class="amount">
                        {currencies[from_currency][2]}
                        {amount:,.2f}
                        {from_currency}
                    </div>

                    <div class="arrow">
                        ⬇️
                    </div>

                    <div class="converted">
                        {currencies[to_currency][2]}
                        {converted:,.2f}
                        {to_currency}
                    </div>

                    <br>

                    <div style="font-size:16px;">
                        ✨ Money transformed successfully!
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            # =================================================
            # RATE
            # =================================================

            st.markdown(
                f"""
                <div class="rate-card">

                    📈 <b>LIVE EXCHANGE RATE</b>

                    <br><br>

                    1 {from_currency}
                    =
                    <b>{rate:.6f}</b>
                    {to_currency}

                </div>
                """,
                unsafe_allow_html=True
            )

            st.success(
                "🎉 Conversion completed successfully!"
            )

            # =================================================
            # HISTORY
            # =================================================

            history = (
                f"{currencies[from_currency][2]}"
                f"{amount:,.2f} {from_currency}"
                f" → "
                f"{currencies[to_currency][2]}"
                f"{converted:,.2f} {to_currency}"
            )

            st.session_state.history.insert(
                0,
                history
            )

            st.session_state.history = \
                st.session_state.history[:5]

            current_time = datetime.now().strftime(
                "%d %B %Y • %I:%M %p"
            )

            st.caption(
                f"🕐 Checked: {current_time}"
            )

# =========================================================
# QUICK CONVERTER
# =========================================================

with st.expander("⚡ Quick Currency Table"):

    quick_amount = st.number_input(
        "Quick amount",
        min_value=1.0,
        value=100.0,
        key="quick"
    )

    rates = get_rates(from_currency)

    if rates:

        quick_currencies = [
            "USD",
            "EUR",
            "GBP",
            "INR",
            "JPY",
            "AUD"
        ]

        for currency in quick_currencies:

            if currency in rates:

                value = (
                    quick_amount *
                    rates[currency]
                )

                st.write(
                    f"{currencies[currency][0]} "
                    f"**{quick_amount:,.2f} "
                    f"{from_currency}** → "
                    f"**{value:,.2f} {currency}**"
                )

# =========================================================
# HISTORY
# =========================================================

with st.expander("🕘 My Conversion History"):

    if st.session_state.history:

        for number, item in enumerate(
            st.session_state.history,
            1
        ):

            st.write(
                f"**{number}.** {item}"
            )

        if st.button(
            "🗑️ Clear History"
        ):

            st.session_state.history = []

            st.rerun()

    else:

        st.info(
            "Your conversion history will appear here."
        )

# =========================================================
# POPULAR CURRENCIES
# =========================================================

with st.expander("🌟 Popular Currency Rates"):

    popular = [
        ("USD", "INR"),
        ("EUR", "INR"),
        ("GBP", "INR"),
        ("AED", "INR"),
        ("USD", "EUR"),
        ("USD", "GBP")
    ]

    for source, target in popular:

        rates = get_rates(source)

        if rates and target in rates:

            st.write(
                f"{currencies[source][0]} "
                f"1 {source} = "
                f"**{rates[target]:.4f} {target}**"
            )

# =========================================================
# ABOUT
# =========================================================

with st.expander("💡 About Kusuma Currency Hub"):

    st.write("""
    ### 💱 Kusuma Currency Hub

    A modern currency converter created using:

    🐍 Python  
    🎈 Streamlit  
    🌐 Live Exchange Rate API  

    ### Main Features

    ✅ Live currency conversion  
    ✅ 15+ currencies  
    ✅ Currency swap  
    ✅ Conversion history  
    ✅ Quick conversion table  
    ✅ Popular currency rates  
    ✅ Attractive glass-style interface  
    ✅ Error handling  
    ✅ Responsive design  

    The application retrieves current exchange-rate
    information from an online exchange-rate service.
    """)

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

    🌸 Designed by Kusuma 🌸

    <br>

    💻 Python + Streamlit

    <br>

    💱 Turning currencies into possibilities!

    </div>
    """,
    unsafe_allow_html=True
)