import os
import subprocess
import tarfile
from pydub import AudioSegment
from pick import pick

def cleanup(target_dir):
    print(f"--- Cleaning and Merging in: {target_dir} ---")
    for subdir, dirs, files in os.walk(target_dir):
        base_names = set()
        for f in files:
            if f.endswith("-L.wav"):
                base_names.add(f.replace("-L.wav", ""))
        
        for name in base_names:
            l_path = os.path.join(subdir, f"{name}-L.wav")
            r_path = os.path.join(subdir, f"{name}-R.wav")
            out_path = os.path.join(subdir, f"{name}.wav")

            if os.path.exists(l_path) and os.path.exists(r_path):
                try:
                    left = AudioSegment.from_wav(l_path)
                    right = AudioSegment.from_wav(r_path)
                    stereo = AudioSegment.from_mono_audiosegments(left, right)
                    stereo.export(out_path, format="wav")
                    print(f"  [FIXED] {name}.wav")
                except Exception as e:
                    print(f"  [SKIP] Could not merge {name}: {e}")
        updated_files = os.listdir(subdir)
        for f in updated_files:
            file_path = os.path.join(subdir, f)
            if os.path.isfile(file_path):
                if f.endswith("-L.wav") or f.endswith("-R.wav") or not f.lower().endswith(".wav"):
                    try:
                        os.remove(file_path)
                    except:
                        pass

def extract(iso_path):
    iso_name = os.path.splitext(os.path.basename(iso_path))[0]
    safe_folder = iso_name.replace(" ", "_").replace(".", "_")
    output_dir = os.path.join(os.getcwd(), safe_folder)
    tar_name = "disk0.tar"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    commands = f"cd /\ngettarwav {tar_name}\nexit\n"
    cmd = 'akaiutil.exe' if os.name == 'nt' else 'akaiutil'
    
    try:
        process = subprocess.Popen(
            [cmd, iso_path],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        print("Extracting from ISO... (this takes a minute)")
        process.communicate(input=commands)
        
        if os.path.exists(tar_name):
            with tarfile.open(tar_name) as tar:
                tar.extractall(path=output_dir)
            os.remove(tar_name) 
            cleanup(output_dir)
            print(f"\nDONE: {iso_name} is cleaned up in /{safe_folder}")
        else:
            print("Extraction failed. Check if akaiutil.exe is in this folder.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    iso_files = [f for f in os.listdir('.') if f.lower().endswith('.iso')]
    if not iso_files:
        print("No .iso files found!")
        return

    title = 'Select an AKAI ISO (Arrow keys to move, Enter to select):'
    option, index = pick(iso_files, title, indicator='=>')
    extract(option)

if __name__ == "__main__":
    main()
