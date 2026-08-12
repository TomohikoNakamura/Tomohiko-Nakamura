from pathlib import Path
import shutil

# data_root_dir = Path("C:\\Users\\nakamura\\Documents\\workspace\\webs\\myhp_mkdocs\\tmp\\主観評価実験\\主観評価実験４")
# dst_root_dir = Path("audio")

# def copy(song_id, out_song_id):
#     for sr in [8,20,32,40,48]:
#         dst_dir = dst_root_dir / f'song{out_song_id:d}' / f'{sr:d}k'
#         # print(dst_dir.exists())
#         # if not dst_dir.exists():
#         #     dst_dir.mkdir(parents=True, exist_ok=True)
#         src_dir = data_root_dir / f'data_{sr:d}k' / f'song{song_id:d}'
#         print(src_dir, dst_dir)
#         shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)

# copy(0,1)
# copy(4,0)


data_root_dir = Path("C:\\Users\\nakamura\\Documents\\workspace\\webs\\myhp_mkdocs\\tmp\\主観評価実験\\主観評価実験3")
dst_root_dir = Path("audio2")

def copy(song_id, out_song_id):
    for sr in [8,12,16,20,24]:
        dst_dir = dst_root_dir / f'song{out_song_id:d}' / f'{sr:d}k'
        src_dir = data_root_dir / f'data_{sr:d}k' / f'song{song_id:d}'
        print(src_dir, dst_dir)
        shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)

copy(0,1)
copy(4,0)