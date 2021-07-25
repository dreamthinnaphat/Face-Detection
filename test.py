import face_recognition

Messi_Pic = face_recognition.load_image_file("messi.jpg")
face_encoding = face_recognition.face_encodings(Messi_Pic)[0]

unknown_Pic = face_recognition.load_image_file("ronaldo.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_Pic)[0]

results = face_recognition.compare_faces([face_encoding], unknown_face_encoding)

if results[0] == True:
    print("It's Messi")
else:
    print("It's not Messi")