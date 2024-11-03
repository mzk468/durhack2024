#https://dev.to/highcenburg/how-to-down-pitch-a-song-using-python-1opc

from pydub import AudioSegment

def modify_pitch( #1 usuage
    file_name,
    output_file_name,
    ext=".mp3"
    ):

    # Load the audio file
    #audio = AudioSegment.from_file("output_1.mp3")
    audio = AudioSegment.from_file(file_name)

    # Adjust pitch by changing speed (higher speed = higher pitch)
    # 1.25x speed increases pitch, 0.8x decreases pitch
    audio = audio._spawn(audio.raw_data, overrides={"frame_rate": int(audio.frame_rate * 1.25)})
    audio = audio.set_frame_rate(44100)  # Set a common frame rate for playback

    # Adjust speed independently by resampling
    # Slow down by 0.9x or speed up by 1.1x
    audio = audio.speedup(playback_speed=1.1) #Maybe convert to semitones (  "pitch_shift(audio, -1)"  )

    # Adjust volume
    audio = audio + 6  # Increase volume by 6 dB

    # Save the modified audio
    audio.export(f"{output_file_name}{ext}", format="mp3")
    print("file saved")




def main():
    print("audio_modifier main")
    #modify_pitch( "output_1.mp3" )


if __name__ == "__main__":
    main()
