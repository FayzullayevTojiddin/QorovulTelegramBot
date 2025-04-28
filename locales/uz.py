start_message = """
Salom!  
Men — guruhingizni tozalovchi qorovulman:

✅ Havolalarni o'chiraman  
✅ So'kinishlarni aniqlab o'chiraman  
✅ Arabcha xabarlarni aniqlab o'chiraman  

📌 **Botni admin qilganingizga ishonch hosil qiling.**  
📌 **Sozlamalarni yaxshilab tekshiring — kerakli filtrlashni yoqing!**

🚀 *Keling, guruhni birga poklaymiz!*
"""

start_button = "✅️️ Boshlash"
documentation_button = "🎥 Qo'llanma"

edit_lang_message = (
    "🌐 *Kerakli tilni tanlang:*\n\n"
    "Tilni o'zgartirish uchun quyidagi tugmalardan birini bosing."
)

edit_lang_button = "🌐 Tilni o'zgartirish"

changed_language_message = "✅ Til muvaffaqiyatli o'zgartirildi!"

main_menu_button = "🏠 Bosh sahifa"

main_menu_message = (
    "🏠 *Bosh sahifa*ga xush kelibsiz!\n\n"
    "Quyidan kerakli bo'limni tanlashingiz mumkin."
)

start_action_message = (
    "👨🏻‍✈️ *Guruhni toza saqlashda yordam beraman!*\n\n"
    "➖ Guruhda *O‘zbekcha* va *Arabcha* reklamalarni, ssilkalarni o‘chirib tashlayman.\n"
    "➖ Yangi a'zolar *kirdi–chiqdi* 🗑 va so‘kingan 🔞+ xabarlarini ham aniqlab o‘chirib beraman.\n\n"
    "ℹ️ *Meni ishlatish uchun guruhingizga qo‘shib*, *Admin* huquqlari berishingiz kerak 😄"
)

add_to_group_action_button = "🚀 Guruhga qoʻshish"
clean_badwords_action_button = "🧹 So‘kinishlarni o‘chirish"
clean_ads_action_button = "📢 Reklamalarni tozalash"

def documentation_message(link):
    return (
        "📚 *Qo'llanma*:\n\n"
        "Ushbu bot guruhingizni toza saqlashda yordam beradi. Quyida asosiy funksiyalarni ko'rib chiqishingiz mumkin:\n\n"
        "1. *Reklamalarni o'chirish*: Guruhdagi *O'zbekcha* va *Arabcha* reklamalarni avtomatik tarzda o'chiradi.\n"
        "2. *So'kinishlarni o'chirish*: Guruhdagi nojo'ya so'zlarni va so'kinishlarni aniqlab, o'chiradi.\n"
        "3. *A'zolarni kuzatish*: Yangi a'zolarni guruhga kirish yoki chiqish holatlarini kuzatib boradi.\n\n"
        "📌 Agar botdan to'liq foydalanish uchun sizga kerak bo'lsa, botni guruhingizga qo'shib, admin huquqlarini berishingiz zarur.\n\n"
        f"*Qo'llanmani ko'rish uchun*: [Qo'llanma havolasi]({link})"
    )

url_documentation = "https://youtube.com/uz_documentation"