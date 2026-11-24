"""Export the project's finite CSV TMX maps with embedded tilesets for Phaser 2."""
import json
import os
from pathlib import Path
import xml.etree.ElementTree as ET


def attributes(node):
    result = dict(node.attrib)
    integers = ('id', 'gid', 'width', 'height', 'tilewidth', 'tileheight',
                'tilecount', 'columns', 'margin', 'spacing', 'firstgid',
                'nextobjectid', 'nextlayerid')
    for key in integers:
        if key in result:
            result[key] = int(result[key])
    for key in ('x', 'y', 'rotation', 'opacity', 'offsetx', 'offsety'):
        if key in result:
            result[key] = float(result[key])
    if 'visible' in result:
        result['visible'] = result['visible'] != '0'
    return result


def export(path):
    source = ET.parse(path).getroot()
    result = attributes(source)
    result.update(version=1, properties={}, layers=[], tilesets=[])
    for node in source:
        if node.tag == 'editorsettings':
            continue
        if node.tag == 'tileset':
            tileset_path = path.parent / node.get('source', '')
            tileset = ET.parse(tileset_path).getroot() if node.get('source') else node
            entry = attributes(tileset)
            entry.pop('version', None)
            entry.pop('tiledversion', None)
            entry.update(firstgid=int(node.get('firstgid')), margin=int(tileset.get('margin', 0)),
                         spacing=int(tileset.get('spacing', 0)), properties={})
            image = tileset.find('image')
            image_path = (tileset_path.parent if node.get('source') else path.parent) / image.get('source')
            if not image_path.is_file():
                raise ValueError(f'Missing image: {image_path}')
            entry.update(image=os.path.relpath(image_path, path.parent).replace('\\', '/'),
                         imagewidth=int(image.get('width')), imageheight=int(image.get('height')))
            result['tilesets'].append(entry)
        elif node.tag in ('layer', 'objectgroup'):
            entry = dict(opacity=1, visible=True, x=0, y=0, **{})
            entry.update(attributes(node))
            if node.tag == 'layer':
                data = node.find('data')
                if data.get('encoding') != 'csv' or data.find('chunk') is not None:
                    raise ValueError('Expected finite CSV tile layers')
                values = [int(value) for value in data.text.strip().split(',') if value.strip()]
                if len(values) != entry['width'] * entry['height']:
                    raise ValueError(f'Invalid tile count in {entry["name"]}')
                entry.update(type='tilelayer', data=values)
            else:
                objects = []
                for obj in node.findall('object'):
                    item = dict(name='', type='', rotation=0, visible=True, properties={})
                    item.update(attributes(obj))
                    objects.append(item)
                entry.update(type='objectgroup', draworder=node.get('draworder', 'topdown'), objects=objects)
            result['layers'].append(entry)
        else:
            raise ValueError(f'Unsupported map element: {node.tag}')
    path.with_suffix('.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(path.name, 'exported:', len(result['layers']), 'layers,', len(result['tilesets']), 'tilesets')


if __name__ == '__main__':
    maps = Path(__file__).resolve().parent / 'assets/tilemaps/maps'
    for name in ('level', 'finale'):
        export(maps / (name + '.tmx'))
