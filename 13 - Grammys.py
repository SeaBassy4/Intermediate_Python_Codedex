from functools import reduce

playlist = [('What Was I Made For?', 3.42), 
('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), 
('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

def longer_than_five(song):
  return song[1] > 5.00

def minutes_to_seconds(song):
  title, minutes = song
  return (title, minutes * 60)

def add_total_time(accu, song):
  return accu + song[1]

playlist_in_seconds = list(map(minutes_to_seconds, playlist))

playlist_total_time = reduce(add_total_time, playlist_in_seconds, 0)

print(playlist_total_time)

