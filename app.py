import streamlit as st

# ---------------------------------------
# PAGE CONFIG
# ---------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# ---------------------------------------
# CSS
# ---------------------------------------
st.markdown("""
<style>

.stApp{
    background:#f5f7fb;
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
    box-shadow:0 4px 12px rgba(0,0,0,.08);
    margin-bottom:20px;
    min-height:250px;
}

.product-title{
    font-size:20px;
    font-weight:bold;
}

.product-price{
    color:green;
    font-weight:bold;
    font-size:18px;
}

.category{
    background:#EEF2FF;
    color:#4F46E5;
    padding:4px 10px;
    border-radius:20px;
    display:inline-block;
    margin-bottom:10px;
}

/* Floating support button */

.support-btn{
    position:fixed;
    bottom:30px;
    right:30px;
    background:#4F46E5;
    color:white;
    padding:15px 25px;
    border-radius:50px;
    text-decoration:none;
    font-weight:bold;
    z-index:999;
    box-shadow:0 6px 15px rgba(0,0,0,.25);
}

.support-btn:hover{
    background:#4338CA;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------
# PRODUCTS
# ---------------------------------------

products = [
    {
        "name":"Wireless Bluetooth Headphones",
        "price":79.99,
        "category":"Electronics",
        "description":"Premium noise-cancelling headphones."
    },
    {
        "name":"Smart Fitness Watch",
        "price":129.99,
        "category":"Wearables",
        "description":"Track fitness and health metrics."
    },
    {
        "name":"Mechanical Keyboard",
        "price":89.99,
        "category":"Electronics",
        "description":"RGB mechanical gaming keyboard."
    },
    {
        "name":"Minimalist Backpack",
        "price":54.99,
        "category":"Fashion",
        "description":"Stylish travel backpack."
    },
    {
        "name":"Portable Coffee Maker",
        "price":39.99,
        "category":"Home & Kitchen",
        "description":"Brew coffee anywhere."
    },
    {
        "name":"LED Desk Lamp",
        "price":29.99,
        "category":"Home & Kitchen",
        "description":"Eye-care LED lighting."
    }
]

# ---------------------------------------
# SIDEBAR
# ---------------------------------------

st.sidebar.title("🛍️ MiniStore")

categories = ["All"] + sorted(
    list(set(p["category"] for p in products))
)

selected = st.sidebar.selectbox(
    "Categories",
    categories
)

st.sidebar.markdown("---")

st.sidebar.subheader("🛒 Cart Summary")
st.sidebar.write("Items: 3")
st.sidebar.write("Subtotal: $249.97")
st.sidebar.success("Total: $249.97")

# ---------------------------------------
# HERO
# ---------------------------------------

st.markdown("""
<div class="hero">
<h1>🛍️ MiniStore</h1>
<p>Your One-Stop Shopping Destination</p>
</div>
""", unsafe_allow_html=True)

st.header("Welcome to MiniStore")

st.write("""
Browse premium products at affordable prices.
Discover our featured collection below.
""")

# ---------------------------------------
# FILTER
# ---------------------------------------

if selected == "All":
    filtered = products
else:
    filtered = [
        p for p in products
        if p["category"] == selected
    ]

# ---------------------------------------
# PRODUCTS
# ---------------------------------------

st.header("Featured Products")

cols = st.columns(3)

for i, product in enumerate(filtered):

    with cols[i % 3]:

        st.markdown(f"""
        <div class="product-card">

        <div class="category">
        {product['category']}
        </div>

        <div class="product-title">
        {product['name']}
        </div>

        <div class="product-price">
        ${product['price']}
        </div>

        <p>{product['description']}</p>

        </div>
        """, unsafe_allow_html=True)

        st.button(
            "Add to Cart",
            key=i
        )

# ---------------------------------------
# FLOATING SUPPORT BUTTON
# ---------------------------------------

st.markdown("""
<a href="/Support_Chatbot" target="_self" class="support-btn">
💬 Support
</a>
""", unsafe_allow_html=True)

