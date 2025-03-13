# 🌩️ **EASGen**: A Fast Python EAS Generation Library

![EASGen](https://github.com/Newton-Communications/EG/blob/main/doc/img/RefactoredEASGen.png?raw=true)

EASGen is a powerful Python library for translating **EAS (Emergency Alert System)** ZCZC strings or other data into **SAME (Specific Area Messaging)** headers. It includes robust support for individual headers, attention tones, EOM generation, emulation modes, and WEA tone generation, ensuring a seamless experience for encoding emergency messages.

---

## 🛠️ **Features**
- ✅ **EAS Generation**: Converts raw ZCZC SAME strings into Individual headers, attention tones. Also allows generation of EOMs.
- ✅ **PyDub AudioSegment Output**: Provides easy integration through PyDub AudioSegments.
- ✅ **Audio File Input**: Allows for audio files to be input to allow for audio messages and other forms of audio injection.
- ✅ **Very Quick**: Generates headers quickly and efficiently, allowing for high performance usage.
- ✅ **Emulation Modes**: Mimic the sound of various EAS hardware/software systems.

---

## 🚀 **Installation**

### Linux (Debian-based)
```bash
sudo apt update
sudo apt install python3 python3-pip
python3 -m pip install EASGen-Remastered
```

### Windows
1. [Install Python](https://www.python.org/downloads/).
2. Open CMD and run:
   ```bash
   python -m pip install EASGen-Remastered
   ```

---

## 📖 **Basic Usage**

### Generate a simple SAME Required Weekly Test:
```python
from EASGen import EASGen
from pydub.playback import play

header = "ZCZC-EAS-RWT-005007+0015-0010000-EAR/FOLF-" ## EAS Header to send
Alert = EASGen.genEAS(header=header, attentionTone=False, endOfMessage=True) ## Generate an EAS SAME message with no ATTN signal, and with EOMs.
play(Alert) ## Play the EAS Message
```

<details>
<summary>Output</summary>

https://github.com/user-attachments/assets/bd1ca2d9-8cc3-4854-b148-f4f13e47b86b


</details>

---

## 🔍 **Advanced Usage**

### To Insert Audio into an alert:
```python
from EASGen import EASGen
from pydub.playback import play
from pydub import AudioSegment

header = "ZCZC-CIV-DMO-033000+0100-0010000-EAR/FOLF-" ## EAS Header to send
audio = AudioSegment.from_wav("NewHampshireDMO.wav") ## Alert Audio import
Alert = EASGen.genEAS(header=header, attentionTone=True, audio=audio, endOfMessage=True) ## Generate an EAS SAME message with an ATTN signal, the imported WAV file as the audio, and with EOMs.
play(Alert) ## Play the EAS Message
## The New Hampshire State Police has activated the New Hampshire Emergency Alert System in order to conduct a practice demo. This concludes this test of the New Hampshire Emergency Alert System.
```

<details>
<summary>Output</summary>
https://github.com/user-attachments/assets/78abb4a6-05e7-45cb-bd58-ba801adb5d72
</details>

---

## Spamming New Hampshire Demos have never been easier!

### For a custom SampleRate:
```python
from EASGen import EASGen
from pydub.playback import play
from pydub import AudioSegment

header = "ZCZC-EAS-DMO-055079+0100-0010000-EAR/FOLF-" ## EAS Header to send
Alert = EASGen.genEAS(header=header, attentionTone=True, endOfMessage=True, sampleRate=48000) ## Generate an EAS SAME message with an ATTN signal, the imported WAV file as the audio, with EOMs, at a samplerate of 48KHz.
play(Alert) ## Play the EAS Message
```

<details>
<summary>Output</summary>
https://github.com/user-attachments/assets/2487366b-02ee-4024-8f96-ecd1dcbb20b3
</details>

---

### To export an alert instead of playing it back:
```python
from EASGen import EASGen
from pydub import AudioSegment

header = "ZCZC-EAS-RWT-055079+0100-0010000-EAR/FOLF-" ## EAS Header to send
Alert = EASGen.genEAS(header=header, attentionTone=True, endOfMessage=True, sampleRate=48000) ## Generate an EAS SAME message with an ATTN signal, the imported WAV file as the audio, and with EOMs.
EASGen.export_wav("Alert.wav", Alert)
```

<details>
<summary>Output</summary>
https://github.com/user-attachments/assets/96522968-63b1-4b20-8a95-4ea075780575
</details>

---

### To resample an alert after generation (If sampleRate is making the audio weird):
```python
from EASGen import EASGen
from pydub.playback import play
from pydub import AudioSegment

header = "ZCZC-EAS-DMO-055079+0100-0010000-EAR/FOLF-" ## EAS Header to send
Alert = EASGen.genEAS(header=header, attentionTone=True, endOfMessage=True) ## Generate an EAS SAME message with an ATTN signal, the imported WAV file as the audio, and with EOMs.
Alert = Alert.set_frame_rate(8000) ## Resample the alert to 8KHz for no reason lol.
play(Alert) ## Play the EAS Message
```

<details>
<summary>Output</summary>
https://github.com/user-attachments/assets/804300e5-1260-40d0-a0e8-7f77ff1c4396
</details>

---

### To simulate an ENDEC type:
```python
from EASGen import EASGen
from pydub.playback import play
from pydub import AudioSegment

header = "ZCZC-CIV-DMO-033000+0100-0010000-EAR/FOLF-" ## EAS Header to send
audio = AudioSegment.from_wav("NewHampshireDMO.wav") ## Alert Audio import
Alert = EASGen.genEAS(header=header, attentionTone=True, audio=audio, mode="DIGITAL", endOfMessage=True) ## Generate an EAS SAME message with an ATTN signal, the imported WAV file as the audio, with EOMs, and with a SAGE DIGITAL ENDEC style.
play(Alert) ## Play the EAS Message
## The New Hampshire State Police has activated the New Hampshire Emergency Alert System in order to conduct a practice demo. This concludes this test of the New Hampshire Emergency Alert System.
```

<details>
<summary>Output</summary>
https://github.com/user-attachments/assets/97adb234-0da6-4cc9-b9fa-69f4ed7edaf3
</details>

---

### Now you can make all the Mocks you want!

## Supported ENDECS:
> - [x] None
> - [x] TFT (Resample to 8KHZ using ".set_frame_rate(8000)" on the generated alert)
> - [x] EASyCAP (Basically the same as None)
> - [x] DASDEC (Crank up the Samplerate to 48000 for this one)
> - [x] SAGE EAS ENDEC (Mode = "SAGE")
> - [x] SAGE DIGITAL ENDEC (Mode = "DIGITAL")
> - [x] Trilithic EASyPLUS/CAST/IPTV (Mode = "TRILITHIC")
> - [x] NWS (Mode = "NWS", Resample to 11KHZ using ".set_frame_rate(11025)" on the generated alert)

## Unsupported ENDECS:
> - [ ] HollyAnne Units (Can't sample down to 5KHz... This is a good thing.)
> - [ ] Gorman-Reidlich Units (Don't listen to them enough to simulate. I think they're like TFT, but donno.)
> - [ ] Cadco Twister Units (No Data)
> - [ ] MTS Units (No Data)

---

### To hear all the ENDEC styles, do this:
```python
from EASGen import EASGen
from pydub.playback import play
from pydub import AudioSegment

print("Normal / EASyCAP")
play(EASGen.genEAS("ZCZC-EAS-DMO-055079+0100-0391810-EAR/FOLF-", True, True, AudioSegment.empty(), "", 24000, False))
print("DAS")
play(EASGen.genEAS("ZCZC-EAS-DMO-055079+0100-0391810-EAR/FOLF-", True, True, AudioSegment.empty(), "", 48000, True))
print("TFT")
play(EASGen.genEAS("ZCZC-EAS-DMO-055079+0100-0391810-EAR/FOLF-", True, True, AudioSegment.empty(), "", 24000, True).set_frame_rate(8000))
print("NWS")
play(EASGen.genEAS("ZCZC-EAS-DMO-055079+0100-0391810-EAR/FOLF-", True, True, AudioSegment.empty(), "NWS", 24000, True).set_frame_rate(11025))
print("SAGE")
play(EASGen.genEAS("ZCZC-EAS-DMO-055079+0100-0391810-EAR/FOLF-", True, True, AudioSegment.empty(), "SAGE", 24000, True))
print("DIGITAL")
play(EASGen.genEAS("ZCZC-EAS-DMO-055079+0100-0391810-EAR/FOLF-", True, True, AudioSegment.empty(), "DIGITAL", 24000, True))
print("EASyPLUS/CAST/IPTV")
play(EASGen.genEAS("ZCZC-EAS-DMO-055079+0100-0391810-EAR/FOLF-", True, True, AudioSegment.empty(), "TRILITHIC", 24000, True))
```

<details>
<summary>Output</summary>
https://github.com/user-attachments/assets/abf9790b-8bc9-4919-9cc6-6145fc309fdb
https://github.com/user-attachments/assets/429d0ced-467e-460f-baa7-2f1d868ae987
https://github.com/user-attachments/assets/c0a9c4ee-d235-4089-9e4e-ce41d92d786e
https://github.com/user-attachments/assets/5918daa8-fc1d-488a-953a-5be0a97e7325
https://github.com/user-attachments/assets/e1f7b4eb-c0f6-4ff4-8ac7-bfcce7099e34
https://github.com/user-attachments/assets/d63eb3d7-43ea-4ab0-86e2-758983004b7d
https://github.com/user-attachments/assets/e08cf34e-3bfc-46ab-aa8a-51ead8bf17a7
</details>

---

## To generate ATTN only alerts, such as NPAS or WEA:

### For NPAS:
```python
from EASGen import EASGen
from pydub.playback import play
from pydub import AudioSegment

Alert = EASGen.genATTN(mode="NPAS") ## Generate an NPAS (AlertReady) Tone
play(Alert) ## Play the NPAS Tones
```

<details>
<summary>Output</summary>
https://github.com/user-attachments/assets/efefb8d8-d54a-40d2-8bdb-e05788c3203d
</details>

---

### For WEA:
```python
from EASGen import EASGen
from pydub.playback import play
from pydub import AudioSegment

Alert = EASGen.genATTN(mode="WEA") ## Generate WEA Tones
play(Alert) ## Play the WEA Tones
```

<details>
<summary>Output</summary>
https://github.com/user-attachments/assets/14fe326c-5f89-4fe3-b25a-8bc7ed12b320
</details>

---

### To use the Bandpass Filter functionality:
```python
from EASGen import EASGen
from pydub.playback import play
from pydub import AudioSegment

header = "ZCZC-CIV-DMO-033000+0100-0010000-EAR/FOLF-" ## EAS Header to send
Alert = EASGen.genEAS(header=header, attentionTone=True, mode="DIGITAL", endOfMessage=True, bandpass=True) # New BandPass feature, which improves the audio quality on some emulation modes.
play(Alert) ## Play the EAS Message
```

<details>
<summary>Output</summary>
https://github.com/user-attachments/assets/b56b42a8-309f-451a-937d-bcdf6913c73f
</details>

---

## ⚠️ **Reporting Issues**

- Bugs and other issues can be reported on [Discord](https://discord.com/users/637078631943897103) or in the GitHub Issues tab.
- Include **entire ZCZC SAME strings** and any Audio Files injected and details for accurate and quick fixes.

---

## 📜 **License**

**MIT License**

---

## 👤 **Contact**

- **Developer**: SecludedHusky Systems/Newton Communications
- **Discord**: [Contact Here](https://discord.com/users/637078631943897103)

---

### ❤️ **Thank You for Using My Version of EASGen!**  
Powered by [SecludedHusky Systems](https://services.secludedhusky.com). Get affordable internet radio services and VPS hosting today.
