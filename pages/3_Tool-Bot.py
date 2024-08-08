import os
import requests
from gnews import GNews
from langchain_core.messages import AIMessage
import streamlit as st
from langchain.schema import HumanMessage,SystemMessage,AIMessage
import datetime
import google.generativeai as genai


def get_weather(city : str):
    """Give weather for a city
    Args:
        city: a python string denoting the name of a city.
    Returns:
        A python dictionary with keys ['Tool', 'Temperature', 'atmospheric pressure', 'humidity', 'weather_id', 'description', 'country', 'longtitude', 'latitude', 'city']"""
    
    api_key = os.environ["WEATHERMAP_API_KEY"]
    base_url_weather = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url_weather + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)

    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        z = x["sys"]
        c = x["coord"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        country = z["country"] 
        city = x["name"]
        longtitude = c["lon"]
        latitude = c["lat"]
        weather = x["weather"]
        weather_id = weather[0]["id"]
        weather_description = weather[0]["description"]
        
        return {"Tool" : "get_weather",
                "Temperature" : str(current_temperature),
                "atmospheric pressure" : str(current_pressure),
                "humidity" : str(current_humidity),
                "weather_id" : str(weather_id),
                "description" : str(weather_description),
                "country" : str(country),
                "longtitude" : str(longtitude),
                "latitude" : str(latitude),
                "city" : str(city)}
    else:
        return ("City Not Found")
    


def get_news(country : str , topic : str):
    """Give news from a given country about a given topic.
    Args:
        country: a python string denoting the name of a country.
        topic: a python string giving topic of news from the list ['World', 'Nation', 'Business', 'Technology', 'Entertainment', 'Sports', 'Science', 'Health'].
    Returns:
        A python dictionary with keys ['Tool', 'Country', 'Topic', 'title', 'description', 'published date', 'url', 'publisher', 'Image']"""

    google_news = GNews(language='en', country=country, max_results=1, exclude_websites=['yahoo.com', 'cnn.com'])
    json_resp = google_news.get_news_by_topic(topic)
    # print(json_resp)
    article = google_news.get_full_article(json_resp[0]['url'])
    llm = genai.GenerativeModel(model_name='gemini-1.5-flash')
    response = llm.generate_content(f"{article.images}\nfor the above links return only the most suitable link according to the description below:\n{json_resp[0]['title']}\ngive only the link not any other text")
    # print((response.text))
    json_resp[0]['Image'] = response.text
    json_resp[0]['Tool'] = "get_news"
    # st.session_state["tool_chat_flow"].append(AIMessage(content=[json_resp[0]]))
    return json_resp[0]
    # return{
    #     "Tool" : "get_news",
    #     "Country" : country.lower(),
    #     "Topic" : topic.lower(),
    #     "title" : "News Headline or Title",
    #     "description" : 'Vivo X Fold 3 Pro vs Samsung Z Fold 6: Price, display, camera and more compared | Mint  MintBehold the new Samsung Galaxy Z Fold6 and Galaxy Z Flip6: A quick hands-on  The Indian ExpressEverything Samsung announced at Galaxy Unpacked: Galaxy Z Fold6, Z Flip6, Galaxy Watch7, Watch Ultra and more  CNBCTV18Samsung brings more Galaxy AI features with 2024 foldable devices: Details  Business StandardSamsung Galaxy Z Fold 6, Flip 6, Watch Ultra, Watch 7, Buds 3 series — full India prices, variants, availability and more  The Financial Express',
    #     "published date": 'Thu, 11 Jul 2024 02:23:45 GMT',
    #     "url" : "https://news.google.com/",
    #     "publisher" : {'href': 'https://www.livemint.com', 'title': 'Mint'},
    #     "Image" : 'https://www.livemint.com/lm-img/img/2024/07/11/600x338/kv_2exclusive_PC_v4_1720664388624_1720664398392.jpg \n'
    # }


weather_id_icon = {
    "2": ":thunder_cloud_and_rain:",
    "3": ":partly_sunny_rain:",
    "5": ":umbrella_with_rain_drops:",
    "6": ":snowflake:",
    "7": ":fog:",
    "8": ":cloud:"
}

topic_icon = {
    'world': ':globe_with_meridians:',
    'nation': ':world_map:',
    'business': ':bar_chart:',
    'technology': ':robot_face:',
    'entertainment': ':performing_arts:',
    'sports': ':cricket_bat_and_ball:',
    'science': ':microscope:',
    'health': ':medical_symbol:'
    }

country_code = {'australia': 'au', 'botswana': 'bw', 'canada': 'ca', 'ethiopia': 'et', 'ghana': 'gh', 'india': 'in', 'indonesia': 'id', 'ireland': 'ie', 'israel': 'il', 'kenya': 'ke', 'latvia': 'lv', 'malaysia': 'my', 'namibia': 'na', 'new zealand': 'nz', 'nigeria': 'ng', 'pakistan': 'pk', 'philippines': 'ph', 'singapore': 'sg', 'south africa': 'za', 'tanzania': 'tz', 'uganda': 'ug', 'united kingdom': 'gb', 'united states': 'us', 'zimbabwe': 'zw', 'czech republic': 'cz', 'germany': 'de', 'austria': 'at', 'switzerland': 'ch', 'argentina': 'ar', 'chile': 'cl', 'colombia': 'co', 'cuba': 'cu', 'mexico': 'mx', 'peru': 'pe', 'venezuela': 've', 'belgium': 'be', 'france': 'fr', 'morocco': 'ma', 'senegal': 'sn', 'italy': 'it', 'lithuania': 'lt', 'hungary': 'hu', 'netherlands': 'nl', 'norway': 'no', 'poland': 'pl', 'brazil': 'br', 'portugal': 'pt', 'romania': 'ro', 'slovakia': 'sk', 'slovenia': 'si', 'sweden': 'se', 'vietnam': 'vn', 'turkey': 'tr', 'greece': 'gr', 'bulgaria': 'bg', 'russia': 'ru', 'ukraine': 'ua', 'serbia': 'rs', 'united arab emirates': 'ae', 'saudi arabia': 'sa', 'lebanon': 'lb', 'egypt': 'eg', 'bangladesh': 'bd', 'thailand': 'th', 'china': 'cn', 'taiwan': 'tw', 'hong kong': 'hk', 'japan': 'jp', 'republic of korea': 'kr'}


# Gemini llm with tool 
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel(model_name='gemini-1.5-flash', tools=[get_weather, get_news])



# Streamlit Page
st.set_page_config(page_title="Tool-Bot")
st.title("Tool-Agent-Bot")
st.markdown("---")



# Create session state to keep the chat flow for model as memory
if "tool_chat_flow" not in st.session_state:
    st.session_state["tool_chat_flow"] = [SystemMessage(content="You are a chatting AI assistant with tools and agent")]

# Get response message function
def get_Gemini_response(human_question):

    st.session_state["tool_chat_flow"].append(HumanMessage(content=human_question))
    chat = model.start_chat(enable_automatic_function_calling=True)
    response = chat.send_message(human_question)
    print("RESPONSE", response.text)
    ai_answer = {}
    for content in chat.history:
        for part in content.parts:
            if fn := part.function_response:
                for key, val in fn.response.items():
                    ai_answer[key] = val
    print("ai answer", ai_answer)
    if ai_answer == {}:
        st.session_state["tool_chat_flow"].append(AIMessage(content=[response.text]))
        return response.text
    else:
        st.session_state["tool_chat_flow"].append(AIMessage(content=[ai_answer]))
        return ai_answer
 



# Chat Area UI
for message in st.session_state['tool_chat_flow']:
    if message.type == "system":
        with st.chat_message("ASSISTANT"):
            st.write("Hello! how can I help you?") 


human_input = st.chat_input("Ask Tool-Agent...")

if human_input:
    Gemini_response = get_Gemini_response(human_input)

    for message in st.session_state['tool_chat_flow']:
        if message.type == "human":
            with st.chat_message("HUMAN"):
                st.write(message.content)

        elif message.type == "ai":
            with st.chat_message("ASSISTANT"):
                with st.container(border=True):
                    if type(message.content[0]) == dict:
                        if message.content[0]["Tool"] == "get_weather":
                            try:
                            # if message.content["Tool"] == "get_weather":
                                dt = datetime.datetime.now()
                                date = dt.strftime('%A')
                                month = dt.strftime('%m %B')
                                hour = dt.strftime('%I:%M %p')
                                st.text(f"{date} | {month} | {hour}")

                                if (((int((dt.strftime('%I')))) in [12,1,2,3,4,5])&(dt.strftime('%p') == "AM")) or (((int((dt.strftime('%I')))) in [7,8,9,10,11])&(dt.strftime('%p') == "PM")):
                                    st.write(f"# :thermometer: {round(float(message.content[0]['Temperature'])-273.15)}$^\circ$C | :crescent_moon:")
                                else:
                                    st.write(f"# :thermometer: {round(float(message.content[0]['Temperature'])-273.15)}$^\circ$C  :sunny:")
                                
                                st.text(f"{message.content[0]['city']} - {message.content[0]['country']}    |    {message.content[0]['latitude']}N - {message.content[0]['longtitude']}E")
                                # ai_mess_con.write(message.content)
                                st.write(f" :droplet: **Humidity** - {message.content[0]['humidity']}%")
                                st.write(f" :earth_asia: **Pressure** - {message.content[0]['atmospheric pressure']}")
                                st.write(f"## {message.content[0]['description'].capitalize()} {weather_id_icon[message.content[0]['weather_id'][0]]}")
                            
                            except Exception as e:
                                st.write(message.content)
                        
                        if message.content[0]["Tool"] == "get_news":
                            try:
                                st.text(f"Published | {message.content[0]['published date']}")
                                st.write(f"### :flag-{country_code[(message.content[0]['Country']).lower()]}: -{topic_icon[message.content[0]['Topic']]}")
                                # st.write(f"##### {(message.content[0]['Country']).lower()} | {topic_icon[message.content[0]['Topic']]}")
                                st.write(f"#### {message.content[0]['title']}")
                                st.image(message.content[0]['Image'], width=360)
                                st.markdown("---")
                                st.write(message.content[0]['description'])
                                st.write(f":newspaper: [Read Article]({message.content[0]['url']})")

                            except Exception as e:
                                st.write(e)
                    else:
                        st.write(message.content[0])

