import sys
import os

# ドラッグ&ドロップしたファイルのパスを取得
for file_path in sys.argv[1:]:

    # ファイルの名前を取得
    file_name = os.path.basename(file_path)

    from pydub import AudioSegment

    # wavファイルを読み込む
    if ".wav" in file_path:
        sound = AudioSegment.from_wav(file_path)
        ogg_file = file_path.replace(".wav", ".ogg")

        sound.export(ogg_file, format="ogg")