import subprocess
import pygame

def text_to_speech(text):
    voice = 'en-GB-SoniaNeural'
    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "data.mp3"'


    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('data.mp3')
    print(f"Kira --> {text}")

    try:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


    except Exception as e:
        print(e)

    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

text_to_speech("Plastic bags are a major cause of environmental pollution. Plastic as a substance is non-biodegradable and thus plastic bags remain in the environment for hundreds of years polluting it immensely.")