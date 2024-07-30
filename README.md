# Sentinel-Datahub-CRUD-Application
In an era defined by rapid technological advancements and increasing digital complexities, the Sentinel Datahub database system emerges as a crucial tool for modern law enforcement. Designed to enhance investigative efficiency and transparency, this system centralizes and manages critical data, supporting thorough analysis and informed decision-making
## EER Model
![image](https://github.com/user-attachments/assets/04fb1e36-3259-4555-b2d7-bc838ea2d31f)


## Relationships:
• One Officer (Personnel) can be associated with multiple Shifts, Cases, CrimeReports,
Arrests, and CourtAppearances. Each Shift, Case, CrimeReport, Arrest, and
CourtAppearance must be associated with one and only one Officer.<br>
• One Shift is associated with one Officer (Personnel), and each Officer can be
associated with multiple Shifts.<br>
• Each Case is associated with one Investigating Officer (Personnel). An Officer can be
associated with multiple Cases.<br>
• Each CrimeReport is associated with one Reporting Officer (Personnel). An Officer
can be associated with multiple CrimeReports.<br>
• Each piece of Evidence is associated with one Case, and a Case can have multiple
pieces of Evidence.<br>
• Each Witness is associated with one Case, and a Case can have multiple Witnesses.<br>
• Each Arrest is associated with one Arresting Officer (Personnel) and one Case. An
Officer and a Case can be associated with multiple Arrests.<br>
• Each Suspect is associated with one Case, and a Case can have multiple Suspects.<br>
• Each Incident is associated with one Case. Each Case can be associated with multiple
Incidents.<br>
• Each CourtAppearance is associated with one Case, and a Case can have multiple
CourtAppearances.<br>
• Each Station is associated with multiple Officers. An Officer is associated with one
Station.<br>
• Each PenalCode can be associated with multiple Cases, and each Case can be
associated with one PenalCode.

## CRUD Application:

![image](https://github.com/user-attachments/assets/8319f929-321b-4266-a7ec-5917b5ab0406)


![image](https://github.com/user-attachments/assets/5e40a9a3-3a51-41e5-af35-9e5749b83ade)


![image](https://github.com/user-attachments/assets/f581afea-60a5-4f53-ba95-3a0286cf8261)


![image](https://github.com/user-attachments/assets/b0708b8c-90cf-4d8f-bf4d-30a689314117)


![image](https://github.com/user-attachments/assets/ec6396a9-47f8-4cf2-9657-a7f4ff13326c)




