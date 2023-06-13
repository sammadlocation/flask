from flask import Flask,render_template,request,jsonify
import whisper
from flask_cors import CORS
import os
LANGUAGES = {
    "en": "english",
    "zh": "chinese",
    "de": "german",
    "es": "spanish",
    "ru": "russian",
    "ko": "korean",
    "fr": "french",
    "ja": "japanese",
    "pt": "portuguese",
    "tr": "turkish",
    "pl": "polish",
    "ca": "catalan",
    "nl": "dutch",
    "ar": "arabic",
    "sv": "swedish",
    "it": "italian",
    "id": "indonesian",
    "hi": "hindi",
    "fi": "finnish",
    "vi": "vietnamese",
    "he": "hebrew",
    "uk": "ukrainian",
    "el": "greek",
    "ms": "malay",
    "cs": "czech",
    "ro": "romanian",
    "da": "danish",
    "hu": "hungarian",
    "ta": "tamil",
    "no": "norwegian",
    "th": "thai",
    "ur": "urdu",
    "hr": "croatian",
    "bg": "bulgarian",
    "lt": "lithuanian",
    "la": "latin",
    "mi": "maori",
    "ml": "malayalam",
    "cy": "welsh",
    "sk": "slovak",
    "te": "telugu",
    "fa": "persian",
    "lv": "latvian",
    "bn": "bengali",
    "sr": "serbian",
    "az": "azerbaijani",
    "sl": "slovenian",
    "kn": "kannada",
    "et": "estonian",
    "mk": "macedonian",
    "br": "breton",
    "eu": "basque",
    "is": "icelandic",
    "hy": "armenian",
    "ne": "nepali",
    "mn": "mongolian",
    "bs": "bosnian",
    "kk": "kazakh",
    "sq": "albanian",
    "sw": "swahili",
    "gl": "galician",
    "mr": "marathi",
    "pa": "punjabi",
    "si": "sinhala",
    "km": "khmer",
    "sn": "shona",
    "yo": "yoruba",
    "so": "somali",
    "af": "afrikaans",
    "oc": "occitan",
    "ka": "georgian",
    "be": "belarusian",
    "tg": "tajik",
    "sd": "sindhi",
    "gu": "gujarati",
    "am": "amharic",
    "yi": "yiddish",
    "lo": "lao",
    "uz": "uzbek",
    "fo": "faroese",
    "ht": "haitian creole",
    "ps": "pashto",
    "tk": "turkmen",
    "nn": "nynorsk",
    "mt": "maltese",
    "sa": "sanskrit",
    "lb": "luxembourgish",
    "my": "myanmar",
    "bo": "tibetan",
    "tl": "tagalog",
    "mg": "malagasy",
    "as": "assamese",
    "tt": "tatar",
    "haw": "hawaiian",
    "ln": "lingala",
    "ha": "hausa",
    "ba": "bashkir",
    "jw": "javanese",
    "su": "sundanese",
}
app = Flask(__name__)
model = whisper.load_model("base") #769M Parameter
app.config['UPLOAD_FOLDER'] = './'
CORS(app)
app.secret_key ='SECRET_KEY'

#page home
@app.route("/")
def Home():
    return render_template('index.html')

#import fichier
@app.route("/import")
def Import():
    return render_template('import.html')
#record audio
@app.route('/record')
def Record():
    return render_template('record.html')
@app.route('/about')
def About():
    return render_template('about.html')
@app.route('/upload',methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        file = request.files['audio']
        if file:
            file.save(app.config['UPLOAD_FOLDER'] + file.filename)
            result = model.transcribe(file.filename)
            os.remove(file.filename)
            print(result['text'])
            # pour dicter la langue
            a = result["language"]
            langue = LANGUAGES.get(a, 'Unknown')
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'texte': result['text'], 'language':langue})
            else:
                return render_template('import.html', posts=result['text'], lang=langue)
        else:
            return "erreur file not found"
    else:
        return "Méthode non autorisée"


if __name__ == "__main__":
    app.run(debug=True)