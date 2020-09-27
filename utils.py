import os
import cv2
def video_path(root, basename, extension):
    return os.path.join(root, f'{basename}{extension}')

def video_basename(filename):
    return os.path.basename(os.path.splitext(filename)[0])

def is_video(filename):
    return any(filename.endswith(ext) for ext in ['.mp4','.avi','.wmv','.MP4','.AVI','.WMV'])

def image_path(root, basename, extension):
    return os.path.join(root, f'{basename}{extension}')

def image_basename(filename):
    return os.path.basename(os.path.splitext(filename)[0])

def is_image(filename):
    return any(filename.endswith(ext) for ext in ['.jpg','.png','.jpeg','.JPG','.PNG','.JPEG'])


def makedir(path):
    if os.path.exists(os.path.join(path)) == False:
        os.mkdir(path)
        print('make :',path)
    else :
        print('{} already exists.'.format(path))

def draw_motion_vector(frame, motion_field):
    height, width = frame.shape
    frame_dummy = frame.copy()
    mv_h , mv_w,_ = motion_field.shape
    b_size = int(height/mv_h)

    for y in range(0, mv_h ):
        for x in range(0, mv_w ):
            idx_x = x * b_size
            idx_y = y * b_size
            mv_x, mv_y = motion_field[y][x]

            cv2.arrowedLine(frame_dummy, (idx_x, idx_y), (int(idx_x + mv_x), int(idx_y + mv_y)), (0, 255, 0), 1)
    return frame_dummy

