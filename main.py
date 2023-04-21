import os
import time
from concurrent.futures import ThreadPoolExecutor

from PIL import Image

ROTATION = {
    1: 0,
    3: 180,
    6: 270,
    8: 90
}


def compress_image(src_dir: str, dest_dir: str, file_path: str, quality: int) -> str:
    src_path = os.path.join(src_dir, file_path)
    dest_path = os.path.join(dest_dir, file_path)

    img = Image.open(src_path)

    width, height = img.size
    new = img.resize(
        (int(width / 2), int(height / 2)),
        Image.LANCZOS
    )
    new = new.rotate(
        ROTATION[img.getexif()[0x0112]],
        expand=True
    )

    new.save(dest_path, quality=quality, optimize=True)
    return dest_path


def main() -> None:
    start = time.time()

    src, dest = "src/", "dest/"
    quality = 90

    with ThreadPoolExecutor(4, "img_comp") as executor:
        for file in os.listdir(src):  # type: str
            executor.submit(compress_image, src, dest, file, quality)

    print(f"Images were compressed in {round(time.time() - start, 2)} seconds")


if __name__ == '__main__':
    main()
