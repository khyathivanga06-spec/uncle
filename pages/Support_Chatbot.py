import streamlit as st
from openai import OpenAI

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="MiniStore Support",
    page_icon="💬"
)

st.title("💬 MiniStore AI Support")

# -----------------------------------
# OPENAI CLIENT
# -----------------------------------
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# -----------------------------------
# STORE PRODUCT CATALOG
# -----------------------------------
catalog = """
MiniStore Product Catalog:

1. Wireless Bluetooth Headphones
   Price: $79.99
   Category: Electronics
   Features:
   - Noise cancellation
   - Bluetooth connectivity
   - Long battery life

2. Smart Fitness Watch
   Price: $129.99
   Category: Wearables
   Features:
   - Heart rate monitoring
   - Sleep tracking
   - Fitness tracking

3. Mechanical Keyboard
   Price: $89.99
   Category: Electronics
   Features:
   - RGB lighting
   - Mechanical switches
   - Gaming and productivity

4. Minimalist Backpack
   Price: $54.99
   Category: Fashion
   Features:
   - Lightweight
   - Travel friendly
   - Durable material

5. Portable Coffee Maker
   Price: $39.99
   Category: Home & Kitchen
   Features:
   - Compact design
   - Travel use
   - Easy cleaning

6. LED Desk Lamp
   Price: $29.99
   Category: Home & Kitchen
   Features:
   - Eye-care lighting
   - Adjustable brightness
   - Energy efficient
"""

# -----------------------------------
# SYSTEM PROMPT
# -----------------------------------
SYSTEM_PROMPT = f"""
You are MiniStore's professional customer support representative.

Your responsibilities:
- Help customers with products.
- Help with orders.
- Help with delivery questions.
- Help with refunds.
- Help with returns.
- Help with payment methods.

Store information:

{catalog}

Rules:
1. Answer ONLY MiniStore-related questions.
2. If a user asks about topics unrelated to MiniStore,
   politely explain that you only provide assistance
   regarding MiniStore products and services.
3. Be friendly, professional, and concise.
4. Use the product catalog when answering product questions.
5. Never invent products not listed in the catalog.
"""

# -----------------------------------
# CHAT HISTORY
# -----------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------------
# DISPLAY CHAT
# -----------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------------
# USER INPUT
# -----------------------------------
prompt = st.chat_input(
    "Ask about products, delivery, refunds, returns or payments..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(st.session_state.messages)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=messages,
                temperature=0.3
            )

            reply = response.choices[0].message.content

            st.markdown(reply)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )