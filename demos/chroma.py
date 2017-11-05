from vidpy import Clip, Composition

video = 'videos/hand1.mp4'

clips = []

for i in range(0, 6):
    clip = Clip(video)

    # attempt to automatically remove background color
    # (use color='#00ff00' to remove green, for example
    clip.chroma(amount=0.2)

    # start the clips 1/2 second after last clip
    clip.set_offset(i * 0.5)

    # change the clips x coordinate
    clip.position(x=(i*100)-300)

    # loop the clip 3 times
    clip.repeat(3)

    clips.append(clip)


comp = Composition(clips, bgcolor='#ff4dff')
# comp.preview()
comp.save('chroma_overlay.mp4')
