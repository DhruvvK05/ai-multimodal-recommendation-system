def get_song_recommendation(weather, emotion):

    songsdict = {

        'Clear': {
            'angry': ["Ziddi Dil"],
            'disgust': ["Channa Mereya"],
            'fear': ["Kabira"],
            'happy': ["Yeh Ishq Hai"],
            'sad': ["Khairiyat"],
            'surprise': ["Dilli Wali Girlfriend"],
            'neutral': ["Ilahi"]
        },

        'Clouds': {
            'angry': ["Break Stuff"],
            'disgust': ["Agar Tum Saath Ho"],
            'fear': ["Kabira"],
            'happy': ["Pal"],
            'sad': ["Channa Mereya"],
            'surprise': ["Phir Le Aaya Dil"],
            'neutral': ["Ilahi"]
        },

        'Rain': {
            'angry': ["Kabhi Jo Baadal Barse"],
            'disgust': ["Aaj Phir Tum Pe"],
            'fear': ["Ae Dil Hai Mushkil"],
            'happy': ["Pyar Hua Ikrar Hua"],
            'sad': ["Tum Hi Ho"],
            'surprise': ["Barso Re Megha"],
            'neutral': ["Jaane Tu... Ya Jaane Na"]
        },

        'Drizzle': {
            'angry': ["Shoutout At Lokhandwala"],
            'disgust': ["Mehngai Dayain"],
            'fear': ["Rabtaa"],
            'happy': ["Aaj Kal Tere Mere"],
            'sad': ["Rimjhim Gire Sawan"],
            'surprise': ["Chaiyya Chaiyya"],
            'neutral': ["Tum Ho"]
        },

        'Thunderstorm': {
            'angry': ["Zinda"],
            'disgust': ["Zehnaseeb"],
            'fear': ["Nadaan Parindey"],
            'happy': ["Galliyan"],
            'sad': ["Tum Hi Ho"],
            'surprise': ["Aaj Ki Raat"],
            'neutral': ["Kyun"]
        },

        'Mist': {
            'angry': ["Bekhayali"],
            'disgust': ["Kabira"],
            'fear': ["Mann Mera"],
            'happy': ["Tum Jo Aaye"],
            'sad': ["Tadap Tadap"],
            'surprise': ["Tera Ban Jaunga"],
            'neutral': ["Tum Mile"]
        }

    }

    weather = weather.capitalize()
    emotion = emotion.lower()

    if weather in songsdict and emotion in songsdict[weather]:
        return songsdict[weather][emotion][0]

    return "Ilahi"