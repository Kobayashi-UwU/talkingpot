from pottyboy import Pottyboy

test = Pottyboy.listen_and_recognize()
if test == "gura":
    Pottyboy.text_to_speech("Hi you can order me now")
    
    