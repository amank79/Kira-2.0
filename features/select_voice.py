class SelectVoiceFeature:
    def __init__(self):
        self.voice = 'sonia'

    def update_voice(self):
        if self.voice == "sonia":
            self.set_voice_to_sonia()
        elif self.voice == "prabhat":
            self.set_voice_to_prabhat()
        else:
            self.handle_unsupported_voice()

    def set_voice_to_sonia(self):
        print("Voice updated to Sonia")

    def set_voice_to_prabhat(self):
        print("Voice updated to Prabhat")

    def handle_unsupported_voice(self):
        print("Unsupported voice selection")
