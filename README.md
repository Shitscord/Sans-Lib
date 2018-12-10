# SansLib
Make any facial image become sans!

The included sansrun.py creates an input and output folder. Just place whatever files into the input folder to be Sansified.
You may also directly import sanslib.py and pass an input file and output file into the sanslib.sans_eye function.
If facial recgnition is successful the string "success" will be returned. Otherwise "noface" will be returned.
Depends on pillow and face_recognition found here https://github.com/ageitgey/face_recognition.
