from django.shortcuts import render
import numpy as np
import pickle
from django.http import HttpResponse
import tensorflow,keras
import pickle
import tensorflow

lang=['R', 'java', 'javascript', 'php', 'python']

def home(request):
    return render(request,'index.html')
    


def predict(request):
    ques=request.POST['ques']


    model=tensorflow.keras.models.load_model('model.h5')
    tokenizer=pickle.load(open('tokenizer.pkl','rb+'))
    seq=tokenizer.texts_to_sequences([ques])
    padseq=tensorflow.keras.preprocessing.sequence.pad_sequences(seq,maxlen=26,padding='post')
    result=model.predict(padseq)
    result_lang=np.argmax(result[0])
    language=lang[result_lang]
    print(language)
    return HttpResponse(language)