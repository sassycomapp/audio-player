from ._anvil_designer import audio_playerTemplate
from anvil import *
import anvil.server
from anvil import Timer
from anvil import *

class audio_player(audio_playerTemplate):

    def __init__(self, **properties):
        # Initialize the form and its components
        super().__init__(**properties)
        self.init_components(**properties)

        # Initialize internal properties
        self._source = ""
        self._auto_play = False
        self._loop = False
        self._volume = 50
        self._mute = False
        self._current_time = 0
        self._duration = 0
        self._show_controls = True
        self._playback_rate = 1
        self._theme_color = "#FFD700"

        # Ensure JS initialization happens when the form is shown
        self.set_event_handler('x-show', self.form_show)

    def form_show(self, **event_args):
        """This method is called when the form is shown on the screen."""
        self.call_js('initializeAudioPlayer')  # Call JS to initialize the audio player

    # Existing methods to update properties...
    def update_audio_source(self):
        self.call_js("set_audio_source", self._source)
        if self._auto_play:
            self.call_js("play_audio")

    def set_audio_properties(self):
        self.update_audio_source()
        self.update_auto_play()
        self.update_loop()
        self.update_volume()
        self.update_mute()
        self.update_current_time()
        self.update_show_controls()
        self.update_playback_rate()
        self.update_theme_color()

##########
  
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
        self.update_audio_source()

    @property
    def auto_play(self):
        return self._auto_play

    @auto_play.setter
    def auto_play(self, value):
        self._auto_play = value
        self.update_auto_play()

    @property
    def loop(self):
        return self._loop

    @loop.setter
    def loop(self, value):
        self._loop = value
        self.update_loop()

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value
        self.update_volume()

    @property
    def mute(self):
        return self._mute

    @mute.setter
    def mute(self, value):
        self._mute = value
        self.update_mute()

    @property
    def current_time(self):
        return self._current_time

    @current_time.setter
    def current_time(self, value):
        self._current_time = value
        self.update_current_time()

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value  # Added a setter for 'duration' to make it writable

    @property
    def show_controls(self):
        return self._show_controls

    @show_controls.setter
    def show_controls(self, value):
        self._show_controls = value
        self.update_show_controls()

    @property
    def playback_rate(self):
        return self._playback_rate

    @playback_rate.setter
    def playback_rate(self, value):
        self._playback_rate = value
        self.update_playback_rate()

    @property
    def theme_color(self):
        return self._theme_color

    @theme_color.setter
    def theme_color(self, value):
        self._theme_color = value
        self.update_theme_color()

    def update_audio_source(self):
        def delayed_call():
            self.call_js("set_audio_source", self._source)
            if self._auto_play:
                self.call_js("play_audio")

    def update_auto_play(self):
        def delayed_call():
            self.call_js("set_auto_play", self._auto_play)
          
    def update_loop(self):
        def delayed_call():
            self.call_js("set_loop", self._loop)

    def update_volume(self):
        def delayed_call():
            self.call_js("set_volume", self._volume)

    def update_mute(self):
        def delayed_call():
            self.call_js("set_mute", self._mute)

    def update_current_time(self):
        def delayed_call():
            self.call_js("set_current_time", self._current_time)

    def update_show_controls(self):
        def delayed_call():
            self.call_js("set_show_controls", self._show_controls)

    def update_playback_rate(self):
        def delayed_call():
            self.call_js("set_playback_rate", self._playback_rate)

    def update_theme_color(self):
        def delayed_call():
            self.call_js("set_theme_color", self._theme_color)

    def on_play(self):
        # Logic for play event
        self.update_playback_state("playing")
       
    def on_pause(self):
        # Logic for pause event
        self.update_playback_state("paused")
        
    def on_time_update(self, current_time):
        # Logic for time update event
        self._current_time = current_time
        print(f"Time updated: {current_time}")

    def on_ended(self):
        # Logic for ended event
        self.update_playback_state("ended")
       
    def on_volume_change(self, volume, muted):
        # Logic for volume change event
        self._volume = volume
        self._mute = muted
        print(f"Volume changed to {volume}, muted: {muted}")

    def on_seeked(self, current_time):
        # Logic for seeked event
        self._current_time = current_time
        print(f"Seeked to {current_time}")

    def on_error(self, error_message):
        # Logic for error event
        print(f"Error occurred: {error_message}")
        self.show_error_message(error_message)
        # You can add more logic here if needed, like displaying an error message in the UI

    def on_loaded_metadata(self, duration):
        # Logic for loaded metadata event
        self._duration = duration
        print(f"Metadata loaded, duration: {duration}")

    def on_mute(self):
        # Logic for mute event
        self._mute = True
        self.update_mute()  # Ensure the UI reflects the mute state
        
    def on_unmute(self):
        # Logic for unmute event
        self._mute = False
        self.update_mute()  # Ensure the UI reflects the unmute state

    def update_playback_state(self, state):
        self.call_js("update_playback_state", state)

    def show_error_message(self, error_message):
        self.call_js("display_error_message", error_message)
