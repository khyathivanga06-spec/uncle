import streamlit as st

st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬"
)

st.title("💬 MiniStore Support Assistant")

st.write(
    "Ask me about products, orders, delivery, returns, refunds and payments."
)

# ---------------------------------------------------
# PRODUCT DATABASE
# ---------------------------------------------------

products = {
    "headphones":"Wireless Bluetooth Headphones ($79.99)",
    "watch":"Smart Fitness Watch ($129.99)",
    "keyboard":"Mechanical Keyboard ($89.99)",
    "backpack":"Minimalist Backpack ($54.99)",
    "coffee":"Portable Coffee Maker ($39.99)",
    "lamp":"LED Desk Lamp ($29.99)"
}

# ---------------------------------------------------
# CHAT HISTORY
# ---------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role":"assistant",
            "content":"Hi! I'm MiniStore Support. How can I help you today?"
        }
    ]

# Display messages

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------------------------------
# RULE-BASED BOT
# ---------------------------------------------------

def get_response(user_text):

    text = user_text.lower()

    # Product Questions

    if "product" in text:
        return """
Available products:

• Wireless Bluetooth Headphones - $79.99
• Smart Fitness Watch - $129.99
• Mechanical Keyboard - $89.99
• Minimalist Backpack - $54.99
• Portable Coffee Maker - $39.99
• LED Desk Lamp - $29.99
"""

    if "headphones" in text:
        return "Our Wireless Bluetooth Headphones cost $79.99 and feature noise cancellation."

    if "watch" in text:
        return "The Smart Fitness Watch costs $129.99 and tracks fitness, sleep and heart rate."

    if "keyboard" in text:
        return "The Mechanical Keyboard costs $89.99 and includes RGB lighting."

    if "backpack" in text:
        return "The Minimalist Backpack costs $54.99 and is great for travel."

    if "lamp" in text:
        return "The LED Desk Lamp costs $29.99 and offers eye-care lighting."

    if "coffee" in text:
        return "The Portable Coffee Maker costs $39.99 and is perfect for travel."

    # Delivery

    if "delivery" in text or "shipping" in text:
        return "Standard delivery takes 3-5 business days."

    # Refunds

    if "refund" in text:
        return "Refunds are processed within 5-7 business days after approval."

    # Returns

    if "return" in text:
        return "Products can be returned within 30 days of delivery."

    # Payment

    if "payment" in text or "pay" in text:
        return """
We accept:

• Visa
• Mastercard
• UPI
• PayPal
• Net Banking
"""
    # Order Status

    if "order" in text or "status" in text:
        return """
Demo Order Status:

Order #MS12345
Status: Shipped 🚚
Estimated Delivery: 2 Days
"""

    return """
I can help with:

• Products
• Delivery
• Refunds
• Returns
• Payments
• Order Status
"""

# ---------------------------------------------------
# CHAT INPUT
# ---------------------------------------------------

user_prompt = st.chat_input(
    "Ask your question..."
)

if user_prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(user_prompt)

    response = get_response(user_prompt)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)