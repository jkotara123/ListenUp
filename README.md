# ListenUp-

Project for AGH University Python course.

Project usage instruction:
1. Clone the repository. 
```
git clone https://github.com/jkotara123/ListenUp.git
```

2. Download two folders - images and sound_files - from following Google Drive:
https://drive.google.com/drive/folders/19COOO1Q7eD3nnUKk5nqNCFtAz8bzyuVo?usp=sharing <br />
Then paste them into *resources* directory.

3. In terminal, enter ListenUp directory and run following code to install all required libraries.
```
pip install -r requirements.txt
```
4. Now you are able to use the application by running it from the folder *App* view.
```
cd App
python .\main.py
```

5. Create a new gmail address and copy it into mail_address.txt file in the Confidential directory.

6. Enable two step verification for that gmail address and generate an app password on this site: (https://myaccount.google.com/)

7. Copy the created app password into the mail_password.txt file in the Confidential direcotry.

8. Lastly, create a new Google Firestore project (https://console.firebase.google.com/) and generate new private python key 
(do it by going to Settings -> Service Accounts and clicking Generate new private key with Python selected). Rename the dowloaded json file to
database_file.json and place it in the Confidential directory.

| | Jakub Kotara                                                  | Jan Masternak                           |
| ------------- |---------------------------------------------------------------|-----------------------------------------|
| Laboratorium 3  | Model wirtualnego pianina (done)                              | Podłączenie dźwięków do klawiszy (done) |
| Laboratorium 4  | Losowanie interwałów i akordów, sprawdzanie odpowiedzi (done) | Menu główne, frontend (done)            |
| Laboratorium 5  | Tworzenie i uwzględnienie statystyk przy losowaniu            | Menu główne (half done)                 |
| Laboratorium 6  | Użytkownicy i logowanie                                       | Grafiki i elementy personalizacji       |
| Laboratorium 7  | Finalne poprawki                                              | Finalne poprawki                        |


