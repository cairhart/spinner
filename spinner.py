import imageio as io
reader = io.get_reader()//todo
fps = reader.get_meta_data()['fps']

output_frames = io.get_writer('~/liliana_spinning.mp4',fps=fps)
for framenum, frame in enumerate(reader):

