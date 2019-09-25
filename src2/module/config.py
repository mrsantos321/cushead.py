#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
import textwrap

from src2.info import get_info
from src2.services.images import ImageService


IMAGEFILES = [
    'favicon_ico_16px.ico',
    'favicon_png_1600px.png',
    'favicon_svg_scalable.svg',
    'preview_png_500px.png',
]


class DefaultSettings:
    """Generate presets"""

    def __init__(self):
        self.info = get_info()

    def default_images(self):
        """Generate images files to attach to the preset settings"""
        binary_files = []
        realpath = path.join(path.dirname(path.realpath(__file__)), '../assets')
        for filename in IMAGEFILES:
            filepath = path.join(realpath, filename)
            with open(filepath, 'rb') as binary_file:
                binary_files.append(
                    {
                        'filename': filename,
                        'content': binary_file.read(),
                    }
                )
        return binary_files

    def default_settings(self):
        """Generate config file in indented JSON format"""
        settings = textwrap.dedent(f"""\
            {{
                'comment':  {{
                    'About':            '{('Config file used by python '
                                           'cushead CLI')}',
                    'Format':           'JSON',
                    'Git':              '{self.info['source']}',
                    'Documentation':    '{self.info['documentation']}'
                }},
                'required': {{
                    'static_url':       '/static/'
                }},
                'recommended': {{
                    'favicon_ico':      './favicon_ico_16px.ico',
                    'favicon_png':      './favicon_png_1600px.png',
                    'favicon_svg':      './favicon_svg_scalable.svg',
                    'preview_png':      './preview_png_500px.png'
                }},
                'default': {{
                    'general': {{
                        'content-type':     'text/html; charset=utf-8',
                        'X-UA-Compatible':  'ie=edge',
                        'viewport':         '{('width=device-width, '
                                               'initial-scale=1')}',
                        'language':         'en',
                        'territory':        'US',
                        'clean_url':        'microsoft.com',
                        'protocol':         'https://',
                        'robots':           'index, follow'
                    }},
                    'basic': {{
                        'title':            'Microsoft',
                        'description':      'Technology Solutions',
                        'subject':          'Home Page',
                        'keywords':         'Microsoft, Windows',
                        'background_color': '#0000FF',
                        'author':           'Lucas Vazquez'
                    }},
                    'social_media': {{
                        'facebook_app_id':  '123456',
                        'twitter_user_@':   '@Microsoft',
                        'twitter_user_id':  '123456'
                    }}
                }},
                'progressive_web_apps': {{
                    'dir':              'ltr',
                    'start_url':        '/',
                    'orientation':      'landscape',
                    'scope':            '/',
                    'display':          'browser',
                    'platform':        'web',
                    'applications':     [
                        {{
                            'platform':     'play',
                            'url':          '{('https://play.google.com/store/'
                                               'apps/details?id=com.example'
                                               '.app')}',
                            'id':           'com.example.app'
                        }},
                        {{
                            'platform':     'itunes',
                            'url':          '{('https://itunes.apple.com/app/'
                                            'example-app/id123456')}'
                        }}
                    ]
                }}
            }}""")
        settings = settings.replace('\'', '"')
        return settings


class DefaultIconsConfig():
    config: dict

    def _png_icons_config(self):
        yandex_content = (f"logo={self.config.get('static_url', '')}"
                           "/yandex.png, "
                          f"color={self.config.get('background_color', '')}")
        return [
            # default png favicons
            {
                'name_ref': 'icon',
                'file_name': 'favicon',
                # https://www.favicon-generator.org/
                # https://stackoverflow.com/questions/4014823/does-a-favicon-have-to-be-32x32-or-16x16
                # https://www.emergeinteractive.com/insights/detail/the-essentials-of-favicons/
                'square_sizes': [16, 24, 32, 48, 57, 60, 64, 70, 72, 76, 96,
                                114, 120, 128, 144, 150, 152, 167, 180, 192,
                                195, 196, 228, 310],
                'type': 'image/png',
                'verbosity': True,
            },
            # windows favicon
            {
                'name_ref': 'msapplication-TileImage',
                'file_name': 'ms-icon',
                'square_sizes': [144],
                'metatag': True,
            },
            # apple touch default
            {
                'name_ref': 'apple-touch-icon',
                'file_name': 'apple-touch-icon',
                'square_sizes': [57],
            },
            # apple touch with differents sizes
            {
                'name_ref': 'apple-touch-icon',
                'file_name': 'apple-touch-icon',
                'square_sizes': [57, 60, 72, 76, 114, 120, 144, 152, 167, 180,
                                1024],
                'verbosity': True,
            },
            # apple touch startup image default
            {
                'name_ref': 'apple-touch-startup-image',
                'file_name': 'launch',
                'square_sizes': [768],
            },
            # apple touch startup image with differents sizes
            {
                'name_ref': 'apple-touch-startup-image',
                'file_name': 'launch',
                # Based on:
                # https://css-tricks.com/snippets/css/media-queries-for-standard-devices/
                'max_min': [
                    [38, 42],
                    [320, 375],
                    [375, 414],
                    [414, 480],
                    [480, 568],
                    [568, 667],
                    [667, 736],
                    [736, 812],
                    [812, 834],
                    [1024, 1112],
                    [1112, 1200],
                    [1200, 1366],
                    [1366, 1600],
                ],
            },
            # Mac fluid icon
            {
                'name_ref': 'fluid-icon',
                'file_name': 'fluidicon',
                'square_sizes': [512],
                'title': self.config.get('title', ''),
            },
            # yandex browser
            {
                'name_ref': 'yandex-tableau-widget',
                'file_name': 'yandex',
                'square_sizes': [120],
                'metatag': True,
                'content': yandex_content,
            },
        ]

    def _browserconfig_icons_config(self):
        return {
            'name_ref': 'browserconfig',
            'file_name': 'ms-icon',
            'square_sizes': [30, 44, 70, 150, 310],
            'non_square_sizes': [[310, 150]],
        }
    def _manifest_icons_config(self):
        return {
            'name_ref': 'manifest',
            'filename': 'android-icon',
            'square_sizes': [36, 48, 72, 96, 144, 192, 256, 384, 512],
            'file_type': 'image/png',
            'verbosity': True,
        }
    def _opensearch_icons_config(self):
        return {
            'name_ref': 'opensearch',
            'filename': 'opensearch',
            'sqyare_sizes': [16],
            'verbosity': True,
        }

    def default_icons_config(self):
        return {
            'favicon_png': self._png_icons_config(),
            'browserconfig': self._browserconfig_icons_config(),
            'manifest': self._manifest_icons_config(),
            'opensearch': self._opensearch_icons_config(),
        }

class ImagesCreationConfig(ImageService):
    config: dict
    icons_config: dict

    def _favicon_ico(self):
        favicon_ico = self.config.get('favicon_ico', '')
        if not favicon_ico: return []
        return [{
            'destination_file_path': path.join(
                self.config.get('output_folder_path'),
                'favicon.ico'
            ),
            'source_file_path': path.join(
                self.config.get('main_folder_path', ''),
                favicon_ico
            ),
        }]

    def _favicon_png(self):
        images_format = []
        favicon_png = self.config.get('favicon_png', '')
        if not favicon_png: return images_format
        source_file_path = path.join(self.config.get('main_folder_path', ''),
                                     favicon_png)
        for brand_icon_config in self.icons_config.get('favicon_png', []):
            file_name = brand_icon_config.get('file_name', '')
            for size in self.format_sizes(brand_icon_config):
                destination_file_path = path.join(
                    self.config.get('static_folder_path', ''),
                    f"{file_name}-{size[0]}x{size[1]}.png")
                images_format.append({
                    'destination_file_path': destination_file_path,
                    'resize': True,
                    'size': size,
                    'source_file_path': source_file_path,
                })
        return images_format

    def _favicon_svg(self):
        favicon_svg = self.config.get('favicon_svg', '')
        if not favicon_svg: return []
        return [{
            'destination_file_path': path.join(
                self.config.get('static_folder_path'),
                'favicon.svg'
            ),
            'source_file_path': path.join(
                self.config.get('main_folder_path', ''),
                favicon_svg
            ),
        }]

    def _preview_png(self):
        preview_png = self.config.get('preview_png', '')
        if not preview_png: return []
        return [{
            'destination_file_path': path.join(
                self.config.get('static_folder_path'),
                'preview-500x500.png'
            ),
            'resize': True,
            'size': [500, 500],
            'source_file_path': path.join(
                self.config.get('main_folder_path', ''),
                preview_png
            )
        }]

    def default_images_creation_config(self):
        images_creation_config = [
            self._favicon_ico(),
            self._favicon_png(),
            self._favicon_svg(),
            self._preview_png(),
        ]
        return [
            element for group in images_creation_config
            for element in group
        ]
