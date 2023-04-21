import os
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass

from PIL import Image


class ImageCompressor:
    ROTATION = {
        1: 0,
        3: 180,
        6: 270,
        8: 90
    }

    def __init__(self, source_dir: str, dest_dir: str, optimize: bool, quality: int) -> None:
        self.source_dir = source_dir
        self.dest_dir = dest_dir
        self.optimize = optimize
        self.quality = quality

    def _compress_image(self, file_path: str) -> str:
        src_path = os.path.join(self.source_dir, file_path)
        dest_path = os.path.join(self.dest_dir, file_path)

        img = Image.open(src_path)

        width, height = img.size
        new = img.resize(
            (int(width / 2), int(height / 2)),
            Image.LANCZOS
        )
        new = new.rotate(
            self.ROTATION[img.getexif()[0x0112]],
            expand=True
        )

        new.save(dest_path, quality=self.quality, optimize=self.optimize)
        return dest_path

    def compress_images(self, workers_count: int = 4) -> 'CompressionResult':
        start = time.time()

        files = os.listdir(self.source_dir)
        with ThreadPoolExecutor(workers_count, "img_comp") as executor:
            for file in files:  # type: str
                executor.submit(self._compress_image, file)

        return CompressionResult(
            len(files),
            time.time() - start
        )


@dataclass
class CompressionResult:
    count: int
    time: float
