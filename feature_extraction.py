import librosa
import soundfile
import pandas as pd


csv_file_path = "test.csv"
csv_paths_dt = pd.read_csv(csv_file_path)
print(csv_paths_dt)
csv_paths_dt['x'], csv_paths_dt['sr']=librosa.load(str(('D:\\poly\\AUTOMNE2021\\CodeML\\data\\test'+csv_paths_dt.Filename)))
print(csv_paths_dt)