import os
import subprocess
import argparse

def fix_mp4s_in_directory(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".mp4"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"fixed_{filename}")

            print(f"Fixing: {input_path}")
            command = [
                "ffmpeg",
                "-y",
                "-err_detect", "ignore_err",
                "-i", input_path,
                "-c", "copy",
                "-fflags", "+genpts",
                output_path
            ]

            try:
                subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(f"✔️ Fixed and saved to: {output_path}")
            except subprocess.CalledProcessError as e:
                print(f"❌ Error fixing {filename}:\n{e.stderr.decode()}")

def main():
    parser = argparse.ArgumentParser(description="Fix MP4 files using ffmpeg.")
    parser.add_argument("--input_path", required=True, help="Path to the directory containing MP4 files")
    parser.add_argument("--output_path", required=True, help="Path to the output directory for fixed MP4s")
    args = parser.parse_args()

    fix_mp4s_in_directory(args.input_path, args.output_path)

if __name__ == "__main__":
    main()
