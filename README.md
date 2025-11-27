# Python Kursmaterial

In diesem Repository sammle ich Skripte und Materialien für die Python-Kurse, die ich gebe. Falls jemand zufällig drüberstolpert - die Materialien sind so geschrieben, dass sie selbstständiges Lernen priorisieren, also feel free dir die Skripte anzusehen und durchzugehen. Alle Notebooks unterstehen einer CC BY-SA 4.0-Lizenz, dürfen also sehr frei genutzt werden.

Der Guide setzt voraus, dass Python bereits installiert wurde.

## Wie fange ich hiermit an?
Bei dieser Seite handelt es sich um ein Git-Repository. Man kann sich diese vorstellen wie einen Ordner in einem Cloud-System (z.B. OneDrive). Um die Daten auf euer Gerät zu kopieren, könnt ihr zwei Methoden verwenden:

Über das grafische Interface:
- Klickt auf den grünen "<> Code"-Button
- Und dann auf "Download ZIP"
- Ihr könnt den heruntergeladenen Ordner nun auf eurem Ordner entzippen wo ihr möchtet

Noch besser ist es aber, wenn ihr euch Git installiert und den Ordner *klont*. Installationsanleitungen für verschiedene Betriebsysteme findet ihr [hier](https://git-scm.com/install/). Habt ihr Git erstmal installiert, könnt ihr ein Terminal öffnen, zum Ordner navigieren in dem ihr diesen Ordner platzieren wollt, und eingeben "git clone https://github.com/raykyn/Python_Kursmaterial.git".

Auch VSCode ermöglicht euch, direkt einen Ordner von Github zu klonen. Einfach ein neues Fenster öffnen, und dort "Clone Git Repository" drücken, dann öffnet sich ein Dialogfenster in dem man die Adresse, also "https://github.com/raykyn/Python_Kursmaterial.git" eingeben kann.

Der grosse Vorteil der zwei letzteren Methoden ist, dass sie das Repository direkt als remote origin vermerken. Das bedeutet, dass wenn ich (z.B. während einem Kurs) neue Dateien auf das Repository lade, man mit dem git command "fetch" diese Dateien sofort herunterladen kann. 

Git kennenzulernen und zu verwenden ist sehr nützlich, ich würde euch daher die zweite Option empfehlen. Mit VSCode lassen sich viele Git Commands auch direkt über die Benutzeroberfläche verwenden. 

## Empfohlene Umgebung
Ich würde empfehlen, [VSCode](https://code.visualstudio.com/download) als Editor zu verwenden, also das Programm, in dem die Notebooks verwendet werden. VSCode ist kostenlos, schnell und es existieren haufenweise (kostenlose) Erweiterungspakete.

Habt ihr VSCode heruntergeladen, könnt ihr den Ordner öffnen indem ihr "Open Folder" drückt (entweder auf dem Startbildschirm oder unter "File" oben links). 

Ihr benötigt zudem noch einige Erweiterungen, um die Notebooks ordentlich auszuführen, klickt links auf "Extensions" und sucht nach:
- Python (alles rund um die Programmiersprache)
- Jupyter (notwendig, damit die Notebooks korrekt funktionieren)

### Virtual Environments in VSCode
Python bietet ein Feature, welches sich *Virtual Environments* ("venv" abgekürzt) nennt. Es ist üblich, in solchen zu arbeiten um Ordnung rund um seine Python-Versionen und Packages zu halten. Habt ihr die Python-Erweiterung in VSCode installiert, solltet ihr nun links am Rand das Python-Symbol sehen, und wenn du darauf klickst, öffnet sich eine Sidebar. In dieser Sidebar kann man durch den "+"-Button neben "venv" super schnell ein Virtual Environment erstellen, und VSCode merkt sich dann auch, dieses weiterhin immer für diesen Arbeitsordner zu verwenden.

## Los geht's!
Im Ordner "Grundlagen 1" findet ihr das erste Notebook - viel Spass beim Programmieren lernen!