import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

.stApp{
    background-color:#f5f7fb;
}

.hero{
    background:linear-gradient(135deg,#4F46E5,#7C3AED);
    padding:40px;
    border-radius:20px;
    color:white;
    text-align:center;
    margin-bottom:30px;
}

.product-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

.product-title{
    font-size:20px;
    font-weight:bold;
}

.product-price{
    color:green;
    font-size:18px;
    font-weight:bold;
}

.category{
    background:#EEF2FF;
    color:#4F46E5;
    padding:4px 10px;
    border-radius:20px;
    display:inline-block;
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# PRODUCT DATA
# --------------------------------------------------
products = [
    {
        "name":"Wireless Bluetooth Headphones",
        "price":79.99,
        "description":"Premium over-ear headphones with noise cancellation.",
        "category":"Electronics"
    },
    {
        "name":"Smart Fitness Watch",
        "price":129.99,
        "description":"Track fitness, sleep and heart rate.",
        "category":"Wearables"
    },
    {
        "name":"Mechanical Keyboard",
        "price":89.99,
        "description":"RGB mechanical keyboard for gaming and work.",
        "category":"Electronics"
    },
    {
        "name":"Minimalist Backpack",
        "price":54.99,
        "description":"Stylish backpack for travel and college.",
        "category":"Fashion"
    },
    {
        "name":"Portable Coffee Maker",
        "price":39.99,
        "description":"Brew coffee anywhere you go.",
        "category":"Home & Kitchen"
    },
    {
        "name":"LED Desk Lamp",
        "price":29.99,
        "description":"Eye-friendly LED lighting for study and work.",
        "category":"Home & Kitchen"
    }
]

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.title("🛍️ MiniStore")

categories = ["All"] + sorted(
    list(set(product["category"] for product in products))
)

selected_category = st.sidebar.selectbox(
    "Browse Categories",
    categories
)

st.sidebar.markdown("---")

st.sidebar.subheader("🛒 Shopping Cart")

st.sidebar.write("Items: 3")
st.sidebar.write("Subtotal: $249.97")
st.sidebar.success("Total: $249.97")

st.sidebar.markdown("---")

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
st.markdown("""
<div class="hero">
<h1>🛍️ MiniStore</h1>
<p>Your One-Stop Shopping Destination</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# WELCOME
# --------------------------------------------------
st.header("Welcome to MiniStore")

st.write("""
Discover premium products at amazing prices.
Browse our featured collection below.
""")

# --------------------------------------------------
# FILTER PRODUCTS
# --------------------------------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        product
        for product in products
        if product["category"] == selected_category
    ]

# --------------------------------------------------
# FEATURED PRODUCTS
# --------------------------------------------------
st.header("Featured Products")

cols = st.columns(3)

for i, product in enumerate(filtered_products):

    with cols[i % 3]:

        st.markdown(
            f"""
            <div class="product-card">
                <div class="category">{product['category']}</div>
                <div class="product-title">{product['name']}</div>
                <div class="product-price">${product['price']}</div>
                <p>{product['description']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.button(
            "Add to Cart",
            key=f"cart_{i}"
        )

# --------------------------------------------------
# SUPPORT MESSAGE
# --------------------------------------------------
st.markdown("---")

st.info(
    "💬 Open the 'Support Chatbot' page from the Streamlit sidebar navigation."
)

