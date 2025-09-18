from PIL import Image, ImageChops
import numpy as np
import consts


def get_num_of_diff_pixel(diff):
    black_pixel_count = 0
    num_of_pixel =0
    pixel_list = np.asarray(diff).tolist()
    for pixel_row in range(len(pixel_list)):
        for pixel_col in range(len(pixel_list[pixel_row])):
            num_of_pixel += 1
            if pixel_list[pixel_row][pixel_col].count(0) == 3:
                black_pixel_count += 1

    return num_of_pixel - black_pixel_count


def compare_two_images(image_from_user, image_from_dict):
    img1 = Image.open(image_from_user)
    img2 = Image.open(image_from_dict)

    half_image_size = consts.IMAGE_SIZE // 2

    # crop image1
    width1, height1 = img1.size
    left1 = width1 // 2 - half_image_size
    top1 = height1 // 2 - half_image_size
    right1 = width1 // 2 + half_image_size
    bottom1 = height1 // 2 + half_image_size

    # crop image2
    width2, height2 = img2.size
    left2 = width2 // 2 - half_image_size
    top2 = height2 // 2 - half_image_size
    right2 = width2 // 2 + half_image_size
    bottom2 = height2 // 2 + half_image_size

    im1 = img1.crop((left1, top1, right1, bottom1))
    im2 = img2.crop((left2, top2, right2, bottom2))

    # find difference
    diff = ImageChops.difference(im1.convert('RGB'), im2.convert('RGB'))
    num_of_diff_pixel = get_num_of_diff_pixel(diff)//3
    return num_of_diff_pixel > consts.IMAGE_SIZE * consts.IMAGE_SIZE * 0.0001

