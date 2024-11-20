import os
import csv

def create_folder(nom_eleve, directory_path):
    student_dir = os.path.join(directory_path, nom_eleve)
    if not os.path.exists(student_dir):
        os.makedirs(student_dir)
    create_file(nom_eleve, student_dir)
    
def create_file(nom_eleve, student_dir):
    file_path = os.path.join(student_dir, f'{nom_eleve}.txt')
    with open(file_path, "a+") as f:
        f.write('') 

with open(r"C:\Users\m.selmi\Documents\liste.csv", 'r') as csvfile:
    heading = next(csvfile)
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        nom_eleve = f'{row[0]} {row[1]}'
        directory_path = r"C:\Users\m.selmi\Documents\Class_NSI"
        create_folder(nom_eleve, directory_path)
