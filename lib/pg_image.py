import pygame
from pygame import *


def pg_rescale_image_factor_bg(image, image_bg_ini, image_bg_end):
    factor_x = image_bg_end.get_rect().size[0] / image_bg_ini.get_rect().size[0]
    factor_y = image_bg_end.get_rect().size[1] / image_bg_ini.get_rect().size[0]
    image_w = int(round(factor_x * image.get_rect().size[0]))
    image_h = int(round(factor_y * image.get_rect().size[1]))
    image_transformed = pygame.transform.scale(image, (image_w, image_h))
    return image_transformed


def pg_rescale_image_full_screen(screen_config, image, perc=1.0):
    w_max = int(round(screen_config.w * perc))
    h_max = int(round(screen_config.h * perc))
    image_w = image.get_rect().size[0]
    image_h = image.get_rect().size[1]
    image_aspect_ratio = image_w / image_h
    if image_aspect_ratio * h_max < w_max:
        image_w = int(round(image_aspect_ratio * h_max))
        image_h = h_max
        x_offset = int((w_max - image_w)/2)
        y_offset = int((h_max - image_h)/2)
    else:
        image_w = w_max
        image_h = int(round(w_max / image_aspect_ratio))
        x_offset = int((w_max - image_w)/2)
        y_offset = int((h_max - image_h)/2)
    image_transformed = pygame.transform.scale(image, (image_w, image_h))
    return (image_transformed, x_offset, y_offset)


def pg_blit_image_full_screen(screen, screen_config, image, perc=1.0):
    w_max = int(round(screen_config.w * perc))
    h_max = int(round(screen_config.h * perc))
    image_w = image.get_rect().size[0]
    image_h = image.get_rect().size[1]
    image_aspect_ratio = image_w / image_h
    if image_aspect_ratio * h_max < w_max:
        image_w = int(round(image_aspect_ratio * h_max))
        image_h = h_max
        x_offset = int((w_max - image_w)/2)
        y_offset = int((h_max - image_h)/2)
    else:
        image_w = w_max
        image_h = int(round(w_max / image_aspect_ratio))
        x_offset = int((w_max - image_w)/2)
        y_offset = int((h_max - image_h)/2)
    image_transformed = pygame.transform.scale(image, (image_w, image_h))
    screen.blit(image_transformed, (screen_config.x_offset+x_offset, screen_config.y_offset+y_offset))


def rescale_image_height_perc(image_file, height, perc=1.0, margin=0.0):
    temp = pygame.image.load(image_file)
    x = temp.get_rect().size[0]
    y = temp.get_rect().size[1]
    factor = (1.0-margin) * ((height*perc) / y)
    temp = pygame.transform.scale(temp, (int(round(factor * x)), int(round(factor * y))))
    return temp


def rescale_image_width_perc(image_file, width, perc=1.0, margin=0.0):
    temp = pygame.image.load(image_file)
    x = temp.get_rect().size[0]
    y = temp.get_rect().size[1]
    factor = (1.0-margin) * ((width*perc) / x)
    temp = pygame.transform.scale(temp, (int(round(factor * x)), int(round(factor * y))))
    return temp


def rescale_image_height_pixels(image_file, height, margin=0.0):
    temp = pygame.image.load(image_file)
    x = temp.get_rect().size[0]
    y = temp.get_rect().size[1]
    factor = (1.0-margin) * (height / y)
    temp = pygame.transform.scale(temp, (int(round(factor * x)), int(round(factor * y))))
    return temp


def rescale_image_width_pixels(image_file, width, margin=0.0):
    temp = pygame.image.load(image_file)
    x = temp.get_rect().size[0]
    y = temp.get_rect().size[1]
    factor = (1.0-margin) * (width / x)
    temp = pygame.transform.scale(temp, (int(round(factor * x)), int(round(factor * y))))
    return temp


def rescale_image_height(image_file, height, diff=0.0):
    return rescale_image_height_pixels(image_file, height, diff)


def rescale_image_width(image_file, width, diff=0.0):
    return rescale_image_width_pixels(image_file, width, diff)

