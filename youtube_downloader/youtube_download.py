from pytube import YouTube

video = YouTube("https://www.youtube.com/watch?v=i7ABlHngi1Q")

video_stream = video.streams.get_highest_resolution()

video_stream.download(output_path="e:/temp")
