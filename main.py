from argparse import ArgumentParser

from lib import ImageCompressor


def main() -> None:
    parser = ArgumentParser(
        "Image Compressor",
        "Simple script to compress your images"
    )
    parser.add_argument("-s", "--source", type=str, required=True, help="Source directory")
    parser.add_argument("-d", "--destination", type=str, required=True, help="Destination directory")
    parser.add_argument("-o", "--optimize", type=bool, help="Optimize images", default=True)
    parser.add_argument("-q", "--quality", type=int, help="Images quality", default=90)
    parser.add_argument("-w", "--workers", type=int, help="Max workers count", default=4)
    args = parser.parse_args()

    comp = ImageCompressor(args.source, args.destination, args.optimize, args.quality)
    result = comp.compress_images(args.workers)

    print(f"{result.count} Image{'s' if result.count > 1 else ''} were compressed in {round(result.time, 2)}"
          f" second{'s' if result.time > 1 else ''}")


if __name__ == '__main__':
    main()
