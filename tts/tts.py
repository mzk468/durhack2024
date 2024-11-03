#https://www.kdnuggets.com/use-hugging-face-transformers-text-to-speech-applications#:~:text=To%20use%20Hugging%20Face%20Transformers%20for%20Text%2Dto%2DSpeech%2C,can%20save%20or%20play%20directly.&text=Hugging%20Face%20provides%20powerful%20models,written%20text%20into%20spoken%20words.
#https://huggingface.co/0x3e9/0x3e9_RVC_models
#https://www.geeksforgeeks.org/convert-text-speech-python/


# Import the required module for text 
# to speech conversion
from gtts import gTTS
import os
from audio_modifier import modify_pitch

OUTPUT_PATH = "out/"

def generate_speech( #1 usage, saves file. Procedure.
                    input_text,
                    output_file_name,
                    input_language='en',
                    deliberate_slow=False,
                    file_extension=".mp3",
                    ): 
    myobj = gTTS(text=input_text, lang=input_language, slow=deliberate_slow)
    myobj.save( f"{OUTPUT_PATH}{output_file_name}{file_extension}" )


def process(data):

    
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)

    #Get input per president 
    #Generate speech per president
    #Modify audio file (pitch etc.) in line with presidents
    #Return
    
    #sample_data = [{'president': 'joe', 'expression': 'happy', 'content': 'Hey there! I’m doing just fine, just working hard, you know?'}, {'president': 'barack', 'expression': 'neutral', 'content': "Well, Joe, I hope you're not just doing fine and actually making a difference."}, {'president': 'donald', 'expression': 'angry', 'content': "Fine? Come on, Barack! You made it look like a college essay—'making a difference.' How about just having a good time?"}, {'president': 'joe', 'expression': 'happy', 'content': 'Sometimes you can have both, Don! It’s all about balance, buddy.'}, {'president': 'barack', 'expression': 'neutral', 'content': 'Exactly! Life isn’t just a game show, Donald.'}, {'president': 'donald', 'expression': 'angry', 'content': 'Game show? You mean like the one I was winning? I was winning everything!'}, {'president': 'joe', 'expression': 'happy', 'content': 'Let’s just say we all bring something to the table—some of us just bring more than others!'}]
    #data = sample_data

    for index, item in enumerate(data):
        #print(f"{item['president'].capitalize()}: {item['content']}")

        #Generate audio AND modify audio based on president
        #Use functions from other py file - WIP
        print_pressident_process_updates = False
        pppu = print_pressident_process_updates

        generated_speech_file_name = f"output_{index}"
        production_output_file_name = f"{OUTPUT_PATH}prod_{index}" #THE FINAL, USED, PRODUCTION AUDIO FILE file name
        
        if item['president'] == 'joe':
             if pppu: print("joe")
             generate_speech( item['content'], generated_speech_file_name, deliberate_slow=True)
             #modify as needed

        elif item['president'] == 'barack':
             if pppu: print("barack")
             generate_speech( item['content'], generated_speech_file_name)
             
             #modify as needed
             modify_pitch(f"{OUTPUT_PATH}{generated_speech_file_name}.mp3", production_output_file_name)

        elif item['president'] == 'donald':
             if pppu: print("donald")
             generate_speech( item['content'], generated_speech_file_name)
             #modify as needed

        if pppu: print("modifications complete")

               
def main():
    sample_data = [{'president': 'joe', 'expression': 'happy', 'content': 'Hey there! I’m doing just fine, just working hard, you know?'}, {'president': 'barack', 'expression': 'neutral', 'content': "Well, Joe, I hope you're not just doing fine and actually making a difference."}, {'president': 'donald', 'expression': 'angry', 'content': "Fine? Come on, Barack! You made it look like a college essay—'making a difference.' How about just having a good time?"}, {'president': 'joe', 'expression': 'happy', 'content': 'Sometimes you can have both, Don! It’s all about balance, buddy.'}, {'president': 'barack', 'expression': 'neutral', 'content': 'Exactly! Life isn’t just a game show, Donald.'}, {'president': 'donald', 'expression': 'angry', 'content': 'Game show? You mean like the one I was winning? I was winning everything!'}, {'president': 'joe', 'expression': 'happy', 'content': 'Let’s just say we all bring something to the table—some of us just bring more than others!'}]
    process( sample_data )


if __name__ == "__main__":
    main()





