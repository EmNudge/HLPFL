import json

new_dat = {
    "location": "puerto rico",
    "disaster": "hurricane",
    "date": "2019-09-20",
    "article": """
Seriously, Puerto Rico is a Caribbean paradise. Forget the Bahamas—just look at the pictures for yourself. Dreamy beaches, palm trees, old Spanish forts, jungles, waterfalls, tropical drinks, delicious seafood—Puerto Rico has it all. I mean, come on—did you know there are rainforests in the USA? It’s no wonder they call it The Island of Enchantment. 

Pro tip: For insider info on all the most amazing gems Puerto Rico has to offer (especially local favorites and off-the-beaten-path treasures), connect with a Puerto Rican local for help creating your Puerto Rico itinerary.

#2. You don’t need a passport to travel to Puerto Rico
People often forget that Puerto Rico is a US territory. That means that you don't need a passport to go there—just the same ID you’d need to fly anywhere else in the US.

#3. You don’t even need to change your money
Because Puerto Rico is a US territory, they also use the US dollar. That means you don't have to exchange your money, and you don’t have to pay foreign transaction fees when using your credit or debit cards. Essentially, traveling to Puerto Rico couldn't be easier—some cellular carriers don’t even charge roaming.

Not the tour group type?

Neither are we. Have a local plan your trip to Puerto Rico.

#4. Most areas have fully recovered from Hurricane Maria
One of the worst disasters in US history, Hurricane Maria claimed the lives of over 3,000 American citizens in 2017. And despite well-publicized issues with federal relief efforts, Puerto Rico has since largely recovered from the tragedy (aside from some very remote areas of the island). Which brings us to our final and most important point:

#5. One of the easiest ways to help the people of Puerto Rico? Spend your tourism dollars there.
No kidding; Puerto Rico is, on the whole, one of the least wealthy areas of the US. And since the tragedy of Hurricane Maria, things have only gotten harder. So aside from donating to charity,  one of the best ways anyone can help the people of Puerto Rico is by putting money directly into the island's economy.

Travel to Puerto Rico and help support the economy

Note: When a ViaHero local helps you plan your trip, 70% of the cost goes directly to the Puerto Rican local doing the planning.

#6. English is widely spoken
Again, Puerto Rico is a US territory. This means that while Spanish is the most popular language on the island, English is an official second language and many people speak it perfectly—so getting around is a breeze, and it’s easy to experience the incredible local culture.

#7. The food is to die for
Travel to Puerto Rico and eat delicious food

Puerto Rico's cuisine is an absolutely mouth-watering mix of Spanish, Caribbean, African, and Asian influences. The fresh seafood is unparalleled (you have to try the aguacate relleno—avocado stuffed with creamy garlic shrimp), and the island grows some of the best coffee, vegetables, and tropical fruit in the entire world. Oh, and did we mention that Puerto Rico is the world’s second-largest producer of rum? Well, we’re mentioning it again. Because rum.

#8. It’s super safe for travelers 
Like any major city, San Juan (the capital of Puerto Rico) has its neighborhoods to avoid. That said, it’s really easy to stay safe in Puerto Rico with a little bit of know-how from a local. As Puerto Rico heavily relies on tourism, the police are very attentive and the island is very, very safe on the whole—just take the same precautions you would in any other city.

#9. Flights are really cheap
Despite its small size, Puerto Rico has over two dozen airports with cheap, daily flights from all over the US and beyond. All the major US airlines fly there (United, American, Delta, JetBlue, Virgin, Southwest, and even Spirit). Plus, fares are ridiculously inexpensive—sometimes as low as $60.

#10. The people are wonderful
Travel to Puerto Rico and meet wonderful people

While it's never good to generalize, Puerto Ricans often pride themselves on their warm, vibrant culture. They did invent salsa dancing, after all. Which brings us to our next point…

#11. The music and dancing are absolutely incredible
Like its food, Puerto Rico's music and dance are a dynamic mix of cultural influences. Salsa dancing was actually invented by Puerto Ricans in 1970’s New York; the Bomba and the Danza, two other popular Puerto Rican dances, were invented on the island hundreds of years ago. And if you think the dancing is incredible, you have to check out the music scene.

#12. Transportation is really easy
Once you’re in Puerto Rico, transportation couldn't be easier. You can rent a car (remember: Puerto Rico is a US territory, so it has all the same car rental places as in the continental US), take public transportation, or just use Uber.

#13. It’s great for families
With its incredible beaches, kid-friendly resorts, and Pirates of the Caribbean-like atmosphere of San Juan, Puerto Rico couldn’t be a better place to take the whole family. Plus, it’s only a 3-hour flight from NYC—so it’s an easy trip for the little ones.

#14. Solo female travelers love Puerto Rico
Solo female travelers enjoy travel to Puerto Rico

Though its culture is all its own, Puerto Rico’s basic social boundaries are the same as in the US. That means that catcalling and harassment issues are similar to those in the states. The violent crime rate, however, is considerably lower in Puerto Rico than in nearly any US state.
"""
}

with open("articles.json", 'r') as fi:
    data = json.load(fi)
    data.append(new_dat)

with open("articles.json", 'w') as fo:
    json.dump(data, fo, indent=2)