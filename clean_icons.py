#!/usr/bin/env python
from pathlib import Path
from bs4 import BeautifulSoup


if __name__ == "__main__":
    # Convenience script for removing bad attributes and making the icons wagtail-able
    icons_dir = Path(__file__).parent.joinpath('wagtail_icomoon', 'templates', 'icons')
    for icon_file in icons_dir.glob('*.svg'):
        markup = BeautifulSoup(icon_file.read_text(), 'html.parser')
        for attr in ['xmlns', 'width', 'height']:
            for element in markup.find_all(attrs={attr: True}):
                del element[attr]
        markup.find('svg').attrs['id'] = f'icon-im-{icon_file.stem}'
        icon_file.write_text(markup.prettify())
        print(f'Cleaned {icon_file}')
