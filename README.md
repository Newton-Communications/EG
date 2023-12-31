![EASGen](https://github.com/A-c0rN/EASGen/blob/main/doc/img/EASGen.png)

![PyPI](https://img.shields.io/pypi/v/EASGen?label=Version&style=flat-square) ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/A-c0rN/EASGen/main.yml?style=flat-square) ![PyPI - Downloads](https://img.shields.io/pypi/dm/EASGen?style=flat-square) ![GitHub language count](https://img.shields.io/github/languages/count/A-c0rN/EASGen?style=flat-square) ![GitHub](https://img.shields.io/github/license/A-c0rN/EASGen?style=flat-square)

A Fast Python EAS Generation Library

## Features
> - [x] EAS Generation 
> - [x] Individual Header, Attention Tone, and EOM Generation
> - [x] Fast
> - [x] PyDub AudioSegment Output for Easy Integration
> - [x] Audio File Input for Audio Injection

## Installation
This package should be installable through Pip.

On a Debian Based Linux OS:
```
sudo apt update
sudo apt install python3 python3-pip
pip3 install EASGen
```


On Windows:

[Install Python](https://www.python.org/downloads/)

In CMD:
```
python -m pip install EASGen
```

## Usage
To generate a simple SAME Required Weekly Test:
```python
from EASGen import EASGen
from pydub.playback import play

header = "ZCZC-EAS-RWT-005007+0015-0010000-WACNTECH-" ## EAS Header to send
Alert = EASGen.genEAS(header=header, attentionTone=False, endOfMessage=True) ## Generate an EAS SAME message with no ATTN signal, and with EOMs.
play(Alert) ## Play the EAS Message
```

To Insert Audio into an alert:
```python
from EASGen import EASGen
from pydub.playback import play
from pydub import AudioSegment

header = "ZCZC-CIV-DMO-033000+0100-0010000-WACNTECH-" ## EAS Header to send
audio = AudioSegment.from_wav("NewHampshireDMO.wav") ## Alert Audio import
Alert = EASGen.genEAS(header=header, attentionTone=True, audio=audio, endOfMessage=True) ## Generate an EAS SAME message with an ATTN signal, the imported WAV file as the audio, and with EOMs.
play(Alert) ## Play the EAS Message
## The New Hampshire State Police has activated the New Hampshire Emergency Alert System in order to conduct a practice demo. This concludes this test of the New Hampshire Emergency Alert System.
```
Spamming New Hampshire Demos have never been easier!

For a custom SampleRate:
```python
from EASGen import EASGen
from pydub.playback import play
from pydub import AudioSegment

header = "ZCZC-EAS-DMO-055079+0100-0010000-WACNTECH-" ## EAS Header to send
Alert = EASGen.genEAS(header=header, attentionTone=True, endOfMessage=True, SampleRate=48000) ## Generate an EAS SAME message with an ATTN signal, the imported WAV file as the audio, with EOMs, at a samplerate of 48KHz.
play(Alert) ## Play the EAS Message
```

To export an alert instead of playing it back:
```python
from EASGen import EASGen
from pydub import AudioSegment

header = "ZCZC-EAS-RWT-055079+0100-0010000-WACNTECH-" ## EAS Header to send
Alert = EASGen.genEAS(header=header, attentionTone=True, endOfMessage=True, SampleRate=48000) ## Generate an EAS SAME message with an ATTN signal, the imported WAV file as the audio, and with EOMs.
EASGen.export_wav("Alert.wav", Alert)
```

To resample an alert after generation (If SampleRate is making the audio weird):
```python
from EASGen import EASGen
from pydub.playback import play
from pydub import AudioSegment

header = "ZCZC-EAS-DMO-055079+0100-0010000-WACNTECH-" ## EAS Header to send
Alert = EASGen.genEAS(header=header, attentionTone=True, endOfMessage=True) ## Generate an EAS SAME message with an ATTN signal, the imported WAV file as the audio, and with EOMs.
Alert = Alert.set_frame_rate(8000) ## Resample the alert to 8KHz for no reason lol.
play(Alert) ## Play the EAS Message
```

To simulate an ENDEC type:
```python
from EASGen import EASGen
from pydub.playback import play
from pydub import AudioSegment

header = "ZCZC-CIV-DMO-033000+0100-0010000-WACNTECH-" ## EAS Header to send
audio = AudioSegment.from_wav("NewHampshireDMO.wav") ## Alert Audio import
Alert = EASGen.genEAS(header=header, attentionTone=True, audio=audio, mode="DIGITAL", endOfMessage=True) ## Generate an EAS SAME message with an ATTN signal, the imported WAV file as the audio, with EOMs, and with a SAGE DIGITAL ENDEC style.
play(Alert) ## Play the EAS Message
## The New Hampshire State Police has activated the New Hampshire Emergency Alert System in order to conduct a practice demo. This concludes this test of the New Hampshire Emergency Alert System.
```
Now you can make all the Mocks you want!

Supported ENDECS:
> - [x] None
> - [x] TFT (Resample to 8KHZ using ".set_frame_rate(8000)" on the generated alert)
> - [x] EASyCAP (Basically the same as None)
> - [x] DASDEC (Crank up the Samplerate to 48000 for this one)
> - [x] SAGE EAS ENDEC (Mode = "SAGE")
> - [x] SAGE DIGITAL ENDEC (Mode = "DIGITAL")
> - [x] Trilithic EASyPLUS/CAST/IPTV (Mode = "TRILITHIC")
> - [x] NWS (Mode = "NWS", Resample to 11KHZ using ".set_frame_rate(11025)" on the generated alert)

Unsupported ENDECS:
> - [ ] HollyAnne Units (Can't sample down to 5KHz... This is a good thing.)
> - [ ] Gorman-Reidlich Units (Don't listen to them enough to simulate. I think they're like TFT, but donno.)
> - [ ] Cadco Twister Units (No Data)
> - [ ] MTS Units (No Data)


To hear all the ENDEC styles, Do this:
```python
from EASGen import EASGen
from pydub.playback import play
from pydub import AudioSegment

print("Normal / EASyCAP")
play(EASGen.genEAS("ZCZC-EAS-DMO-055079+0100-0391810-WACN    -", True, True, AudioSegment.empty(), "", 24000, False))
print("DAS")
play(EASGen.genEAS("ZCZC-EAS-DMO-055079+0100-0391810-WACN    -", True, True, AudioSegment.empty(), "", 48000, True))
print("TFT")
play(EASGen.genEAS("ZCZC-EAS-DMO-055079+0100-0391810-WACN    -", True, True, AudioSegment.empty(), "", 24000, True).set_frame_rate(8000))
print("NWS")
play(EASGen.genEAS("ZCZC-EAS-DMO-055079+0100-0391810-WACN    -", True, True, AudioSegment.empty(), "NWS", 24000, True).set_frame_rate(11025))
print("SAGE")
play(EASGen.genEAS("ZCZC-EAS-DMO-055079+0100-0391810-WACN    -", True, True, AudioSegment.empty(), "SAGE", 24000, True))
print("DIGITAL")
play(EASGen.genEAS("ZCZC-EAS-DMO-055079+0100-0391810-WACN    -", True, True, AudioSegment.empty(), "DIGITAL", 24000, True))
print("EASyPLUS/CAST/IPTV")
play(EASGen.genEAS("ZCZC-EAS-DMO-055079+0100-0391810-WACN    -", True, True, AudioSegment.empty(), "TRILITHIC", 24000, True))
```

To generate ATTN only alerts, such as NPAS or WEA:

For NPAS:
```python
from EASGen import EASGen
from pydub.playback import play
from pydub import AudioSegment

Alert = EASGen.genATTN(mode="NPAS") ## Generate an NPAS (AlertReady) Tone
play(Alert) ## Play the NPAS Tones
```

For WEA:
```python
from EASGen import EASGen
from pydub.playback import play
from pydub import AudioSegment

Alert = EASGen.genATTN(mode="WEA") ## Generate WEA Tones
play(Alert) ## Play the WEA Tones
```

## NEW FEATURE:
(Thanks to Dondaplayer)
Added a Bandpass Filter:

```python
from EASGen import EASGen
from pydub.playback import play
from pydub import AudioSegment

header = "ZCZC-CIV-DMO-033000+0100-0010000-WACNTECH-" ## EAS Header to send
Alert = EASGen.genEAS(header=header, attentionTone=True, mode="DIGITAL", endOfMessage=True, bandpass=True) # New BandPass feature, which improves the audio quality on some emulation modes.
play(Alert) ## Play the EAS Message
```

Hope you enjoy!
