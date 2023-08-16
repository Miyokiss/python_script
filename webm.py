import os
import threading

# Define a function to convert a single file
def convert_file(input_file, output_file):
    # 使用ffmpeg命令将输入MKV文件转换为WebM格式
    # -i选项指定输入文件
    # -c:v h264_nvenc选项指定要使用的视频编解码器
    # -c:a aac选项指定要使用的音频编解码器（aac用于WebM）
    # -qscale:v 0选项保持与源文件相同的视频质量
    os.system(f'ffmpeg -i "{input_file}" -c:v libvpx-vp9 -c:a libopus "{output_file}"')

# 如果输出目录不存在，则创建它
output_dir = 'video'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 获取当前目录中所有MKV文件的列表
mkv_files = [f for f in os.listdir() if f.endswith('.mkv')]

# 计算总文件数
total_files = len(mkv_files)

# 创建一个线程列表
threads = []

# 将每个MKV文件转换为WebM格式
for input_file in mkv_files:
    # 设置最终输出文件路径（使用原始文件名）
    output_file = os.path.join(output_dir, os.path.splitext(input_file)[0] + '.webm')

    # 创建一个新线程来转换文件
    thread = threading.Thread(target=convert_file, args=(input_file, output_file))
    thread.start()
    threads.append(thread)

# 等待所有线程完成
for thread in threads:
    thread.join()

# 显示完成消息
print('Conversion complete!')
