start_message = """
Hello!  
I'm the guard who keeps your group clean:

✅ I delete links  
✅ I detect and delete profanity  
✅ I detect and delete Arabic messages  

📌 **Make sure the bot has admin rights.**  
📌 **Check the settings carefully — enable the necessary filters!**

🚀 *Let's keep the group clean together!*
"""

start_button = "✅️️ Start"
documentation_button = "🎥 Guide"

edit_lang_message = (
    "🌐 *Select your preferred language:*\n\n"
    "To change the language, please click one of the buttons below."
)

edit_lang_button = "🌐 Change language"

changed_language_message = "✅ Language has been changed successfully!"

main_menu_button = "🏠 Main Menu"

main_menu_message = (
    "🏠 *Welcome to the Main Menu!*\n\n"
    "Please select the section you need below."
)

start_action_message = (
    "👨🏻‍✈️ *I will help keep your group clean!*\n\n"
    "➖ I will automatically delete *Uzbek* and *Arabic* advertisements and links.\n"
    "➖ I will also remove *join–leave* 🗑 messages and any *profanity* 🔞+ content.\n\n"
    "ℹ️ *To activate me, please add me to your group and grant Admin rights* 😄"
)

add_to_group_action_button = "🚀 Add to group"
clean_badwords_action_button = "🧹 Remove bad words"
clean_ads_action_button = "📢 Clean advertisements"

def documentation_message(link):
    return (
        "📚 *Documentation*:\n\n"
        "This bot helps you maintain cleanliness in your group. Below are the main features:\n\n"
        "1. *Ad removal*: Automatically removes *Uzbek* and *Arabic* ads.\n"
        "2. *Swear word removal*: Detects and removes inappropriate language and offensive words.\n"
        "3. *Member tracking*: Tracks when new members join or leave the group.\n\n"
        "📌 To fully use the bot, you need to add it to your group and grant admin rights.\n\n"
        f"*View the documentation*: [Documentation Link]({link})"
    )

url_documentation = "https://youtube.com/en_documentation"