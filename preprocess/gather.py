from pathlib import Path

import click


@click.command()
@click.argument('output_filename', type=click.Path())
@click.argument('suffix')
@click.argument('inputs', type=click.Path(exists=True), nargs=-1)
def main(output_filename, suffix, inputs):
    input_files = []
    for input in inputs:
        p = Path('.') / input
        print(p, p.exists(), p.is_dir())
        if p.is_dir():
            input_files.extend(p.glob('**/*' + suffix))
        elif p.exists():
            input_files.append(p)

    print(f"Processing {len(input_files)} files...")
    with open(output_filename, 'w') as outf:
        for filename in input_files:
            try:
                with open(filename, 'r') as inf:
                    outf.write(inf.read())
            except Exception as e:
                # Skip files with weird encodings or other problems
                print(f"ERROR reading {filename}: {e}")


if __name__ == '__main__':
    main()
