import cv2

from preprocess import perform_preprocessing


def ocr_operation(img_url):

    raw_image = cv2.imread(img_url, 0)
    
    # pre process the raw image for noise removal and
    # smoothing and binarization

    image_for_det, image_for_ext = perform_preprocessing(raw_image)

    # to write the output into a file
    fp = open("output.txt", 'w')
    fp.truncate()

    print "\n"
    fp.write("\n")

    fp.close()
