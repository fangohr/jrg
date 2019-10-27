# Schritt 1: Zugriff auf die "turtle" Bibliothek bekommen
import turtle

# Schritt 2: Eine Schildkröte erzeugen. Wir nennen sie "lisa". 
# (Variablenname wie "lisa" werde im allgemeinen klein geschrieben.)
lisa = turtle.Turtle()

# Schritt 3: Bewege lisa 50 Pixel (Punkte) in die Richtung, in die sie bereits guckt.
lisa.forward(50)

# Schritt 4: Bescheid sagen, dass wir fertig (engl: *done*) sind 
turtle.done()     # Fenster zeigen
turtle.bye()      # Turtle object löschen
