def count_lively(students):
    return sum(1 for s in students if str(s.get('Ζωηρός', '')).upper() in ['Ν', 'ΝΑΙ'])

def count_special(students):
    return sum(1 for s in students if str(s.get('Ιδιαιτερότητα', '')).upper() in ['Ν', 'ΝΑΙ'])

def count_teacher_children(students):
    return sum(1 for s in students if str(s.get('Παιδί Εκπαιδευτικού', '')).upper() in ['Ν', 'ΝΑΙ'])

def count_language_proficient(students):
    return sum(1 for s in students if str(s.get('Καλή γνώση Ελληνικών', '')).upper() in ['Ν', 'ΝΑΙ'])

def is_friend(student1, student2):
    friends1 = str(student1.get('Φίλος/Φίλη', '')).split(',')
    friends2 = str(student2.get('Φίλος/Φίλη', '')).split(',')
    return student2['Όνομα'] in [f.strip() for f in friends1] and student1['Όνομα'] in [f.strip() for f in friends2]

# Η υπόλοιπη εφαρμογή ακολουθεί (παραλείπεται εδώ για συντομία)
