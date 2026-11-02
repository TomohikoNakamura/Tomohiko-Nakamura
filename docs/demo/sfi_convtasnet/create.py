TEMPLATE1="""<tr>
    <td class="font-weight-normal" style="vertical-align: middle;" rowspan="4">
        Song {song_id:d}<br>
        {mixtures}
    </td><td style="vertical-align: middle;">{inst}</td>
    <td>
        {gt}
    </td>
    <td>
        {methodA}
    </td>
    <td>
        {methodB}
    </td>
</tr>"""

TEMPLATE2="""<tr>
    <td style="vertical-align: middle;">{inst}</td>
    <td>
        {gt}
    </td>
    <td>
        {methodA}
    </td>
    <td>
        {methodB}
    </td>
</tr>"""

MIXTURE_TEMPLATE="""{sr:d} kHz<audio controls preload="metadata" src="{audio_dir}/song{song_id:d}/{sr:d}k/mix.wav"></audio><br>"""

SEPARATED_TEMPLATE="""{sr:d} kHz<audio controls preload="metadata" src="{audio_dir}/song{song_id:d}/{sr:d}k/{method}_{inst}.wav"></audio><br>"""

# METHOD_LIST=["gt","conv", "proposed"]
# SR_LIST=[8,20,32,40,48]
# for song_id in range(2):
#     for inst_index, inst in enumerate(["vocals", "bass", "drums", "other"]):
#         mixtures=""
#         if inst_index == 0:
#             for sr in SR_LIST:
#                 mixtures+=MIXTURE_TEMPLATE.format(song_id=song_id,sr=sr,audio_dir="audio")
#             methods = ["", "", ""]
#             for i, method in enumerate(METHOD_LIST):
#                 for sr in SR_LIST:
#                     methods[i]+=SEPARATED_TEMPLATE.format(sr=sr,song_id=song_id,method=method,inst=inst,audio_dir="audio")
#             print(TEMPLATE1.format(mixtures=mixtures,song_id=song_id,inst=inst,gt=methods[0],methodA=methods[1],methodB=methods[2]))
#         else:
#             methods = ["", "", ""]
#             for i, method in enumerate(METHOD_LIST):
#                 for sr in SR_LIST:
#                     methods[i]+=SEPARATED_TEMPLATE.format(sr=sr,song_id=song_id,method=method,inst=inst)
#             print(TEMPLATE2.format(inst=inst,gt=methods[0],methodA=methods[1],methodB=methods[2]))

METHOD_LIST=["gt", "resample", "proposed"]
SR_LIST=[8,12,16,20,24]
for song_id in range(2):
    for inst_index, inst in enumerate(["vocals", "bass", "drums", "other"]):
        mixtures=""
        if inst_index == 0:
            for sr in SR_LIST:
                mixtures+=MIXTURE_TEMPLATE.format(song_id=song_id,sr=sr,audio_dir="audio2")
            methods = ["", "", ""]
            for i, method in enumerate(METHOD_LIST):
                for sr in SR_LIST:
                    methods[i]+=SEPARATED_TEMPLATE.format(sr=sr,song_id=song_id,method=method,inst=inst,audio_dir="audio2")
            print(TEMPLATE1.format(mixtures=mixtures,song_id=song_id,inst=inst,gt=methods[0],methodA=methods[1],methodB=methods[2]))
        else:
            methods = ["", "", ""]
            for i, method in enumerate(METHOD_LIST):
                for sr in SR_LIST:
                    methods[i]+=SEPARATED_TEMPLATE.format(sr=sr,song_id=song_id,method=method,inst=inst,audio_dir="audio2")
            print(TEMPLATE2.format(inst=inst,gt=methods[0],methodA=methods[1],methodB=methods[2]))