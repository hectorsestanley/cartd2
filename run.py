import streamlit as st

# Set page configuration
st.set_page_config(page_title="Instagram Food Creator", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Recipes", "Cookbooks", "Live Cook-A-Long"])

# Home page
if page == "Home":
    st.title("Welcome to My Food Blog!")
    st.image("https://your-image-url.jpg", use_column_width=True)
    st.write("Hello foodies! Welcome to my food blog where I share my favorite recipes, recommend cookbooks, and host live cook-a-long sessions. Stay tuned and happy cooking!")

# Recipes page
elif page == "Recipes":
    st.title("Delicious Recipes")
    st.write("Here are some of my favorite recipes:")
    
    recipe_1 = {
        "title": "Spaghetti Carbonara",
        "image": "https://your-recipe-image-url.jpg",
        "ingredients": ["200g spaghetti", "100g pancetta", "2 large eggs", "50g pecorino cheese", "50g parmesan", "Black pepper", "Salt"],
        "instructions": "Cook the spaghetti. Fry the pancetta. Beat the eggs and mix with cheese. Combine all ingredients and serve."
    }

    recipe_2 = {
        "title": "Chocolate Cake",
        "image": "https://your-recipe-image-url.jpg",
        "ingredients": ["200g flour", "200g sugar", "100g cocoa powder", "1 tsp baking powder", "1 tsp baking soda", "2 large eggs", "240ml milk", "120ml vegetable oil"],
        "instructions": "Mix dry ingredients. Add wet ingredients and mix well. Bake at 180°C for 30 minutes."
    }

    recipes = [recipe_1, recipe_2]
    
    for recipe in recipes:
        st.subheader(recipe["title"])
        st.image(recipe["image"], width=300)
        st.write("### Ingredients")
        for ingredient in recipe["ingredients"]:
            st.write(f"- {ingredient}")
        st.write("### Instructions")
        st.write(recipe["instructions"])

# Cookbooks page
elif page == "Cookbooks":
    st.title("Recommended Cookbooks")
    st.write("Check out these cookbooks to enhance your culinary skills:")
    
    cookbooks = [
        {"title": "Mastering the Art of French Cooking", "author": "Julia Child", "image": "https://your-cookbook-image-url.jpg", "buy_link": "https://your-buy-link.com"},
        {"title": "The Joy of Cooking", "author": "Irma S. Rombauer", "image": "https://your-cookbook-image-url.jpg", "buy_link": "https://your-buy-link.com"}
    ]
    
    for book in cookbooks:
        st.subheader(book["title"])
        st.image(book["image"], width=200)
        st.write(f"**Author:** {book['author']}")
        st.write(f"[Buy Here]({book['buy_link']})")

# Live Cook-A-Long page
elif page == "Live Cook-A-Long":
    st.title("Join Our Live Cook-A-Long!")
    st.write("Sign up for our next live cook-a-long session and cook together with me in real-time!")
    
    with st.form(key='cookalong_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        recipe_choice = st.selectbox("Choose a recipe to cook", ["Spaghetti Carbonara", "Chocolate Cake"])
        submit_button = st.form_submit_button(label='Sign Up')
    
    if submit_button:
        st.success(f"Thank you for signing up, {name}! An email with the details has been sent to {email}.")

# Running the app
if __name__ == "__main__":
    st.write(page)
