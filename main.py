import random
import threading
import time

files = ["photo.jpg", "document.pdf", "video.mp4", "archive.zip", "music.mp3"]


def download_file(file_name):
    print(f"Початок завантаження {file_name}...")
    time.sleep(random.uniform(1, 3))
    print(f"Завершено: {file_name}")


def main():
    # Це імітація завантаження: мережеві запити не виконуються.
    print("Послідовно:")
    start = time.perf_counter()
    for file_name in files:
        download_file(file_name)
    sequential_time = time.perf_counter() - start

    print("\nПаралельно:")
    threads = [threading.Thread(target=download_file, args=(name,)) for name in files]
    start = time.perf_counter()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    parallel_time = time.perf_counter() - start

    print(f"Послідовно: {sequential_time:.2f} с")
    print(f"Паралельно: {parallel_time:.2f} с")
    print(f"Різниця: {sequential_time - parallel_time:.2f} с")
    print("Затримки випадкові, тому результати різняться між запусками.")


if __name__ == "__main__":
    main()
