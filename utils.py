import os
import tempfile
import subprocess
# import whisper
# import torch
import librosa
import joblib
import imageio_ffmpeg
import  numpy as np
# from tensorflow.keras.models import load_model
# import tensorflow as tf
# from keras.models import load_model
# from tensorflow.python.keras.layers.recurrent_v2. import load_model
# from tensorflow.python.keras import
# import tensorflow as tf
# from keras.api._v2.keras.models import  load_model
from tensorflow.keras.models import load_model
import  tensorflow as tf
# from keras.models import load_model
def download_video(url):
    temp_dir = tempfile.mkdtemp()
    video_path = os.path.join(temp_dir, "video.mp4")
    subprocess.call(["yt-dlp", "-o", video_path, url])
    return video_path
def extract_audio(video_path):
    audio_path = video_path.replace(".mp4", ".wav")
    ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

    subprocess.call([
        ffmpeg_path,
        "-i", video_path,
        "-ar", "16000",
        "-ac", "1",
        "-t", "10",
        audio_path
    ])
    return audio_path
# def extract_audio(video_path):
#     audio_path = video_path.replace(".mp4", ".wav")
#     subprocess.call(["ffmpeg", "-i", video_path, "-ar", "16000", "-ac", "1", audio_path])
#     return audio_path

def transcribe_audio(audio_path):
    # model = whisper.load_model("base")
    # result = model.transcribe(audio_path)
    return 'result["text"]'

def classify_accent(transcript, audio_path):

    print(audio_path)
    # Example using MFCCs + pretrained classifier
    scaler = joblib.load("models/scaler.save")

    # filename = '/kaggle/input/fffdd54322/speaker11_male_india.mp3'

    filename = audio_path
    Librosa_data, Librosa_sample_rate = librosa.load(filename,sr=None)

    mfccs = librosa.feature.mfcc(y=Librosa_data, sr=Librosa_sample_rate, n_mfcc=20)

    mfccs.tolist()
    # model=tf.keras.models.load_model('models/accent_calssiffication_model.h5')
    model=load_model('models/accent_classiffication_alpha-c2.keras')
    # model=load_model("models/accent_calssiffication_model.h5")
    # model=load_model('models/accent_calssiffication_model.h5')

    Xd = np.mean(mfccs.T, axis=0).reshape(1, -1)

    # Scale the feature
    mfccs_scaled = scaler.transform(Xd)
    print(mfccs_scaled)

    prediction = model.predict(mfccs_scaled)
    print('zzzz')
    print(prediction)
    formatted = [round(float(val), 6) for val in prediction.flatten()]
    print('flatten prediction :')
    print(formatted)
    max_index = formatted.index(max(formatted))

    # prediction_ANN_rounded = [np.argmax(i) for i in formatted]
    # prediction_ANN_rounded = [np.argmax(i) for i in formatted]
    print('prediction_ANN_rounded :')
    print(max_index)


    # speaker = ['american', 'welsh', 'telugu', 'bangla', 'australian', 'british', 'odiya',
    #            'indian', 'malayalam']

    # speaker = ['indian', 'british', 'american', 'australian']

    # speaker = ['australian', 'american', 'british','indian']
    speaker = ['American','British','Indian','Canadian','Australian']


    print(speaker[max_index])

    # confidence = int(max(model.predict_proba(mfccs_scaled)[0]) * 100)
    # confidence = int(max(prediction[0]) * 100)
    percentages = [round(float(val) * 100, 2) for val in prediction.flatten()]
    print(percentages)
    # probs = tf.nn.softmax(prediction).numpy()
    # confidence = int(max(probs[0]) * 100)
    #
    # clf = joblib.load("models/accent_classifier.pkl")
    # prediction = clf.predict(feature)[0]
    # confidence = int(max(clf.predict_proba(feature)[0]) * 100)
    # return prediction, confidence
    return speaker[max_index], max(percentages)



# def classify_accent(transcript, audio_path):
#     # Example using MFCCs + pretrained classifier
#     y, sr = librosa.load(audio_path, sr=16000)
#     mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
#     feature = mfccs.mean(axis=1).reshape(1, -1)
#
#     clf = joblib.load("models/accent_classifier.pkl")
#     prediction = clf.predict(feature)[0]
#     confidence = int(max(clf.predict_proba(feature)[0]) * 100)
#     return prediction, confidence