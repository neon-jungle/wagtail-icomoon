from wagtail.core import hooks
from pathlib import Path


@hooks.register('register_icons')
def add_icons(icons):
    svg_folder = Path(__file__).parent.joinpath('templates', 'icons')
    for svg_file in svg_folder.glob('*.svg'):
        icons.append(f'icons/{svg_file.name}')
    return icons
