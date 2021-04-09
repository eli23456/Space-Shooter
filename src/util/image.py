from os import path
import pygame


class Image:
    util_dir = path.join(path.dirname(__file__))
    src_dir = path.dirname(util_dir)
    assets_dir = path.join(src_dir, "assets")
    img_dir = path.join(assets_dir, "images")

    def __init__(self):
        pass

    @staticmethod
    def load(filename_str):
        img = pygame.image.load(path.join(Image.img_dir, filename_str))
        return img

    @staticmethod
    def transform(surface, width, height):
        img = pygame.transform.scale(surface, (width, height))
        return img