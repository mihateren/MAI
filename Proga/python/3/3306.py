{key.lower(): text.count(key.lower()) + text.count(key.upper()) for key in str([text.split()]) if key.isalpha()}