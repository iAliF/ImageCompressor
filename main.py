from compressor import ImageCompressor


def main() -> None:
    src, dest = "src/", "dest/"
    quality = 90

    obj = ImageCompressor(src, dest, True, quality)
    result = obj.compress_images()

    print(f"{result.count} Image{'s' if result.count > 1 else ''} were compressed in {round(result.time, 2)}"
          f" second{'s' if result.time > 1 else ''}")


if __name__ == '__main__':
    main()
