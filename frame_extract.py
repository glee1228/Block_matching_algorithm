import cv2

vidcap = cv2.VideoCapture('data/video/mozart.mp4')
count = 0
get_count = [i for i in range(1200,1300,2)]
pics_len = len(get_count)
write_len = 0
while (vidcap.isOpened() and write_len < pics_len):
    ret, image = vidcap.read()
    if count in get_count:
        width = image.shape[1]
        height = image.shape[0]

        image = cv2.resize(image, dsize=(int(width * 0.5), int(height * 0.5)), interpolation=cv2.INTER_LINEAR)
        cv2.imwrite("data/frame/frame%04d.jpg" % count, image)
        print('Saved frame%04d.jpg' % count)
        write_len +=1

    count += 1


vidcap.release()
