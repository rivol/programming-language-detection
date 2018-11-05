import random
from pathlib import Path

import click
from PIL import Image, ImageDraw, ImageFont


IMAGE_SIZE = 299


def render_text(text: str, filename: Path, font: ImageFont):
    img = Image.new('RGB', (IMAGE_SIZE, IMAGE_SIZE), (0, 0, 0))

    d = ImageDraw.Draw(img)
    d.text((2, 2), text, font=font, fill=(255, 255, 255), spacing=1)

    img.save(filename, 'PNG')


def render_test(output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    font = ImageFont.truetype('RobotoMono-Regular.ttf', 8)

    text = '\n'.join([f"line number {i} ..." for i in range(50)])
    render_text(text, output_dir / 'test.png', font)


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.argument('count', type=click.INT)
@click.argument('output_dir', type=click.Path(file_okay=False, dir_okay=True))
def main(filename, count, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    print(filename, count, output_dir)

    font = ImageFont.truetype('RobotoMono-Regular.ttf', 8)
    # 256x256: 17 lines per image with 10-sized font and default spacing. 27 lines per 8-size font and spacing=1
    # 299x299: 32 lines per 8-size font and spacing=1
    lines_per_image = 32

    with open(filename, 'r') as f:
        input_lines = f.readlines()

    print(f"Rendering {count} images from {len(input_lines)} lines ", end='', flush=True)
    offsets = sorted([random.randint(0, len(input_lines) - lines_per_image) for _ in range(count)])
    for i in range(count):
        first_line_no = offsets[i]
        text = '\n'.join(input_lines[first_line_no : first_line_no + lines_per_image])

        render_text(text, output_dir / f'{i:03d}.png', font)

        print('.', end='', flush=True)

    print(' DONE')


if __name__ == '__main__':
    main()
