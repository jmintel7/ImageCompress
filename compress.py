import ffmpy
import os

input = "VID_20200503_111104.mp4"
t1 = time.time()
os.path.exists(input)
input_name = os.path.join(os.getcwd(), input)
output_name = os.path.join(os.getcwd(),'compressed_30_'+input)

crf = 30
out = {output_name:f'-vcodec libx264 -crf {crf}'}
inp = {input_name:None}
ff = ffmpy.FFmpeg(inputs=inp, outputs=out)
print(ff.cmd)
ff.run()
t2 = time.time()
print(f"done in {t2 - t1} seconds")