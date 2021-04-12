import ffmpy
import os


def video_reduce(source, destination):

    input_name = source
    output_name = destination
    crf = 30
    out = {output_name:f'-vcodec libx264 -crf {crf}'}
    inp = {input_name:None}
    ff = ffmpy.FFmpeg(inputs=inp, outputs=out)
    if os.path.exists(destination):
        print("Video already present in destination, restarting compression")
        os.remove(destination)
    ff.run(stdout=None)
        
            
        
            

