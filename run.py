import streamlit as st

# Set page configuration
st.set_page_config(page_title="Nat's Nourishments", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Recipes", "Cookbooks", "Live Cook-A-Long"])

# Home page
if page == "Home":
    st.title("Nat's Nourishments - Colourful recipes, mostly healthy - sometimes not!")
    st.image("https://your-image-url.jpg", use_column_width=True)
    st.write("Hello foodies! Welcome to my food blog where I share my favorite recipes, recommend cookbooks, and host live cook-a-long sessions. Stay tuned and happy cooking!")

# Recipes page
elif page == "Recipes":
    st.title("Delicious Recipes")
    st.write("Here are some of my favorite recipes:")
    
    recipe_1 = {
        "title": "Spaghetti Carbonara",
        "image": "data:image/jpeg;base64,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",
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
