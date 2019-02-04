from sys import argv, stderr
import moviepy.editor as ed

if len(argv) < 7:
    print('Use com:')
    print('\"python3 cut.py [filename] [start_minute] [start_second] [end_minute] [end_second] [out_file_prefix]\"', file=stderr)
    exit(1)

_, f, start_minute, start_second, end_minute, end_second, out_file_prefix,  *_ = argv
v = ed.VideoFileClip(f, audio=False)

sub = v.subclip(60*int(start_minute) + int(start_second), 60*int(end_minute) + int(end_second))
sub.write_videofile(out_file_prefix + 'Big.mp4', audio=False)

sub = sub.resize(height=360)
sub.write_videofile(out_file_prefix + '.mp4', audio=False, fps=30)
# sub.write_gif(out_file_prefix + '.gif', fps=30)
